---
title: "Gradient fills - Affinity Help Center"
source: https://www.affinity.studio/help/clr-gradient-editor/
slug: clr-gradient-editor
fetched: 2026-08-06
---

# Gradient fills - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/clr-gradient-editor/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Gradient fills

The Fill Tool lets you draw a simple color gradient or a solid, bitmap or hatch fill across objects and layers.

Gradients can be applied to pixel layers, fill layers, adjustment layers, live filter layers, layer masks, and the fills and strokes of vector content.

The created fill path can be edited directly on the object to:

*   introduce more than two colors along the path.
*   vary opacity along the path.
*   reposition added colors or control color transitions.

You can also apply a more complex gradient via a Gradient Editor.

If needed, you can precisely define the fill path via the color swatch on the tool's context toolbar. This should be done with no handles selected.

However, you might want to apply a more complex fill, introducing more than two colors along the gradient path, adjust where each color is positioned and/or control color transitions. You can do this in two ways:

*   Directly on the gradient's fill path.
*   Via the tool's context toolbar.

Using the former, you modify the gradient by eye; the latter lets you design with precision and absolute control.

If you apply a gradient directly to your image's layer, you'll destroy the layer content. Instead, apply gradients to a separate pixel, fill, adjustment, filter, mask or vector layer. With Fill layers, your gradient path will additionally remain editable.

![Image 1: Gradient and bitmap fill examples](https://images.ctfassets.net/3p2fxa94bzao/7n1MTVQrGn6q7RcYB8b7WH/2ae71a67f8fcae3ba51e4d6bde22b551/gradient.png)

(From left to right) Elliptical, Radial, Linear, Conical, and Bitmap fill types applied to a basic shape.

1.   Select layer content or an object.
2.   Select the **Fill Tool**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/4AbVamuwkW3QLOJP3GQiV1/254daa0b4c76a58d6ef299e8068f0519/fill_tool.svg) .
3.   On the context toolbar: 
    *   If you selected an object, select either 'Stroke' or 'Fill' from the **Context** pop-up menu.
    *   Select a fill type from the **Type** pop-up menu.

4.   Drag across the selected layer/the selected object's stroke or fill.

Select and drag an end stop on the path to change the length and direction of the path. End stops can be recolored and be given reduced opacity from the **Color** panel.

Create your own gradient fills by clicking the color swatch, adjacent to the Type pop-up menu, on the context toolbar.

For preset gradient fills, use the Swatches panel.

You can pick up color as you design by holding the **⌥** key (Mac) / **Alt** key (Windows) and dragging.

1.   Use the **Move Tool** to select an object.
2.   Select the **Fill Tool**.
3.    Do one of the following: 
    *   For Mac: From your Finder window, drag the file of choice and drop it onto either the **Swatches** panel, **Color** panel or the Foreground/Background color selector.
    *   For Windows: From your File Explorer window, drag the file of choice and drop it onto either the **Swatches** panel, **Color** panel or the Foreground/Background color selector.
    *   On the **Assets** panel, click an asset, e.g. a texture, shape or other.
    *   On the **Stock** panel, click one of the photos from your search results.

4.   Use the context toolbar settings and the tool's nodes to modify the fill as required.

Alternatively, with the **Fill Tool**, you can select **Bitmap** from the **Type** pop-up menu on the context toolbar, then navigate to the image you will use to fill.

Instead of using the **Fill Tool**, you can also create a bitmap fill using the **Move Tool**. To do so, drag the file of choice from your Finder window (Mac) or File Explorer window (Windows) and drop it onto the areas suggested above.

1.   Select an object.
2.   Select the **Fill Tool**.
3.    Do one of the following: 
    *   For assets: from the **Assets** panel, select your chosen asset's thumbnail.
    *   For stock images: from the **Stock** panel, select a chosen image.

4.   Drag to reposition the fill origin, or drag on either axis nodes to adjust the scaling and rotation of the bitmap. Hold down one finger to constrain the angle to 45°.

1.   With the **Fill Tool** active, make a selection.
2.   On the context toolbar, click **Rotate gradient** to change the orientation of the fill at 90° clockwise intervals.
3.   Enable **Maintain aspect ratio** to ensure the bitmap fill is not stretched or squashed when edited.
4.   Set the **Extend** and **Quality** options as desired. The former option controls how the tile that makes up the bitmap is presented; the latter how the bitmap fill is resampled on object resize.
5.   Check **Scale with object** to allow for stretching or shrinking of the bitmap fill while resizing. Leave it unchecked to ensure stretching or shrinking isn't taking place thus preserving the texture of the image.

With the **Fill Tool** selected, click the content with a gradient fill applied and then do any of the following:

