---
title: "Undo Brush Tool - Affinity Help Center"
source: https://www.affinity.studio/help/tools-tools-undo-brush/
slug: tools-tools-undo-brush
fetched: 2026-08-06
---

# Undo Brush Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tools-tools-undo-brush/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Undo Brush Tool

The Undo Brush Tool

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/4YfcEAr6dIBz22Hh8y1MFx/0c24b41846c2e73422707e13b8ceffd2/undo_brush_tool.svg)

 can be used to selectively undo modifications to individual pixels, restoring them to a previous history state or a saved snapshot.

1.   On the **History**panel, click the source icon to the left of the history state or snapshot you want to restore to. This sets it as the brush source.
2.   On the **Layers**panel, select the layer to work on.
3.   Select the **Undo Brush Tool**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/4YfcEAr6dIBz22Hh8y1MFx/0c24b41846c2e73422707e13b8ceffd2/undo_brush_tool.svg) .
4.   Adjust brush options on the context toolbar as needed.
5.   Paint over the areas of the image you want to restore.

Use a low **Flow** setting to blend the restored pixels gradually into the current image state, giving you more control over the transition.

The **Undo Brush Tool**

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/4YfcEAr6dIBz22Hh8y1MFx/0c24b41846c2e73422707e13b8ceffd2/undo_brush_tool.svg)

 is available by default in Pixel Studio, on the Clone Brush Tool's flyout.

