---
title: "Constraints - Affinity Help Center"
source: https://www.affinity.studio/help/design-aids-constraints/
slug: design-aids-constraints
fetched: 2026-08-06
---

# Constraints - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/design-aids-constraints/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Constraints

Constraints ensures that designs can be presented in different layouts quickly and easily.

The feature is perfect for:

*   Designing UI/device mockups, e.g. to envisage how dialogs can be resized without affecting the position of every dialog control.
*   Intelligent captioning in the Layout Studio![Image 1](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg) , i.e. adding caption strips within your picture frames, whose shape and caption text can be controlled with respect to anchoring and scaling.

![Image 2: After](https://images.ctfassets.net/3p2fxa94bzao/27d6cU6ml6VtgWC3ko0d5q/23ad644b9c21f13af84d2ab9d89b8370/constraints-after.png)

Scaling has been disabled for all objects except the text, trophy button and the top lines. Anchoring has been applied to most objects except the text and trophy button.

![Image 3: Before](https://images.ctfassets.net/3p2fxa94bzao/2HG8yMLfoELdCOjQ1PS2G0/7b200c059b9e64e6cf0cd5d8416160c7/constraints-before.png)

Scaling has been disabled for all objects except the text, trophy button and the top lines. Anchoring has been applied to most objects except the text and trophy button.

A child object can be prevented from being scaled when resizing its parent and be anchored to its parent in different ways. This ensures that designs can be presented in different layouts quickly and easily.

Using constraints gives you the freedom to design without worrying that design rework will be adversely affected by unwanted object rescaling. By controlling selectively which objects will/won't be scaled and anchored, your design will always respond correctly to scaling.

Constraints only work in parent - child object relationships, i.e. where a parent object (container) contains nested content. A child object's scaling and anchoring is always in relation its container. For example, in UI design, a device mockup could have parent - child object relationships such as artboard - panel, panel - button, etc.

Constraining is exclusively carried out from the Constraints panel. The panel controls:

*   horizontal and vertical scaling in relation to its parent's size
*   anchoring of an object by its top, left, right and/or bottom edge in relation to its parent object's equivalent edge.

By default, nested content will scale when its container is resized. A child object is _not_ anchored by default.

To prevent a child object losing its aspect ratio when its parent is scaled disproportionately, you can set it to **Min Fit** or **Max Fit**.

*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/3mRmlAjx5OGdFFv1UXmp29/9ddae4701b5d40b8ca4c1782ea7a709e/constraints_minfit.png) **Min Fit**—when the parent object is resized disproportionately, the child object may scale so it always fits within its parent object (if unanchored). Use on text to ensure it always fully displays.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3OiUfLlzSS1p4qt1p8egHI/8a9e525323b237934a53edfca82e0038/constraints_maxfit.png) **Max Fit**—when the parent object is resized disproportionately, the child object may scale. The child object can become bigger than its parent object, potentially clipping content from view. Using a web banner mockup as an example, a child object (e.g., an image) will always fully fill the containing banner area (avoiding white letterboxing) but may be subject to clipping.

In both cases, if the parent object is resized proportionately, the child object will also scale proportionally.

If a child object is set to **Min Fit** and its parent object is resized wider, the child object will not scale. However, if the parent object is later made taller, the child object will begin scale to honor its original aspect ratio and size with respect to it parent.

1.   Select a child object.
2.   On the **Constraints** panel, click the horizontal or vertical solid double arrow (or both) in the panel's inner square. A grayed-out dashed arrow means that scaling won't occur when its parent object is resized.

In Vector Studio

![Image 6](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg)

, an artboard, when resized, will not scale its contents by default. To allow constraints to operate as for other parent - child objects, uncheck **Lock Children** on the context toolbar.

1.   Select a child object.
2.   On the **Constraints** panel, click a grayed-out dashed line between the inner and outer square to anchor the object to its parent in that direction (top, bottom, left, or right). A solid line means anchoring is being applied.

1.   Select a child object.
2.   On the **Constraints** panel, click **Min Fit** or **Max Fit**.

*   [Transforming](https://www.affinity.studio/help/object-control-transform/)
*   [Constraints panel](https://www.affinity.studio/help/panels-constraints-panel/) (desktop only)

How would you rate the help you received from this article?
