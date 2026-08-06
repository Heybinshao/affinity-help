---
title: "Building shapes with the Shape Builder Tool - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-join-shape-builder/
slug: object-control-join-shape-builder
fetched: 2026-08-06
---

# Building shapes with the Shape Builder Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-join-shape-builder/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Graphic design](https://www.affinity.studio/help/graphic-design/)
3.   Building shapes with the Shape Builder Tool

Shape building adds separate shapes together to make more complex shape designs using the Shape Builder Tool. It can also be used to delete shape areas.

![Image 1: Shape building after](https://images.ctfassets.net/3p2fxa94bzao/2uXzWT167vHemyIDq6mmBy/f9917a5b960a3c5ef619073d208da7b2/shape_building_after.jpg)

(A) Adding shapes, (B) deleting unwanted areas, (C) deleting areas on an open filled curve.

![Image 2: Shape building before](https://images.ctfassets.net/3p2fxa94bzao/3VFnVFxg10vUVuYCN7NCEc/33b5fe0320fade119821abed28a9edb7/shape_building_before.jpg)

(A) Adding shapes, (B) deleting unwanted areas, (C) deleting areas on an open filled curve.

Shape building lets you add geometric and closed shapes into a single, identifiable real-world shape, e.g. a guitar, steam train silhouette, celtic knot, etc. You can also delete unwanted areas that result from overlapped shapes for interesting cutout effects. Open filled and unfilled curves can also have concave or enclosed areas deleted.

The tool works by making an in-tool selection of 'candidate' shape areas for shape building, then either adding the selected areas together to form a new shape or removing selected areas, or both.

Objects need to be previously selected prior to shape building. Typically, drag a marquee over the shapes you want to work with. You can then choose which objects will be shape building candidates by dragging across shape areas in different ways, i.e. using a freehand line, straight line or selection marquee.

The default tool behavior is to build up a selection of candidate shape areas, then once you're happy with your selection you can add or delete them in a final operation. This offers maximum flexibility and experimentation while shape building in advance of committing to your changes. Alternatively, you can take an 'as-you-go' approach to shape building where different Action modes will add, delete or create areas immediately using the different drag methods mentioned previously.

1.   In the Vector Studio ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg) , select the **Shape Builder Tool**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6Qt7iNQGUBJt9ih4meyore/395b4d3e00ef6e016607c08170cc0b94/shape_builder_tool.svg) .
2.   Drag a marquee over the objects you want to include.

You're not actually performing shape building at this point—just including the objects you want to work on.

1.   Ensure the **Shape Builder Tool**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/6Qt7iNQGUBJt9ih4meyore/395b4d3e00ef6e016607c08170cc0b94/shape_builder_tool.svg)  is active and objects are selected.
2.   On the context toolbar, choose a **Drag method**, then drag across shape areas to include them as candidates for shape building—you can use a freehand or straight line drawn between adjacent areas, or a marquee drawn over the selected shapes. A strong outline indicates a targeted area ready for candidate selection. Once selected, linear hatching indicates the shape area is a candidate.
3.   (Optional) On the context toolbar, choose a **Clean up** method for automatically removing unwanted internal or connected curves, as well as all unused geometry.
4.   When you're happy with your chosen shape areas, select one of three **Action** options on the context toolbar: 
    *   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/GXhN3miWqGN4hfZoSHTFv/e2f98f4e7a232acd03511c813b93bea4/add_to_shape.svg)  Creates a new shape from selected areas; the original affected objects are removed. Alternatively, press the **⏎** key (Mac) / **Return** key (Windows).
    *   ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/1gUWUFMmYBNeYqZEs7IT5M/f737ada42872842dc19234072819cb1c/remove_from_shape.svg)  Deletes selected shape areas. Alternatively, press the **⌫** key (Mac) / **Backspace** key (Windows).
    *   ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/65FxyvESwMrqye4ttZojlp/93ae76e23b52e05a1d518170261648b8/create_new_shape.svg)  Creates a new shape from selected areas while retaining the original selected objects.

Use +, - and * keys on your numeric keypad for the above actions, respectively.

To deselect any selected areas, press the **Esc** key.

1.   In the Vector Studio ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg)  select the **Shape Builder Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/6Qt7iNQGUBJt9ih4meyore/395b4d3e00ef6e016607c08170cc0b94/shape_builder_tool.svg)  and objects.
2.   On the context toolbar, enable one of the **Action** options (![Image 11](https://images.ctfassets.net/3p2fxa94bzao/GXhN3miWqGN4hfZoSHTFv/e2f98f4e7a232acd03511c813b93bea4/add_to_shape.svg) ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/1gUWUFMmYBNeYqZEs7IT5M/f737ada42872842dc19234072819cb1c/remove_from_shape.svg) ![Image 13](https://images.ctfassets.net/3p2fxa94bzao/65FxyvESwMrqye4ttZojlp/93ae76e23b52e05a1d518170261648b8/create_new_shape.svg) ).
3.   Choose a **Drag method** to shape build with.
4.   Drag from a starting area to other areas and release to add, delete or create immediately.

When adding areas, the object style (fill/stroke color, layer effects and stroke properties) from the heavily outlined area you drag from (or marquee select from) is carried over by default; dragging from outside the area will pick up the currently set default stroke/fill instead. You can disable this by unchecking **Use style from first selected area** on the tool's context toolbar. Instead, the currently set default stroke/fill will be applied to the newly created area.

The following modifier keys can be used:

*   To instantly delete selected areas (instead of adding together) or manually remove unwanted curves while dragging, press the **⌥** key (Mac) / **Alt** key (Windows) as you drag using any drag method.
*   The **⌘** key (Mac) / **Ctrl** key (Windows) clears the selected areas when clicked and makes a new layer selection of the clicked object.
*   The **⇧****⏎** keys (Mac) / **Shift**+**Return** keys (Windows) create a new shape from selected areas.

*   [Selecting](https://www.affinity.studio/help/object-control-select/)
*   [Shape Builder Tool](https://www.affinity.studio/help/tools-tools-shape-builder/)
*   [Building shapes with the Blob and Erase brushes](https://www.affinity.studio/help/object-control-join-vector-brushes/)
*   [Keyboard shortcuts for general editing](https://www.affinity.studio/help/workspace-shortcuts-editing/)

How would you rate the help you received from this article?
