# Affinity Help Center — 站点结构与检索参考

官方帮助中心：`https://www.affinity.studio/help`

## 称呼映射：用户说的「V3」= 本库覆盖版本 ★

官方正式名 **Affinity by Canva**（2025 年 10 月发布），官方**不使用「V3」版本号**；但用户社区普遍称其为 V3。**二者同指，本库完全适用。**

| 用户可能说 | 实际所指 | 本库适用 |
|---|---|---|
| V3 / Affinity 3 / 新版 / 免费版 | Affinity by Canva（2025-10） | ✅ |
| Affinity by Canva | 同上 | ✅ |
| V2 / 买断版 / 三款分立应用 | Serif 旧产品线 | ❌ 指向 `affinity.help` |
| V1 | 更早旧版 | ❌ 指向 `affinity.help` |

证据：
- `info-for-v1-and-v2-users.md` 原文以 "Affinity by Canva user (launched October 2025)" 自称，并把 V1/V2 归为「与本文档无关」的旧产品。
- `release-notes.md` 提及兼容性时称旧版为 "version 2.6"，新版自身不带数字版本号。

**应答原则**：用户说「V3」时**不要纠正为「这不是 V3」**，直接确认「就是本库覆盖的版本」，必要时补一句官方叫法即可。

**官方推荐的标准表述**（来自 `ai-connector-setup.md`，官方 FAQ 原题为 "Why does Claude think I'm using an older version of Affinity?"）：

> "I'm using **Affinity by Canva, April '26 release**."

格式 = **产品名 + 月份'年份 release**。官方以「按月发行」代替版本号：
- `release-notes` = 当月最新发行说明；历史版 slug 形如 `mar-26-release-notes`
- 描述功能引入时间时，优先写「26 年 4 月版起」，不要写笼统的「新版」

V1/V2 用户资源（官方 `info-for-v1-and-v2-users` 给出）：文档 `affinity.help`、产品 `affinity.serif.com/v2/`、账户 `store.serif.com`、支持 `support.serif.com`。

## 版本归属（重要勘误）
本站文档覆盖的是 **Canva 收购后的新版统一 Affinity（= 用户口中的 V3）**，**不是 V2**。

| | 新版 Affinity（本站） | Affinity V2（旧） |
|---|---|---|
| 形态 | **单一应用** | 三款独立应用 Designer / Photo / Publisher |
| 工作区术语 | **Studio**（Vector / Pixel / Layout / Liquify / Develop / Tone Mapping） | Persona |
| 获取方式 | Canva 账户免费使用，付费 Canva 计划解锁 AI 工具 | 一次性买断 |
| 文档地址 | `affinity.studio/help` | `affinity.help`（产品介绍页为 `affinity.serif.com/v2/`，本站仅外链至此） |

判定依据（均取自本地库原文）：
- `introduction-about-affinity` 定义为 "a multi-discipline design app"，并用**过去时**追述 2014 年起的三款产品线。
- `workspace-about-studios` 定义 Studio 为按设计门类分组工具与面板的工作区，可在工具栏切换。
- `free-affinity-access` / `install-affinity` 把 "Affinity V2" 作为**外部链接**指向 serif 域名，即 V2 是另一个产品而非本文档对象。
- 全库 417 篇出现 `persona` 字样，经排查**全部**来自图标文件名（`persona_vector.svg` 等）与遗留 slug `liquify-persona-liquify`，正文术语已无 Persona。

## 文章 URL 规律
- 文章为扁平 slug：`https://www.affinity.studio/help/<slug>/`
- 主题分类页：`https://www.affinity.studio/help/<topic>/`（下列 11 个）
- 搜索：`https://www.affinity.studio/help/?query=<关键词>`

## 11 个主题分类（topic slug）
1. `installation-setup` — 安装、激活、许可、试用
2. `getting-started` — 入门：界面 / 工作室(Studio) / 快捷键 / 新建·打开文档 / 导入(PDF·IDML·PSD·CAD)
3. `canva-integrations` — Canva / Brand Kit / AI 工具集成
4. `design-fundamentals` — 设计基础：颜色、文本、对象
5. `graphic-design` — 矢量设计、图层、画板(Artboard)
6. `photo-editing` — 照片编辑、RAW 显影、修饰、像素
7. `page-layout` — 页面布局、排版、脚注、目录、索引
8. `export-share-publish` — 导出/分享：JPEG/PNG/PDF/SVG/EPUB 等
9. `account-billing` — 账户与计费、Enterprise
10. `working-with-other-apps-and-devices` — 与其他应用/设备（手写笔、平板等）协作
11. `automation` — 自动化 / 连接 AI 助手(MCP)

## 全量文章清单（权威来源：sitemap）★
**不要再用「主题页 + 关键词搜索」去枚举文章**，那样会系统性漏抓（首版仅得 467/845）。

