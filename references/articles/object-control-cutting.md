---
title: "Cutting - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-cutting/
slug: object-control-cutting
fetched: 2026-08-06
---

# Cutting - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-cutting/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Graphic design](https://www.affinity.studio/help/graphic-design/)
3.   Cutting

Objects can be easily cut up in various ways using the Knife Tool or a Divide Boolean operation.

![Image 1: Cutting after](https://images.ctfassets.net/3p2fxa94bzao/6IAI0hgYE6AJiFTyaWvAUk/f248694b7b223a8a9b9c079a025a8427/cuttingobject_after.jpg)

Knife Tool: (A) Single-stroke cut and delete, (B) Intersecting multi-stroke cut and delete, (C) Single-stroke cut and separate, (D) Multi-stroke cut and recolor of fragments.

![Image 2: Cutting before](https://images.ctfassets.net/3p2fxa94bzao/59UQV0viO9tjsQHlijZqW9/cd7adfdcc66da04ec2fb9e1c0ad513bd/cuttingobject_before.jpg)

Knife Tool: (A) Single-stroke cut and delete, (B) Intersecting multi-stroke cut and delete, (C) Single-stroke cut and separate, (D) Multi-stroke cut and recolor of fragments.

![Image 3: Cutting curves after](https://images.ctfassets.net/3p2fxa94bzao/4NoNGGqyjBmwkuSuB8yIHl/4540446e758416e339667e2cca42500d/cuttingcurves_after.png)

Knife Tool: (A) Cutting a single curve with two scissor cuts and (B) cutting multiple straight lines simultaneously using a single-stroke cut. Unwanted curve fragment(s) are subsequently deleted in both.

![Image 4: Cutting curves before](https://images.ctfassets.net/3p2fxa94bzao/4szEVPCLjlU4pbpEUIk9k/9197ed2100f827113d748d9afce7907c/cuttingcurves_before.png)

Knife Tool: (A) Cutting a single curve with two scissor cuts and (B) cutting multiple straight lines simultaneously using a single-stroke cut. Unwanted curve fragment(s) are subsequently deleted in both.

![Image 5: Cutting after](https://images.ctfassets.net/3p2fxa94bzao/7MlskB1HYZFkNmvGUoezQz/a305876fa5db1ff628e2256ddf75cfb1/cuttingdivide_after.jpg)

Divide Boolean operation: splitting an object with a Bézier curve (drawn with the Pen Tool).

![Image 6: Cutting before](https://images.ctfassets.net/3p2fxa94bzao/3GWc319C31D4FKyHtf1oJI/2edf62878f56563fd4b68bb948fbc809/cuttingdivide_before.jpg)

Divide Boolean operation: splitting an object with a Bézier curve (drawn with the Pen Tool).

Two techniques are possible using different features:

*   Knife Tool—cuts objects quickly in one operation using a freeform or straight line drawn with the Knife Tool. Key features include: 
    *   Stroke stabilization: smoothing of the knife stroke.
    *   Autoclosing of open curves to cut out holes from objects.
    *   Scissor cuts: to break open curves at a target node or anywhere on a curve segment or to break open closed shapes too.

*   Divide—takes advantage of the power of the Pen Tool to create a 'cutting' Bézier curve (editable with the Node Tool) to cut from in advance of dividing up into object fragments. This approach lets you fine-tune the cutting line before cutting.

For either technique, instead of repositioning, reshaping or deleting specific fragments after cutting, you can simply recolor each fragment independently.

Cutting works irrespective of layers. You can cut across any selection of objects as long as the selection is in place.

Partially cutting into an object will create a split, i.e. a 'closed up' cut with each side of the cut touching. The appearance is of a single stroke but editing either curve (by moving overlapped/overlapping nodes apart) will open the cut.

When you draw a series of separate strokes that intersect each other, you create a polycurve that cuts out the underlying object.

1.   In the Vector Studio ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg) , select the **Knife Tool**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/3W41poan013uoERhxDhVSA/1f92eb4a00e695076d5e9b1f40bc0047/knife_tool.svg) .
2.   (Optional) Cut with a straight line by enabling **Straight Line**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/4UlRc9n52SzJGlsXOu3fEQ/c2d46fe177a4e49270e62191ff9b1863/line_mode.svg)  on the context toolbar before you drag. By default, you'll cut using a drawn freehand line.
3.   (Optional) For drawn freehand lines, check **Stabilizer** on the tool's context toolbar to draw smoothed lines using a Rope Mode or Windows Mode; use the former for redirecting a smoothed path using a draggable rope that can introduce sharp corners; the latter for a consistently smooth curve.
4.   Drag the cursor across the shape.
5.   With the **Move Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg)  enabled, do any of the following: 
    *   Drag the newly split fragments apart after reselection.
    *   Delete an unwanted fragment by pressing the **⌘** key (Mac) / **Ctrl** key (Windows), clicking a fragment, then pressing the **⌫** key (Mac) / **Backspace** key (Windows).
    *   Select a fragment and recolor with the **Color** panel.

1.   In the Vector Studio ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg) , select the **Knife Tool** from the **Pencil Tool** flyout.
2.   Do one of the following: 
    *   For a knife cut (creating separate curves): Drag the cursor across the curve.
    *   For a scissor cut (creating a polycurve): Hover over a selected curve's target node or anywhere along a curve segment, then click to make the cut (a scissors cursor will show). Use **Vector > Separate Curves** and the **Move Tool** to create separate curves from the polycurve, then reposition the curves independently.

3.   Hold the **⌘** key (Mac) / **Ctrl** key (Windows) to edit the curve(s) (Node Tool behavior), or hold the **⌃(ctrl)⌘** keys (Mac) to delete an unwanted segment on clicking.

Use **Vector > Cut curves with key object** to cut into curves and shapes using a previously targeted key object (assigned with **⌥**-click (Mac) / **Alt**-click (Windows) in a multi-object selection. For example, you could use a morphed geometric shape to cut into underlying vector content. The stroke and fill of the key object are not considered in the cut.

1.   With the **Pen Tool**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/5yh8WdvU7rTqDSqQzwd7ds/3dec05a9bf475b37380b1f79e99125ee/pen_tool.svg) , draw a Bézier curve(s) over an object.
2.   With the **Move Tool**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg) , select the curve(s) and the underlying object.
3.   On the Toolbar, select **Divide**![Image 14](https://images.ctfassets.net/3p2fxa94bzao/01rSjRwpBCN0vFvVz1zEdP/6d2f80a42ab8db370c8f57338c8d2ed3/divide.svg) .

The Divide operation will remove the pen strokes by default, although you can retain them by pressing the **⌥** key (Mac) / **Alt** key (Windows) during the Divide operation.

*   The **⇧⌥** keys (Mac) / **Shift**+**Alt** keys (Windows) draw a straight knife stroke across your object from a fixed position.
*   The **⇧** key (Mac) / **Shift** key (Windows) constrains a straight knife stroke to 45° intervals, including to horizontal and vertical.
*   For Mac: The **⌃(ctrl)** key, while it remains pressed, converts a freehand knife stroke to a straight line stroke as you draw; release the key to continue freehand knife cuts.
*   For Windows: The right-mouse button, while it remains pressed, converts a freehand knife stroke to a straight line stroke as you draw; release the button to continue freehand knife cuts.
*   To delete or edit cut fragments, press the **⌘** key (Mac) / **Ctrl** key (Windows), then the **Backspace** key.

*   [Knife Tool](https://www.affinity.studio/help/tools-tools-knife/)
*   [Draw lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-draw-lines-and-shapes/)
*   [Edit lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-edit-lines-and-shapes/)
*   [Joining with Booleans](https://www.affinity.studio/help/object-control-join/)

How would you rate the help you received from this article?
