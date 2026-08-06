---
title: "Creating pixel selections - Affinity Help Center"
source: https://www.affinity.studio/help/selections-selections-create/
slug: selections-selections-create
fetched: 2026-08-06
---

# Creating pixel selections - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/selections-selections-create/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Creating pixel selections

Pixel selections can be created for targeted editing of specific pixel regions. Selection boundaries are defined depending on whether individual pixels are included or excluded.

![Image 1: Pixel selection made with the Selection Brush Tool in Affinity.](https://images.ctfassets.net/3p2fxa94bzao/1pdmeW56wQIsdX8G0FuPmL/695935e7a1e477e6a2508c99093b337b/selections.jpg)

Pixel selection made with the Selection Brush Tool in Affinity.

A pixel selection is simply a drawn area on your image (bounded by a flashing dashed line, often referred to as marching ants). For most selections, the marching ants mark a firm boundary between selected and unselected pixels. However, for selections based on layer intensity or luminosity, pixels can be partially selected. In these cases, the ants mark the boundary where selection strength crosses 50% — pixels outside the ants may still be weakly selected. See [Pixel selection from layers](https://www.affinity.studio/help/selections-pixel-selections-fromlayers/) for more detail.

Various tools for pixel selections are available in the Pixel Studio. A selection is created for various reasons:

*   To limit editing (e.g., painting, applying fills, etc.) to within the selection area only.
*   To selectively copy pixels.
*   As a precursor to creating a mask layer.
*   To draw areas for removal (cutout).

In Affinity, you can perform pixel selection on RAW layers, which opens up a number of options for various flexible workflows.

Note the following behaviors when working with RAW layers, with a pixel selection active and an image layer selected in the panel:

*   Deleting the selection will mask the layer rather than delete it entirely from the layer stack. This aids local editing workflows, especially when targeting inverted selection areas.
*   Duplicating the layer will create a new pixel layer with just the selected pixel data.

You can use the **Assistant** options (found in the app's **Settings**) to change the above default behaviors.

Additionally, the following two options are available by **⌃(ctrl)**-clicking (Mac) / **right**-clicking (Windows) a layer in the panel:

*   **Merge Down**—merges a layer with a pixel layer below.
*   **Merge Visible**—merges all visible layers in the panel into a new pixel layer.

*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/5y7NARvjCJUGwBuFpEc2p3/661f2366873068591331bb4218dd80e8/selection_new.svg) **New**—cancels all current selections and creates a new selection.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/1enLKrGYUHugvrigPRQx07/0f3078675092e74f1915c5dfe91643b1/selection_add.svg) **Add**—adds areas to the current selection. If there is no selection in place, a new selection will be created.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/LDnymHjCEVcIWYP4DbyRp/f69fff408e1cdb1f5584937fe47f1f9c/selection_subtract.svg) **Subtract**—removes areas from the current selection.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/2yE4QenPYn8WX54j531qbC/b1315e9c7159f9150b1ef0b0a346fabb/selection_intersect.svg) **Intersect**—a new selection area is created from the overlap between the newly added selection area and the current selection.

When you switch to one of the tools listed above, its mode may vary according to the following rules:

*   If pixels are selected the tool remembers its last-used mode.
*   If pixels are not selected, the tool defaults to **New** or **Add** mode.

