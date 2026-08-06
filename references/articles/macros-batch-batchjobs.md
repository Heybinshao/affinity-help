---
title: "Batch jobs - Affinity Help Center"
source: https://www.affinity.studio/help/macros-batch-batchjobs/
slug: macros-batch-batchjobs
fetched: 2026-08-06
---

# Batch jobs - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/macros-batch-batchjobs/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Batch jobs

Batch jobs allow a number of image files to be processed: specific processing instructions can be automated, boosting workflow efficiency.

The **Batch Job** feature allows you to specify an unrestricted number of source files to process and export. RAW files will be automatically developed, and both the exported file format and image dimensions are configurable.

When assembling your files, Affinity lets you choose the **Default tone curve**applied for the batch job process. The options can be found in **Settings > Assistant > Develop Assistant**.

Batch jobs can work in conjunction with [Macros](https://www.affinity.studio/help/macros-batch-macros/). Any number of pre-recorded macros can be applied to the source files, meaning you can very quickly apply operations to several files.

1.   On the **File** menu, select **New Image Process > Batch Job**.
2.   Below the **Sources** list, choose **Add** to bring up a file import dialog.
3.   Select your desired image files (including RAW files) to add to the **Sources** list and click **Add**.
4.   Set your Output options (see below for more information), then click **OK** to begin batch processing.

If you want to export multiple images to a specific pixel value along their long edge, enter the required value in both the **W** (Width) and **H** (Height) fields, then enable **A** (Lock Aspect Ratio). Affinity will automatically apply the value to the longest edge of each image, scaling the other dimension proportionally.

The following settings are available in the **Batch Job** panel:

*   **Parallel processing**—when checked, allows images to be processed asynchronously—one for each processor core or thread. For most modern machines with dual/quad-core processors, leaving this on is recommended for more efficient processing.
*   **Output**: 
    *   **Save into original location**—writes the new image files into the same directory as the originals. For Macs, you need to click **Authorize**, then navigate to your root Macintosh HD folder, then click **Authorize**. Once done, the **OK** button will be available to click. There's no need to navigate to the folder containing your images for batching.
    *   **Save into:**—allows you to specify a different directory to write the new image files into.

*   **Save as Affinity file**—writes an **.af** version of each source image.
*   **Save as JPEG**—writes a **JPEG** version of each source image.
*   **Save as PNG**—writes a **PNG** version of each source image.
*   **Save as TIFF**—writes a **TIFF** version of each source image.
*   **Save as OpenEXR** (For Mac)—writes a **32-bit OpenEXR** version of each source image.
*   **Save as EXR** (For Windows)—writes a **32-bit EXR** version of each source image.
*   **Save as WEBP**—writes a **WebP** version of each source image.
*   **Save as JPEG-XL** (For Mac)—writes a **JPEG-XL** version of each source image.
*   **Save as JPEGXL** (For Windows)—writes a **JPEGXL** version of each source image.
*   **Width**/**Height**—manually enter size dimensions for the source image.
*   **Aspect**—when checked, maintains the aspect ratio of the source image.
*   **Available Macros**—lists all macros in their respective categories for adding to the batch job. Click **Apply** to add the currently selected macro to the **Applied Macros** list.
*   **Applied Macros**—lists macros that will be applied to each source image in the batch job.

How would you rate the help you received from this article?
