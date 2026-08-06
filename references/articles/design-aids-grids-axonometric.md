---
title: "Advanced axonometric grids - Affinity Help Center"
source: https://www.affinity.studio/help/design-aids-grids-axonometric/
slug: design-aids-grids-axonometric
fetched: 2026-08-06
---

# Advanced axonometric grids - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/design-aids-grids-axonometric/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Advanced axonometric grids

Beyond isometric grids, Affinity makes use of highly customizable advanced axonometric grids.

The **Grid and Snapping Axis** dialog's Advanced tab is ideal for laying out advanced axonometric grids as well as two-dimensional fixed grids and isometric grids.

Instead of the commonly used isometric grid set up via the **Isometric** panel, a choice of other project grid presets can also be selected (e.g., dimetric, triangular); you can even create custom axonometric grids with options for enabling plane sets, grid sizing, custom aspect ratios and angles for more advanced use.

If you're looking beyond the presets such as isometric you can customize the grid to your liking.

The grid origin is a point at which axes meet and is the corner of the logical plane. The origin is shown as a set of axis handles (in red, green and blue) which can be extended or repositioned on the page.

For most axonometric grids, the axis handles remain locked in relation to each other but can all be lengthened by the same amount simultaneously to set grid spacing.

The origin is set by dragging the grid origin (top-left corner of page) by its intersection point and positioning it on the page. As you change between planes, the handles on the active plane will be shown thicker.

