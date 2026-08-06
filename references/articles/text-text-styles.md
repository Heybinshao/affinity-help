---
title: "Using text styles - Affinity Help Center"
source: https://www.affinity.studio/help/text-text-styles/
slug: text-text-styles
fetched: 2026-08-06
---

# Using text styles - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/text-text-styles/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Using text styles

Text styles can be applied to text within your designs for efficiency and consistency.

A text style is a set of one or more text attributes that can be applied to text in bulk. An attribute could be a font family, font trait, font size, spacing, or alignment, for example.

If you modify a text style, any text that uses that style will update to conform to the attribute changes you've made.

Every new document comes with a default set of text styles. The **Text Styles** panel provides the ability to create and manage a document's text styles, as well as remove them.

Text styles are assigned to one of three **types** (paragraph, character, and group), but are flexible in how they can be used.

**Local formatting** means that you apply text attributes directly as a character, word, or paragraph. The attribute's settings are not stored for reuse, so if you want to apply them to other text, you'd have to do it all again. This is fine for small ranges of text, but for longer passages it might be laborious and lead to inconsistency.

**Character styles** overcome this by saving attributes' settings as a named text style that can be quickly applied to any selected range of text.

Likewise, you can save settings as named **paragraph styles** in order to quickly format whole paragraphs.

Text styles can be applied to text using the context toolbar; the Text Styles, Paragraph, and Character panels; and custom keyboard shortcuts.

Furthermore, if you have established a strict order in which several text styles should be applied to consecutive paragraphs, by setting their **Next Style** attributes, you can apply those styles to all or some of a story—a linked sequence of text frames—all at once.

If local formatting has been applied to text, it can be quickly removed using the Text Styles panel without removing any applied text styles.

Text styles can be copied and pasted between text by using the **Style Picker Tool**

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6po4wOSvY5gMywHyYOPCkP/c4adfef55a04dd8bee680ae265da5618/format_picker_tool.svg)

.

1.   Do one of the following to choose which text will be styled: 
    *   To affect all paragraphs in a text object, select the object.
    *   To affect some paragraphs in a text object, select a text range within them.
    *   To affect an individual paragraph, create an insertion point within it.

2.   Do one of the following to apply the required style: 
    *   On the context toolbar, select a character style from the **Character Style**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/14s6gBEEfR9KoZKoyZzspq/1607b73812623d25a70f07f6fb3224ef/CharacterStyle.svg)  pop-up menu.
    *   On the context toolbar, select a paragraph style from the **Paragraph Style**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2Z1fGYfMPi7gUNPsxlpsuE/e9b6aca401c04ce90c5e05f5af722665/ParagraphStyle.svg)  pop-up menu.
    *   On the **Paragraph** panel, select a text style from the **Paragraph Style** pop-up menu.
    *   On the **Text Styles** panel, select a text style.

1.   Select the exact range of text to be formatted.
2.   Do one of the following: 
    *   On the context toolbar, select a text style from the **Character Style**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/14s6gBEEfR9KoZKoyZzspq/1607b73812623d25a70f07f6fb3224ef/CharacterStyle.svg)  pop-up menu.
    *   On the **Character** panel, select a text style from the **Character Style** pop-up menu.
    *   On the **Text Styles** panel, select a character style.
    *   On the **Text Styles** panel, on a paragraph style's options menu ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg) , select **Apply "<style name>" to Characters** or **Apply "<style name> to Characters and Preserve Local Formatting** as appropriate.

1.   Select multiple paragraphs.
2.   On the **Text Styles** panel, on the options menu ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg)  of the style you want to apply to the first paragraph, select **Apply "<style name>" Then Next Styles**.

Starting with the applied style, the sequence of **Next Style** settings is applied in order to the selected paragraphs.

For example, if _Style 1_ is followed by _Style 2_, and _Style 2_ is followed by _Style 3_, _Style 1_ is applied to the first paragraph, _Style 2_ to the second, and _Style 3_ to any others you've selected.

1.   Select the text range that contains unwanted local formatting.
2.   Do one of the following: 
    *   To remove only local formatting: On the **Text Styles** panel, select **Reapply Text Styles**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/1L27T36bjS1MWWXQ4z6145/ef9f6897cf692c432d33f5768574b1f2/ReapplyTextStyles_white.svg)  (or select **Text Styles > Reapply Text Styles** on the **Text** menu).
    *   To remove local formatting and any applied character style: On the **Text** menu, select **Text Styles > Reapply Base Styles**.

 Any paragraph style that was already applied to the selection remains applied. 

If a paragraph has a mix of local formatting and character styles, and you apply a different paragraph style to that paragraph, you can control the override behavior of local and character formatting, i.e. whether it is removed or kept.

1.   Select the paragraphs you wish to affect.
2.   On the **Text Styles** panel, on the required paragraph style's options menu ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg) , select the behavior you want: 
    *   **Apply "<style name>" to Paragraphs**—character styles are kept but local formatting (bold, italic, etc.) is removed; paragraph indents and alignment settings are overridden.
    *   **Apply "<style name>" to Paragraphs and Clear Character Styles**—the paragraph style is applied but local formatting (bold, italic, etc.) and character styles are removed.
    *   **Apply "<style name>" to Paragraphs and Preserve Character Formatting**—the style is applied and local formatting (bold, italic, etc.) and character styles are kept; paragraph indents and alignment settings are overridden.
    *   **Apply "<style name>" to Paragraphs and Preserve Local Formatting**—the style is applied and local formatting (bold, italic, etc.) and character styles are kept; paragraph indents and alignment settings are kept.

Two additional **Apply "<style name>" to Characters** options let you apply the chosen paragraph style as a character style to selected text—either removing or retaining any local formatting.

Related behaviors can be adjusted from the app's Settings:

*   **Miscellaneous > Reset Text Styles**

*   [Creating and managing text styles](https://www.affinity.studio/help/text-text-styles-create/)
*   [Removing text styles](https://www.affinity.studio/help/text-text-styles-remove/)
*   [Text style types](https://www.affinity.studio/help/text-text-styles-types/)
*   [Text Styles panel](https://www.affinity.studio/help/panels-text-styles-panel/)
*   [Settings](https://www.affinity.studio/help/workspace-settings/)
*   [Typography Studio](https://www.affinity.studio/help/workspace-typography-studio/)
*   [Using fonts](https://www.affinity.studio/help/addons-using-fonts/)

How would you rate the help you received from this article?
