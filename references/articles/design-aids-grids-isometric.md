---
title: "Isometric grids - Affinity Help Center"
source: https://www.affinity.studio/help/design-aids-grids-isometric/
slug: design-aids-grids-isometric
fetched: 2026-08-06
---

# Isometric grids - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/design-aids-grids-isometric/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Isometric grids

An isometric grid is a popular axonometric grid type which is perfect for UI/game design, digital design models and mock ups. The combination of dedicated panel designed for isometric grids plus easy in-panel plane switching makes isometric drawing easy.

![Image 1: isometric grid](https://images.ctfassets.net/3p2fxa94bzao/2SEnPlPkIGY07IGD6HRWT0/1435068834c710d3c503c6fcd79e55ef/grid_isometric.png)

Isometric drawing.

Isometric grids, like other axonometric grids are, by nature, parallel projections. This means that grid lines never converge to a vanishing point as in perspective projections. Perspective projections are not supported in Affinity.

Like all axonometric grids, a front, side and top plane can be drawn on. Planes can be switched between so you can apply in-plane transforms on these planes in turn.

![Image 2: Front plane](https://images.ctfassets.net/3p2fxa94bzao/3ByUJipktpDSIQFGAXZ2bb/dccb8429b1c4e346d1addaedc25d0ca9/projection_frontsidetop.png)

Front, Side and Top planes of isometric grid showing selected object transformed to fit in-plane.

Once a grid is set up, you can draw geometric shapes, art text and gradients directly on the active plane and selectively transform curves, closed shapes and placed images to the plane of your choice using the Move Tool.

Grids work best when combined with snapping. Object handles and curve nodes snap precisely to any grid line and line intersections.

Grids can be based on any document unit, shown when switching on the rulers.

When drawing curves on plane, take advantage of the **Cycle Selection Box** setting on the **Select** Menu. Its 'Planar bounds' option transforms the curve’s selection box (not the object) to that of the current plane, allowing easier positioning/snapping of curves to the grid. Once Planar bounds is set, fitting the curve to a different plane subsequently will change the planar box too.

![Image 3: Front plane](https://images.ctfassets.net/3p2fxa94bzao/79lIadLDhgbsU4xRC6egWo/5bb1a868d2ec9b17701f17c8d5cbee26/projection_curveselectionbox.png)

Selection box (not object) changed to 'Planar bounds'.

For out-of-plane editing, choose a **Cycle Selection Box** setting of _Base Box_ or _Regular Bounds_.

1.   From the **Window** menu, select **Vector > Isometric** to display the **Isometric** panel.
2.   Click **Modify Grid**.
3.   On the now displayed **Grid and Snapping Axis** dialog, check **Show Grid**.

If you haven't set up a grid previously, you'll be prompted to initially modify the settings (e.g., grid Spacing) for your new isometric grid; you can then make the grid visible.

If an isometric or other type of axonometric grid was already set up, the you won't be prompted for settings.

Do one of the following:

*   On the **Isometric** panel, click **Front**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/7DFKTgnCIpPTf9b0CX32oP/7cf99a2d64be1bf14b7328ab06059dc2/planar_front.png) , **Side**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/23cSrutKfFjSCCAc0Q9chG/a0fa9e964bf49a28110d74710b1945ba/planar_side.png) , or **Top**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/2PZJfoFeo8NEONxsxRfKRz/d0f4e8f4736738bda0022df1bf6de06d/planar_top.png) .
*   Press the apostrophe (') key to cycle between planes.

This plane-swapping behaviour is a fundamental principle in drawing the 'faces' of an object (Front, Side and then Top plane).

*   On the **Grid and Snapping Axis** dialog, set the **Spacing**, **Divisions**, or **Gutter** values.

1.   On the Toolbar, select **Snapping**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/4ZvAvUGmRtnDVzuGQvtjnT/77b8a44ec48b78f76d4cc9e53107331d/snapping.svg) .
2.   Select a **Preset**, e.g. Curve drawing, ensuring that **Snap to grid** is also checked.