When defaulting to **New**/**Add** mode, the**Selection Brush Tool** and the **Object Selection Tool** default to the former while other selection tools default to the latter.

1.   In the Pixel Studio ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Object Selection Tool**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/C3NB8httu4Ctqf1QkQHGD/1e133e366f542b290d41d8557e790e0a/object_selection_tool.svg) .
2.   Adjust the settings on the context toolbar.
3.   Hover over the object you wish to select.

When using the tool, the following shortcuts can be used:

*    Pressing **⌥** (Mac) / **Alt** (Windows) while clicking to confirm selections separates them into object components, which inevitably may consist of varied textures. For example, it is possible to separate a model's face from the eyes. 
*    Pressing **⌥****⇧** key (Mac) / **Alt**+**Shift** key (Windows), in addition to the above, further separates object components. For example, it is possible to separate parts of an outfit consisting of varied colors or textures. 
*   Dragging on an object enables you to establish smaller selection areas, as indicated by the hatched pattern during the operation.

Use the **Object Selection Tool** for making selections of either the main subject of the composition or its individual parts while employing the above shortcuts.

On the tool's context toolbar, toggle the **Multi-part Objects** option on to enable selections of similar textures, particularly when separated by other objects.

Do one of the following:

*   On the **Pixel** menu, choose **Pixel Selection > From Layer Subject**.
*   In the **Canva AI Studio**, choose **Select Subject**![Image 8: Select Subject](https://images.ctfassets.net/3p2fxa94bzao/4mEgTsFkovEXcgIgAKpu7H/26d062e431316d09455cb2b11ba6feec/select_subject.svg) .

1.   In the Pixel Studio ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Selection Brush Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/2RPHHEjmTXhZrgZfZUSPO8/644f0916603d39b4ce0658e0f0125fa5/selection_brush_tool.svg) .
2.   Adjust the settings on the context toolbar.
3.   Drag on your page.

When using the Selection Brush Tool, the following modifier keys can be used to aid in the creation of selections:

*    The **⌘** key (Mac) / **Ctrl** key (Windows) temporarily toggles **Snap to edges**![Image 11: Snap to edges](https://images.ctfassets.net/3p2fxa94bzao/2Aeq2yyZaTJcJpC38qzshX/fbdc35231d25572a0fa1693970cc4a45/snap_to_edges.svg)  setting on and off. 
*    For Mac: With the selection mode set to Subtract, the **⌃(ctrl)** key automatically adds areas to the current selection. 
*    The **⌥** key (Mac) / **Alt** key (Windows) automatically removes areas from the current selection. 

1.   In the Pixel Studio ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Rectangular**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/1ooe7qXQrJMsHaSPO5hW6P/bb95ad59fe27d96a11e337e59fec3c92/rectangular_marquee_tool.svg)  ,**Elliptical**![Image 14](https://images.ctfassets.net/3p2fxa94bzao/7n4FzMUYzRDRFBUTZF7mhF/9afc976f5178728f63e40e6d1938e43d/elliptical_marquee_tool.svg) , **Row**![Image 15](https://images.ctfassets.net/3p2fxa94bzao/2smIm7kcATxHnWy39C1swR/de9e37eab9972323b417df7debb1b814/row_marquee_tool.svg)  or **Column Marquee Tool**![Image 16](https://images.ctfassets.net/3p2fxa94bzao/3riOFunV682pqAktNFFq2R/93f87d4db6cc10647a6f4f78f9d90074/column_marquee_tool.svg) .
2.   Adjust the settings on the context toolbar.
3.   Drag on your page.

When using the Marquee Selection tools, the following modifier keys can be used to aid in the creation of selections:

*    Pressing the **⌘** key (Mac) / **Ctrl** key (Windows) while dragging constrains the marquee's proportions. 
*    Pressing the **⇧** key (Mac) / **Shift** key (Windows) while dragging adds to the current selection. 
*    Pressing the **⌥** key (Mac) / **Alt** key (Windows) while dragging removes areas from the current selection. 
*    Pressing the **⌘** key (Mac) / **Ctrl** key (Windows) while dragging inside the current marquee selection repositions it. 

1.   In the Pixel Studio ![Image 17](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Freehand Selection Tool**![Image 18](https://images.ctfassets.net/3p2fxa94bzao/5KiRiFTL8vPE9FR1Gf8IxU/63189dd8150a70456d6db61885fdcd6e/free_hand_selection_tool.svg) .
2.   On the context toolbar, choose a selection **Type**.
3.    Do one of the following: 
    *   With **Freehand** selected, drag on the page to draw the edge of the selection and release to close the selection.
    *   With **Polygon** selected, click to define the beginning of the selection and then click for every change in direction.
    *   With **Magnetic** selected, click to define the beginning of the selection and then click to place a custom node position. Automatic nodes will be placed along distinct image edges as the cursor moves.

4.   Double-click to close the selection (**Polygon** and **Magnetic** only).

When using the Freehand Selection Tool, the following modifier keys can be used to aid in the creation of selections:

*   The **⇧** key (Mac) / **Shift** key adds to pixel selection.
*   If using **Polygonal** and **Magnetic**, dragging will temporarily invoke **Freehand**.
*   Holding the **⌥** key (Mac) / **Alt** key (Windows) temporarily switches the mode to Subtract.
*   When using **Freehand** mode, holding the **⌘** key (Mac) / **Ctrl** key (Windows) temporarily allows you to add straight edges.
*   Pressing the **⌘** key (Mac) / **Ctrl** key (Windows) while dragging from inside the selected area, allows you to move layer with the selection.

*   In the Pixel Studio ![Image 19](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , from the **Pixel** menu, select **Pixel Selection > Select All**.

Do one of the following:

*   In the Pixel Studio ![Image 20](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , on the **Layers** panel, click the chosen layer's thumbnail while pressing the **⌘** key (Mac) / **Ctrl** key (Windows).
*   On the **Pixel** menu, select **Pixel Selection > From Layer.**

*   In the Pixel Studio ![Image 21](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , with a selection in place, from the **Pixel** menu, select **Pixel Selection > Invert**.

*   [Selection Brush Tool](https://www.affinity.studio/help/tools-tools-selection-brush/)
*   [Object Selection Tool (ML)](https://www.affinity.studio/help/tools-tools-object-selection/)
*   [Flood Select Tool](https://www.affinity.studio/help/tools-tools-flood-select/)
*   [Pixel selection from layers](https://www.affinity.studio/help/selections-pixel-selections-fromlayers/)
*   [Range pixel selections](https://www.affinity.studio/help/selections-selections-range/)
*   [Sampled color pixel selections](https://www.affinity.studio/help/selections-selections-sampled/)
*   [Modifying pixel selections](https://www.affinity.studio/help/selections-selections-modify/)
*   [Select Subject (Canva AI)](https://www.affinity.studio/help/canva-ai-canva-ai-select-subject/)
*   [Canva AI and Affinity (ML)](https://www.affinity.studio/help/canva-ai-canva-ai-affinity-ml/)
*   [Keyboard shortcuts for the Pixel Studio](https://www.affinity.studio/help/workspace-shortcuts-pixel-studio/)
*   [Settings](https://www.affinity.studio/help/workspace-settings/)

How would you rate the help you received from this article?
