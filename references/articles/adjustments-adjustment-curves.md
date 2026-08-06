---
title: "Curves adjustment - Affinity Help Center"
source: https://www.affinity.studio/help/adjustments-adjustment-curves/
slug: adjustments-adjustment-curves
fetched: 2026-08-06
---

# Curves adjustment - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/adjustments-adjustment-curves/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Curves adjustment

Modify color, tone and alpha channels with the Curves adjustment

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/3sUtJeUQMZ6GrVHc9V5TPv/19fd2cb45e125061fc1c3a451f05d31c/curves_adjustment_type.svg)

 either on individual channels or by tweaking the master curve.

![Image 2: Default Curve in its linear graph form.](https://images.ctfassets.net/3p2fxa94bzao/5atLZuP4QLAylTD8BZTUR4/1d085eb2645d674e1b99cbba22a32d81/tab1_curve_reset.jpg)

![Image 3: Inverted S-Curve](https://images.ctfassets.net/3p2fxa94bzao/2vVLykfAAeC5nKkPJHh4dr/eb1dc17e8f6b20732312483d0b1fa75d/tab2_S_curve_inverted.jpg)

![Image 4: S-Curve](https://images.ctfassets.net/3p2fxa94bzao/2DaPfoWZHJxfhHzwRRkwK7/eb70d584367aa95dc760edca065a2f76/tab3_S_curve.jpg)

In the examples above, the effects of a default curve, an inverted "S" curve and an "S" curve are presented. As shown, the inverted "S" curve can be used to reveal more detail in the shadows while protecting the highlights. The "S" curve is typically used to increase overall contrast while delivering deeper shadows and brighter highlights.

Curves can be used as a powerful alternative to controlling your composition tonality. Depending on the position of the nodes on the curve, various luminance levels can be achieved. The Curves graph is divided into three distinct areas responsible for:

*   the shadows (dark tones) on the left.
*   the midtones in the center.
*   the highlights on the right-hand side.

When the curve is lifted up, the area affected will increase in its luminance value making those regions brighter. When pulled down, the luminance value will decrease thus making those areas darker.

![Image 5: Curves affecting tonal regions](https://images.ctfassets.net/3p2fxa94bzao/2NqtYjrPLaeERftYO2Hm3V/1515982bea26ae3e0ce61a1d28b58961/adjustment_curves.png)

From left: Curves adjustments affecting highlights, shadows, and midtones, respectively.

In general:

*   Drag the curve downwards to correct overexposure.
*   Drag the curve upwards to correct underexposure.
*   Create a gentle S-shape by adding nodes (see above) and dragging the curve in opposite directions to correct washed out images.

To fine-tune node positions, try nudging a selected node by pressing the left, right, up, or down arrow key (or alter **X** and **Y** values).

Adjustments can be made in any color mode, regardless of the document's current color mode.

You can use the Curves adjustment to manipulate individual color channels. The adjustment can be used on placed images as well.

You can also adjust the tonal range of compositions using the **Levels** and **Brightness and Contrast** adjustments.

This adjustment is also available in the Develop Studio on the **Tones** panel.

The following settings can be adjusted in the dialog:

*   **Add Preset**—allows you to save a custom Curve adjustment.
*   **Merge**—merges the Curve adjustment layer with the ones below it.
*   **Delete**—deletes the Curves adjustment and its layer from the panel.
*   **Reset**—reverts the spline graph to its default position.
*   Select a color mode (**GREY/RGB/CMYK/LAB**) from the pop-up menu.
*   Specify a single color channel to apply the adjustment to, including the layer's alpha channel. **Master** (default) applies the adjustment to all color channels, excluding the alpha channel.
*   **Picker**—click to activate the picker which allows you to drag on the image to modify the adjustment. Regardless of the color model set, a click-drag places a node on the curve in relation to the selected pixel intensity; a 1x1 pixel area is considered. Secondly, dragging up (to lighten the image) or dragging down (to darken it) modifies the adjustment. The curve graph will update accordingly.
*   **X**—accurately positions any added and currently selected node on the X-axis of the graph. Use for precision in 32-bit linear workflows.
*   **Y**—accurately positions any added and currently selected node on the Y-axis of the graph. Use for precision in 32-bit linear workflows.
*   **Min** and **Max** are the input minimums and input maximums and let you determine the range/threshold of values that are affected by the adjustment. They use a normalized 0-1 range (regardless of bit depth) but setting **Max** to >1 allows for the adjustment to manipulate HDR values as well. They can be also be used to fine-tune the manipulated tonal range in 8-bit and 16-bit documents.
*   **Opacity**—sets the level of visibility of the adjustment.
*   **Blend Mode**—controls how the adjustment interacts with the layers below it.

The color mode, **Alpha** channel and **Picker** options are not available in the Develop Studio.

*   On the **Layers** panel, click **Adjustments**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/4ZFx9I9M7MiUBPmytBqZrt/cad5a29a5e39b1b3faa42c5fa29402f3/add_adjustment_layer.svg)  and select **Curves**.
*   On the **Adjustment** panel, select **Curves**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3sUtJeUQMZ6GrVHc9V5TPv/19fd2cb45e125061fc1c3a451f05d31c/curves_adjustment_type.svg)  and then click one of the available presets.
*   On the **Pixel** menu, select **New Adjustment Layer > Curves**.

The **Adjustment** panel is not visible by default. To enable it, navigate to the top menu and select **Window > Pixel > Adjustment**.

On the curves graph, do any of the following:

*   On the dialog, click **Picker** and then drag up or down on the page.
*   Drag the curve to adjust the tonal range.
*   Click on the curve to add additional nodes.
*    Click to select a node and then press the **⌫** key (Mac) / **Backspace** key (Windows) to remove it. 

*   [Applying adjustments](https://www.affinity.studio/help/adjustments-adjustment-applying/)
*   [Levels adjustment](https://www.affinity.studio/help/adjustments-adjustment-levels/)
*   [Brightness and Contrast adjustment](https://www.affinity.studio/help/adjustments-adjustment-brightness-contrast/)
*   [Develop Studio](https://www.affinity.studio/help/raw-raw/)

How would you rate the help you received from this article?