It can be added to other Studios. See [Customizing tools](https://www.affinity.studio/help/workspace-customizing-tools-panel/) for details.

The Undo Brush Tool does not have a default keyboard shortcut, but you can assign one manually if desired. See [Customizing keyboard shortcuts](https://www.affinity.studio/help/workspace-customizing-shortcuts/) for details.

Unlike a standard undo — which reverses the last action across the entire image — the Undo Brush Tool lets you selectively restore specific areas while leaving the rest of the image untouched. This makes it ideal for recovering detail in a localized area after applying a global edit that went too far.

Before painting, you set a source in the **History** panel — either a history state (a recorded step in your editing session) or a snapshot (a manually saved version of the image at a specific point). The tool then paints that source state back into the current image wherever you brush.

The following options can be adjusted from the context toolbar:

*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/1DZ3BiVUNw49gMKmpfsxjY/cd1aedf8a4cd6086f5386c7898ba6846/slider_width.svg) **Size**—the brush (stroke) size in pixels. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3xN42iDOBeb6NfoMb1Nb3S/676173212d209b96e478c68304a4b2b5/slider_opacity.svg) **Opacity**—how see-through the brush is. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/6YT2BTrlyBpYlL2uIKpJtk/b378569b35626974ee7c0f69e47176c7/slider_flow.svg) **Flow**—how fast the brush effect is applied (1% is very slow, 100% is immediate). Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3jeAVEQerphjqYhdiT8BLR/00fd4f48c15e79b94b796a70cf1d9838/slider_hardness.svg) **Hardness**—how hard the edges of the brush are. The brush appears softer as the percentage decreases. Type directly in the text box or drag the pop-up slider to set the value.
*   ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/5SP1uGJgqSeBn3skj2msps/6d75ed636e0da4b0c60d12298eeb5ac1/slider_accumulation.svg) **Accumulation**—sets the deviation in the opacity or visibility of the stroke as it is painted.
*   **More**—click to display the [Brushes](https://www.affinity.studio/help/painting-raster-modify/) dialog to access advanced brush settings.
*   ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/2G6RXXZFvI6HUYZid36cJo/c0e6d0e34e179a4a70883fb3b37709c7/forcepressure.svg) **Force pressure**—Click to control brush size with pressure if using a pressure-sensitive device. This overrides brush defaults.
*   **Stabilizer**—enables stroke stabilization. Choose from:
    *   **Rope mode**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/1dQYbLS5to2P0NEVKWr05P/ed77646476b191fed3c1e20aaa13921d/stabiliser_rope.svg) —smooths the stroke by dragging the stroke end along a virtual rope. Sharp corners can be introduced by redirecting the slackened rope. Set the rope radius using **Rope length**.
    *   **Window mode**![Image 11](https://images.ctfassets.net/3p2fxa94bzao/4wgNDHLUHFBM5dfxTQYqrO/ae9cf7f82a75be64e0cc071f94e56a04/stabiliser_window.svg) —smooths the stroke by averaging sampled input positions within a configurable **Window**size.

*   **Blend Mode**—changes how the applied pixels interact with existing pixels on a layer. Select from the pop-up menu.
*   ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/2tGWKzaSgpL3un8gg3T3h4/55ab3a7be07c377621e8b97244bd9665/blend.svg) **Blend**—when selected (default), pixels which do not overlap those in the selected history or snapshot state are unaffected, allowing the blending of the current document state with the selected, previous state. If this option is off, all pixels are returned to the previous state when painted.
*   ![Image 13](https://images.ctfassets.net/3p2fxa94bzao/2Jk9PNrTpGzTAFr2oVmFcS/b539869ec6cc10a4455b3728c9837382/wetedges.svg) **Wet Edges**—builds paint up along the edges of your pixel brush stroke, producing a watercolor effect. Check **Custom** and either apply a preset **Standard profile** or draw a custom profile using the chart; both subtly changes how watery the stroke appears.
*   ![Image 14](https://images.ctfassets.net/3p2fxa94bzao/33nEL6S3iwlM1lNgAK4ZdT/a7fb128eead8d77dee8c5a55e60beedc/protectalpha.svg) **Protect Alpha**—when checked, you are not able to paint on the current layer's transparent regions, only those that are opaque.
*   ![Image 15](https://images.ctfassets.net/3p2fxa94bzao/48gU5vr3XwFWtBjwhAJWTo/28e1a43a4063087555940fbc383932d4/reset-global.svg) **Reset**—resets brush settings to their defaults.
*   ![Image 16](https://images.ctfassets.net/3p2fxa94bzao/7eblP76vdFdrp2uaZ3g2uC/4609ca56c51ddfe4b1aeb480e5ac5d9e/view.svg) **Symmetry settings**—offers various symmetry line control options.
    *   **Lines**—when set to greater than 0, repeats the brush stroke around a number of axes (defined by the symmetry value). The center axis point can be repositioned by click-dragging it.
    *   **Mirror**—with symmetry enabled, causes brush strokes to be mirrored along the X and Y axis.
    *   **Lock**—when checked, prevents the symmetry line from being moved.

The following settings are available on a pop-up dialog when accessed via right-clicking on the page:

*   **Rotation**—sets the nozzle rotation.
*   **Blend mode**—sets the blend mode for the strokes.
*   **Size**—sets the stroke size in pixels. Drag the slider or type in a value in the field.
*   **Opacity**—sets the opacity level for the applied strokes. Drag the slider or type in a value in the field.
*   **Hardness**—sets how hard the edges of the brush are. The brush appears softer as the percentage decreases. Drag the slider or type in a value in the field.
*   **Flow**—controls how fast color is built up under your brush. Drag the slider or type in a value in the field

This Brush Tool can be associated with a particular brush on the **Brushes** panel. For more information, see the [Modifying raster brushes](https://www.affinity.studio/help/painting-raster-modify/) topic.

*   The Undo Brush Tool has no keyboard shortcut by default, but one can be assigned via the app's settings.
*   When accessed via right-click on the page, holding the **⇧** key (Mac) / **Shift** key (Windows) restricts the on-dialog **Rotation**setting to 45°. Double-click the rotation point to reset it.

*   [Using undo, redo and history](https://www.affinity.studio/help/design-aids-undo/)
*   [Context toolbar](https://www.affinity.studio/help/workspace-context-bar/)

How would you rate the help you received from this article?
