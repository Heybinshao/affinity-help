---
title: "Background Erase Brush Tool - Affinity Help Center"
source: https://www.affinity.studio/help/tools-tools-background-erase-brush/
slug: tools-tools-background-erase-brush
fetched: 2026-08-06
---

# Background Erase Brush Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tools-tools-background-erase-brush/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Background Erase Brush Tool

With the Background Erase Brush Tool

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/qVXPS6ANyBsLqEXAcfKu2/b978da6518719f8dba41410aaeb85237/background_eraser_tool.svg)

, you can erase pixels of a similar color. This makes it useful for tasks such as erasing the background while leaving the foreground intact.

The Background Erase Brush Tool is available by default in Pixel Studio, on the Erase Brush Tool's flyout.

It can be added to other Studios. See 'Customizing tools' for details.

Tool shortcut key: E.

The following options can be adjusted from the context toolbar:

*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/1DZ3BiVUNw49gMKmpfsxjY/cd1aedf8a4cd6086f5386c7898ba6846/slider_width.svg) **Size**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3xN42iDOBeb6NfoMb1Nb3S/676173212d209b96e478c68304a4b2b5/slider_opacity.svg) **Opacity**—how see-through the brush is. 100% opacity erases pixels completely on the first pass. A lower opacity only partially erases the pixels.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6YT2BTrlyBpYlL2uIKpJtk/b378569b35626974ee7c0f69e47176c7/slider_flow.svg) **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3jeAVEQerphjqYhdiT8BLR/00fd4f48c15e79b94b796a70cf1d9838/slider_hardness.svg) **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/5SP1uGJgqSeBn3skj2msps/6d75ed636e0da4b0c60d12298eeb5ac1/slider_accumulation.svg) **Accumulation**—sets the deviation in the opacity or visibility of the stroke as it is painted.
*   **More**—click to display the [Brushes](https://www.affinity.studio/help/painting-raster-modify/) dialog to access advanced brush settings.
*   ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/2G6RXXZFvI6HUYZid36cJo/c0e6d0e34e179a4a70883fb3b37709c7/forcepressure.svg) **Force pressure**—click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
*   **Stabilizer**—enables stroke stabilization using either a **Rope mode**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/1dQYbLS5to2P0NEVKWr05P/ed77646476b191fed3c1e20aaa13921d/stabiliser_rope.svg)  or **Window mode**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/4wgNDHLUHFBM5dfxTQYqrO/ae9cf7f82a75be64e0cc071f94e56a04/stabiliser_window.svg) ; the former drags the stroke end by a 'rope' to smooth the stroke but lets you introduce sharp corners at increasing **Rope Length** (radius) values by redirecting the slackened rope; the latter will smooth the stroke by averaging sampled input positions within a **Window** whose size is configurable.
*   ![Image 10](https://images.ctfassets.net/3p2fxa94bzao/3c6bcFKU8dGvWvVeezWFGK/57add34659ed6eb94ff823207e420513/slider_tolerance.svg) **Tolerance**—how dissimilar the pixels can be compared to the sampled pixel for the pixels to be erased. A low percentage affects only pixels very similar to the sampled pixel
*   ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/7yAGdn6nsywVzkJ4wUGfIs/796e3af687715eb6a52c6e452a03030d/sample_continuously.svg) **Sample continuously**—if this option is off (default), samples the color only once on the first click. When selected, samples color continuously as you drag.
*   ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/7woEXMQmetxCfDKBS0p3qc/ac24f3b7a63beda41ced378c7eb9d0b6/contiguous.svg) **Contiguous**—when selected (default), affects neighboring pixels as well as the sampled pixel color. If this option is off, affects only the selected pixel color.
*   ![Image 13](https://images.ctfassets.net/3p2fxa94bzao/2Jk9PNrTpGzTAFr2oVmFcS/b539869ec6cc10a4455b3728c9837382/wetedges.svg) **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.
*   ![Image 14](https://images.ctfassets.net/3p2fxa94bzao/48gU5vr3XwFWtBjwhAJWTo/28e1a43a4063087555940fbc383932d4/reset-global.svg) **Reset**—resets brush settings to their defaults.

The following settings are available on a pop-up dialog when accessed via right-clicking on the page:

*   **Rotation**—allows to set nozzle rotation.
*   **Blend mode**—sets the blend mode for the strokes.
*   **Size**—sets the stroke size in pixels. Drag the slider or type in a value in the field.
*   **Opacity**—sets the opacity level for the applied strokes. Drag the slider or type in a value in the field.
*   **Hardness**—sets how hard the edges of the brush are. The brush appears softer as the percentage decreases. Drag the slider or type in a value in the field.
*   **Flow**—controls how fast color is built up under your brush. Drag the slider or type in a value in the field.

This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying raster brushes](https://www.affinity.studio/help/painting-raster-modify/) topic.

*   To select the Background Erase Brush Tool, press the **E**key. This key cycles through related erase tools.
*   When accessed via right-click on the page, holding the **⇧** key (Mac) / **Shift** key (Windows) restricts the on-dialog **Rotation**setting to 45°. Double-click the rotation point to reset it.

*   [Erasing](https://www.affinity.studio/help/painting-erasing/)
*   [Context toolbar](https://www.affinity.studio/help/workspace-context-bar/)

How would you rate the help you received from this article?
