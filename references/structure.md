# Affinity Help Center — 站点结构与检索参考

官方帮助中心：`https://www.affinity.studio/help`

> Affinity 已被 Canva 收购，当前为 Affinity V2（Canva 时代）文档，持续更新。
> 旧版 V1 文档位于 `https://affinity.serif.com/help`（仅当用户明确问 V1 时参考）。

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

## 检索方式（agent 执行）
- 搜索：`curl -sL "https://r.jina.ai/https://www.affinity.studio/help/?query=<英文关键词>"`
- 主题浏览：`curl -sL "https://r.jina.ai/https://www.affinity.studio/help/<topic>/"`
- 抓文章全文：`curl -sL "https://r.jina.ai/https://www.affinity.studio/help/<slug>/"`
- Jina 约 20 次/分钟，连续抓取每两次间 `sleep 3`。

## 本地知识库
`~/.workbuddy/skills/affinity-help/references/articles/<slug>.md`
每篇含 frontmatter：`title / source / slug / fetched`，正文为官方英文原文（markdown）。
优先 Grep 此目录；未命中再走上面的实时检索。