正确做法：
```bash
curl -s -A "curl/8.7.1" https://sitemap.canva.com/affinity_sitemap_0.xml -o /tmp/aff.xml
# 提取英文版 slug（无语言前缀的即英文）
grep -oE 'affinity\.studio/help/[a-z0-9-]+' /tmp/aff.xml | sed 's|.*/help/||' | sort -u
```
- sitemap 入口链：`robots.txt` → `https://www.affinity.studio/sitemap_index.xml` → `https://sitemap.canva.com/affinity_sitemap_0.xml`
- 该文件约 7.6 MB / 9273 条 URL，其中英文 **845** 条，其余为 10 个语言变体。
- 多语言（含 `zh_cn`）**不可用**：抽检显示部分 404、部分回退英文原文，无翻译价值。答题仍需实时中译。
- sitemap 未收录但真实存在的页面约 14 篇（Canva 账户/计费类，如 `install-affinity`、`account-payment-method`），本地已单独保留。

## 检索方式（agent 执行）
- 搜索：`curl -sL "https://r.jina.ai/https://www.affinity.studio/help/?query=<英文关键词>"`
- 主题浏览：`curl -sL "https://r.jina.ai/https://www.affinity.studio/help/<topic>/"`
- 抓文章全文：`curl -sL "https://r.jina.ai/https://www.affinity.studio/help/<slug>/"`
- Jina 约 20 次/分钟，连续抓取每两次间 `sleep 3`。
- Jina 对浏览器型 UA 返回 403，必须用 `-A "curl/8.7.1"`。

## 完整性自检
```bash
cd ~/.workbuddy/skills/affinity-help/references
# 本地 vs _urls.json（已同步为 sitemap 权威清单）
comm -13 <(ls articles/ | sed 's/\.md$//' | sort) <(python3 -c "import json;[print(s) for s in json.load(open('_urls.json'))]" | sort)
```
输出为空即表示已抓全。

## 本地知识库
`~/.workbuddy/skills/affinity-help/references/articles/<slug>.md`

**状态（2026-08-06 全量核对完成）**
- **859 篇 = 845（sitemap 英文全集）+ 14（sitemap 未收录的 Canva 账户类）**，对照 sitemap 缺失数 **0**。
- 体积 7.7 MB，平均 7.2 KB/篇；最小 2.1 KB，最大 31 KB；无 <800B 的空壳文件。
- 全部含合规 frontmatter：`title / source / slug / fetched`，正文为官方英文原文（markdown）。
- 全库 grep 检索约 **0.12 秒**。

**使用顺序**：优先 Grep 此目录；未命中再走上面的实时检索。命中后按需实时中译作答并附官方链接。

**检索陷阱（实测）**

| 坏写法 | 命中 | 问题 | 好写法 |
|---|---|---|---|
| `grep -ri "studio"` | **859/859** | 每篇 frontmatter 都有 `source: affinity.studio/...` | `grep -riE "(Vector\|Pixel\|Layout\|Liquify\|Develop) Studio"` → 241 篇 |
| `grep -ri "LUT"` | 420 | 匹配 abso**lut**ely、so**lut**ion 词根 | `grep -riw "LUT"` |
| `grep -ri "mask"` | 多 | 过宽 | `grep -ri "vector mask"` → 4 篇 |

通则：**用完整短语 + 词边界；命中后先 grep 上下文验真，别只看文件名下结论。**

## 更新知识库

用 `scripts/update_kb.py`，四种模式：

```bash
python3 update_kb.py check        # 体检：比对 sitemap，只报差异不下载（12 秒）
python3 update_kb.py diff         # 增量：抓新增 + 归档下架（默认模式）
python3 update_kb.py refresh 90   # 刷新 fetched 早于 N 天的文章
python3 update_kb.py full         # 全量重抓 859 篇（约 50 分钟）
```

脚本自动定位 skill 目录，跨 agent（Hermes / WorkBuddy）通用，无需改路径。

**关于「增量」的重要限制（勘误）**
早前记录「sitemap 条目带 `lastmod`，可据此做增量重抓」——**此说法错误**。实测该 sitemap 9273 条 URL 中 `<lastmod>` 出现 **0 次**，官方未提供该字段。

因此：
- **结构变化**（新增 / 下架文章）→ 可精确 diff，成本极低。
- **内容变化**（既有文章被官方改写）→ **无法检测**，只能 `full` 或 `refresh` 重抓比对。

**下架处理**：diff 模式将本地有、sitemap 无的文章移入 `references/_retired/` 归档，不删除。脚本内 `KEEP_EXTRA` 白名单保护那 14 篇 Canva 账户类页面（sitemap 未收录但页面真实存在），避免被误归档。
