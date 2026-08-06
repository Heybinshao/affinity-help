---
title: "Selecting - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-select/
slug: object-control-select
fetched: 2026-08-06
---

# Selecting - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-select/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Selecting

Before you can move or modify objects or layer content, you must first select them.

![Image 1: Selecting](https://images.ctfassets.net/3p2fxa94bzao/1garQD0dQSQi4M7wBXVdDL/0e8409c9eb2521328001bee982eadad6/selecting_objects.png)

By default, the **Auto-select** option is enabled on the context toolbar. As expected, it automatically selects the object and its layer when you select it on the page. The option can be disabled if preferred.

The selection behavior depends on the current **Edit within current container** setting on the **Layers** panel:

*   When enabled, the command will select objects across all layers and sub-layers.
*   When disabled, only objects on the current layer are selected. Objects within sub-layers are not selected.

For some shapes (e.g. star shapes), a **Base box** type will be established on shape creation to accommodate the range of different potential shape sizes when creating variants of that shape. However, you can temporarily swap to a 'tighter' bounding box called **Regular bounds** if needed. The latter is useful for accurately resizing a shape by its corner/edge handles to another object or page element.

![Image 2: Base box and regular bounds](https://images.ctfassets.net/3p2fxa94bzao/5Tu8JOOgF1819IkA1tEnYw/db4f83d0217c4857379ce58333dc61ba/selectionbox_shape.png)

Selection box types: Base box (A) and Regular bounds (B)

For rotated multiple selections of objects or pixel layers, you can temporarily reorient the selection's selection box to vertical using the same Regular bounds type. Otherwise, the selection box will stay transformed with the transformed items (using the Base Box type).

![Image 3: Rotated multiple selection with reoriented selection box](https://images.ctfassets.net/3p2fxa94bzao/3RpmApRfsLziHT8CuwBNfN/abdf619129972edf6fb5cad3017a6f60/selectionbox_multiselection.png)

Rotated multiple selection before (A) and after (B) reorienting the selection box to Regular bounds

It's possible to permanently set the object's selection box to orient to the page's horizontal and vertical edges. The object is unaffected. When reselecting the items again, the selection box will remain unrotated.

If you're using axonometric grids, the additional selection box type _Planar bounds_, which matches the current grid, can also be swapped to and be made permanent if needed.

The fundamental methods of selecting objects described here are complemented by advanced **Select Same** and **Select Layer** commands that [build selections based on object attributes](https://www.affinity.studio/help/object-control-select-by-attribute/), such as type, fill color, or stroke width.

1.   On the **Select**menu, choose **Select All on Current Layer**.

**Select All on Current Layer** is only available when the active layer is a **Container Layer**. If no Container Layer is active, the command is unavailable.

*   On the **Layers** panel, click **Edit within current container**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/7Mk5jz4pzwPhVhM6CPJAOg/b3d17c0013c768b2e5861e717791947e/edit_all_layers.svg) .

Do one of the following:

*   With the **Move Tool**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg)  selected, click an object, group or layer content on the page to select it.
*   On the **Layers** panel, click a layer entry.

*   With the **Move Tool**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg)  selected, hold the **⌘** key (Mac) / **Ctrl** key (Windows) and right-click an object in the view.
*   On the contextual menu that appears, select any content contained in the same group/layer as (or deeper than) the object you clicked.

Do one of the following:

*   With the **Move Tool**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg)  selected, **⇧**-click (Mac) / **Shift**-click (Windows) each object on the page in turn to select them.
*   With the **Move Tool** selected, drag to draw a marquee around the object(s).
*   On the **Layers** panel, **⌘**-click (Mac) / **Ctrl**-click (Windows) each object or layer.
*   On the **Layers** panel, **⇧**-click (Mac) / **Shift**-click (Windows) two objects or layers to select them and all those between.

*   On the **Edit** menu, click **Select All** or **Deselect**, respectively.

Do one of the following:

*   With the object or layer selected, on the **Layer** menu, choose from the **Select** flyout: 
    *   **Next Layer** / **Previous Layer**—selects an object adjacent to the selected object in z-order sequence, within the same layer, group or entire layer stack. The option will cycle selection from bottom to top and vice versa.
    *   **Top Layer** / **Bottom Layer*******—as above but selection is made of the top or bottom object in the layer, group or entire layer stack in z-order.
    *   **Parent Layer**—selects the parent clipping object, layer or group in which the selected object or layer is placed.

*   **^(ctrl)**-click (Mac) / **right**-click (Windows) the object or layer, then choose the equivalent options as above from the pop-up menu.

*   With an object or layer selected, on the **Layers** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) and choose **Select Same Name** from the pop-up menu.

Naming has to be custom naming rather than the default naming, e.g. Rectangle, Curve, Art Text, etc.

*   With an object or layer selected, on the **Layers** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) and choose **Select Same Tag Color** from the pop-up menu.

*   On the Move Tool's context toolbar, choose one of the options below. These let you optionally select only objects or groups on the page, or just from the Layers panel (on-page selection is prevented). 
    *   **Default**—objects and groups can be selected on the page or Layers panel.
    *   **Objects** (or **Layers***)—only objects can be selected on the page, while grouped items will be selected as if ungrouped; layers, groups and objects can be selected from the Layers panel.
    *   **Groups**—only groups can be selected on the page; layers, groups and objects can be selected from the Layers panel.

*   On the **Layer** Menu, choose **Select > Cycle Selection Box**.

1.   Cycle to the selection box as above.
2.   On the same menu, choose **Set Selection Box**.

For example, this includes objects such as shapes that have been rotated by 90, 180 or -90°.

When using the Move Tool, the following modifier keys can be used to aid layer selection:

*   With the **Auto-select** option disabled: 
    *   **⌘**-click (Mac) / **Ctrl**-click (Windows) an object or layer content on the page to temporarily override the option and enable the selection.

*   With the **Auto-select** option enabled: 
    *   On the **Layers** panel, holding the **⇧** key (Mac) / **Shift** key (Windows) and clicking selects multiple objects or layer contents. The same is achieved by clicking objects or layer content on the page while holding the key.
    *   Holding the **⇧⌘** keys (Mac) / **Shift**+**Ctrl** keys (Windows) while clicking on multiple objects or layer contents on the page in turn, selects them.
    *   The **.** (period) key toggles a shape's bounding box between a default Base box and a Regular bounds box; the former accommodates the range of different potential shape sizes when creating variants of that shape; the latter lets you manually swap to a tighter regular bounding box, for tighter snapping control. Alternatively, use **Select > Cycle Selection Box** on the **Layer** Menu.
    *   For Mac: As you drag a selection marquee, pressing the **⌃(ctrl)** key selects objects or layers which are only partially covered by the selection marquee. This behavior can be made the default in the [the app's settings](https://www.affinity.studio/help/workspace-settings/).

Related behaviors can be adjusted from the app's settings:

*   **Tools > Select object when intersects with selection marquee**

*   [Selecting by attribute](https://www.affinity.studio/help/object-control-select-by-attribute/)
*   [Move Tool](https://www.affinity.studio/help/tools-tools-move/)
*   [Layers panel](https://www.affinity.studio/help/panels-layers-panel/)
*   [Settings](https://www.affinity.studio/help/workspace-settings/)

How would you rate the help you received from this article?
