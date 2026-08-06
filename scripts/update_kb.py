#!/usr/bin/env python3
"""
Affinity 帮助文档知识库更新器

用法：
  python3 update_kb.py check        # 只体检，不下载（约 10 秒）
  python3 update_kb.py diff         # 增量：抓新增、删下架（默认）
  python3 update_kb.py full         # 全量重抓（覆盖全部 859 篇，约 50 分钟）
  python3 update_kb.py refresh 90   # 刷新 fetched 早于 90 天的文章

说明：sitemap 不含 lastmod，无法判断单篇是否被官方修改。
      因此「内容更新」只能靠 full 或 refresh 重抓。
"""
import urllib.request, urllib.error, re, os, sys, time, json, threading, collections, shutil
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

BASE    = "https://www.affinity.studio/help"
JINA    = "https://r.jina.ai/"
SITEMAP = "https://sitemap.canva.com/affinity_sitemap_0.xml"
UA      = "curl/8.7.1"                       # ⚠️ 浏览器型 UA 会被 Jina 403
ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB      = os.path.join(ROOT, "references", "articles")
URLS    = os.path.join(ROOT, "references", "_urls.json")
ATTIC   = os.path.join(ROOT, "references", "_retired")   # 下架文章归档处，不直接删

# sitemap 未收录但真实存在（Canva 账户/计费类），保护其不被误判为「下架」
KEEP_EXTRA = {
    "about-canva-enterprise", "about-canva-for-education", "about-canva-teams",
    "account-payment-method", "cancel-canva-plan", "canva-for-nonprofits",
    "change-password", "delete-account", "free-affinity-access",
    "install-affinity", "pause-annual-canva-plan", "payment-options",
    "sign-up-log-in", "upgrade-to-canva-pro-or-business",
}

# ---------- 限流 ----------
class RateLimiter:
    def __init__(self, max_calls, period=60):
        self.max_calls, self.period = max_calls, period
        self.lock, self.calls = threading.Lock(), collections.deque()
    def acquire(self):
        while True:
            with self.lock:
                now = time.time()
                while self.calls and self.calls[0] <= now - self.period:
                    self.calls.popleft()
                if len(self.calls) < self.max_calls:
                    self.calls.append(now); return
                wait = self.calls[0] + self.period - now
            time.sleep(max(wait, 0.2))

RL = RateLimiter(18, 60)   # Jina 上限 20/min，留 2 次余量

def jina_get(page_url, max_retry=5):
    for _ in range(max_retry):
        RL.acquire()
        try:
            req = urllib.request.Request(JINA + page_url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 503, 504):
                time.sleep(60); continue
            return None
        except Exception:
            time.sleep(5)
    return None

# ---------- sitemap ----------
def fetch_sitemap_slugs():
    req = urllib.request.Request(SITEMAP, headers={"User-Agent": UA})
    xml = urllib.request.urlopen(req, timeout=180).read().decode("utf-8", "replace")
    slugs = set()
    for u in re.findall(r"<loc>(.*?)</loc>", xml):
        m = re.match(r"https://www\.affinity\.studio/help/([^/?#]+)/?$", u.strip())
        if m:                                     # 无语言前缀 = 英文版
            slugs.add(m.group(1))
    return slugs, len(xml)

def local_slugs():
    if not os.path.isdir(KB): return set()
    return {f[:-3] for f in os.listdir(KB) if f.endswith(".md")}

def fetched_date(slug):
    p = os.path.join(KB, slug + ".md")
    try:
        head = open(p, encoding="utf-8", errors="replace").read(400)
        m = re.search(r"^fetched:\s*(\S+)", head, re.M)
        return m.group(1) if m else None
    except Exception:
        return None

# ---------- 抓取入库 ----------
def save_article(slug, overwrite=False):
    path = os.path.join(KB, slug + ".md")
    if os.path.exists(path) and not overwrite:
        return "skip"
    txt = jina_get(f"{BASE}/{slug}/")
    if not txt: return "fail"
    if "Warning: Target URL returned error 404" in txt[:400]: return "404"
    mt = re.search(r'^Title:\s*(.+)$', txt, re.M)
    ms = re.search(r'^URL Source:\s*(\S+)$', txt, re.M)
    mc = re.search(r'Markdown Content:\n(.*)', txt, re.S)
    title   = mt.group(1).strip() if mt else slug
    source  = ms.group(1).strip() if ms else f"{BASE}/{slug}/"
    content = mc.group(1).strip() if mc else txt
    if len(content) < 200: return "thin"
    old = ""
    if os.path.exists(path):
        old = open(path, encoding="utf-8", errors="replace").read()
        old = old.split("---", 2)[-1].strip()
    fm = (f'---\ntitle: "{title.replace(chr(34), chr(39))}"\nsource: {source}\nslug: {slug}\n'
          f'fetched: {time.strftime("%Y-%m-%d")}\n---\n\n# {title}\n\n'
          f'> 官方来源：{source}\n\n{content}\n')
    open(path, "w").write(fm)
    if overwrite and old and old.replace(f"> 官方来源：{source}", "").strip() != \
       (f"# {title}\n\n\n{content}").replace(f"# {title}", "").strip():
        return "changed"
    return "ok"

