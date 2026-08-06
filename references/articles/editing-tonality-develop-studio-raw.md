---
title: "Editing tonality in Develop Studio (RAW) - Affinity Help Center"
source: https://www.affinity.studio/help/editing-tonality-develop-studio-raw/
slug: editing-tonality-develop-studio-raw
fetched: 2026-08-06
---

# Editing tonality in Develop Studio (RAW) - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/editing-tonality-develop-studio-raw/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Editing tonality in Develop Studio (RAW)

When working with RAW images, tonal adjustments are first made in Develop Studio. This stage establishes overall exposure, dynamic range, and contrast before moving to further refinement in the main editing workspace.

![Image 1: After applying local adjustments to lift the clipped tones.](https://images.ctfassets.net/3p2fxa94bzao/3Fv7nMpDzkA9Hh6QRr1C3n/f73f90d8a896b7c30ba5c8b6df38a200/tonalityLocalRaw_after.jpg)

After applying local adjustments to lift the clipped tones.

Editing tonality at the RAW stage preserves more image data and allows for greater flexibility when recovering highlights, lifting shadows, or correcting exposure. RAW files contain a wider tonal range than standard image formats. Adjusting tone before developing the image allows you to:

*   recover highlight detail that may appear clipped.
*   lift shadow areas with reduced noise.
*   adjust overall exposure with minimal quality loss.
*   establish balanced contrast before applying creative edits.

*   For best results, complete global tonal corrections before moving on to local adjustments.
*   To evaluate problem areas at the start, on the context toolbar, try enabling **Show Clipped Tones**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/6EEyFmuUJU0GHlsO4oAGL3/e98b9226e7895b02cc6b23b4e55060b3/show_clipped_tones.svg) .

*   **Exposure**—adjusts overall brightness across the image. Use this to correct underexposed or overexposed captures before refining contrast.
*   **Blackpoint**—defines the darkest tonal value in the image. Increasing Blackpoint deepens shadows and improves contrast; reducing it lifts shadow detail.
*   **Brightness**—fine-tunes midtone intensity without dramatically altering highlight or shadow structure.
*   **Contrast**—expands or compresses tonal separation between shadows and highlights.
*   **Highlights**—recovers detail in bright areas that may appear clipped.
*   **Shadows**—restores detail in darker regions while maintaining natural transitions.

Clipped tones occur when detail is lost in the darkest or brightest areas of an image. In highlights, clipping results in areas that appear pure white with no visible texture. In shadows, clipping produces areas that appear completely black. Although midtone clipping is less common, excessive contrast can reduce detail and flatten tonal transitions.

Before making corrections, review the image carefully and monitor the **Histogram** to identify whether tonal information is compressed at either end of the range.

When clipped areas are localized rather than global, you can target them using the **Masks** panel. You can use either the **Mask Gradient Tool**

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/tzzGrTQ7p5FvQcfAmtArv/6be070c9a1a9961164de6d472af375e1/gradient_overlay_tool.svg)

 or the **Mask Paint Tool**

![Image 4](https://images.ctfassets.net/3p2fxa94bzao/3locI94qeasHTEGWfhYhbg/c851457b3a254b6f26745e88f61f2107/overlay_brush_tool.svg)

 individually or combine both for greater control. The goal is to define the regions where tonal recovery is required.

*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/tzzGrTQ7p5FvQcfAmtArv/6be070c9a1a9961164de6d472af375e1/gradient_overlay_tool.svg) **Mask Gradient Tool**—creates a smooth transition between corrected and uncorrected regions. This is useful when clipping affects large areas such as skies or foreground shadows.
*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3locI94qeasHTEGWfhYhbg/c851457b3a254b6f26745e88f61f2107/overlay_brush_tool.svg) **Mask Paint Tool**—allows precise manual selection of clipped areas. This is helpful for targeting smaller regions or complex shapes.

To learn more about these tools, visit the dedicated [Using masks (Develop Studio)](https://www.affinity.studio/help/raw-using-masks-develop-studio/) topic.

**Clarity** influences tonal perception and separation. It enhances midtone contrast, improving perceived depth and structure. It should be used subtly to avoid introducing unnatural contrast or haloing.

On the top bar, do one of the following:

*   Click **Show Clipped Highlights**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/6yVmnnwjh0HjAeRiqo5Jh1/947997e1084e5316c0ae86468dbc84f9/show_clipped_highlights.svg) to display all 'blown' highlights as a high-contrast red color.
*   Click **Show Clipped Shadows**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/hz1W7gRPMocIkJ7TGTlVY/7f1c40c1fe31feda5c0d0d0591761028/show_clipped_shadows.svg) to display all clipped shadow areas as a high-contrast blue color.
*   Click **Show Clipped Tones**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/6EEyFmuUJU0GHlsO4oAGL3/e98b9226e7895b02cc6b23b4e55060b3/show_clipped_tones.svg) to display all clipped midtone areas as a high-contrast yellow color.

In Develop Studio, on the **Basic** panel:

1.   Do one of the following, as required:
    *   Correct overall exposure.
    *   Adjust Blackpoint to establish depth.
    *   Refine contrast.
    *   Recover highlights and lift shadows.
    *   Apply subtle clarity adjustments.

2.   Click **Develop**to develop the image.

*   Avoid pushing highlight or shadow recovery to extremes.
*   Monitor tonal distribution using the **Histogram**.
*   Aim for balanced dynamic range before applying creative grading.
*   Preserve flexibility by keeping adjustments moderate at this stage.

1.   On the **Masks**panel, or from the toolbar, select either the **Mask Gradient Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/tzzGrTQ7p5FvQcfAmtArv/6be070c9a1a9961164de6d472af375e1/gradient_overlay_tool.svg) or **Mask Paint Tool**![Image 11](https://images.ctfassets.net/3p2fxa94bzao/3locI94qeasHTEGWfhYhbg/c851457b3a254b6f26745e88f61f2107/overlay_brush_tool.svg) .
2.   Mark areas of interest — a red overlay indicates the areas selected.
3.   (Optional) Select the **Mask Erase Tool**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/7FntY0YnpexlxtRDjssV90/cba51f14d527051511fc8084b602267a/overlay_eraser_tool.svg) and erase any areas painted outside the target region.
4.   On the **Basic**panel, adjust **Exposure**, **Blackpoint**, **Shadows**, **Highlights**, as required, to correct clipped tones.
5.   Click **Develop**to develop the image.

*   Avoid extreme corrections that may introduce noise or reduce natural contrast.
*   Use gradual adjustments and compare before and after results.
*   Combine masking with moderate global corrections for balanced tonal recovery.

*   [Developing RAW images](https://www.affinity.studio/help/raw-raw/)
*   [Using masks (Develop Studio)](https://www.affinity.studio/help/raw-using-masks-develop-studio/)
*   [Understanding tonality](https://www.affinity.studio/help/understanding-tonality/)
*   [Recovering and preserving highlights](https://www.affinity.studio/help/recovering-preserving-highlights/)
*   [Brush-based tonal adjustments](https://www.affinity.studio/help/brush-based-tonal-adjustments/)
*   [Tonal adjustments in compositing](https://www.affinity.studio/help/tonal-adjustments-compositing/)

How would you rate the help you received from this article?
