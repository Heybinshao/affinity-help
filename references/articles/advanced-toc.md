---
title: "Table of contents - Affinity Help Center"
source: https://www.affinity.studio/help/advanced-toc/
slug: advanced-toc
fetched: 2026-08-06
---

# Table of contents - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/advanced-toc/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Table of contents

Affinity provides the ability to easily insert and manage a table of contents (TOC) for your document.

When you insert a table of contents, Affinity looks for text that has your chosen text styles applied to it, usually headings. The table of contents contains entries for the styled text and the page number that contains the styled text.

A document can have as many TOCs as required, but typically a single TOC at the start of your publication is used.

The TOC includes entries from the same page or later pages in the document.

If you create a document with sufficient pages containing headings in styles used by your TOC, you'll need to plan out the number of pages to accommodate the automatically generated TOC:

*   If the number of TOC entries necessitates two or more pages for your TOC, you will need to make room for this by inserting pages.
*   If the number of TOC entries overflows its text frame, create and link additional text frames on the pages allocated to your TOC.

A publication may require secondary, section-specific TOCs, e.g. one for each chapter of a book. You can generate and present a secondary TOC within a selected section.

You can include all qualifying headings in the section and those that follow, or limit it to just the section.

Affinity creates corresponding TOC text styles for each of the regular text styles that are used to generate TOC entries.

For example, if a document contains a single TOC that's generated from uses of the _Heading 1_ text style, Affinity creates _TOC 1: Heading 1_ and _TOC 1: Heading 1 Number_ text styles.

A TOC's text styles are shown on the **Text Styles** panel only when the text frame containing the TOC is selected or an insertion point is positioned in the TOC's text.

By default, each TOC has its own set of text styles. The names of these styles are prefixed with the value of **TOC Style** that's shown on the **Table of Contents** panel when the TOC's text frame is selected.

Leader lines link TOC entries to their page numbers. They are not shown by default. To add them, use tab stops in the TOC's text styles. Leader lines can show an underline, a strikethrough, or a repeating symbol (glyph).

You can display leader lines only for specific TOC entries—you may want only _TOC 1: Heading 1_ to display leader lines, for example—or for all TOC entries by editing your TOC's default entry style, e.g. _TOC 1: Entry_.

1.   In a text frame, create an insertion point.
2.    Do one of the following: 
    *   On the **Text** menu, select **Table of Contents > Insert**. The **Table of Contents** panel will open automatically.
    *   On the **Table of Contents** panel, click **Insert**![Image 1](https://images.ctfassets.net/3p2fxa94bzao/2m47rLOVPg6hgwZ5CEnjac/87c4ef9308c5f81c9be1c9cc3213a6d7/insertToc.svg) .

3.   In the list of text styles at the bottom of the panel, ensure only styles to be used for TOC entries are checked. If no entries appear in the TOC, check the text you expect to appear has one of your chosen styles applied.

Do one of the following:

*   To update an individual table of contents, select it on the page and then select **Update**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/1UA1wOj97gWuxMfjdy5Zkv/02dc0ef6081924027bda46ba268a834c/update_toc.svg)  on the **Table of Contents** panel.Alternatively, on the **Text** menu, select **Table of Contents > Update**.
*   To update every table of contents in your document, select **Update All Tables of Contents**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/1nD6ADgbXI1nmPJudPqfxK/5bc1e86cd1bfc827010a170471e30113/updateAllTocs.svg)  on the **Table of Contents** panel.Alternatively, on the **Text** menu, select **Table of Contents > Update All Tables of Contents**.

When exporting your document, you will be prompted to update tables of contents even if all are up to date.

Before you begin, your document must contain sections. If it doesn't, see the "Adding sections" topic for details.

1.   On the page where the secondary TOC needs to appear, create a text frame.
2.   On the **Table of Contents** panel:
    1.   Select **Insert**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/2m47rLOVPg6hgwZ5CEnjac/87c4ef9308c5f81c9be1c9cc3213a6d7/insertToc.svg) . (Optionally, select **Rename**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/5zZjqQ6w90u11JT5q1m0un/b199409dfc3c7dee5bbf3c327d48d20b/renameToc.svg)  and give the TOC a meaningful name.)
    2.   Set **Scope** to either:
        1.   **Document**—if you want the TOC to be generated from styled text across all your pages.
        2.   **Section**—if you want the TOC to be generated from styled text only in the same section as the TOC.

    3.   Enable **Stop at next TOC**. If you don't, the TOC may contain entries based on styled text after the next TOC's page.
    4.   (Optional) Select a **TOC Style**, meaning the group of styles that format the TOC itself, not the text that creates it. For example, you may want to reuse an earlier TOC's text styles.
    5.   In the text styles list, check only the styles you want as TOC entry sources.

If the TOC doesn't automatically update on the page, select **Update**

![Image 6](https://images.ctfassets.net/3p2fxa94bzao/1UA1wOj97gWuxMfjdy5Zkv/02dc0ef6081924027bda46ba268a834c/update_toc.svg)

 on the Table of Contents panel.

1.   Select a text frame that contains a table of contents. The TOC's text styles only appear on the **Text Styles** panel when the frame is selected or an insertion point is positioned in the TOC.
2.   On the Text Styles panel, select **Options**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg)  next to the TOC text style you wish to edit, then select **Edit "<style name>"**.
3.   On the dialog that appears, edit the settings as required.
4.   Click **OK**.

1.   Select a text frame that contains a table of contents.
2.   On the **Table of Contents** panel, note the selected **TOC Style**.
3.    On the **Text Styles** panel, do one of the following: 
    *   For leader lines on all TOC entries, select **Edit "<style name>"** on the options menu of the corresponding _Entry_ style, e.g. _TOC 1: Entry_.
    *   For leader lines on specific TOC entries, select **Edit "<style name>"** on the options menu of the corresponding TOC style, e.g. _TOC 1: Heading 1_.

4.   On the dialog that appears: 
    1.   Select **Tab Stops** on the left.
    2.   On the right, click the predefined tab stop's **More options** button (labeled "**…**").
    3.   Select the required **Leader** character: **None**, **Glyph**, **Underline**, or **Strikeout**.
    4.   (Optional) If you selected Glyph, type the required glyph to repeat along the leader line in the **Character** field.
    5.   Click **OK**.

*   [Table of Contents (ToC) panel](https://www.affinity.studio/help/panels-toc-panel/)
*   [Text Styles panel](https://www.affinity.studio/help/panels-text-styles-panel/)
*   [Adding sections](https://www.affinity.studio/help/pages-adding-sections/)

How would you rate the help you received from this article?
