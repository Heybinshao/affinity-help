---
title: "Copying and pasting - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-copy-paste-options/
slug: object-control-copy-paste-options
fetched: 2026-08-06
---

# Copying and pasting - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-copy-paste-options/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Copying and pasting

There are multiple ways to copy and paste content. Pasted content can include/exclude specific copied object properties.

![Image 1: Paste options](https://images.ctfassets.net/3p2fxa94bzao/5Tt7JbZmQvdbuLGEnnPNUt/ec0305dfbab9c68b106203d19181a391/pasteOptions.png)

(A) Paste, (B) Paste Inside, (C) Paste Style (Stroke, Fill and Outer Shadow), (D) Paste FX (Outer Shadow layer effect only), (E) Paste without Format (retains target formatting), (F) Paste Special (Windows only); pastes as a choice of clipboard formats such as SVG, Device Independent Bitmap, etc.

You can copy content throughout the app or externally to third-party apps. Both need a reciprocal pasting operation to add the content to the target page.

As well as the commonly used Paste command, other paste commands can be used to selectively control which properties will be included/excluded from the pasted content.

| Paste option | Description |
| --- | --- |
| Paste | Pastes objects, preserving the copied object's look and formatting. |
| Paste Inside 1 | Pastes (and clips) an object inside another object or layer. |
| Paste Style | Pastes an object's stroke, fill and layer effect(s) and text formatting styles 2, 3, 4 to another object, text or layer. |
| Paste FX | Pastes only layer effect(s) to another object or layer. |
| Paste without Format | Pastes unformatted text by stripping the formatting from the copied text. When pasted, the target text will retain its text formatting. |
| Paste Special (Windows desktop only) | Pastes copied content into and out of Affinity using a choice of clipboard formats that show dynamically by the type of content copied externally or within Affinity. |

1 If pasting a single image inside a picture frame, it is positioned within the frame's bounding box and the frame's scaling behavior (Scale to Max Fit, Scale to Min Fit, Stretch to Fit, or None) is applied to it. If pasting multiple images at once, they are clipped by the picture frame and may be positioned outside of its bounding box.

2 Use the Style Picker Tool instead if you want to paste only some of the copied style attributes, e.g. paragraph settings but not character settings and other object styles.

3 If the copied text contains text ranges with different formatting, the formatting of its first character will be pasted.

4 If copied text's formatting includes settings that are incompatible with the target text, the incompatible settings will not be pasted. For example, horizontal centering is ignored when pasting onto a range _within_ a left-aligned paragraph.

If text is selected in Affinity and you paste a URL beginning with a protocol (e.g. https:// or http://), the selected text is converted into a hyperlink to that URL.

When using Paste Special you will be offered a choice of clipboard formats to use for pasting. These options are dependent on the type of content copied and will dynamically change accordingly.

For example, for copied curves and shapes your formats are:

*   image/x-inkscape-svg 1
*   SVG 1
*   Portable Document Format
*   PNG
*   Device Independent Bitmap
*   Affinity Nodes 2

For text, the available choices will be different, and may include:

*   Unicode text
*   Rich Text Format
*   Affinity Story 2

1 These clipboard formats are available when **Copy items as SVG** is enabled [(via **Settings** (General section)].

2 These are proprietary Affinity formats that retain the highest level of fidelity to the original copied object. This format is used by default when copying and pasting between Affinity documents.

1.   Select one or more objects or layers.
2.   On the **Edit** menu, select **Copy** or **Cut**.

1.   Select one or more objects or layers.
2.   On the **Edit** menu, select one of the paste options.

Related behaviors can be adjusted from [the app's settings](https://www.affinity.studio/help/workspace-settings/):

*   **General > Copy items as SVG** copies objects in SVG format in readiness for pasting to external apps.
*   **General > Preserve Unicode breaks when copying plain text** preserves paragraph markers, preventing the conversion of line breaks to line feeds in copied text that is pasted to external apps.

*   [Applying layer effects](https://www.affinity.studio/help/layer-fx-create-layer-fx/)
*   [Styles](https://www.affinity.studio/help/object-control-styles/)
*   [Layer clipping](https://www.affinity.studio/help/layers-layer-clip/)
*   [Keyboard shortcuts for general editing](https://www.affinity.studio/help/workspace-shortcuts-editing/)

How would you rate the help you received from this article?
