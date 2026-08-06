---
title: "Hyphenation - Affinity Help Center"
source: https://www.affinity.studio/help/text-hyphenation/
slug: text-hyphenation
fetched: 2026-08-06
---

# Hyphenation - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/text-hyphenation/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Hyphenation

Affinity can automatically hyphenate words that are split across lines, and provides extensive control of when and where hyphenation occurs.

The auto-hyphenation feature recognizes and corrects lines which would otherwise be too ragged or use overly large word spacing. This results in better fitting and neater frame text.

You can also introduce your own hyphens manually at hyphenation points in frame text.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/1fC3r1bZXYn0VBAdJOYqDl/ff92ed7856c3215514f61d6f3c0d08b8/hyphenation_after.jpg)

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/1qGS6AqVeCcPUiqwKg60Sg/d59a6fedabf259b6695d4fbbc8652613/hyphenation_before.jpg)

Words have predefined **hyphenation points** at which hyphenation will occur, specified in language-specific hyphenation dictionaries. Each hyphenation point has a value weighting associated with it.

For example, the hyphenation point in the middle of the word _yellow_ (to hyphenate it as "yel-low" across lines) has a score value of 1, i.e. _yel1low_. For "acc-ommo-date", the hyphenation points and values are _acc2ommo5date_.

A higher **Minimum Score** results in less frequent hyphenation.

Affinity can also prevent splitting words that are too short or would leave too few characters at front or back.

**Hyphenation zones** can be used to affect how ragged or loose text can be. Hyphenation points will be ignored if they fall within these hyphenation zones. Thus setting a wider zone will hyphenate less often.

Zones are measured from the frame text's right indent, ignoring alignment or justification.

Several types of hyphenation zone can be applied in different situations. They work in combination. You can prevent hyphenation in each situation by setting the corresponding zone to a very large number (e.g., 100 cm), or you can set a smaller number so that hyphenation can still be used if the text would be very ragged or loose without it.

Hyphens can be manually inserted into specific words irrespective of whether auto-hyphenation is enabled.

Perhaps a word you are using breaks onto a new line at an undesirable position. A **soft hyphen** inserted into the word will force the word to always break at a manually chosen hyphenation point.

The soft hyphen will display automatically when the word is broken over lines, but is invisible when the word is unbroken.

Alternatively, it may be desirable that a manually hyphenated word is never broken across lines. A **non-breaking hyphen** can be inserted in this situation to keep both components of the word on the same line.

Successful hyphenation relies on whether:

*   an appropriate hyphenation dictionary for the text's language is installed.
*   the proper hyphenation language is selected on the **Character** panel's **Language** section.
*   good auto-hyphenation settings are applied on the **Paragraph** panel's **Hyphenation** section.

Hyphenation settings, scores and zones are paragraph attributes, while spelling/hyphenation language is a character attribute.

*   On the **Character** panel's **Language** section, set **Hyphenation** to the required language.

By default, text's selected language for **Spelling** is also used for hyphenation.

On the **Paragraph** panel's **Hyphenation** section:

1.   Enable **Use auto-hyphenation**.
2.    (Optional) Adjust auto-hyphenation settings as required: 
    *   **Minimum score**—the amount of extra space at the end of each line that is considered acceptable. If the amount of extra space exceeds this value, auto-hyphenation will try to split words to reduce the excess. Try incrementing values upwards from 1 to experiment.
    *   **Minimum word length**—the minimum number of characters that a word must have before it is considered valid to hyphenate the word at the end of a line.
    *   **Minimum prefix**—determines the minimum number of prefixed letters each part of a word must contain if the word is split by auto-hyphenation.
    *   **Minimum suffix**—determines the minimum number of suffixed letters each part of a word must contain if the word is split by auto-hyphenation.
    *   **Max consecutive hyphens**—prevents too many consecutive lines from ending with a hyphen.
    *   **Hyphenation zone**—defines an area from the right edge of frame text where hyphenation rules are ignored. This always applies.
    *   **Capital zone**—defines the amount of space allowed before hyphenation begins where words are in all capitals.
    *   **Paragraph end zone**—defines the amount of space allowed at the end of a paragraph before hyphenation begins.
    *   **Column end zone**—defines the amount of space allowed at the end of a column before hyphenation begins.

*   On the **Text** menu, hover over **Insert > Dashes and Hyphens**, then select **Soft Hyphen** or **Non-Breaking Hyphen**.

Soft hyphens are usually only visible when containing words are split across lines at the corresponding positions. Their positions can be confirmed by enabling **Show Special Characters** on the **Text** menu.

Auto-hyphenation has no effect on words that contain a soft hyphen. You can insert a soft hyphen at the beginning of a word to prevent it being hyphenated altogether.

To prevent the affected range from breaking (for any reason other than a soft hyphen), enable **No break** on the **Character** panel's **Position & Transform** section.

*   [Managing spelling and hyphenation dictionaries (Desktop only)](https://www.affinity.studio/help/text-hyphenation-installing/)
*   [Frame text](https://www.affinity.studio/help/text-frame-text/)
*   [Character panel](https://www.affinity.studio/help/panels-character-panel/)
*   [Paragraph panel](https://www.affinity.studio/help/panels-paragraph-panel/)

How would you rate the help you received from this article?
