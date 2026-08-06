---
title: "Snapping - Affinity Help Center"
source: https://www.affinity.studio/help/design-aids-snapping/
slug: design-aids-snapping
fetched: 2026-08-06
---

# Snapping - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/design-aids-snapping/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Snapping

Snapping simplifies the positioning of new and existing items by 'magnetizing' them to align with other objects or document elements.

![Image 1: Snapping](https://images.ctfassets.net/3p2fxa94bzao/72zvgImr8DvEV9odAPSjo3/e800dfb76348935b32d95d1580279626/snapping_example.png)

Snapping causes images, strokes, lines, shapes and selection areas to align to nearby grid lines, guides, margins, artboards or spreads, or any combination of these. You can also snap to object bounding boxes, key points on shapes, and object geometry when those targets are available. Text can also snap to the baseline of other text (the first line only for text frames) and artistic text objects can snap to the height of previously created artistic text.

To help understand snapping behavior, colored Smart guides and target nodes display when you snap to objects. The colors used are:

*   Red line: The snapped item aligns horizontally with the target.
*   Green line: The snapped item aligns vertically with the target.
*   Yellow node: The snapped item aligns to shape key points (often centers) or object geometry.
*   Blue line: The snapped item aligns to the third plane when using a triangular projection grid.
*   Orange line: The snapped item aligns horizontally or vertically with the target if a projection grid is active.

Smart guides work in conjunction with snapping to provide a visual aid when aligning. Smart guides also include labels which report the distance between the snapping objects (measured in the document's set units).

To precisely create these areas you can use snapping to position to previously placed guides or to the page edge itself.

Simply drag out your crop or selection area until its edge meets the positioned guide or page edge.

Snapping candidates are page items which are available for you to snap to. You can set how candidates are determined using the following settings:

*   **Candidate List**—limits the number of items which are snapping candidates to the number you set. Creating a new object, selecting or hovering over an existing one (desktop only), designates it as a snapping candidate in this case. Only the active snapping candidates can be snapped to.
*   **Immediate layers**—limits the number of candidates to those on the current layer, layers that are siblings or the immediate parent layer.
*   **Immediate layers and children**—limits the number of candidates to those on the current layer and any of the layer's subordinate child layers.
*   **All layers**—does not limit the number of snapping candidates in the document.

*   On the Toolbar, click **Snapping**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/4ZvAvUGmRtnDVzuGQvtjnT/77b8a44ec48b78f76d4cc9e53107331d/snapping.svg) .

*   Press the **⌥** key (Mac) / **Alt** key (Windows) while you're positioning an object. Snapping won't occur while the key is depressed. 

*   On the **Layers** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) the entry and select **Exclude From Snapping**. 

A symbol,

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/40zbHs4XAE9cHrsKtz0Ec5/19fc93d78d76a09577e52d1634476b57/exclude_from_snapping.png)

, appears on the layer entry to indicate this exclusion.

Individual snapping options can be switched on or off to suit your needs, drawing style, and the project you are working on. The preset that you initially adopted will be customized in the process.

The following options are available:

*   **Enable snapping**—when enabled, objects will snap to specified criteria. This must be enabled to change other options (except those for pixel alignment).
*   **Screen tolerance**—controls the distance you have to be to an object before snapping occurs.
*   **Presets**—Select a preset which is a grouping of snapping options for specific ways of working. 
    *   _Page layouts_—for designs to be printed, where snapping to placed guides, margins, and spreads is important.
    *   _Page layouts with objects_—as above but with additional object-to-object alignment.
    *   _Object creation_—perfect for simple object-to-object alignment to bounding boxes and their midpoints, plus for aligning some shapes to key points. Key points are predefined reference points on shapes (often the centre).
    *   _Curve drawing_—the setup for non-geometric use (e.g., drawing with the pen tool).
    *   _UI design_—for UI/web design for pixel accuracy when using snapping to fixed guides and grid.
    *   _Pixel work_—for pixel-only brush work where vector-based object snapping is not needed.

*   **Candidates**—sets how candidates are created. Select from the pop-up menu. 
    *   **Maximum**—limits the number of active candidates when **Candidate List** is selected (see above). If you reach this limit, new candidates replace older candidates in chronological order.
    *   **Show snapping candidates**—when checked, highlights the active snapping candidates, i.e. objects that can be snapped to by prior selection or hover over. Candidates will display a 'purple halo'.

*   **Force pixel alignment**—when selected, vector content will snap to full pixels when created, moved or modified. If this option is off, vector content can occupy partial pixels.—see [Force Pixel Alignment](https://www.affinity.studio/help/design-aids-pixel-align/). 
    *   **Move by whole pixels**—allows you to constrain the movement of vector objects, nodes and handles to whole pixels—see [Force Pixel Alignment](https://www.affinity.studio/help/design-aids-pixel-align/).

*   **Page snapping**—lets you enable or disable the selected page-related snapping options all at once:
    *   **Snap to grid**—when checked, content snaps to a line grid (if switched on from the **View** menu). Not available when using Force Pixel Alignment.
    *   **Snap to baseline grid** (Layout Studio![Image 4](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg) )—when checked, content will snap to the active document baseline grid (if switched on via **View > Baseline Grid**.
    *   **Snap to guides**—when checked, content snaps to guides (if switched on from the **View** menu).
    *   **Snap to spread**—when checked, content snaps to the edge of the document (ignoring margins). 
    *   **Include spread mid points**—when checked, content snaps to vertical or horizontal center of the page. This option is only available if the above option is selected.
    *   **Snap to margin**—when checked, content snaps to page margins (if switched on from the **View** menu). 
        *   **Include margin mid points**—when checked, content snaps to vertical or horizontal center of the page margin. This option is only available if the above option is selected.

*   **Object snapping**—lets you enable or disable the selected object-level snapping options all at once:
    *   **Only snap to visible objects**—when checked, only visible objects are snapped to.
    *   **Snap to object bounding boxes**—when checked, objects can be aligned based on its bounding box. 
        *   **Include bounding box mid points**—when checked, objects snap to vertical or horizontal center of a target object. This option is only available if the above option is selected.
        *   **Snap to gaps and sizes**—when checked, arrows represent matched gaps between snapping candidates and matched horizontal and/or vertical sizes.

    *   **Snap to shape key points**—when checked, objects can be aligned to predefined key points on shapes (e.g. the center of a rectangle or ellipse) when moving nodes.
    *   **Snap to object geometry**—when checked, snapping can target object vertices and intersections when drawing new objects, resizing objects, or moving nodes, rather than only bounding boxes or shape key points. Vertices are object corners or intersections, such as the points of a star.
    *   **Snap to pixel selection bounds**—when checked, objects can be snapped to the bounds of a pixel selection. For example, using the Flood Select Tool, a pixel selection drawn over image 'edges', which would otherwise not be snappable, will expose those edges for snapping.

Some object snapping options apply only during specific actions, such as drawing new objects, resizing objects, or moving nodes with the Node Tool. They do not affect moving objects with the Move Tool.

Snapping always snaps to the currently set measurement unit.

*   [Force Pixel Alignment](https://www.affinity.studio/help/design-aids-pixel-align/)
*   [Smart guides](https://www.affinity.studio/help/design-aids-dynamic-guides/)
*   [Grids](https://www.affinity.studio/help/design-aids-grids/)
*   [Guides](https://www.affinity.studio/help/design-aids-guides/)
*   [Margins](https://www.affinity.studio/help/design-aids-margins/)
*   [Document units](https://www.affinity.studio/help/get-started-document-units/)

How would you rate the help you received from this article?
