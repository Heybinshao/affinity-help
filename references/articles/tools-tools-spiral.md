---
title: "Spiral Tool - Affinity Help Center"
source: https://www.affinity.studio/help/tools-tools-spiral/
slug: tools-tools-spiral
fetched: 2026-08-06
---

# Spiral Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tools-tools-spiral/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Spiral Tool

The Spiral Tool

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/2NgaWfhTPx5l19OD7yqv1Q/d0d04f575eb877b578a8540d03ab1bce/spiral_tool.svg)

 enables you to create a multitude of different spiral shapes.

The Spiral Tool is available by default in all Studios, on the shape tools flyout.

It can be added to other Studios. See 'Customizing tools' for details.

The **Spiral Tool** has several styles and options on its context toolbar to change the spiral's design.

![Image 2: Spiral examples](https://images.ctfassets.net/3p2fxa94bzao/4R86rihvdgIreUOQOLnko1/23807ab9147d33b6ff55ddb728b9a4b8/shapes_spiral_styles.png)

Spiral styles: (A) Linear, (B) Decaying, (C) Semi-circular*, (D) Counter semi-circular, (E) Fibonacci, (F) Plotted * Shaded semi-circles shown for illustrative purposes

A spiral's appearance can also be dramatically changed by presenting it with straight-line 'cusped' edges.

![Image 3: Cusped spiral designs](https://images.ctfassets.net/3p2fxa94bzao/iQi2aeVjMRGBGlOMLq1Sr/2f1b68045b364919a099610ddb4c8e23/shapes_spiral_cusped.png)

Spiral examples with cusped edges

In Affinity, a spiral is made up of a series of arcs stretching its full length; each arc is used to shape the spiral. As the number of turns of the spiral increases, the more arcs are needed to draw the spiral as intended.

![Image 4: Spiral anatomy](https://images.ctfassets.net/3p2fxa94bzao/7EXGRVVSjaOS2ZbFuKnrGm/862ef8b61edb4efc8f0952f22bc1aa55/spiral_anatomy.png)

Spiral anatomy: (A) Full turn, (B) Arc, (C) Points, (D) Arc angle (set to 90°)

The arc angle can be increased beyond 90° (default) to create increasingly uneven, and even chaotic, spirals the greater the angle. Points will appear along the spiral at each angle interval and will reposition according to the arc angle.

![Image 5: Spiral arc angles](https://images.ctfassets.net/3p2fxa94bzao/3AK8MyuIZfMeupnlqml7ia/8df071006a1ed80d60bf7d0305b7cfac/spiral_arcangles.png)

Spiral arc angles (Linear spiral style): (A) 20°, (B) 90°, (C) 130°, (D) 270°

Spirals display a series of non-editable points along their path which help to indicate the shape's geometry and resulting node positions if the spiral is [converted to curves](https://www.affinity.studio/help/object-control-converttocurves/).

All spiral styles create logarithmic spirals with the exception of the Plotted style which creates true spirals that are mathematically calculated.

You can add text inside or along the edges of objects created with this tool and Affinity's other shape tools. See the "Shape text" and "Text on a path" topics for details.

The following options can be adjusted from the context toolbar:

*   **Fill**—click the color swatch to display a pop-up panel to update fill color.
*   **Stroke**—click the color swatch to display a pop-up panel to update stroke color.
*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3rYvQ5X8bUYnIRpXvMBBlv/ee8198bb2731db49a0f3ec426d194fb2/stroke_width.svg) **Stroke width**—set a stroke width for the stroke using direct input or slider.
*   ![Image 7: Edit stroke settings](https://images.ctfassets.net/3p2fxa94bzao/LAIAniI5tfK3bknzYOUQB/9af81e28e315cea94436ab657c986f85/stroke.svg) **Edit stroke settings**—click to change stroke style, width, and alignment.
*   ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/3r0nypKaA5WwUhRidZ60F7/e75a1a686b28be34e9d4c8e77fc52f00/presets.svg) **Presets**—click to display a pop-up panel from which you may select an existing preset (if any are available) or create a new preset.
*   **Style**—select a spiral style for a different look—this can be done in advance of spiral creation or to swap the spiral to another style at any time. (See examples above.) 
    *   **Linear**—this basic spiral creates an even gap between each spiral turn when the arc angle is >90°; angles exceeding this will create an increasingly uneven look to the spiral the greater the angle. The spiral is drawn inwards towards the spiral center. Settings are: 
        *   **Arc angle**—sets the angle to which all arcs on the spiral will conform to.
        *   **Inner radius**—moves the inner spiral start position out from the object center.

    *   **Decaying**—the gap between each spiral turn decreases the nearer the curve gets to the spiral center. This is controlled by a **Decay** value. Settings are: 
        *   **Arc angle**—sets the angle to which all arcs on the spiral will conform to.
        *   **Decay**—sets the percentage decay rate along the spiral from the outer end of the spiral to the spiral center.
        *   ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/2E1rqZ6wti4mpoQ6SsxwXV/e9b75554b50a1dd50718d72142cd417b/spiral_decay_turn.svg) **Decay per turn**—the decay rate set by the **Decay** value is calculated across a full turn.
        *   ![Image 10](https://images.ctfassets.net/3p2fxa94bzao/1aRPHN1emHta0N6gg3yQhM/8f61bf69308a20ff1810b2188ff35fe7/spiral_decay_segment.svg) **Decay per arc**—as for **Decay per turn** but the calculation is made across an arc rather than a full turn.
        *   **Minimum radius**—sets the least amount that the spiral can decay to at its center.
        *   ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/3kmGJohUK3srgsTspiqtlg/26f1fb9193051a195e4619d03d256c96/spiral_cap_inside.svg) **Cap inside with circle**—when enabled, a circular cap is used to terminate the inner end of the spiral. When disabled, the inner end of the spiral will remain open.

    *   **Semi-circular**—like a Linear spiral but the spiral is composed of semi-circular arcs that double in size as they are drawn outwards from the spiral center; they only have a customizable number of turns.
    *   **Counter semi-circular**—like a semi-circular spiral but the spiral doubles back on itself, creating a spiral with two 'tails'.
    *   **Fibonacci**—the spiral approximates the golden spiral using quarter turn angles derived from the Fibonacci sequence (0,1,1,2,3,5,8,13); the spiral is drawn out from its center.
    *   **Plotted**—this mathematically calculated 'true' spiral has linear lines, called divisions, between points. Settings are: 
        *   **Divisions**—sets the number of straight-lined divisions on the spiral per turn.
        *   **Inner radius**—moves the inner spiral start position out from the object center.
        *   **Bias**—controls arc distribution along the spiral by setting the interpolation bias of the spiral.

*   ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/1cQPysfw6rZf5kce5krzBU/47e679ea62b2d5529cf0ac9cd5b4b112/spiral_use_cusped.svg) **Use cusped segments**—when enabled, the spiral will have straight lines between points. When disabled (default) the spiral is a continuous curve that winds outwards from the spiral center.
*   ![Image 13](https://images.ctfassets.net/3p2fxa94bzao/xARoL10God3TVkvzuXRHP/cb432c59f7c27412b3b03dfe7e9ea8d4/spiral_clockwise.svg) **Spiral clockwise**—the spiral winds in a clockwise direction.
*   ![Image 14](https://images.ctfassets.net/3p2fxa94bzao/2s6FGuW5mZPDRjwtf8OjOi/15f544b0f7c12a07dffe76f5f70903d3/spiral_anti-clockwise.svg) **Spiral counter-clockwise**—the spiral winds in a counter-clockwise direction.
*   **Turns**—increases or decreases the number of winding turns between the start and end of the spiral, counted from the spiral center.
*   **Angle of partial turns**—applies the angle to the outside of an arc to add the partial turn. Use for fine control of spiral at ends.
*   ![Image 15](https://images.ctfassets.net/3p2fxa94bzao/3TbUr2Rcs8WORkpB9F1k0k/ac87f174562fc2ec8a5e5ceb73693b92/convert_to_curves.svg) **Convert to Curves**—converts the selected object into a series of connected lines and nodes.
*   ![Image 16](https://images.ctfassets.net/3p2fxa94bzao/4VogDhXOgqw0F83jmJq0G8/6909b686388d52610397775cc0bbc4d7/multiple_transform.svg) **Transform Objects Separately**—when selected, where multiple objects are selected, they can be be resized, rotated and sheared independently of each other instead of transforming the bounding box.
*   ![Image 17](https://images.ctfassets.net/3p2fxa94bzao/58wNyMZl0DuNFi96wwd2r6/c8656fa6079dda8976d13873f64e0565/keep_selected.svg) **Keep selected**—when enabled (default), the new shape layer will be selected on creation. When disabled, the new object is deselected which prevents it from adopting the next object’s stroke/fill properties.
*   ![Image 18](https://images.ctfassets.net/3p2fxa94bzao/7e47FwYJ0eBW8yOWy3elSz/813ccca2419c99817334e5bb65c2a0db/cog_icon_2.svg) **Settings**—for general tool settings:
    *   **Enable Transform Origin**—displays a movable transform origin about which the shape can be rotated.
    *   **Hide Selection while Dragging**—when selected, the object's selection box is temporarily hidden when transforming the object. If this option is off, the selection box remains visible during transformation. The selected behavior persists across all objects unless it is manually switched.
    *   **Show Alignment Handles**—when selected, displays alignment handles at the center and edges of the selected object. Hovering over these handles displays a floating guideline across the page. You can drag the handles to position the center or edges of the selected object in line with this guide.

*   The Spiral Tool has no keyboard shortcut by default, but one can be assigned via the app's settings.

*   [Draw and edit geometric shapes](https://www.affinity.studio/help/curves-shapes-draw-geometric-shapes/)
*   [Context toolbar](https://www.affinity.studio/help/workspace-context-bar/)
*   [Shape text](https://www.affinity.studio/help/text-shape-text/)
*   [Text on a path](https://www.affinity.studio/help/text-path-text/)

How would you rate the help you received from this article?
