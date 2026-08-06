---
title: "Desktop settings: Assistant - Affinity Help Center"
source: https://www.affinity.studio/help/desktop-settings-assistant/
slug: desktop-settings-assistant
fetched: 2026-08-06
---

# Desktop settings: Assistant - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/desktop-settings-assistant/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Desktop settings: Assistant

Decide how the Assistant responds to specific editing actions, including whether it takes automatic corrective steps, displays alerts, or alters undo behavior.

When you perform certain operations—for example, pixel painting (or erasing) on vector-based container layers, or applying adjustments to selections—the Assistant will take action according to your settings and display an alert message to make you aware.

The following settings are available:

*   **Enable assistant**—When checked, the Assistant will perform your chosen action for any operation it can help with. When unchecked, the Assistant does not perform any actions.
*   **Automatically undo and redo assistant actions**—When checked, any action that has been recorded as multiple consecutive history states is treated like one state by the Undo and Redo commands. When unchecked, the commands need to be selected multiple times to undo/redo multi-state Assistant actions.
*   **Alert when assistant takes an action**—When checked, the Assistant will display an alert message whenever it takes action. When unchecked, alert messages are not displayed.
*   **Painting with no layer selected**—In the Pixel Studio, you can choose to create a new pixel layer for your brush strokes using 'Create pixel layer and paint'; 'Take no action' means that no pixel painting is allowed. If a vector object is selected, a new pixel layer is created above the vector object. If a pixel layer is selected, your brush stroke is added to the pixel layer.
*   **Erasing from vector layers**—In the Pixel Studio, this option lets you choose to erase on a created pixel mask over your vector-base container layer or vector object, immediately rasterize the vector layer and erase directly on it, or take no action.
*   **Other brushes on vector layers**—For retouching pixel brushes (e.g., Burn Brush Tool, Smudge Brush Tool, etc.), any applied brush stroke rasterizes the vector-based container layer or vector object by default. You can change this behavior by selecting 'Take no action', which doesn't convert the layer or apply the stroke.
*   **Brush tool sharing**—Choose whether a selected brush and context toolbar settings are shared between tools of a similar nature (e.g. Dodge, Burn and Sponge Brush Tools), shared across all tools, or each tool's brush is set independently.
*   **Applying filters to non-pixel layers**—In the Pixel Studio, when a filter is added to a vector layer, the Assistant can either rasterize the vector layer and apply the filter to it, or take no action.
*   **Adding adjustment layer to selection**—Depending on if a layer is selected or not, the created adjustment layer is placed differently: With the **Add Adjustment layer to parent layer**option set (default), when an item is selected, the adjustment layer is applied directly above the item's layer. With no selection in place, the adjustment is applied at the top of the layer stack.
*   **Adding mask layer to selection**—Analogous to 'Adding adjustment layer to selection' above, but for mask layers.
*   **Adding filter layer to selection**—Analogous to 'Adding adjustment layer to selection' above, but for filter layers.
*   **Delete selection from Image/RAW layer**—In the Pixel Studio, when deleting a selection from an Image or RAW layer, you can choose whether a mask layer is added or the current layer rasterized and deleted.
*   **Duplicate selection from Image/RAW layer**—In the Pixel Studio, when duplicating a selection from an Image or RAW layer, you can choose whether the layer is duplicated and rasterized or duplicated with a mask layer added.
*   **Develop Assistant**—Select to display a dialog with settings for raw photo development behaviours.

The following settings are available on the **Develop Assistant** dialog:

*   **RAW Engine**—For Mac, this provides a choice of RAW processing engines for you to use—Affinity RAW engine (used by default) or Apple's Core Image RAW engine. For Windows, only the Affinity RAW engine is available.
*   **Default lens profile**—The **Auto-select**option enables automatic lens correction for supported camera [Lens profiles](https://affinity.studio/help/supported-lens-profiles) if installed with the app. If a camera is not included (perhaps a new model), you can include it by adding its profile—a downloaded Lensfun XML file or Adobe Lens Correction Profile (LCP)—to the database by using **Settings > General**. The **Last used**option uses the **Lens Profile**previously chosen from the Develop Studio's **Lens panel**(under **Lens Correction**).
*   **Noise reduction**—Automatically enables either color noise reduction, color and luminance noise reduction, or disables any initial noise reduction. Color noise reduction is recommended for the vast majority of camera RAW images.
*   **Sharpening**—Automatically enables or disables sharpening. A light or moderate approach is taken which controls the sharpening intensity at image edges and detail.
*   **RAW output format**—Choose between **RGB (16 bit)**or **RGB (32 bit)**output when developing a RAW image. Choosing the latter option allows you to maintain a full 32-bit float environment from initial raw development to export and take advantage of extra precision.
*   **Default tone curve**—Controls how RAW images are treated upon import and during a selected image process: Panorama, Stack, HDR Merge, Focus Merge, Astrophotography Stack, Batch Job, and Acquire Image. RGB 32-bit color format images can also output with the setting active, resulting in HDR unbounded pixel merges. If the output format remains set to RGB16 (default), you can apply alternative tone curves such as Compressed, Natural, Contrast, or Log. These curves perform tone mapping by compressing the RAW image’s dynamic range into a standard displayable range, making them a suitable starting point for merge operations such as panorama stitching where exposure equalisation is required. Alternatively, for full manual workflows, you can choose not to apply a default tone curve, which is respected for all subsequent image processes. 
*   **Exposure bias**—Choose whether to apply exposure bias value if stored in the RAW image's EXIF data. Like Histogram stretch, both 'default' and 'initial' give the same results but reports zeroed or actual values, respectively. The 'Take no action' option ignores the exposure bias value.
*   **Map default region**—(For Mac): Sets the map that displays in the **Location**panel to a chosen region, if the RAW image contains no GPS location data in its EXIF data.

*   For Mac: From the Affinity app menu, select **Settings**.
*   For Windows: On the **Edit** menu, select**Settings**.

*   From **Settings**, tap **Assistant Options** and select options.

*   From **Settings**, tap **Assistant Options** and uncheck **Enable assistant**.

*   [About Settings for desktop](https://www.affinity.studio/help/workspace-settings/)
*   [Settings: Auto-Correct, Abbreviations, Filler Text, and Title Exceptions](https://www.affinity.studio/help/desktop-settings-auto-correct-and-other-text/)

How would you rate the help you received from this article?
