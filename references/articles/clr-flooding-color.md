---
title: "Flooding color - Affinity Help Center"
source: https://www.affinity.studio/help/clr-flooding-color/
slug: clr-flooding-color
fetched: 2026-08-06
---

# Flooding color - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/clr-flooding-color/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Flooding color

Fill areas of a pixel layer with solid color in a single action, using the **Flood Fill Tool**

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6sNv2LU9WmTyZDVqEAPvTQ/2d6e97ebc34d06e363b24d30256e61c4/flood_fill_tool.svg)

.

![Image 2: After filling an area with solid color.](https://images.ctfassets.net/3p2fxa94bzao/8w0osFyFjOT0iXU1QFYOr/45ea81a607246649c74fbbfdf4dade7d/floodfill_after.jpg)

After filling an area with solid color.

Pixel filling replaces the existing color of pixels on the active layer with your chosen fill color. Unlike painting, which deposits color along a brush stroke, filling acts on a connected region or selection as a single operation — useful for blocking in flat color, replacing a background, masking an area for editing, or coloring line art.

Filling pixels only works on a pixel layer. Check the **Layers** panel and confirm the active layer is a pixel layer (or a mask layer); if it's a vector object, use the **Vector Flood Fill** Tool instead.

The Fill color used is the current Fill color shown on the **Color** panel. Set this before you fill.

1.   In the **Pixel Studio**, from the Fill Tool's flyout, select the **Flood Fill Tool**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/6sNv2LU9WmTyZDVqEAPvTQ/2d6e97ebc34d06e363b24d30256e61c4/flood_fill_tool.svg) .
2.   On the **Color** panel, set the fill color.
3.   (Optional) On the context toolbar, set the **Tolerance** to control how closely a neighbouring pixel must match the clicked pixel to be included in the fill.
4.   (Optional) On the context toolbar, set the **Blend mode** and **Source**, as required.
5.   (Optional) Enable **Contiguous** to restrict the fill to pixels directly connected to the clicked point. Disable it to fill all matching pixels across the layer.
6.   Click anywhere on the area to fill the matching region.

Use the **Flood Fill Tool**

![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6sNv2LU9WmTyZDVqEAPvTQ/2d6e97ebc34d06e363b24d30256e61c4/flood_fill_tool.svg)

 when you want to fill an area defined by color similarity — for example, a flat background, an enclosed shape in line art, or a single colored region.

*   **Working non-destructively:** to fill an area without altering the original pixels, add a new pixel layer above your image and fill on that layer instead. You can then adjust opacity, blend mode or mask the fill independently.
*   **Refining the edge:** if a flood fill leaves a thin halo of unfilled pixels around the boundary, raise the Tolerance value, or grow the fill area using a pixel selection before filling.
*   **Filling with a gradient or pattern:** to apply a gradient or bitmap fill instead of solid color, use a fill layer rather than a pixel fill.

*   [Flood Fill Tool](https://www.affinity.studio/help/tools-tools-flood-fill/)
*   [Vector Flood Fill Tool](https://www.affinity.studio/help/tools-tools-vector-flood-fill/)
*   [Fill layers](https://www.affinity.studio/help/layers-layer-fill/)

How would you rate the help you received from this article?
