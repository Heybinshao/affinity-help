---
title: "Merging to 32-bit HDR - Affinity Help Center"
source: https://www.affinity.studio/help/hdr-hdr-merging/
slug: hdr-hdr-merging
fetched: 2026-08-06
---

# Merging to 32-bit HDR - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/hdr-hdr-merging/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
4.   Merging to 32-bit HDR

You can merge multiple exposures of the same scene to create a 32-bit HDR image with an extended tonal range. This allows you to retain detail in both shadows and highlights, providing greater flexibility for tonal adjustments and creative editing.

A 32-bit HDR image stores a wider range of tonal information than standard image formats, often exceeding what most displays can show directly. This additional range allows for more precise control when editing exposure and contrast. To produce a display-ready result, the image can be tone-mapped, compressing the tonal range while preserving detail across the scene.

When merging your files, Affinity lets you choose the **Default tone curve** for the process. The options can be found in **Settings > Assistant > Develop Assistant**. RGB 32-bit color format images output with the setting active, resulting in unbounded merges.

1.   On the **File** menu, select **New Image Process > HDR Merge**.
2.   From the dialog, click **Add** to locate and select your images.
3.   (Optional) Choose a Perspective or Scaling operation from the menu to allow for successful auto-alignment. The former applies a perspective adjustment to each image; the latter repositions and/or sizes the image layer.
4.   (Optional) If your image set contains moving subjects between each exposure, check **Automatically Remove Ghosts**.
5.   (Optional) Keep **Noise reduction** checked to enable color and luminance noise reduction; Uncheck to disable noise reduction (you can address this post HDR merge using the Denoise filter).
6.   Click **OK** to begin merging the images.

The HDR merging is previewed in stages: first, the image alignment, then the HDR merge itself. By default, the merged result will then be taken into the **Tone Mapping Studio** for tone mapping. See Tone Mapping HDR images topic for more information.

You can stop Affinity from automatically entering the Tone Mapping Studio and tone mapping your 32-bit image. On the **New HDR Merge** dialog, uncheck **Tone map HDR image**. Once the HDR merge is complete, you will then remain in the Pixel Studio to make further edits.

If you choose not to automatically tone map your image, the **Sources** panel will be displayed, allowing you to manually retouch the merged result. If **Automatically Remove Ghosts** was checked, the **Sources** panel will contain a de-ghosted source as well as the original merged source. See Sources panel topic for more information.

Below you will see a 32-bit image being displayed as 8-bit with no tone mapping or further tonal adjustments applied. 32-bit simply contains too much tonal range to display, so we typically apply a procedure called _Tone Mapping_ to map that tonal information to a range that can be displayed accurately. See Tone Mapping HDR images topic for more information.

![Image 1: Tone Mapped 32-bit](https://images.ctfassets.net/3p2fxa94bzao/4pEsNB6znMPw369rJu65EQ/4848f7345981ca62482592d64e55babf/feature_hdr_tonemappedrange.jpg)

Before: A 32-bit image with no tone mapping—the range of 32-bit is too great to display. Instead we see an image with extreme contrast. After: A 32-bit image after being tone-mapped. The vast range of tonal information has been "mapped" to a range that can be reproduced by most displays.

![Image 2: Full 32-bit range](https://images.ctfassets.net/3p2fxa94bzao/43f2KxXIUftxeW8WPb4idC/f512deb1477366fdccdb1057fea02518/feature_hdr_fullrange.jpg)

Before: A 32-bit image with no tone mapping—the range of 32-bit is too great to display. Instead we see an image with extreme contrast. After: A 32-bit image after being tone-mapped. The vast range of tonal information has been "mapped" to a range that can be reproduced by most displays.

Once work on a 32-bit image is completed, you may need to convert its color format and, crucially, its color profile if you intend to distribute or share it. For example, you might want to export as an 8-bit JPEG with an sRGB color profile. Alternatively, if you are maintaining a lossless workflow, you can stay in 32-bit and export to a linear unbounded format.

1.   On the **Document** menu, select **Setup > Convert Format / ICC Profile**.
2.   On the dialog that appears, set **Color Format** as needed.
3.   (Optional) A color profile will be automatically assigned—for RGB/8 and RGB/16, this will be **sRGB IEC61966-2.1**. Choose a different one if needed.

1.   On the **File** menu, select **Export**.
2.   Choose the **OpenEXR** format and click **Export**, then specify where to save your document.

*   [Tone Mapping HDR images](https://www.affinity.studio/help/hdr-hdr-tonemapping/)
*   [32-bit HDR editing](https://www.affinity.studio/help/hdr-hdr-editing/)
*   [Sources panel](https://www.affinity.studio/help/panels-sources-panel/)
*   [Settings](https://www.affinity.studio/help/workspace-settings/)

How would you rate the help you received from this article?
