# 🎨 Affinity Help — 基于官方帮助文档的中文问答

> Affinity official-help Q&A skill — answer Affinity Photo / Designer / Publisher questions in Chinese, strictly grounded in the official help center.

> 当用户问「Affinity 怎么做 X」「Affinity 的快捷键」「导出 PDF 要注意什么」时，基于 affinity.studio/help 官方帮助中心的最新原文，用简体中文作答、附来源链接。**不臆测、不编造功能。**

---

## 这是什么

一个 **Affinity 官方帮助文档问答 skill**：把 Affinity Photo / Designer / Publisher 的官方帮助中心（`affinity.studio/help`）变成可检索的中文问答助手。

回答**严格基于官方文档原文**，所有结论都能追溯到具体文章 URL，不臆测、不编造功能。最终用**简体中文**作答，保留专业术语英文原名（Persona、Studio、Artboard）便于对照。

> 背景：Affinity 已被 Canva 收购，当前帮助中心为 Canva 时代（Affinity V2）版本。旧版 V1 文档在 `affinity.serif.com/help`，仅在用户明确问 V1 时参考。

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

**本地知识库**：`references/articles/` 已落地 460+ 篇官方英文原文（每篇含 frontmatter：title/source/slug/fetched），离线可查；未命中时实时抓取官方帮助中心。

---

## 工作流程

1. **判断是否需要检索** — 涉及具体操作步骤/面板位置/参数含义/版本差异/故障排查，必须检索官方文档；不确定时，检索
2. **提炼英文关键词** — 文档为英文，英文检索命中率最高（「怎么给图层加蒙版」→ `layer mask`）
3. **优先查本地知识库** — Grep `references/articles/`，命中即用
4. **未命中则实时检索** — 通过 Jina 把官方页面转 Markdown，搜索 / 浏览主题分类 / 抓取全文
5. **基于原文作答** — 简体中文 + 保留英文术语 + 附来源 URL

---

## 使用方式

对 AI 助手说：

> 「Affinity 里怎么给图层加蒙版？」

> 「导出带出血的 PDF 要注意什么？」

> 「Affinity Photo 的 RAW 显影流程是怎样的？」

---

## 目录结构

```
affinity-help/
├── SKILL.md                 # 主文件：定位 + 工作流程 + 检索方法
└── references/
    ├── structure.md         # 官方站点结构 + 11 主题分类
    ├── _urls.json           # 465 篇文章 slug 清单
    └── articles/            # 本地知识库：460+ 篇官方英文原文
```

> ⚠️ 注意：SKILL.md 中的本地路径 `~/.workbuddy/skills/affinity-help/references/articles/` 是作者本机路径。安装到自己的 agent 时，按实际安装路径修改。

---

## 数据来源

- 官方帮助中心：https://www.affinity.studio/help
- 本地文章抓取：affinity.studio/help 官方英文原文（含抓取日期 frontmatter）

> ⚠️ **缓存声明**：`references/articles/` 是对官方帮助中心的**快照缓存**（抓取日期 2026-08-06，见各文件 frontmatter `fetched` 字段）。官方文档持续更新，缓存可能滞后。skill 已内置「本地命中但涉及最新改动/版本差异 → 走在线实时检索」的兜底逻辑（SKILL.md 第 3 步，通过 Jina 实时抓取官方页面），**本地缓存 + 在线实时双通道**，两者结合保证答案基于最新官方原文。

---

## 关于作者

宝藏彬少（Heybinshao）—— 一个什么都折腾一下的人：装系统 · 玩 AI · 搭知识库 · 做设计。

折腾，是为了更好用。
