---
title: "Reading Order panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-reading-order-panel/
slug: panels-reading-order-panel
fetched: 2026-08-06
---

# Reading Order panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-reading-order-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Reading Order panel

The **Reading Order** panel allows you to specify the order in which assistive technologies, such as screen readers, will present your document's contents to the reader.

For Mac/Windows: On the **Window** menu, select **Layout > Reading Order**.

The panel automatically lists text objects from each publication page, except for empty text frames, which are ignored until they contain text. It also lists any objects with alt text set on the **Tags** panel.

You can drag items up or down to change the order. Group items into articles to make the reading order easier to manage.

Items are named according to the following rules:

*   If an object's layer has a custom name, that name becomes the item name.
*   If it doesn't have a custom name:
    *   Text objects use the start of the text as the item name<sup>1</sup>.
    *   Non-text objects with alt text use that text as the item name (and layer name).
    *   Non-text objects without alt text use the object's default layer name as the item name 2.
    *   For articles, which can be used to group other items, _Article_ is used as the default name 3.

1 Objects inherited from a master page are an exception: they only appear in the list after their text is edited where the master page is applied, and their item name is their original master-page text.

2 If you manually add an object to the reading order, you must also add alt text for it to appear in the exported PDF's reading order.

3 To rename an article, select it, then click it again.

Text objects inherited from a master page are excluded from the reading order unless you edit their text on the page where the master is applied.

Non-text objects with alt text set on a master page are excluded from the reading order.

The following options are available on the panel:

*   **Article list**—shows all qualifying objects from your document in the order they will be presented by assistive technologies.
*   **Go to Object**—selects the object that corresponds to the selected item in the list. The document view focuses on the object, if it is not already in view.
*   **Add Article**—creates a new article. If two or more reading order items are selected, they are added to the article.
*   **Add selected object(s)**—adds to the list any objects which are selected but not already in the list.
*   **Remove**—removes the selected Articles from the list. Any items they contain are moved to the top level.

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 The following options are available on the **Panel Preferences** menu:

*   **Expand All Articles**—opens all articles to reveal all items in the reading order.
*   **Collapse All Articles**—closes all articles, hiding the items within them. This gives you a high-level view of the reading order.
*   **Collapse Selection**—closes the selected article, hiding the items within it. This is useful when a specific article contains many items that you don't need to see.
*   **Panels**—opens a dialog where you can quickly set the visibility of all panels in the current Studio.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

*   [Accessible PDFs](https://www.affinity.studio/help/sharing-accessible-pdfs/)
*   [Publishing PDF files](https://www.affinity.studio/help/sharing-publish-pdffiles/)

How would you rate the help you received from this article?