This ensures that objects will fit accurately to grid lines.

1.   On the **Isometric** panel, enable **Edit in plane**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/3UkNjnbCvnagUzuVafSujg/4292b7659eb9886b136ecc13b3548bd6/edit_in_plane.svg) .
2.   With a shape tool selected, drag out a chosen shape. You can snap your shape to the grid on creation when dragging initially from any grid intersecion or when repositioning and/or scaling the shape.

1.   Select a curve, closed shape, artistic text or image.
2.   On the **Isometric** panel, choose a plane (**Front**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/7DFKTgnCIpPTf9b0CX32oP/7cf99a2d64be1bf14b7328ab06059dc2/planar_front.png) , **Side**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/23cSrutKfFjSCCAc0Q9chG/a0fa9e964bf49a28110d74710b1945ba/planar_side.png) , or **Top**![Image 11](https://images.ctfassets.net/3p2fxa94bzao/2PZJfoFeo8NEONxsxRfKRz/d0f4e8f4736738bda0022df1bf6de06d/planar_top.png) ) to send the object to.
3.   On the same panel, select **Fit to plane**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/WWGtlONhid0csCrYmwuXl/63e81077c9afd98a34bb6aa84ca01c99/correct_to_plane.svg) .

If you [clip](https://www.affinity.studio/help/layers-layer-clip/) objects to parent objects before fitting them to the plane of your choice, these child objects will automatically follow the parent object's transformation on plane.

If including text on any plane, ensure artistic text is used rather than frame text. The frame properties of frame text means that transformation on plane is not exact.

*    Select the object in the plane, then do one of the following: 
    *   On the **Isometric** panel, ensure the correct Current plane is set (must be the same plane as that which the object was originally drawn on), then use the panel's 180° flip and 90° rotate options ![Image 13](https://images.ctfassets.net/3p2fxa94bzao/7AD9HsRKpwFPDNimdbcYMP/16337df2e4a29579cfd8afc1bdd56079/planar_flip_horizontal.png) ![Image 14](https://images.ctfassets.net/3p2fxa94bzao/3DK526cn0HcLggLpBOMUf3/25f4ea9fa7809ee0945f943fc58dcbf1/planar_flip_vertical.png) ![Image 15](https://images.ctfassets.net/3p2fxa94bzao/7AD9HsRKpwFPDNimdbcYMP/16337df2e4a29579cfd8afc1bdd56079/planar_flip_horizontal.png) ![Image 16](https://images.ctfassets.net/3p2fxa94bzao/2hQDltUSPhJtuGK9FbZg46/6a9faf5cac72d67209986e05a86d2b45/planar_rotate_anti_clockwise.png) ![Image 17](https://images.ctfassets.net/3p2fxa94bzao/673ExutZRSvUkoPenGYPlt/fcb21dadccb16ba867df8e97a5f4547d/planar_rotate_clockwise.png) .
    *   To rotate the object on the page, drag its Rotation Handle clockwise or counter-clockwise. Press the **⇧** key (Mac) / **Shift** key (Windows) to rotate in 15° increments.

If you wish to rotate objects using Rotation Handles, ensure **Edit in plane** is enabled.

*   On the **Isometric** panel, select **Grid Settings**. From here, you can: 
    *   Switch on the grid origin (axis editing handles).
    *   Add intermediate grid angles for snapping or constraining to.
    *   Add an axis perpendicular to the current plane for snapping or constraining to.
    *   Set the grid color and transparency.

*   [Draw lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-draw-lines-and-shapes/)
*   [Draw and edit geometric shapes](https://www.affinity.studio/help/curves-shapes-draw-geometric-shapes/)
*   [Grids](https://www.affinity.studio/help/design-aids-grids/)
*   [Advanced axonometric grids](https://www.affinity.studio/help/design-aids-grids-axonometric/)
*   [Snapping](https://www.affinity.studio/help/design-aids-snapping/)

How would you rate the help you received from this article?
