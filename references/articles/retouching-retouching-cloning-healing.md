---
title: "Cloning and healing - Affinity Help Center"
source: https://www.affinity.studio/help/retouching-retouching-cloning-healing/
slug: retouching-retouching-cloning-healing
fetched: 2026-08-06
---

# Cloning and healing - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/retouching-retouching-cloning-healing/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Cloning and healing

Cloning is the process of duplicating samples from one part of an image to introduce replicated content for creative effect or to repair the original.

The **Clone Brush Tool** copies pixels from one part of an image (or layer) to another. The tool uses a source (shown as a '+' cursor) to clone from; this moves in relation to the tool's cursor (shown as an 'o' cursor) with its position being able to be redefined as you clone from different areas.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/6jLVRVQGppAaGjlqKisg8a/5c5c7fa85776c092bc2e1681fe5d4dce/clonebrush_after.jpg)

After cloning to introduce a cloned object to the image.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/5WmINbh46Mg7rn3vmeChBJ/8354aff20eeda4316525b563fa69e327/clonebrush_before.jpg)

Before cloning.

The clone source can be one of the following context toolbar options:

*   **Current Layer**—pixels on the selected layer only.
*   **Current Layer & Below**—pixels on the currently selected layer and any visible layers beneath (including vector objects and the effects produced by adjustment layers).
*   **Layers Beneath**—pixels on any visible layer beneath the currently selected layer (including those from any vector objects and the effects produced by any visible adjustment layers).

You can define a global _source_ in a secondary open document and paint the sampled pixels into your working document by selecting the clone source option 'Add Global Source'. The **Sources** panel stores all your global sources; you can then select any stored global source and clone from it. Any new documents can make use of the panel's global sources.

The Global source can only be defined from a single pixel layer. To use a document containing multiple layers and/or vector objects, you must flatten the document first.

The Healing Brush Tool paints samples from one part of an image onto another. It's useful for removing defects and for general photo retouching. In many respects it works like cloning, however, it blends the target pixels with the sample pixels by matching the texture, tone, and transparency of the sample pixels with the target pixels.

![Image 3: After](https://images.ctfassets.net/3p2fxa94bzao/4EmDJVTpW82k5rOPxIYbn/53dc6bce4adaa81ec9f86f47bdcfdf3c/healingbrush_after.jpg)

Before and after healing of an unwanted line crossing an image.

![Image 4: Before](https://images.ctfassets.net/3p2fxa94bzao/hPgyIHjIwDVXRcu3sg1Cr/462a0150cf2df38fe41b0386cc53d934/healingbrush_before.jpg)

Before and after healing of an unwanted line crossing an image.

1.   Use the **Layers** panel to either select an existing pixel layer to copy to, or to create a new pixel layer.
2.   In the Pixel Studio ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Clone Brush Tool**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/6wjaMiRZVMjIDgCWz2Nw2k/0f4f71b964e43b2369662b4b43d0e5f8/clone_brush_tool.svg)  or **Healing Brush Tool**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3S7TRAmOosle6WPuWsIzT8/8776a022b9d607cddc9c940dfca08498/healing_brush_tool.svg) .
3.   The tool uses a soft-round brush by default. To use a different brush style, choose one from the **Brushes** panel.
4.   Adjust the context toolbar settings.
5.    To define (or re-define) the cloning source, hold the **⌥** key (Mac) / **Alt** key (Windows) and click on the area you wish to begin sampling from. 
6.   (Optional) Rotate the sample by either using the left and right arrow keys or the **Rotation** control on the context toolbar.
7.   (Optional) Set the scale of the sample by either using the up and down arrow keys or the **Scale** control on the context toolbar.
8.   (Optional) Transform the sample by using the **Flip** pop-up menu on the context toolbar.
9.   Drag on the image to paint the sample.

It is best practice to temporarily hide adjustment layers during the above procedure. This allows you to copy the original image. If the adjustment layers are visible, the _adjusted_ pixels will be permanently applied.

The following can be used:

*   To change brush size, use the **[** or **]** key.

1.   Open the image that you want to copy pixels from and use the **Layers** panel to select the pixel layer that you wish to copy from. To source from vector layers you need to rasterize it first.
2.   In the Pixel Studio ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Clone Brush Tool**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/6wjaMiRZVMjIDgCWz2Nw2k/0f4f71b964e43b2369662b4b43d0e5f8/clone_brush_tool.svg)  or **Healing Brush Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/3S7TRAmOosle6WPuWsIzT8/8776a022b9d607cddc9c940dfca08498/healing_brush_tool.svg) .
3.    To define (or re-define) the cloning source, hold the **⌥** key (Mac) / **Alt** key (Windows) and click on the area you wish to begin sampling from. 
4.   On the context toolbar, click **Add Global Source**.The source is stored, along with other global sources, in the **Sources** panel. The panel can be switched on via the **Window** menu.
5.   Open the image that you want to paint the sample into.
6.   Use the **Layers** panel to either select an existing pixel layer to copy to, or to create a new pixel layer.
7.   In the Pixel Studio ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Clone Brush Tool**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/6wjaMiRZVMjIDgCWz2Nw2k/0f4f71b964e43b2369662b4b43d0e5f8/clone_brush_tool.svg)  or **Healing Brush Tool**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/3S7TRAmOosle6WPuWsIzT8/8776a022b9d607cddc9c940dfca08498/healing_brush_tool.svg) .
8.   The tool uses a soft-round brush by default. To use a different brush style, choose one from the **Brushes** panel.
9.   Adjust the context toolbar settings.
10.   Select a stored global source from the **Sources** panel. If you only have one global source you can simply select the **Global** source from the pop-up menu on the context toolbar instead of using the panel.
11.   (Optional) Select rotate, scale or flip options as described above.
12.   Drag on the image to paint the sample.

*   [Clone Brush Tool](https://www.affinity.studio/help/tools-tools-clone-brush/)
*   [Healing Brush Tool](https://www.affinity.studio/help/tools-tools-healing-brush/)
*   [Removing Blemishes](https://www.affinity.studio/help/retouching-retouching-blemishes/)
*   [Patching](https://www.affinity.studio/help/retouching-retouching-patching/)
*   [Sources panel](https://www.affinity.studio/help/panels-sources-panel/)

How would you rate the help you received from this article?