*   Click on the gradient path to add a stop.
*   Click a stop to select it. Selected stops display larger than other stops.
*   Drag a stop to reposition it along the gradient path. End stops can be repositioned (by dragging) to extend or contract the gradient's length; the angle of the gradient can also be changed by dragging.
*   Drag a midpoint marker to adjust the spread of colors between two color stops.
*   Apply a color (or opacity or noise value) to a selected stop from the **Color** panel.
*    Delete a selected stop by pressing the **⌫** key (Mac) / **Backspace** key (Windows). 

When you scale or shear an object with a linear or radial gradient applied, the gradient will intelligently reapply itself to fit the modified object's new proportions.

1.   To open the Gradient Editor, do one of the following:
    *   With the **Fill Tool** selected, click an object or layer content. Deselect any selected stops, select the color swatch on the context toolbar, then click the **Gradient** option.
    *   On the **Swatches** panel, **^(ctrl)-click** (Mac) / **right-click** (Windows) the gradient swatch and select **Edit Fill**.

2.   Modify your gradient using the following settings: 
    *   **Type**—determines the gradient type (linear, elliptical, etc.) via a pop-up menu.
    *   **Position**—controls the position of the stop along the gradient from left (0%) to right (100%), with 50% representing the central point.
    *   **Mid Point**—adjusts the spread of colors between the selected color stop and the stop to its right.
    *   **Color**—click the color swatch to display a pop-up panel where you can modify the selected stop's color (including noise value).
    *   **Opacity**—controls how see-through the stop is. 100% represents fully opaque, 0% represents fully transparent.
    *   **Insert**—adds a new stop between a selected stop and the stop to its right. The stop adopts the color at its new position.
    *   **Copy**—duplicates the selected stop, positioning it between the selected stop and the stop to its right.
    *   **Delete**—removes the selected stop from the gradient.
    *   **Reverse**—the gradient is reversed, i.e. like a mirror image.

It is possible to rescale a bitmap fill by either restricting or allowing for the bitmap fill to grow or shrink when transforming, depending on the desired effect. One benefit here is that it is possible to leave the bitmap image and its texture unaffected by shrinking or stretching.

![Image 3: Scale with Object](https://images.ctfassets.net/3p2fxa94bzao/40FgFzPbrJTF2PJN3njuk2/e1129f38f5240399fcc7215612cfba23/scale_with_object.png)

A bitmap fill's texture unaffected by stretching a square object.

When creating a bitmap fill, the image will be placed as a tiled or repeating pattern that fills the selected area.

When you scale or shear an object with a linear, radial or conical gradient applied, the gradient will automatically reapply itself to fit the modified object's new shape. For shearing, dashed correction paths are applied to the gradient to indicate the gradient transformation.

The paths can be edited to control the shear and scale on the fill if needed—the path and stop can also be removed to ignore the gradient transform if needed.

![Image 4: Unsheared and sheared rectangle showing correction paths](https://images.ctfassets.net/3p2fxa94bzao/7KleC8MHsYOgZhawZESO3l/f8ca3faa4297bdaa4174edcb3a3f4bb2/fillhandles.jpg)

Unsheared and sheared rectangle (the latter showing correction paths)

This is also important when transforming two-dimensional objects onto an isometric grid plane as the gradient also needs to be intelligently transformed onto the plane, along with the shape's outline. On the transformed object, a dashed correction path is automatically applied as before.

![Image 5: Transforming object onto isometric plane](https://images.ctfassets.net/3p2fxa94bzao/2fk6zwAqBO09VmFlOlFauT/04b44e805abe2ebc60e3bc3e6576628c/gradient2.png)

Circle with radial fill transformed onto an isometric plane (Front Plane), showing a single correction path.

*   Double-click the correction end stop to remove the correction path.

When using the tool, the following shortcuts can be used:

*   Double-click a stop to reset the fill back to be true linear, radial, elliptical or conical.
*   For Mac: Double-click while pressing the **⌃** key to reset the fill scale.
*   **⇧** key (Mac) / **Shift** key (Windows) aligns the path to an axis.
*   **⌘** key (Mac) / **Ctrl** key (Windows) repositions the gradient without affecting its length or direction. Use the **⇧** key (Mac / **Shift** key (Windows) additionally to constrain along an axis.
*   For Mac: **⌃****⌘** keys move the path independently of another path.
*   For Mac: **⌃** key constrains the path.
*   For Windows: Additional press of right-hand mouse button constrains the path.

*   [Fill Tool](https://www.affinity.studio/help/tools-tools-gradient/)
*   [Selecting colors](https://www.affinity.studio/help/clr-selecting-clr/)
*   [Transparency](https://www.affinity.studio/help/clr-transparency/)

How would you rate the help you received from this article?