![Image 1: Grid origin after](https://images.ctfassets.net/3p2fxa94bzao/38XHqoB9qqJFhXmqJJrDRK/01ebb921c1958d61ea46eddfb8a4424f/gridorigin_after.png)

![Image 2: Grid origin before](https://images.ctfassets.net/3p2fxa94bzao/7i7GMDsRIi81CGOp17DcMn/ce2684976b33e499a6a07af5f9d110a3/gridorigin_before.png)

You can snap the grid origin to an object on any plane and equally snap an object to a fixed grid origin.

You can introduce additional angles and an extra axis to your grid that gives you extra options for snapping and constraining object edges, corners and curve nodes to.

*   **Intermediate angles**—adds additional angles between axes that can be snapped or constrained to.
*   **Intermediate divisions**—Divides the angle between axes by a set number (set to 4 for 22.5° divisions for origami).
*   **Plane perpendicular axis**—creates another axis perpendicular to any active plane on axonometric grids. **Create plane set** must be enabled.
*   **Horizontal axis**—adds an additional horizontal axis for constraining or snapping.
*   **Vertical axis**—adds an additional vertical axis for constraining or snapping.

You may see the following colors which indicate different axes while snapping or constraining:

*   Red line: First axis (X axis on basic square grid)
*   Green line: Second axis (Y axis on basic square grid)
*   Blue line: Third axis (Z axis; axonometric grids)
*   Yellow node: Intersection point
*   Purple node: construction snap
*   Orange node: intermediate angles

1.   On the **View** menu, select **Grid and Axis**.
2.   Do one of the following, on the **Grid and Snapping Axis** dialog: 
    *   Select a non-isometric Parallel perspective preset from the **Presets** pop-up menu.
    *   Click **Advanced**, then from the **Grid type** pop-up menu, select a grid, then edit its settings in the dialog.

1.   On the **Grid and Snapping Axis** dialog, choose a preset or create your own.
2.   Click **Options**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg) , then select **Set as Default** or **Clear Default**.

1.   On the **Grid and Snapping Axis** dialog, check **Show axis editing handles**. By default, the grid origin will show at the top-left corner of your page.
2.   Drag the grid origin intersection to a point on your page, e.g. a corner of a geometric shape.

Reset the origin by double-clicking the intersection.

*   On the page, drag the end of one of the red, green or blue axis-editing handles outwards or inwards to size the grid. If snapped to an object you can size the grid to the object.

Cube mode offers a natural approach to setting up an axonometric grid. You can alter the elevation, orientation and roll of the cube, which automatically repositions your grid on the page.

![Image 4: grid Cube](https://images.ctfassets.net/3p2fxa94bzao/1vpUdYyTlCbGP8x9OTkWqg/3337c8bbbb1a4b9f9c0440fe773effdc/grid_cube.png)

Changing the Elevation (A), Orientation (B) and Roll (C) when using the grid Cube mode.

*   Visually preview and configure the grid using a controllable cube.
*   Keeps the logical scale to be the same as 2D objects where axes are foreshortened rather than relying on mathematical values to define axis length.

1.   On the **View** menu, select **Grid and Axis**.
2.   Set the **Mode** to be _Cube_.
3.   Set the **Cube Scale** which is the edge size of the cube and any **Divisions** value for all axes.
4.   Change the Elevation (**E**) by dragging the blue marker on the vertical slider next to the cube (or input a specific E value), using available snapping points if needed.
5.   On the cube, adjust the cube Orientation (**O**) by dragging left or right (or enter an O value). The angle and the lengths of the grid axes are derived from the cube orientation.
6.   On the outer ring gauge around the cube, drag the blue marker to adjust the Roll (**R**) setting.

For a true isometric grid, a snapping point at 35.3° OR -35.3° can be combined with an O (Orientation) angle of 45°.

The following modifier keys can be used:

*    The **⌥** key (Mac) / **Alt** key (Windows) temporarily overrides snapping. 
*    The **⇧** key (Mac) / **Shift** key (Windows) adjusts Orientation and Roll in 5° increments. 

For custom grids, any grid origin's axis editing handle’s length and direction can be changed in relation to and independently of other handles.

1.   On the **Grid and Snapping Axis** dialog, select either **Two axis custom** or **Triangular custom**.
2.   Enable **Uniform** to keep grid spacing the same across axes.
3.   Enable **Create plane set** to activate and configure the **Up** axis.
4.   Enable **Fixed aspect ratio** to configure the aspect ratio between axes. Disable to keep the same aspect ratios for Second and Up axes.
5.    Do one of the following: 
    *   Configure **Spacing**, **Division** and **Angle** setting for First, Second and Up axes.
    *   With the **Move Tool** enabled, drag an axis editing handle on the grid origin inwards or outwards, changing its angle. 

As you adjust the handles, the following modifier keys can be used:

        *   The **⇧** key (Mac) / **Shift** key (Windows) locks axis angles so length (i.e. grid spacing) is changed and not angles.
        *   The **⌘** key (Mac) / **Ctrl** key (Windows) changes the angle of the moving handle (not length) while locking other axis angles.

6.   Click **Close**.

Do one of the following:

*   For Mac: Hold the **⌃(ctrl)** key and drag any axis handle.
*   For Windows: With a hardware connected mouse, press both the left and right buttons together and drag any axis handle.

As you adjust the handles, the following modifier keys can be used:

General:

*   The **⇧** key (Mac) / **Shift** key (Windows) locks axis angles so length (i.e. grid spacing) is changed and not angles.
*   With **Snapping** enabled, the **⌥** key (Mac) / **Alt** key (Windows) temporarily ignores it while adjusting a custom grid.
*   **Double-click** matches the second axis length (if resized).

For Mac:

*   The **⌘** key changes the angle of the moving handle (not length) while locking other axis angles.
*   The **⌃(ctrl)** key allows you to rotate the custom grid along an axis handle.
*   The **⌃(ctrl)⇧** keys combination constrains rotation angle to 15°.
*   The **⌃(ctrl)⌘** keys combination constrains rotation to a single axis.
*   The **⌃(ctrl)⌘⇧** keys combination constrains rotation to a single axis and to 15° increments.

For Windows:

*   Dragging with the left and right mouse buttons pressed together allows you to rotate a custom grid.
*   Left and right mouse button with the **Shift** key pressed constrains grid rotation to 15° increments.

*   [Draw lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-draw-lines-and-shapes/)
*   [Draw and edit geometric shapes](https://www.affinity.studio/help/curves-shapes-draw-geometric-shapes/)
*   [Grids](https://www.affinity.studio/help/design-aids-grids/)
*   [Isometric grids](https://www.affinity.studio/help/design-aids-grids-isometric/)
*   [Snapping](https://www.affinity.studio/help/design-aids-snapping/)

How would you rate the help you received from this article?
