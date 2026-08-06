---
title: "Using multi-level lists - Affinity Help Center"
source: https://www.affinity.studio/help/text-text-multi-level-lists/
slug: text-text-multi-level-lists
fetched: 2026-08-06
---

# Using multi-level lists - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/text-text-multi-level-lists/

For multi-level lists, you can set a different format of list item marker (symbol, text, or number) and indentation for each level.

![Image 1: A multi-level list](https://images.ctfassets.net/3p2fxa94bzao/4ru4bIfWhImPvktBnO8Lig/5a80a4ccf3118122ec1890533b146116/multilevel.png)

Levels are usually **subordinate** to each other: Level 1 (first), Level 2 (second), Level 3 (third), and so on—each less important than the last. For example, the multi-level list shown above is arranged at three levels. (An item at Level 1 is **superior** to items at Level 2, Level 3 and so on.)

The flexibility of Affinity's multi-level bullet and numbering system means that you have full control over what gets displayed at each level. For this reason, no common numbering schema needs to exist between levels, i.e. the list could equally be prefixed with a different symbol, text prefix, or number combination at each level.

When you apply a multi-level list to paragraphs as local formatting, the paragraphs will be set to Level 1 by default. Unless you use text styles, you'll have to change to levels 2, 3, 4 and so on and other settings as required for that list. This is time consuming and prone to introducing inconsistencies.

For this reason, in complex documents it's recommended that you add list formatting to a hierarchy of text styles and apply those styles to your lists. It's easier to edit your text styles for lists knowing that all your lists will be updated automatically.

Markers in a multi-level list can include numbers or text from their direct superiors. For example, a list item labelled _4._ may have subordinate items like _4a._, _4b._, and so on.

To do this, you type special character sequences into the text that defines a subordinate level's marker. In this case, that text would be _\1\#.\t_, in which:

*   \1—is the number/letter of the current list item's superior item at level 1. Equally, \2, \3 and so on represent the number/letter of the current item's ancestor at levels 2, 3 and so on, respectively.
*   \#—is the subordinate item's number/letter.
*   \t—is a tab character, which we're using to indent Level 2 items and space out their markers and text.

If you're working on long publications, you may have assigned text styles (Heading 1, Heading 2, etc.) to format paragraphs.

You can modify the text styles to include list formatting so that headings or paragraphs are automatically numbered. This avoids the need to manually format headings or paragraphs as lists.

For example, headings and paragraphs in technical and legal publications are typically prefixed by numbers for easy reference. The advantage of using a style-driven approach is that you can let the numbering take care of itself as you apply text styles.

Each document you create automatically includes text styles for multi-level lists up to three levels deep, which address simple but common formatting needs. The styles are named _Bulleted_ or _Numbered_ with a numeric suffix representing each one's list level.

These styles can be modified to suit your requirements. You can create new text styles to implement formatting for any additional levels needed for your lists.

Let's say we need text styles to format two levels of heading. We've created two paragraph styles from scratch, named _Numbered Heading 1_ and _Numbered Heading 2_.

In Numbered Heading 1's **Bullets & Numbering** settings, we set **Type** to _1,2,3,4…_, **Level** to _1_, and **Text** to _\#.\t_.

Paragraphs using this style will be numbered 1., 2., 3. and so on.

In Numbered Heading 2's Bullets & Numbering settings, we set **Type** to _a, b, c, d…_, **Level** to _2_, and **Text** to _\t\1\#.\t_.

Paragraphs using this style will be numbered 1a., 1b., 1c., 2a., 2b., and so on.

Finally, we set Numbered Heading 1's **Next Level** setting to _Numbered Heading 2_ to establish a hierarchy between these styles.

Text styles for additional list levels can be created from scratch or by selecting **Create Style Based on "<style name>"** on a style's options menu

![Image 2](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg)

. For each style, set **Next Level** based on your required hierarchy of styles.
