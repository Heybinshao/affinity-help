---
title: "Painting pixel selections - Affinity Help Center"
source: https://www.affinity.studio/help/selections-selections-brush/
slug: selections-selections-brush
fetched: 2026-08-06
---

# Painting pixel selections - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/selections-selections-brush/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Painting pixel selections

Using the **Selection Brush Tool** you can define a selection by painting on your page.

By default the Selection Brush Tool is set to expand the selection to include similar color value pixels to those already selected. In other words, the selection will grow up to high contrast edges within the image.

![Image 1: Expansion](https://images.ctfassets.net/3p2fxa94bzao/6RoCLuUKnMLwnTBv4SHdSK/5f728cc50b54ff9a0ab45f78b22ca465/selections_brush_after.jpg)

Difference in selection method: expansion method.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/6eSaViTxCMeLMkzsyVAKXi/1ebe05cf6e52ed22aac00f687a6f98f2/selections_brush_before.jpg)

Before painting a selection.

The number of pixels selected is determined by the size of the brush in two ways:

*   A larger brush size will paint a larger area in one stroke and therefore more pixels will be selected.
*   A larger brush size will give a larger sample size in which to determine how far the selection should expand when selecting similar color value pixels.

This makes selecting an area of similar color and tone effortless.

The selection will only expand to pixels with similar color values if they are adjacent to the stroke painted. To select a separate area, you must start another stroke within the new region.

As an alternative to the expansion method detailed above, the **Selection Brush Tool** also offers a non-expansion method of selection. This method will only select pixels which are under the brush when the stroke is painted. To use this method, on the context toolbar, toggle **Snap to edges**

![Image 3: Snap to edges](https://images.ctfassets.net/3p2fxa94bzao/2Aeq2yyZaTJcJpC38qzshX/fbdc35231d25572a0fa1693970cc4a45/snap_to_edges.svg)

 option off.

![Image 4: Expansion](https://images.ctfassets.net/3p2fxa94bzao/6RoCLuUKnMLwnTBv4SHdSK/5f728cc50b54ff9a0ab45f78b22ca465/selections_brush_after.jpg)

Difference in selection method: expansion method.

![Image 5: Non-expansion](https://images.ctfassets.net/3p2fxa94bzao/vOblvcX2OBevB0j1aVeOT/4a512b351f4f2b9732cece9cf6a28bee/selections_brush_nonexpand.jpg)

Difference in selection method: non-expansion method.

Pixels along the edge of a selection made using the Selection Brush Tool are fully opaque by default, which may result in a ragged edge when the selection is used as a mask or to composite a cut-out against a new background, for example.

If the area being selected has a relatively simple edge, turn on **Soft edges**

![Image 6: Soft edges](https://images.ctfassets.net/3p2fxa94bzao/6pFBLZ5I5C3dLnwfqv0HnR/397e8ba7dcab32b84a4ec2f1a8da1522/soft_edges.svg)

 on the context toolbar and then make your selection. The tool will antialias the selection's edge; some pixels will be semi-transparent, giving an appearance that is less sharp yet often more desirable.

![Image 7: Soft edges comparison](https://images.ctfassets.net/3p2fxa94bzao/2D6nS3v4gIIF2E7nzg51pw/368a2be2b2e4dce1881f97c440b12800/selections_brush_soft_edges.jpg)

Edge fidelity of a selection made with the Soft edges option disabled (left) and enabled (right).

For complex edges, such as finely detailed hair or fur, better results can be achieved using the tool's Refine option. See Refining pixel selection edges topic to learn more.

In the Pixel Studio

![Image 8](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg)

, with the **Selection Brush Tool**

![Image 9](https://images.ctfassets.net/3p2fxa94bzao/2RPHHEjmTXhZrgZfZUSPO8/644f0916603d39b4ce0658e0f0125fa5/selection_brush_tool.svg)

 selected:

1.   Adjust the context toolbar settings. (To learn more, see the Selection Brush Tool topic.)
2.   Drag on your page.

In the Pixel Studio

![Image 10](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg)

, with the **Selection Brush Tool**

![Image 11](https://images.ctfassets.net/3p2fxa94bzao/2RPHHEjmTXhZrgZfZUSPO8/644f0916603d39b4ce0658e0f0125fa5/selection_brush_tool.svg)

 selected, do any of the following:

*   Switch the tool's working **Mode** on the context toolbar. **Add** grows the existing selection or creates a second selection area; **Subtract** paints away from an existing selection.
*   Change the brush **Size**.

*   In the Pixel Studio ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , with the **Selection Brush Tool**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/2RPHHEjmTXhZrgZfZUSPO8/644f0916603d39b4ce0658e0f0125fa5/selection_brush_tool.svg)  selected, on the context toolbar, ensure the **Snap to edges**![Image 14: Snap to edges](https://images.ctfassets.net/3p2fxa94bzao/2Aeq2yyZaTJcJpC38qzshX/fbdc35231d25572a0fa1693970cc4a45/snap_to_edges.svg)  option is off.

The following modifier keys can be used to aid in the creation of selections:

*    For Mac: The **⌃(ctrl)** key automatically adds areas to the current selection. 
*    The **⌥** key (Mac) / **Alt** key (Windows) automatically removes areas from the current selection. 
*   For Windows: Drag with left and right button down to automatically add areas to the current selection.
*    To change brush size, press the **⌃(ctrl)⌥** keys (Mac) / **Ctrl**+**Alt** keys (Windows) and drag on the page. Dragging left or right will also decrease or increase the brush size, respectively. Alternatively, use the **[** or **]** keys. 
*   To temporarily switch to the Move Tool, press **⌘** key (Mac) / **Ctrl** key (Windows) and drag.

*   [Selection Brush Tool](https://www.affinity.studio/help/tools-tools-selection-brush/)
*   [Creating pixel selections](https://www.affinity.studio/help/selections-selections-create/)
*   [Modifying pixel selections](https://www.affinity.studio/help/selections-selections-modify/)
*   [Refining pixel selection edges](https://www.affinity.studio/help/selections-selections-refine/)
*   [Flooding pixel selections](https://www.affinity.studio/help/selections-selections-flood/)

How would you rate the help you received from this article?
