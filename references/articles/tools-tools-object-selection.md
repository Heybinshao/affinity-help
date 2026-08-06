---
title: "Object Selection Tool - Affinity Help Center"
source: https://www.affinity.studio/help/tools-tools-object-selection/
slug: tools-tools-object-selection
fetched: 2026-08-06
---

# Object Selection Tool - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tools-tools-object-selection/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   [Canva integrations](https://www.affinity.studio/help/canva-integrations/)
4.   Object Selection Tool

The Object Selection Tool

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/C3NB8httu4Ctqf1QkQHGD/1e133e366f542b290d41d8557e790e0a/object_selection_tool.svg)

 allows you to easily select parts of your composition with a single click.

![Image 2: Pencil drawn example](https://images.ctfassets.net/3p2fxa94bzao/01Nuq4rfvlM2yRm8KHNmNu/090874d60568eef3cc23165aa593bdb7/object_selection_tool_modifiers.jpg)

The Object Selection Tool in its default operation (A), separating object components with a modifier (B), isolating components further with a modifier combo (C).

The **Segmentation** model must be downloaded prior to using the Object Selection Tool. The model is available in **Settings > Machine Learning Models** section.

1.   In the **Canva AI Studio**or **Pixel Studio**, on the **Layers**panel, select the image layer you want to work on.
2.   Select the **Object Selection Tool**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/C3NB8httu4Ctqf1QkQHGD/1e133e366f542b290d41d8557e790e0a/object_selection_tool.svg) .
3.   Drag over the object or area you want to select.
4.   Wait for Affinity to analyze the image.
5.   Review the selection outline.
6.   (Optional) Refine the selection using Affinity’s selection tools, masks, or selection refinement options.

This feature uses Machine Learning (ML) model for automatic object and subject selection. This is in line with Affinity’s ambition to implement ML for the benefit of faster workflow. Models are installed as pre-trained and do not use any of your own data for further training. Because these operations all work 'on device' none of your data leaves your machine at any time.

Affinity's Machine Learning functionality is not generative and advocates human creativity.

The **Object Selection Tool** uses a Segmentation Machine Learning model to identify objects on a layer.

Initially, while hovering over an area, the tool will indicate the inference processing by changing its icon temporarily. Once ready, the hatched lines will appear over the object to indicate what will be selected when clicked. Every newly selected area is treated as a new object selection.

The selection is post-processed with **Soft Edges** enabled on the context toolbar by default. For more complex elements, such as hair or fur, use [**Refine**](https://www.affinity.studio/help/selections-selections-refine/) to clean up your selections.

![Image 4: After Multi-part Objects option toggled on.](https://images.ctfassets.net/3p2fxa94bzao/3fb6mgx409s5Zk078HZ8t1/257e16ef7983ce99af9c5e46d2436a98/multi_object_on.jpg)

After Multi-part Objects option toggled on.

![Image 5: Before Multi-part Objects option toggled on.](https://images.ctfassets.net/3p2fxa94bzao/3OmU53co0coXfytzoT1r0c/c6ecc6cfe9038c4de57b15f743a9296a/multi_object_off.jpg)

Before Multi-part Objects option toggled on.

The following options can be adjusted from the context toolbar:

*   **Mode:**
    *   **New**—when enabled (default), each selection will be treated as an individual one. Pre-visualized selections are indicated by a blue hatched pattern.
    *   **Add**—when enabled, each subsequent selection will be added to the previous one. Pre-visualized selections are indicated by a green hatched pattern.
    *   **Subtract**—when enabled, each subsequent selection will be removed from the previous one. Pre-visualized selections are indicated by a red hatched pattern.
    *   **Intersect**—when enabled, the selection will include the overlapping areas (between two or more previously selected areas). Pre-visualized selections are indicated by a blue hatched pattern.

*   **Multi-part Objects**—when enabled (default), the selection will include all parts of an object (if obstructed by another object, say). When disabled, the sampling object of the mask is bounded to the area you hover over.
*   **Soft Edges**—when enabled (default), the selection will be refined using a small border value to help matte and soften the selection bounds.
*   **Refine**—opens a dialog with options to assist removing elements from your selections.

Use **Soft Edges** (above) for the majority of raster-based workflows. Consider disabling the setting for edge-focus scenarios.

*   The Object Selection Tool has no keyboard shortcut by default, but one can be assigned via the app's Settings. See '[Customizing keyboard shortcuts](https://www.affinity.studio/help/workspace-customizing-shortcuts/)' for details.
*   To separate selections into object components, which inevitably may consist of varied textures, hold the **⌥** key (Mac) / **Alt** key (Windows) while hovering your mouse (or stylus) cursor over the object. For example, it is possible to separate a model's face from the eyes.
*   To further separate object components, hold the **⌥⇧** keys (Mac) / **Alt**+**Shift** keys (Windows) while clicking. For example, it is possible to separate parts of an outfit consisting of varied colors or textures.
*   To establish smaller selection areas, as indicated by the hatched pattern during the operation, dragging on an object enables you to pre-visualize the regions to be selected.

*   [Canva AI and Affinity Machine Learning (ML)](https://www.affinity.studio/help/canva-ai-canva-ai-affinity-ml/)

How would you rate the help you received from this article?
