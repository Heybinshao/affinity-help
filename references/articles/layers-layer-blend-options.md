---
title: "Layer blend options - Affinity Help Center"
source: https://www.affinity.studio/help/layers-layer-blend-options/
slug: layers-layer-blend-options
fetched: 2026-08-06
---

# Layer blend options - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/layers-layer-blend-options/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Layer blend options

Blending options let you blend layers in a project tonally.

Blend options allow you to specify how tonal values of a layer blend with the layer(s) below. You can set the range of the tonal values affected with varied level of opacity (from opaque to transparent).

![Image 1: Blend Options reset](https://images.ctfassets.net/3p2fxa94bzao/52hzkv0eevqKRBjPo05uvB/47c06fc6317c8087e5b656c0638d2b70/tab1_blend_ranges_reset.jpg)

No blending applied on a gradient fill shape. The image layer resides below the gradient fill shape layer. The latter is selected.

![Image 2: Source Layer Ranges dark values reduced](https://images.ctfassets.net/3p2fxa94bzao/2kfNptV30XAtHj068OBhKf/800ca28bb2221cd2fac958e5a155f77f/tab2_dark_values_reduced.jpg)

Darker values of the shape layer blending with the image layer; by pulling the left side of the Source Layer Ranges graph down, the dark tones of the gradient fill shape are being hidden.

![Image 3: Source Layer Ranges light values reduced](https://images.ctfassets.net/3p2fxa94bzao/3cE8xnLWVomtPRPMBGqAiM/b8183a87ea15c1a8b355af61e060b358/tab3_light_values_reduced.jpg)

Lighter values of the shape layer blending with the image layer; by pulling the right side of the Source Layer Ranges graph down, the light tones of the gradient fill shape are being hidden.

![Image 4: Underlying Composition dark values through](https://images.ctfassets.net/3p2fxa94bzao/yaKnc8YdHElsBWpLe9NRI/7e0d045ec4fbc9759891e6eabf150757/tab4_dark_values_through.jpg)

The darker values of the image coming through the shape layer; by pulling the left side of the Underlying Composition Ranges graph down, the dark tones of the image layer are showing through.

![Image 5: Underlying Composition light values through](https://images.ctfassets.net/3p2fxa94bzao/4DK0TaQ6YSO7VyHRvFHcNV/b1fab6b4d2529b5e563c1707b0e3ceab/tab5_light_values_through.jpg)

The lighter values of the image coming through; by pulling the right side of the Underlying Composition Ranges graph down, the light tones of the image layer are showing through.

The two side-by-side blend range graphs (above) represent the Source Layer Ranges and Underlying Composition Ranges on layers. The first controls how the current layer worked on blends tonally with the layers _beneath_ it, whereas the second determines how the underlying layers blend _through_ the current one.

Each graph includes two nodes. The left-hand one represents minimum intensity, whereas the right-hand node represents maximum intensity.

For each of the two graphs, the dark values are represented on the left, whereas the bright ones are on the right. By modifying the graphs, you're affecting how those tones (including those in the middle) blend.

You can change the blend range for individual color channels by changing the setting above the spline graphs.

Modifying **Gamma** offers full power over how the tones of semi-transparent or antialiased edged objects interact with the mid-range of gray tones underneath. Using Gamma via [Levels](https://www.affinity.studio/help/adjustments-adjustment-levels/), for example, is a great alternative to controlling the image's overall exposure, high dynamic range and color balance.

**Blend Gamma** options (on the Blend Options dialog) open up even more control over how the midtones are affected by an applied adjustment and how it blends with your image. The dialog also gives you the option of using a linear-RGB color space (1.0), regular sRGB-blending (2.2) or any gamma value up to 3.0, depending on your desired output.

![Image 6: Blend gamma example](https://images.ctfassets.net/3p2fxa94bzao/3ZygXBLZg3FUAp08WATp5f/f1b1c566c3f703c800772d0a4e66f5b4/blendgamma.jpg)

Blend Gamma adjustments targeting midtones via Levels: high dynamic range and color balance corrections via individual channels before (left) and after (right), respectively.

By default, text layers are set to a gamma of 1.45 and all other types of layer to 2.2 (regular sRGB-blending). The former's default setting can be changed in [Settings](https://www.affinity.studio/help/workspace-settings/) (Tools option).

**Antialiasing** is the reduction of the appearance of jagged line edges. It is achieved by the addition of semi-transparent pixels along the line to smooth the transition from the line's edge to background objects. This area of transition is sometimes referred to as the **antialiasing ramp** or **antialiasing coverage**.

On the dialog, you can adjust the antialiasing ramp (coverage) of the selected layer, as well as control how (and if) antialiasing is inherited or set independently of other layers. For improved workflow, child layers nested hierarchically in a parent layer can inherent the parent layer's antialiasing setting automatically but can be forced to apply antialiasing or ignore it.

![Image 7: Antialiasing coverage example](https://images.ctfassets.net/3p2fxa94bzao/3rLpiFsaFDocU155bk1McQ/7ec637f34461e7622acde66022f243fc/blendcoverage.png)

Antialiased line with linear coverage map (left) and custom coverage map (right), respectively. Viewed at 800% zoom.

The following options are available in the Blend Options dialog:

*   **Blend Gamma**—controls the layer's blend gamma.
*   **Antialiasing**—controls antialiasing behavior for the selected layer: **Inherit** (default) adopts antialiasing from any parent layer, while **Force On** and **Force Off** respectively applies or disables antialiasing independently of any other layers.
*   **Coverage Map**—controls the layer's antialiasing ramp and how strong the edges of the blended objects will become.
*   **Fill Opacity**—alters the opacity of the layer without affecting blending. Use for layers with one of the 'special 8' blend modes applied, especially Hard Mix.
*   **Channels**—controls which channel is affected when adjusting the blend range. Select from the pop-up menu.

The following options can be adjusted for both the **Source Layer Ranges** and the **Underlying Composition Ranges**:

*   **Graph**—controls the affected range of pixels and the opacity of pixels within the specified range.
*   **In**—sets the horizontal position of the selected node. Type directly in the text box or drag the pop-up slider to set the value.
*   **Out**—sets the vertical position of the selected node. Type directly in the text box or drag the pop-up slider to set the value.
*   **Linear**—when selected (default), the graduation between two nodes is linear (i.e., nodes on the graph are connected using straight lines). If this option is off, nodes are connected using smooth curves.
*   **Reset**—returns the graph to the default position (a straight line between two nodes positioned at the top of the grid).

When adjusting the graphs in the dialog it is worth noting the following:

*   The graphs represent tonal values from darkest on the left to lightest on the right.
*   Content on the selected layer becomes less visible as nodes on the **Source Layer Ranges** graph are moved downwards.
*   Content on the underlying layers becomes more visible as nodes on the **Underlying Composition Ranges** graph are moved downwards.

1.   On the **Layers** panel, select a layer and then click **Blend Options**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/5aLt8lzEcmovjtpJrbbZFI/521800938c5909fe2677c5c56dc42a30/settings_cog_layers.svg) .
2.   Adjust the settings in the dialog.
3.   Close the dialog.

Do any of the following:

*   Drag a node horizontally to control which range of tonal values it affects.
*   Drag a node vertically to affect the visibility of pixels at the tonal value selected.
*   Click on the curve to add additional nodes.
*    Click to select a node and then press the **⌫** key (Mac) / **Backspace** key (Windows) to remove it. 

1.   Click the **Coverage Map** thumbnail.
2.   From the displayed chart, select a node on the profile's line and drag it vertically or horizontally to a new position.
3.   Repeat for other nodes as needed.

For more complex profiles, click on the profile line to add a node which can be positioned as for any generated node.

To remove antialiasing, set a straight, horizontal profile line at the top of the chart.

1.   Click the **Coverage Map** thumbnail.
2.   From the displayed chart's pop-up dialog, click **Reset**.

*   Under the chart, click **Save Profile**. The profile shows under the chart.

1.   Click the **Coverage Map** thumbnail.
2.   Select a custom profile thumbnail from below the chart. The chart will update, showing the chosen profile.

*   [Layer blend modes](https://www.affinity.studio/help/layers-layer-blend-modes/)
*   [Applying adjustments](https://www.affinity.studio/help/adjustments-adjustment-applying/)
*   [Levels adjustment](https://www.affinity.studio/help/adjustments-adjustment-levels/)

How would you rate the help you received from this article?