def run_batch(slugs, overwrite=False, label="抓取"):
    stats = collections.Counter(); lock = threading.Lock(); done = [0]
    total = len(slugs)
    if not total:
        print(f"  {label}：无待处理项"); return stats
    print(f"  {label} {total} 篇，预计 {total/18:.0f} 分钟…", flush=True)
    def work(s):
        r = save_article(s, overwrite)
        with lock:
            stats[r] += 1; done[0] += 1
            if done[0] % 25 == 0 or done[0] == total:
                print(f"    进度 {done[0]}/{total}  {dict(stats)}", flush=True)
        if r in ("fail", "404", "thin"):
            print(f"    [{r}] {s}", flush=True)
    with ThreadPoolExecutor(max_workers=5) as ex:
        list(ex.map(work, slugs))
    return stats

# ---------- 主流程 ----------
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "diff"
    print(f"=== Affinity KB 更新器 · 模式 {mode} · {datetime.now():%Y-%m-%d %H:%M} ===\n")

    print("[1/4] 拉取官方 sitemap…", flush=True)
    sm, size = fetch_sitemap_slugs()
    loc = local_slugs()
    print(f"  sitemap 英文文章: {len(sm)} 篇  (文件 {size/1024/1024:.1f} MB)")
    print(f"  本地知识库:       {len(loc)} 篇\n")

    added   = sorted(sm - loc)                          # 官方新增
    retired = sorted(loc - sm - KEEP_EXTRA)             # 官方已下架
    print("[2/4] 差异分析")
    print(f"  官方新增（本地缺）: {len(added)}")
    for s in added[:20]: print(f"      + {s}")
    if len(added) > 20: print(f"      … 另 {len(added)-20} 篇")
    print(f"  疑似下架（本地多）: {len(retired)}")
    for s in retired[:20]: print(f"      - {s}  (fetched {fetched_date(s)})")
    if len(retired) > 20: print(f"      … 另 {len(retired)-20} 篇")

    # 新鲜度
    dates = collections.Counter(fetched_date(s) for s in loc)
    print(f"\n  抓取日期分布: {dict(sorted(dates.items()))}")
    oldest = min((d for d in dates if d), default=None)
    if oldest:
        age = (datetime.now() - datetime.strptime(oldest, "%Y-%m-%d")).days
        print(f"  最旧快照距今 {age} 天\n")

    if mode == "check":
        print("[3/4] check 模式：只体检，不下载。")
        print("[4/4] 建议：")
        if added:   print(f"  · 有 {len(added)} 篇新增 → 跑 `update_kb.py diff`")
        if retired: print(f"  · 有 {len(retired)} 篇疑似下架 → diff 模式会移入 _retired/ 归档")
        if oldest and age > 90: print(f"  · 快照已 {age} 天 → 考虑 `update_kb.py full` 全量重抓")
        if not added and not retired: print("  · 结构无变化，知识库完整。")
        return

    print("[3/4] 执行更新")
    if mode == "full":
        st = run_batch(sorted(sm | (loc & KEEP_EXTRA)), overwrite=True, label="全量重抓")
    elif mode == "refresh":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 90
        cut = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        stale = sorted(s for s in loc if (fetched_date(s) or "0000") < cut)
        print(f"  fetched 早于 {cut} 的文章: {len(stale)} 篇")
        st = run_batch(stale, overwrite=True, label="刷新重抓")
    else:  # diff
        st = run_batch(added, overwrite=False, label="增量抓取")
        if retired:
            os.makedirs(ATTIC, exist_ok=True)
            for s in retired:
                shutil.move(os.path.join(KB, s + ".md"), os.path.join(ATTIC, s + ".md"))
            print(f"  已归档 {len(retired)} 篇下架文章 → references/_retired/（未删除）")

    print(f"\n[4/4] 收尾")
    json.dump(sorted(sm), open(URLS, "w"), indent=0)
    final = local_slugs()
    miss  = sorted(sm - final)
    total_size = sum(os.path.getsize(os.path.join(KB, f)) for f in os.listdir(KB) if f.endswith(".md"))
    print(f"  _urls.json 已同步为 sitemap 权威清单（{len(sm)} 条）")
    print(f"  本地最终: {len(final)} 篇  {total_size/1024/1024:.2f} MB")
    print(f"  对照 sitemap 缺失: {len(miss)}  {miss[:5] if miss else '(无)'}")
    print(f"  结果: {dict(st)}")
    print("\nDONE")

if __name__ == "__main__":
    main()
