---
title: "Fill modes - Affinity Help Center"
source: https://www.affinity.studio/help/curves-shapes-fill-mode/
slug: curves-shapes-fill-mode
fetched: 2026-08-06
---

# Fill modes - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/curves-shapes-fill-mode/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Graphic design](https://www.affinity.studio/help/graphic-design/)
3.   Fill modes

Shapes which have been constructed using self-intersecting lines can be filled in two different ways: **Alternate** or **Winding**.

Fill mode is a property of any polycurve that has intersecting lines. Because a polycurve is a complex shape, what is considered inside and outside the shape can become unclear. The fill mode is an algorithm that decides the shape's inside and outside so that filling can be understood when exporting complex shapes to SVG document fragments for use in web apps.

*   Alternate—applies a fill or transparency to contiguous sections alternately along the lines. The mode determines whether a segment of the shape will be filled by drawing a ray from that point to infinity in any direction, and counting the number of segments within the given shape that the ray crosses through. If this number is odd, the segment exists in the fill region; if even, the segment is outside the fill region.
*   Winding—fills all sections encompassed by the shape's outer lines. This is determined by whether a segment of the shape will be filled by drawing a ray from that point to infinity in any direction, and counting the number of instances in which a segment of the shape crosses the ray. Starting from zero, one count is added each time a segment crosses the ray from left to right and one count is subtracted each time a path segment crosses the ray from right to left, from the perspective of the ray. After the number of crossings has been counted, if the result is zero, then the point is considered to be outside the fill path. Otherwise, it is inside the path.

![Image 1: Fill Mode example](https://images.ctfassets.net/3p2fxa94bzao/3Kv6zh1ZEKZQwCXzoZtBkH/9ae7977e0084a2cd63a5cfd24068bb6a/fillmode.png)

A self-intersecting line (left) can make an unfilled (center) and filled closed shape (right) using Alternate and Winding fill modes, respectively.

The last shape's red-line indicator leading up to the end node shows drawing direction. This is enabled by default on lines and closed shapes to help identify the start node position and winding orientation—in this case, clockwise. It can be switched off if this is distracting.

Imported Adobe Illustrator objects will have the **Winding** mode set by default.

*   With the object selected, on the **Vector** menu, select an option from the **Fill Mode** submenu.

*   On the **Pen Tool** or **Node Tool**'s context toolbar, click **Settings**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/7e47FwYJ0eBW8yOWy3elSz/813ccca2419c99817334e5bb65c2a0db/cog_icon_2.svg)  and then uncheck/check **Show curve orientation**.

*   [About lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-about-lines-and-shapes/)
*   [Edit lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-edit-lines-and-shapes/)

How would you rate the help you received from this article?
