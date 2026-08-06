---
title: "Patch Tool - Affinity Help Center"
source: https://www.affinity.studio/help/tools-tools-patch/
slug: tools-tools-patch
fetched: 2026-08-06
---

# Patch Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tools-tools-patch/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Patch Tool

The Patch Tool

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/1WiDOmOcTbepbc53hU45Ne/52f362ed2ba778c925d9299f937112ed/patch_tool.svg)

 allows you to repair a more extensive area of an image by selecting pixels and replacing them from another target area.

![Image 2: Patch Tool](https://images.ctfassets.net/3p2fxa94bzao/8gcFwGybG8GtXRsgSWkaC/65e7e591c0b34fdcf65e44b5400e4913/patchTool.jpg)

The Patch Tool is available by default in Pixel Studio.

It can be added to other Studios. See [Customizing tools](https://www.affinity.studio/help/workspace-customizing-tools-panel/) for details.

The tool makes it easy to substitute pixels of one area with those sampled from another, more pleasing region. For example, as seen in the example above, the **Patch Tool** may be used to remove and replace imperfections under people's eyes in portraiture.

Context toolbar settings are remembered when switching between documents.

The following options can be adjusted from the context toolbar:

*   Mode—determines how your selection develops. Choose from: 
    *   **New**—cancels all current selections and creates a new selection.
    *   **Add**—adds areas to the current selection. If there is no selection in place, a new selection will be created.
    *   **Subtract**—removes areas from the current selection.
    *   **Intersect**—a new selection area is created from the overlap between the newly added selection area and the current selection.

*   **Selection is source**—if this option is off (default), the selection is the target area where pixels will be replaced. When selected, the selection is the source area from where pixels will be copied.
*   **Texture Only**—if this option is off (default), hue information from the source area is preserved and the target area's hue will update accordingly. When selected, hue information from the source area is disregarded and the target area's hue will remain unchanged.
*   **Transparent**—if this option is off (default), the source area is placed on the target area as fully opaque. When selected, the source area is placed one the target area with varying transparency depending on the color value of individual pixels.
*   Source—the source determines the layer(s) from which the pixels are sampled. Select from the pop-up menu. The 'Global' option enables patching using pixels previously sampled in another document (pixel layer only).
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/23KckJCXRxlLbsm2LBA38c/5ae5e79fcb9a6d3e50df74bfa4e8461e/add_global_source.svg) **Set Global Source**—sets the currently defined sample origin as a global source for use in other images.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/3WhxupTfhFgTPOi2Cq10DP/7875afb205755ff608969ea9d0476a87/slider_rotation.svg) **Rotation**—sets the degree of rotation applied to the sample. The result can be previewed inside the selection. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/YtIstAJxagUs6S0hV3kMs/9be82fc1107efe1926df3622571773f7/scale.png) **Scale**—sets the scale of the sample between 1% and 1000%. Type directly in the text box or drag the pop-up slider to set the value. The result can be previewed inside the selection.

1.   On the **Layers**panel, select the layer to work on.
2.   Select the **Patch Tool**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/1WiDOmOcTbepbc53hU45Ne/52f362ed2ba778c925d9299f937112ed/patch_tool.svg) .
3.   On the context toolbar, ensure **Selection is source**is off (default). This makes your selection the **target**— the area to be replaced.
4.   Drag around the area you want to repair to create a selection.
5.   Click and drag the selection to the area of the image you want to sample from. A preview of the replacement appears inside the selection as you drag.
6.   Release to apply the patch.

To reverse the workflow — selecting the source area first — enable **Selection is source** on the context toolbar before drawing your selection, then drag to the area you want to replace.

*   To select the Patch Tool, press the **J** key. This key cycles through related tools.

*   [Patching](https://www.affinity.studio/help/retouching-retouching-patching/)
*   [Context toolbar](https://www.affinity.studio/help/workspace-context-bar/)

How would you rate the help you received from this article?
