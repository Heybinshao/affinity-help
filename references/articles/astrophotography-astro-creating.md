---
title: "Creating an astrophotography stack - Affinity Help Center"
source: https://www.affinity.studio/help/astrophotography-astro-creating/
slug: astrophotography-astro-creating
fetched: 2026-08-06
---

# Creating an astrophotography stack - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/astrophotography-astro-creating/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
4.   Creating an astrophotography stack

The Astrophotography Stack Studio's key controls are located in the right panel group, where you can specify the files to be stacked and how they are processed.

This feature is only available in Affinity for desktop.

The Studio provides the [**Bad Pixel Map Tool**](https://www.affinity.studio/help/tools-tools-bad-pixel-map/), which helps to identify and correct defective pixels that originate in a camera setup.

*   [**Files**](https://www.affinity.studio/help/panels-astro-panel-files/)—specify the light frames and calibration frames to be processed. 
*   [**Stacking Options**](https://www.affinity.studio/help/panels-astro-panel-stacking-options/)—choose and control the stacking method used to process the frames. 
*   [**RAW Options**](https://www.affinity.studio/help/panels-astro-panel-raw-options/)—choose how the frames are interpreted. 
*   **Stacked Images**—all images created during a single session in the Studio are added here.

At minimum, a set of light frames must be added to the **Files** panel. It is recommended that you add [calibration frames](https://www.affinity.studio/help/astrophotography-astro-about/) as well.

Each set of light frames and calibration frames constitutes a file group. Multiple file groups can be added to the panel for processing into a single end result.

Each file group should contain frames taken at different times, i.e. across several nights, during which shooting conditions may have changed.

Use the **Stacked Images** panel to compare results from using different files and options.

To rename a stacked image, double-click it on the panel.

Each stacked image becomes a pixel layer (of the same name) in the resulting document.

You can assign channel colour mapping to each stacked layer from the **Stacked Images** panel. When the stack is applied, the selected channel mapping is preserved non-destructively, allowing you to continue refining the result afterwards. You can also generate a full-colour preview layer from the panel to check how the mapped channels combine before continuing with further edits.

*   ![Image 1](https://images.ctfassets.net/3p2fxa94bzao/16xclkZTOokIeWj5LpEvxi/915d082ebd3ac857b57212d382357078/view_tool.svg) **Hand Tool**— move around the document by dragging on it.
*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/6jmWPErECQEdSLoFK86wRd/4df92fffdb8d65af90c0a607ed39cdb2/zoom_tool.svg) **Zoom Tool**— zoom in and out of the document.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/1h7jiPUfGZiR8vLhdYmJdR/75ae8719b5cd1c4c33776fa9eab8995d/raster_crop_tool.svg) **Crop Tool**—crop the document to remove unwanted areas.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/1aXC8e9Dk1sdPffFEXzmHG/ab83323e45c5e38b25a9925db5f52e82/astro_bad_pixel_tool.svg) **Bad Pixel Map Tool**—automatically or manually identify defective pixels in specific kinds of calibration frame.

**Tone Stretch** can now be disabled in workflows where automatic tonal expansion is not required. When opening an individual FIT file that already contains color data, no tone stretch is applied by default. In the Astrophotography Stack studio, tone stretching can also be turned off from the **Preview** panel, allowing you to preview stacked data without an automatic stretch and apply your own stretching method later, if preferred.

*   Select **File > New Image Process > Astrophotography Stack**.

1.   On the **Files** panel, set **Type** to Light frames, then select **Add Files**.
2.   Browse to your light frames, select them, then select **Open**.
3.    (Optional but recommended) For each set of calibration frames that you have shot: 
    1.   Set **Type** as appropriate.
    2.   Select **Add Files**.
    3.   Browse to the corresponding frames, select them, then select **Open**.

4.   (Optional) For each collection of light and calibration frames taken at a different time, select **Add a file group** and repeat steps 1 through to 3 as appropriate.

1.   (Optional) Adjust the Studio's [stacking options](https://www.affinity.studio/help/panels-astro-panel-stacking-options/).
2.   (Optional) Adjust the Studio's [RAW options](https://www.affinity.studio/help/panels-astro-panel-raw-options/).
3.   On the context toolbar, select **Stack**.

When the stacking process is complete, its end result is added to the **Stacked Images** panel.

The frames you added remain in the **Files** panel, enabling you to add additional frames or file groups and adjust settings to create additional stacked images, i.e. to try for improved results.

1.   On the **Stacked Images** panel, with the files assembled, click **Create Color Mapped Image** .
2.   Select the stacked image.
3.   Assign a color channel mapping using the drop-down button.

1.   On the context toolbar, select **Apply**. The workspace switches to the Pixel Studio.
2.   Select **File > Save**.
3.   Browse to where you want to save your document.
4.   Name your document and select **Save**.

Upon leaving the Astrophotography Stack Studio, each image in the **Stacked Images** panel is added as a new pixel layer near the bottom of the document's layer stack.

Curves and Levels adjustments, with settings calculated during the stacking process, are added at the top of the layer stack. Perform any post-processing you wish, including editing these adjustments.

*   [About astrophotography stacking](https://www.affinity.studio/help/astrophotography-astro-about/)
*   [Files panel](https://www.affinity.studio/help/panels-astro-panel-files/)
*   [Stacking Options panel](https://www.affinity.studio/help/panels-astro-panel-stacking-options/)
*   [RAW Options panel](https://www.affinity.studio/help/panels-astro-panel-raw-options/)
*   [Bad Pixel Map Tool](https://www.affinity.studio/help/tools-tools-bad-pixel-map/)
*   [Compositing narrowband images](https://www.affinity.studio/help/astrophotography-astro-narrowband/)
*   [Tone Stretch adjustment](https://www.affinity.studio/help/adjustments-adjustment-tone-stretch/)

How would you rate the help you received from this article?
