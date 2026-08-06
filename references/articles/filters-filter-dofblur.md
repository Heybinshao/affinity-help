---
title: "Depth Of Field Blur filter - Affinity Help Center"
source: https://www.affinity.studio/help/filters-filter-dofblur/
slug: filters-filter-dofblur
fetched: 2026-08-06
---

# Depth Of Field Blur filter - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-filter-dofblur/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Depth Of Field Blur filter

The Depth Of Field Blur

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/1DgG4y32fro0ssjVf1Bhx0/a0d21e90ce36802630596f4957f046cc/dof_blur_tool.svg)

 filter applies a blur gradient that can be used to simulate extreme depth of field and miniaturization effects, such as tilt shift.

![Image 2: After](https://images.ctfassets.net/3p2fxa94bzao/3Jq2igKwLuIu0cpweiPtSr/932bf4422b87b9758a73e0fa9805bc9c/filter_dofblur_after.jpg)

![Image 3: Before](https://images.ctfassets.net/3p2fxa94bzao/65AN8WjhVULHDFmYu6zTNa/105812d18d0f0e8cdba147801363be9d/filter_dofblur_before.jpg)

The filter applies variable blur across an image based on a focus plane or depth range. Areas closer to the focus point remain sharp, while those further away are progressively blurred. Unlike simple blur filters that apply the same effect everywhere, Depth of Field blur filter mimics optical lens behaviour and thus creates gradual transitions between sharp and blurred regions, which produces a more natural photographic result.

To use the destructive version of the filter, select it from the **Pixel > Filters > Blur** menu. The live version can be accessed from:

*   the **Layers**panel by clicking **Live Filters**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6jrlitTLwUvWbBWmQ3gUls/95c943cf10acdb62f3053cf6dff7aaa9/add_live_filter_layer.svg) .
*   the **Pixel > New Live Filter Layer > Blur** menu.

When using the tilt shift effect to "miniaturize" a scene, you will get the best effect if you choose your images carefully. Models are generally viewed from above, so the tilt shift effect will work best on images taken with an elevated viewpoint and a wide angle of view. Buildings, roads, traffic and railways make excellent subjects.

*   **Portrait Enhancement**—Blur backgrounds subtly to isolate the subject while keeping facial features crisp and natural.
*   **Product and Mocuk Design**—Apply controlled blur to backgrounds or foregrounds so products, packaging, or UI elements stand out clearly.
*   **Compositing and Scene Integration**—Match the focus characteistics of different elements ina composite, helping them feel part of the same scene.
*   **Miniature or Tilt-Shift-Style Effects**—Apply stronger blur gradients to create a stylised miniature look where only a narrow band of the image remains sharp.
*   **Visual Hierarchy in Layouts**—Introduce depth cues that support reading order or emphasis in marketing visuals and presentations.

The gradient stops determine the position and extent of the transition between the areas in sharp focus and those that are blurred.

![Image 5: DOF blur ](https://images.ctfassets.net/3p2fxa94bzao/WKvL1ZrOY70roGASXbOfG/3a0fe0b067b11108c8d889c05b586a98/filter_dofblur_annotated.jpg)

(A) Focus origin, (B) Inner lines, (C) Outer lines, (D) Transition areas.

The focus origin (A) defines the central point at which the image is kept completely in focus. Reposition the focus origin by dragging on the stop.

The inner lines (B) define the width of the area in focus. For the Tilt Shift mode these can be set independently by dragging each of the stops in turn, or, symmetrically by dragging one of the stops while holding the **⌘** key (Mac) / **Ctrl** key (Windows). The Elliptical mode always matches the shape of the inner lines to the outer lines so that only the width can be specified.

The outer lines (C) define the end of the blur transition. For the Tilt Shift mode, these can be set independently by dragging each of the stops in turn, or, symmetrically by dragging one of the stops while holding the **⌘** key (Mac) / **Ctrl** key (Windows). The Elliptical mode always sets the stops in pairs.

The transition areas (D) between the inner and outer lines are where the blurring gradually increases. The wider the lines, the more gradual the transition. The area on the outside of the lines has the filter applied at the full amount set by the **Radius** slider.

The angle of the filter can be changed by dragging the stops at an angle. Once the desired angle is achieved, holding the **⇧** key (Mac) / **Shift** key (Windows) will temporarily lock the angle to allow for further adjustment of the width of the adjustment.

When using the tilt shift effect to "miniaturize" a scene, you will get the best effect if you choose your images carefully. Models are generally viewed from above, so the tilt shift effect will work best on images taken with an elevated viewpoint and a wide angle of view. Buildings, roads, traffic and railways make excellent subjects.

The following settings can be adjusted in the filter dialog:

*   **Mode**—choose from the pop-up menu to define the type of blur generated.
*   **Radius**—controls intensity of the blur. Type directly in the text box or drag the slider to set the value.
*   **Vibrance**—controls the color intensity of less saturated colors (a high value increases the 'model-like' effect).
*   **Clarity**—increases the local contrast and gives the appearance of increasing the sharpness of the image.

*   **Elliptical**—useful for photos with a single subject, as it creates an graduated elliptical blur vignette.
*   **Tilt Shift**—often used to simulate a scene created by models.

*   [Using live filters](https://www.affinity.studio/help/layers-livefilters/)
*   [Applying filter](https://www.affinity.studio/help/filters-filters-applying/)
*   [Diffuse Glow filter](https://www.affinity.studio/help/filters-filter-diffuse-glow/)
*   [Compositing Studio](https://www.affinity.studio/help/workspace-compositing-studio/)

How would you rate the help you received from this article?
