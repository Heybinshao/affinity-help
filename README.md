# 🎨 Affinity Help — 基于官方帮助文档的中文问答

> Affinity official-help Q&A skill — answer Affinity by Canva (a.k.a. V3) questions in Chinese, strictly grounded in the official help center.

> 当用户问「Affinity 怎么做 X」「Affinity 的快捷键」「导出 PDF 要注意什么」时，基于 affinity.studio/help 官方帮助中心的最新原文，用简体中文作答、附来源链接。**不臆测、不编造功能。**

---

## 这是什么

一个 **Affinity 官方帮助文档问答 skill**：把新版统一 Affinity（**Affinity by Canva**，2025-10 发布，用户社区常称 **V3**）的官方帮助中心（`affinity.studio/help`）变成可检索的中文问答助手。

回答**严格基于官方文档原文**，所有结论都能追溯到具体文章 URL，不臆测、不编造功能。最终用**简体中文**作答，保留专业术语英文原名（Studio、Artboard、Live Filter）便于对照。

> **版本背景（重要）**：Affinity 已被 Canva 收购，官方推出统一应用 **Affinity by Canva**（用户常称 V3）——一个应用内含 Vector / Pixel / Layout 等多个 **Studio**。V2 的三款分立应用（Designer / Photo / Publisher）与 Persona 术语属于旧产品线，本库不覆盖（指向 `affinity.help`）。官方不使用版本号，以「按月发行」标识（如 "Affinity by Canva, April '26 release"）。

> **称呼对照**：用户说「V3 / Affinity 3 / 新版 / 免费版」= 本库覆盖版本 ✅；说「V2 / 买断版 / Designer·Photo·Publisher 三款」= Serif 旧产品线 ❌。

---

## 覆盖范围

11 个主题分类，覆盖 Affinity 全功能：

| # | 主题 | 覆盖 |
|---|------|------|
| 1 | 安装与激活 | 安装、激活、许可、试用 |
| 2 | 入门 | 界面、工作室(Studio)、快捷键、新建/打开文档、导入(PDF/IDML/PSD/CAD) |
| 3 | Canva 集成 | Canva / Brand Kit / AI 工具集成 |
| 4 | 设计基础 | 颜色、文本、对象 |
| 5 | 矢量设计 | 矢量、图层、画板(Artboard) |
| 6 | 照片编辑 | RAW 显影、修饰、像素、HDR |
| 7 | 页面布局 | 排版、脚注、目录、索引 |
| 8 | 导出/分享 | JPEG/PNG/PDF/SVG/EPUB 等 |
| 9 | 账户与计费 | 账户、订阅、付款方式 |
| 10 | 跨应用协作 | 与其他应用/设备协作 |
| 11 | 自动化 | 自动化 / 连接 AI 助手 |

**本地知识库**：`references/articles/` 已落地 **859 篇**官方英文原文（845 篇 sitemap 全集 + 14 篇 Canva 账户类），每篇含 frontmatter：title/source/slug/fetched，离线可查；未命中时实时抓取官方帮助中心。

---

## 工作流程

1. **判断是否需要检索** — 涉及具体操作步骤/面板位置/参数含义/版本差异/故障排查，必须检索官方文档；不确定时，检索
2. **提炼英文关键词** — 文档为英文，英文检索命中率最高（「怎么给图层加蒙版」→ `layer mask`）
3. **优先查本地知识库** — Grep `references/articles/`，命中即用
4. **未命中则实时检索** — 通过 Jina 把官方页面转 Markdown，搜索 / 浏览主题分类 / 抓取全文
5. **基于原文作答** — 简体中文 + 保留英文术语 + 附来源 URL

---

## 知识库更新（维护模式）

本地知识库是官方文档的快照缓存，官方持续更新。内置更新脚本 `scripts/update_kb.py`，对 AI 助手说「更新 Affinity 知识库」「体检一下」即可触发：

```bash
cd <skill目录>/scripts
python3 update_kb.py check        # 体检：只比对 sitemap，不下载（约 12 秒）
python3 update_kb.py diff         # 增量：抓官方新增、归档已下架（默认）
python3 update_kb.py refresh 90   # 刷新 fetched 早于 90 天的文章
python3 update_kb.py full         # 全量重抓 859 篇，约 50 分钟
```

| 用户说法 | 用哪个模式 | 耗时 |
|---|---|---|
| 「有没有更新」「体检一下」 | `check` | 12 秒 |
| 「更新一下」（默认理解） | 先 `check`，有新增再 `diff` | 12 秒 + 新增数/18 分钟 |
| 「Affinity 大版本更新了」「内容太旧了」 | `full` | 约 50 分钟 |
| 「刷新半年前的」 | `refresh <天数>` | 视命中数 |

**设计要点**：
- 下架文章移入 `references/_retired/` **归档而非删除**，避免误判导致内容丢失
- 脚本自动定位 skill 目录，跨 agent（Hermes / WorkBuddy）通用，无需改路径
- `KEEP_EXTRA` 白名单保护 14 篇 sitemap 未收录但真实存在的 Canva 账户类页面
- ⚠️ 官方 sitemap **不含 `lastmod`**（实测 9273 条 URL 中 `<lastmod>` 出现 0 次），无法检测单篇内容是否被改写——内容更新只能靠 `full` / `refresh` 重抓比对。这是站点侧限制，不是脚本缺陷

---

## 使用方式

对 AI 助手说：

> 「Affinity 里怎么给图层加蒙版？」

> 「导出带出血的 PDF 要注意什么？」

> 「Affinity 的 RAW 显影流程是怎样的？」

---

## 目录结构

```
affinity-help/
├── SKILL.md                 # 主文件：定位 + 工作流程 + 检索方法
├── scripts/
│   └── update_kb.py         # 知识库更新器（check/diff/refresh/full）
└── references/
    ├── structure.md         # 官方站点结构 + 11 主题分类 + 完整性自检
    ├── _urls.json           # 845 篇 sitemap 权威 slug 清单
    ├── articles/            # 本地知识库：859 篇官方英文原文
    └── _retired/            # 下架文章归档（diff 模式生成）
```

---

## 数据来源

- 官方帮助中心：https://www.affinity.studio/help
- 官方 sitemap：https://sitemap.canva.com/affinity_sitemap_0.xml
- 本地文章抓取：affinity.studio/help 官方英文原文（含抓取日期 frontmatter）

> ⚠️ **缓存声明**：`references/articles/` 是对官方帮助中心的**快照缓存**（抓取日期 2026-08-06，见各文件 frontmatter `fetched` 字段）。官方文档持续更新，缓存可能滞后。skill 已内置「本地命中但涉及最新改动/版本差异 → 走在线实时检索」的兜底逻辑（SKILL.md 第 3 步，通过 Jina 实时抓取官方页面），并支持「更新 Affinity 知识库」触发更新脚本。**本地缓存 + 在线实时 + 定时更新**三通道，保证答案基于最新官方原文。

---

## 关于作者

**彬少** —— 一个什么都折腾一下的人：装系统 · 玩AI · 搭知识库 · 做设计。这套 Skill 是我自己在用的，基于官方帮助文档搭的中文问答库。

微信公众号 **「宝藏彬少」**：折腾，是为了更好用。欢迎关注交流。
