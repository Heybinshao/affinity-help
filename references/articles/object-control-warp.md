---
title: "Warping - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-warp/
slug: object-control-warp
fetched: 2026-08-06
---

# Warping - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-warp/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Graphic design](https://www.affinity.studio/help/graphic-design/)
3.   Warping

The Vector Warp feature lets you warp one or more objects non-destructively. A choice of warp presets is available, with any preset being editable using a customizable warp mesh.

![Image 1: Vector warp after](https://images.ctfassets.net/3p2fxa94bzao/5oSfvJlYEcvW2xGUdEZUPe/0bcfdcde53362ef47a690810dd887f61/vectorwarp_after.jpg)

![Image 2: Vector Warp before](https://images.ctfassets.net/3p2fxa94bzao/41HtJQdNKiinGOJi7aYWRN/c82711431076fc97d9d409f610e42464/vectorwarp_before.jpg)

You can warp shapes, straight lines, curves and text by applying a warp preset directly to selected objects. All warp presets apply a mesh to the objects which can be manipulated.

Vector warps can also be symbolized to allow warp edits to update across multiple instances of the same design at the same time. For example, when designing warped logos across artboards.

With these warp presets, objects are not initially warped but need to be warped manually. The Mesh preset lets you reposition existing or manually added mesh junctions (circular nodes) as well as their control handles. Quad and Perspective presets let you drag by the mesh's corner junctions and control handles.

The presets differ because the mesh's junctions and control handles are set up specifically for mesh grid, quad and perspective warp design.

![Image 3: Warp types](https://images.ctfassets.net/3p2fxa94bzao/VewpC2pGiGYphn06ckFri/3b7664a8761cf85db67abfbaff81dfb7/meshquad_edit_after.jpg)

Mesh (left) and Quad/Perspective presets (right) showing their pre-warp state (Before) and after applying a warp by editing mesh junctions (After).

![Image 4: Warp types](https://images.ctfassets.net/3p2fxa94bzao/30vgAy4rhViSUpNMXefPo5/bd2d51ea608ebaa4aca07bf1168528a4/meshquad_edit_before.jpg)

Mesh (left) and Quad/Perspective presets (right) showing their pre-warp state (Before) and after applying a warp by editing mesh junctions (After).

Different shaped warp presets can be applied automatically depending on the design you're looking for. They offer familiar and popular warps and can be a good starting point before fine-tuning the warp.

![Image 5: Warp types](https://images.ctfassets.net/3p2fxa94bzao/1ZWJuQ0ceC2EjUb8WkiYfN/ff3ee196b32dd39ec48441a8b01ec237/warp_types.png)

Shaped warp presets: Arc - Horizontal, Bend - Vertical, Fish Eye, Twist (left to right).

Any warp preset will create a warp group that controls the warp. Contained objects within the warp group remain unaffected, giving the feature its non-destructive behavior.

Warp groups behave much like ordinary groups. Any group can be moved on the page, while any contained object can be dragged in or out of the group at any time.

You can create warp groups within a warp group to introduce warp-in-warp effects with each warp potentially using different warping styles.

1.   Select one or more objects.
2.   On the **Vector** menu, select a preset from the **New Warp Group** flyout.
3.   On the context toolbar, adjust settings specific to the type of warp preset chosen.

*   On the context toolbar, select **Mute Mesh**.

*   On the context toolbar, select **Convert to Curves**.

The object is turned into a closed shape made up of curves. For text, each text character is converted to a separate curve. The resulting curves are grouped automatically.

Once warped, you can edit the warp using the **Node Tool** in a similar way to editing a curve, except you are actively warping as you edit, as opposed to reforming a curve or shape. Editing will let you reposition one or more junctions, adjust any selected junction's control handles, add junctions or reposition a mesh patch (the area enclosed by four mesh junctions).

You can use various techniques for making multiple selections of junctions. This allows you to warp from multiple points in one operation. Selection methods include:

*   Marquee selection—you drag a marquee over a range of junctions to encompass them.
*   Individual selection—use a modifier to select multiple junctions one-by-one.
*   Lasso/polygon selection—use a modifier to drag a lasso around junctions or draw polygons (click-by-click or tap-by-tap) for more precise targeting of specific junctions.

When you reposition junctions you can make use of two types of snapping, i.e.

*   Global snapping—you can snap junctions to page horizontal/vertical center and page elements (e.g., margins and placed guides) just like snapping nodes when pen drawing.
*   Junction-to-junction snapping—use context toolbar **Snap** options to align junctions to each other vertically and horizontally.

Any contained object in a warp group can be edited independently of the group and other grouped objects. For example, you can fix a typographic error or rename the warped text at any time, or recolor a specific object.

1.   On the **Layers** panel, click the chosen warp group's layer thumbnail.
2.   With the **Node Tool** now active, reposition the junctions or connected control handles by dragging.

Do any of the following within the warp's outline:

*   Click on a mesh line.
*   Double-click in any area enclosed by mesh lines.

The new mesh junction can then be repositioned to warp the area directly under the junction.

1.   Click anywhere within a mesh patch, i.e. the area enclosed by four junctions, to place a circular 'hollow' junction target.
2.   Drag the target in any direction to warp the entire patch, moving its four junctions simultaneously and in relation to each other.

*   Select a junction and drag one of its control handles.

1.   Select **Snapping** from the top right of your workspace.
2.   Drag a junction to page horizontal/vertical center or page elements (e.g., margins and placed guides).

*   On the warp group's context toolbar, select a **Snap** menu option. 
    *   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/51HD6zgLpqG5UqA2jobNPE/8c9fcdb16ae0dd211d8231c775479444/snap_align_selected.svg) **Align to nodes of selected curves**—will horizontally or vertically align any node you drag to any other node in the same warp group.
    *   ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3J6BVdOa08adck0Vw0bsx7/5555298ad5f79b3dd03e2a4ceb18696f/snap_selected_dragging.svg) **Snap all selected nodes when dragging**—will snap multiple selected nodes, when dragging, to a "target" node in the same warp group.

Do any of the following:

1.   With the **Move Tool** active, click on the target object in the warp group until it becomes selected.
2.   Edit the object as you would normally do.

When using the Node Tool, the following modifier keys can be used to edit the mesh:

*   Pressing the **⇧** key (Mac) / **Shift** key (Windows) while dragging a selected junction(s) will constrain vertically, horizontally or diagonally (45°).
*   Select junctions with the **⇧** key (Mac) / **Shift** key (Windows) pressed to create multiple selections; click individual junctions to remove from the selection.
*   Pressing the **⌥** key (Mac) / **Alt** key (Windows) and dragging a control handle creates a sharp (cusp) corner on a mesh junction.
*   Pressing the **⌥** key (Mac) / **Alt** key (Windows) and drag over junctions to select multiple junctions within the drawn lasso area. Alternatively, select by drawing polygonal areas click-by-click.
*   The **⌥** key (Mac) / **Alt** key (Windows) temporarily overrides snapping.
*   **⌘****Y** (Mac) / **Ctrl**+**Y** (Windows) toggles between the active warp and an X-ray 'filled' view mode showing the warp muted (unwarped).

*   [Selecting and aligning nodes](https://www.affinity.studio/help/curves-shapes-select-align-nodes/)
*   [Snapping](https://www.affinity.studio/help/design-aids-snapping/)
*   [Layers panel](https://www.affinity.studio/help/panels-layers-panel/)

How would you rate the help you received from this article?
