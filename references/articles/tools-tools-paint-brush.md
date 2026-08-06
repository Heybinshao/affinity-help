---
title: "Paint Brush Tool - Affinity Help Center"
source: https://www.affinity.studio/help/tools-tools-paint-brush/
slug: tools-tools-paint-brush
fetched: 2026-08-06
---

# Paint Brush Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tools-tools-paint-brush/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Paint Brush Tool

The Paint Brush Tool

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6wRLtJhFhZTJ4aDIQnm8IX/9d71a0d96b84246e136cb94660a5ef88/paint_brush_tool.svg)

 lays down pixels on the page, creating strokes with antialiased edges. This creates a natural transition between the stroke and the surrounding pixels.

The Paint Brush Tool is available by default in Pixel Studio.

It can be added to other Studios. See 'Customizing tools' for details.

Tool shortcut key: **B**.

Its variable width lines can be controlled either by velocity—most useful when drawing with a mouse or touch—or by pressure—for use when drawing with a pressure-sensitive device.

Other raster brush-based tools use similar settings to control the appearance of the applied pixels, although there may be slight variations.

Most brushes use a soft, round nozzle as their default. Alternative styles can be selected from the **Brushes** panel.

When using the Paint Brush Tool on a RAW or image layer, a new nested pixel layer is created with the strokes applied onto it. You will be notified of this via the Assistant's pop up message. This aids non-destructive, layer-based workflows whereby the newly created layer can be switched off from view to investigate the effects of painting quickly. This also aids layer data management as the original image or RAW layer is not rasterized.

The following options can be adjusted on the context toolbar:

*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/1DZ3BiVUNw49gMKmpfsxjY/cd1aedf8a4cd6086f5386c7898ba6846/slider_width.svg) **Size**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3xN42iDOBeb6NfoMb1Nb3S/676173212d209b96e478c68304a4b2b5/slider_opacity.svg) **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6YT2BTrlyBpYlL2uIKpJtk/b378569b35626974ee7c0f69e47176c7/slider_flow.svg) **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3jeAVEQerphjqYhdiT8BLR/00fd4f48c15e79b94b796a70cf1d9838/slider_hardness.svg) **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
*   **More**—click to display the [Brushes](https://www.affinity.studio/help/painting-raster-modify/) dialog to access advanced brush settings.
*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/2G6RXXZFvI6HUYZid36cJo/c0e6d0e34e179a4a70883fb3b37709c7/forcepressure.svg) **Force pressure**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
*   **Stabilizer**—enables stroke stabilization using either a **Rope mode**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/1dQYbLS5to2P0NEVKWr05P/ed77646476b191fed3c1e20aaa13921d/stabiliser_rope.svg)  or **Window mode**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/4wgNDHLUHFBM5dfxTQYqrO/ae9cf7f82a75be64e0cc071f94e56a04/stabiliser_window.svg) ; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing **Rope****Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
*   **Blend Mode**—changes how the stroke's color interacts with existing colors on a layer.
*   ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/2Jk9PNrTpGzTAFr2oVmFcS/b539869ec6cc10a4455b3728c9837382/wetedges.svg) **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.
*   ![Image 10](https://images.ctfassets.net/3p2fxa94bzao/33nEL6S3iwlM1lNgAK4ZdT/a7fb128eead8d77dee8c5a55e60beedc/protectalpha.svg) **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions, only those that are opaque.
*   ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/48gU5vr3XwFWtBjwhAJWTo/28e1a43a4063087555940fbc383932d4/reset-global.svg) **Reset**—resets brush settings to their defaults.
*   ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/7eblP76vdFdrp2uaZ3g2uC/4609ca56c51ddfe4b1aeb480e5ac5d9e/view.svg) **Symmetry settings**—offers various symmetry line control options.
    *   **Lines**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The center axis point can be repositioned by click-dragging it.
    *   **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
    *   **Lock**—when checked, prevents the symmetry line from being moved.

The following settings are available on a pop-up dialog when accessed via right-clicking on the page:

*   **Rotation**—allows to set nozzle rotation.
*   **Blend mode**—sets the blend mode for the strokes.
*   **Size**—sets the stroke size in pixels. Drag the slider or type in a value in the field.
*   **Opacity**—sets the opacity level for the applied strokes. Drag the slider or type in a value in the field.
*   **Hardness**—sets how hard the edges of the brush are. The brush appears softer as the percentage decreases. Drag the slider or type in a value in the field.
*   **Flow**—controls how fast color is built up under your brush. Drag the slider or type in a value in the field.

The tool can be associated with a particular brush when editing it in the **Brushes** panel. For more information, see the [Modifying raster brushes](https://www.affinity.studio/help/painting-raster-modify/) topic.

*   To select the Paint Brush Tool, press the **B** key.
*   With any brush tool selected, you can quickly decrease or increase the size (width) of your brush by holding the **⌃(ctrl)⌥** keys (Mac) / **Ctrl**+**Alt** keys (Windows) then dragging left or right, respectively. If the brush tool has a hardness attribute, this can be adjusted in a similar way by holding the **⌃(ctrl)⌥** keys (Mac) / **Ctrl**+**Alt** keys (Windows) then dragging up or down.
*   With any brush tool selected in Pixel Studio, you can quickly change the opacity of your brush using numerical keys. For more information, see the [Transparency](https://www.affinity.studio/help/clr-transparency/) topic.
*   When accessed via right-click on the page, holding the **⇧** key (Mac) / **Shift** key (Windows) restricts the on-dialog **Rotation**setting to 45°. Double-click the rotation point to reset it.
*   To temporarily switch to the Move Tool, press **⌘** key (Mac) / **Ctrl** key (Windows) and drag.

*   [Painting raster brush strokes](https://www.affinity.studio/help/painting-raster-painting/)
*   [Context toolbar](https://www.affinity.studio/help/workspace-context-bar/)

How would you rate the help you received from this article?
