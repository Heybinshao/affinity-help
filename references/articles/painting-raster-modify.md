---
title: "Modifying raster brushes - Affinity Help Center"
source: https://www.affinity.studio/help/painting-raster-modify/
slug: painting-raster-modify
fetched: 2026-08-06
---

# Modifying raster brushes - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/painting-raster-modify/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Modifying raster brushes

Raster brushes can be modified before you paint to adjust brush and pressure-sensitive attributes.

Brush attributes range from brush size to nozzle rotation.

![Image 1: Size](https://images.ctfassets.net/3p2fxa94bzao/QYeAwo0n5mmIBQgzZx4wN/da816d2dcff0dc30fd7bed97834aff6d/tab1-brush_width_size.png)

![Image 2: Accumulation](https://images.ctfassets.net/3p2fxa94bzao/11oN9Os2sv47mCAKoLQguI/d71c16f1508ecfbbba36d4352d24dd97/tab2-accumulation_brush.png)

![Image 3: Hardness](https://images.ctfassets.net/3p2fxa94bzao/DIGuha9P7sETuW3UWzDJv/2d98541a245a7d4172959344385dfcc4/tab3-hardness_brush.png)

![Image 4: Spacing](https://images.ctfassets.net/3p2fxa94bzao/drOMduBZBWUvZbedqaPp5/1902e2ef700a2b92d45cfe77e604cdcb/tab4-spacing_brush.png)

![Image 5: Flow](https://images.ctfassets.net/3p2fxa94bzao/5n8sltsprH7dxYdUlxC5Nr/b7199aca7a67724a1ca9e46123caaca1/tab5-flow_brush.png)

![Image 6: Shape](https://images.ctfassets.net/3p2fxa94bzao/3gImPiffeIN5BIldheDSb5/795ee9013cf415a1f95db2f5d557f035/tab6-shape_brush.png)

Basic modifications can be made from the tool's context toolbar, while advanced adjustments can be made from the Brushes panel. Both methods set brush properties for subsequent brush strokes, but the latter edits your brush permanently.

The following settings are available in General brush settings:

*   **Size**—sets the default width of the stroke. This can still be overwritten for individual brush strokes using the context toolbar.
*   **Accumulation**—sets the deviation in the opacity or visibility of the stroke as it is painted.
*   **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases.
*   **Spacing**—sets the distance between each nozzle point. A lower percentage results in the nozzles blending together to give a flowing stroke. A higher percentage pushes nozzles away from each other creating a spray-style stroke.
*   **Flow**—controls how fast color is built up under your brush.
*   **Shape**—sets the diameter of the brush nozzles.
*   **Rotation**—sets the angle at which the brush nozzles are drawn. Great for non-round brushes, e.g. for calligraphic effects.
*   **Blend Mode**—changes how the applied color interacts with existing colors on a layer.
*   **Wet edges**—sets the default 'wet edge' behavior of the brush. Check **Custom** and apply a preset or custom profile, which subtly changes how watery the stroke appears.The 'wet edge' behavior builds paint up along the edges of your raster brush stroke, producing a watercolor effect.
*   **Associated Tool**—sets the tool which is automatically selected when the brush is selected. The associated tool's icon will appear next to the brush on the **Brushes** panel.

*   Jitter settings determine the extent to which a chosen controller (Pressure, Velocity, Rotation, etc.) will affect the above General brush settings. Pick a controller from the pop-up menu and click the adjacent Ramp profile icon to select a standard profile from lower thumbnails or create your own using the ramp chart. Move circular nodes to reshape the ramp, add nodes to the ramp by clicking on the line, or select a node to delete a node with the **⌫** key (Mac) / **Backspace** key (Windows), simplifying the ramp. Check **Linear** for straight lines between all nodes; If unchecked (non-linear), nodes are connected using smooth curves.
*   **Scatter X**—sets the deviation in the horizontal position of the stroke the preset will allow as a stroke is painted.
*   **Scatter Y**—sets the deviation in the vertical position of the stroke the preset will allow as a stroke is painted.

Hue, Saturation, and Luminosity Jitter settings affect the brush color, which is set via the **Color** panel. Similarly, Flow Jitter affects brush opacity, also set on the Color panel.

For nozzle control:

*   **Brush Nozzles**—displays the nozzles currently used in the current brush.
*   **Add**—adds an additional nozzle to the preset.
*   **Remove**—deletes the selected nozzle from the preset.
*   Nozzle-specific controller (Pressure, Velocity, Rotation, etc.)—for multi-nozzle brushes, pick a controller from the pop-up menu and click the adjacent Ramp profile icon to select a standard profile from lower thumbnails or create your own using the ramp chart.
*   **Interpolate**—when checked, the quality of the brush tip is improved when affected by the currently set brush tip controller option.

For base texture control:

*   **Base Texture**—displays the underlying texture or pattern for the current brush.
*   **Set Texture**—launches a dialog to add a base texture, as an image, to the brush. For example, to simulate a textured surface like paper or canvas.
*   **Remove**—deletes the base texture from the current brush.
*   **Invert**—creates a negative version of the texture.
*   **Mode**—controls how the base texture contributes to the current brush. Select from the pop-up menu. 
    *   **None**—the base texture is ignored, so only the brush nozzles are used.
    *   **Nozzle**—allows nozzles to build up brush color onto the base texture depending on flow and opacity response.
    *   **Final**—the density of the base texture is kept constant, with no nozzle flow or opacity response.

*   **Scale**—sets the size at which the texture is displayed. A lower percentage will display the texture at a larger size. A higher percentage will display the texture tiled at a smaller size.

Images for base textures should be JPEG or PNG. Any reasonably sized image will be acceptable as the base texture can be scaled (above). We recommend using an 8bit grayscale image with a size greater than or equal to 1024 x 1024 pixels. 16bit brushes will generally be slower with no appreciable increase in quality but can also be used.

*   **Drawing**—controls where the sub brush is drawn in relation to the main brush.
*   **Blending**—controls how the sub brush blends with the main brush.
*   **Sync size**—when checked, sets the default size of the stroke to match that of the main brush.
*   **Sync spacing**—when checked, sets the distance between each nozzle point to match that of the main brush.
*   **Edit**—launches the Sub Brush Editor for the selected nozzle.
*   **Remove**—deletes the selected nozzle.
*   **Add Bitmap**—launches an Open dialog to load another raster nozzle file.
*   **Add Round**—adds a basic untextured brush to which nozzles can be added.

*   **Reset**—returns all stroke settings to those of the saved brush preset.
*   **Save As**—saves the current stroke settings to a new preset.
*   **Close**—exits the dialog and applies stroke settings to the selected preset.

The following settings are available on a pop-up dialog when accessed via right-clicking on the page:

*   **Rotation**—allows to set nozzle rotation.
*   **Blend mode**—sets the blend mode for the strokes.
*   **Size**—sets the stroke size in pixels. Drag the slider or type in a value in the field.
*   **Opacity**—sets the opacity level for the applied strokes. Drag the slider or type in a value in the field.
*   **Hardness**—sets how hard the edges of the brush are. The brush appears softer as the percentage decreases. Drag the slider or type in a value in the field.
*   **Flow**—controls how fast color is built up under your brush. Drag the slider or type in a value in the field.

1.   Do one of the following: 
    *   With the Paint Brush Tool selected, on the context toolbar, click **More**.
    *   On the **Brushes** panel, double-click the brush you would like to alter.

2.   Adjust the settings in the dialog.
3.   Click **Close**.

1.   Do one of the following: 
    *   With the Paint Brush Tool selected, on the context toolbar, click **More** and then **Save As** in the pop-up dialog.
    *   On the **Brushes** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) the brush you would like to rename and select **Edit Brush**. 
    *   On the **Brushes** panel, double-click the brush you would like to rename.
    *   On the **Brushes** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) the brush you would like to rename and select **Rename Brush**. 

2.   Enter the new name for the brush.
3.   Press **⏎** (Mac) / **Return** (Windows) to confirm.
4.   Click **Close** or **OK** in the dialog, depending on the option from those listed above.

1.   **^(ctrl)**-click (Mac) / **right**-click (Windows) the brush you would like to modify and select the option.

1.   Select the **Paint Brush Tool**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/6wRLtJhFhZTJ4aDIQnm8IX/9d71a0d96b84246e136cb94660a5ef88/paint_brush_tool.svg) .
2.   On the **Brushes** panel, select a brush.
3.    Do one of the following: 
    *   From your Finder window (Mac) or File Explorer window (Windows), drag a bitmap file and drop it onto the **Color** panel or the active color selector.
    *   On the **Assets** panel, drag an asset, e.g. a texture, onto the **Swatches** panel, **Color** panel or the active color selector.
    *   On the **Stock** panel, click or drag a photo onto the **Swatches** panel, **Color** panel or the active color selector.

Bitmap loaded brushes are great for stamp-styled strokes, where a single click on the page places the loaded texture. They are often used in placing a watermark, e.g. the author's logo on digital artwork.

*   **Random** (suited to tablet pens and mice)—The value of the attribute will be randomly determined based on the percentage of jitter set. The range of this jitter can be seen by the length of the blue bar in the **General** tab.
*   **Pressure** (suited to tablet pens)—The appearance of the brush stroke will be affected by the amount of pressure applied to the tablet.
*   **Angle** (suited to tablet pens)—The behavior of the brush stroke will be mapped to match the angle of the tablet pen (this varies from 0 to 360°).
*   **Tilt** (suited to tablet pens)—The behavior of the brush stroke will be mapped to match the tilt of the tablet pen (this varies from 0 to 90°).
*   **Rotation** (suited to tablet pens 1, 2)—The behavior of the brush stroke will be mapped to match the tablet pen's barrel rotation.
*   **Cyclic** (suited to tablet pens and mice)—The behavior of the brush stroke will cycle between the range of available values shown on the slider. 3
*   **Velocity** (suited to tablet pens and mice)—The appearance of the brush stroke will be modified as the speed of the tablet pen or mouse movement increases. The range of the jitter can be seen by the length of the blue bar with low velocity on the left and high velocity on the right.
*   **Velocity Inverse** (suited to tablet pens and mice)—The appearance of the brush stroke will be modified inversely as the speed of the tablet pen or mouse movement increases. The range of the jitter can be seen by the length of the blue bar with high velocity on the left and low velocity on the right.
*   **Direction** (suited to tablet pens and mice)—The appearance of the brush stroke will be affected by the direction the pen or mouse is moving in.
*   **Wheel** (suited to tablet pens 1, 2)—The appearance of the brush stroke will change depending on the setting of the wheel on the airbrush pen.
*   **Distance** (suited to tablet pens and mice)—The size of the brush stroke will be affected by the length of the continuous stroke.

1 This setting is only supported on certain Wacom tablet pens.

2 The Apple Pencil does not support this setting.

3 You will need to ensure the **Jitter** setting is sufficiently high enough for the effect to change.

*   [Painting raster brush strokes](https://www.affinity.studio/help/painting-raster-painting/)
*   [Creating custom raster brushes](https://www.affinity.studio/help/painting-custom-raster-brushes/)
*   [Creating multi-brushes](https://www.affinity.studio/help/painting-raster-multi-brushes/)

How would you rate the help you received from this article?
