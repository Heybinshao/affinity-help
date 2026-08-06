---
title: "Understanding tonality - Affinity Help Center"
source: https://www.affinity.studio/help/understanding-tonality/
slug: understanding-tonality
fetched: 2026-08-06
---

# Understanding tonality - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/understanding-tonality/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Understanding tonality

Editing tones (tonality) involves adjusting the distribution, balance, and relationships between shadows, midtones, and highlights. Strong tonal structure gives an image depth and clarity, while weak tonal separation can make it appear flat or lacking detail.

![Image 1: After lifting shadows, midtones, and highlights in the scene, and recoloring using RGB curves.](https://images.ctfassets.net/3p2fxa94bzao/1XENGbV3D5nU6df5ZuX52C/df67b54511c270f692f5ebd73222d76f/tonality_after.jpg)

After lifting shadows, midtones, and highlights in the scene, and recoloring using RGB curves.

Tonality refers to how light and dark the tonal values are arranged across an image. It determines perceived contrast, depth, and visual emphasis. Even before color is considered, tonal balance shapes how an image _feels_ — whether soft and muted, high-contrast and dramatic, or evenly balanced. Images with good tonal separation retain detail in both shadows and highlights while maintaining smooth transitions through the midtones.

![Image 2: Examples of images with different tonality: A. Soft & muted; B. High-contrast & dramatic; C. Evenly lit scene.](https://images.ctfassets.net/3p2fxa94bzao/7GbVBsP9UDtJS5vOf2F5v5/55d842f2c64b1c194ae38990886dcb24/tonal_examples.jpg)

Examples of images with different tonality: A. Soft & muted; B. High-contrast & dramatic; C. Evenly lit scene.

Tonal editing controls how shadows, midtones, and highlights are distributed across an image. In Affinity, tonal adjustments can be made globally using adjustment layers, or refined locally using masks, Blend Options, Dodge & Burn, and Tone Brush tools.

Tonal adjustments can affect color perception. Establish tonal balance first, then refine color for more controlled grading.

Images with balanced dynamic range retain detail in both shadows and highlights. Increasing contrast expands the separation between tones, while reducing contrast compresses them. Understanding this balance helps you decide whether to recover detail or emphasize drama.

![Image 3: An example of a Histogram: A. Shadows, B. Midtones, C. Highlights information. ](https://images.ctfassets.net/3p2fxa94bzao/1m3pEC4TdzBlLPdq8KzCVE/1f1306e4e8c04ff9133100e5de5e0cf9/histogram.jpg)

An example of a Histogram: A. Shadows, B. Midtones, C. Highlights information.

A **Histogram** can help you evaluate tonal distribution. If most of the data is concentrated in the midtones, the image may appear flat. If tones are clipped at either end, detail may be lost in shadows or highlights.

Common tonal problems and solutions:

*   Flat image — increase midtone contrast with Curves.
*   Washed-out highlights — reduce Highlights or adjust Blackpoint (Develop Studio).
*   Crushed shadows — lift shadows or reduce contrast.
*   Low depth in composites — use Dodge & Burn or Tone Brush Tool to restore separation.

Think of global adjustments as setting the tonal foundation for the entire image — like adjusting the overall lighting in a room before focusing on individual objects. When you apply a global adjustment, every part of the image shifts together: shadows lift, highlights pull back, or contrast changes across the whole frame. This makes global tools such as Curves and Levels ideal for correcting overall exposure or establishing the image's tonal mood early in your workflow.

Local adjustments work differently — rather than affecting everything equally, they let you target specific areas while leaving the rest untouched. You can brighten a subject's face without affecting the background, deepen a shadow in one corner without flattening the rest of the image, or recover detail in a clipped sky without disrupting the foreground. For someone new to tonal editing, a useful way to think about it is: global adjustments correct the image, local adjustments shape it.

Tonal editing typically follows two stages:

*   Global adjustments establish overall exposure and contrast.
*   Local adjustments refine specific areas to guide attention, restore detail, or enhance depth.

Starting with global tonal balance and then refining locally produces more controlled and predictable results.

![Image 4: After applying global adjustments to brighten up the scene and add contrast.](https://images.ctfassets.net/3p2fxa94bzao/5hdJDQtYJLgeWGu3MX6Hj1/f1593197e47a2c332d290ac4c1263717/global_tonal_adjustments_after.jpg)

After applying global adjustments to brighten up the scene and add contrast.

For precise local tonal control, Affinity offers a number of adjustments, brushes, filters, and other features to complete the task. These drive and often simplify complex layer and mask-based workflows.

![Image 5: After applying local adjustments to brighten up the main subject.](https://images.ctfassets.net/3p2fxa94bzao/WdZzTM6amSGqn8gF0Oci7/ca8b64a56f133f7bb8c2e40b9f6d55bc/local_tonal_after.jpg)

After applying local adjustments to brighten up the main subject.

*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3sUtJeUQMZ6GrVHc9V5TPv/19fd2cb45e125061fc1c3a451f05d31c/curves_adjustment_type.svg) **Curves**—control contrast and tonal range precisely.
*   ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/2BlFCLiDYRlPu3d67dykNp/ddaeec3ef156c516b7660ced6ad4426b/levels_adjustment_type.svg) **Levels**—quickly set black and white points and refine midtones.
*   ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/3s8XDsbkEYrU8HbclM9knU/2ef272566ec4e3f75bd5d9698253dbf4/shadows_highlight_live_filter.svg) **Shadows/Highlights**—recover detail in dark or bright areas without reshaping the full tonal curve.
*   ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/585EbECVUPqAnHHd8YJVzO/22f568c05dbc5f7269562ece0343b792/brightness_contrast_adjustment_type.svg) **Brightness/Contrast**—fast global changes, best used subtly.
*   ![Image 10](https://images.ctfassets.net/3p2fxa94bzao/7GOVxSX9cIrGUggVNknZn/6a5d4570ad927da6f562e5cb1d87e97f/hsl_adjustment_type.svg) **HSL**—use the Lightness channel to adjust the tonal weight of specific colors.
*   ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/3PgOWd2qBooTcJXPAKxsk1/9209748380a579021b8067e31d47a007/black_and_white_adjustment_type.svg) **Black & White**—sculpt tonal relationships by adjusting color channels.

*   **Dodge & Burn**—lighten and darken specific areas to shape depth and guide attention.
*   **Blend Options**—limit an adjustment to shadows, midtones, or highlights without complex masking.
*   ![Image 12: Tone Brush Tool](https://images.ctfassets.net/3p2fxa94bzao/5QTKKA3wxWlh9RBxHiJzvd/3fc00e66cc0e8b9c3058725bd5c8d774/toneBrushl_tool.svg) **Tone Brush Tool**—blend tones by sampling content of underlying layers.
*   ![Image 13: Live Tone Blend Group](https://images.ctfassets.net/3p2fxa94bzao/4QwnwbtLzNdMFmosyTP9zQ/eba11ef9ff6694eff2139b714bc5cdd7/live_tone_blend_group.svg) **Live Tone Blend Group**—blend groups containing objects and layers seamlessly with the content of underlying layers.

The **Tone Brush Tool** and the **Live Tone Blend Group** are especially useful for compositing and tone-matching workflows where realistic light and precise blending is key.

1.   Evaluate tonal distribution using the image preview and the **Histogram**panel.
2.   Establish overall tonal range by setting black and white points using **Levels**![Image 14](https://images.ctfassets.net/3p2fxa94bzao/2BlFCLiDYRlPu3d67dykNp/ddaeec3ef156c516b7660ced6ad4426b/levels_adjustment_type.svg) or refining contrast with **Curves**![Image 15](https://images.ctfassets.net/3p2fxa94bzao/3sUtJeUQMZ6GrVHc9V5TPv/19fd2cb45e125061fc1c3a451f05d31c/curves_adjustment_type.svg) .
3.   Adjust overall exposure and contrast as needed using **Shadows/Highlights**![Image 16](https://images.ctfassets.net/3p2fxa94bzao/3s8XDsbkEYrU8HbclM9knU/2ef272566ec4e3f75bd5d9698253dbf4/shadows_highlight_live_filter.svg) , **Exposure**![Image 17](https://images.ctfassets.net/3p2fxa94bzao/74nD4jSneuAdTnqBODoFsJ/b8241e9ccf512d7b8b7cbe69f18bc05f/exposure_adjustment_type.svg) , or **Brightness/Contrast**![Image 18](https://images.ctfassets.net/3p2fxa94bzao/585EbECVUPqAnHHd8YJVzO/22f568c05dbc5f7269562ece0343b792/brightness_contrast_adjustment_type.svg) .
4.   (Optional) Target specific tonal ranges using **Blend Options**or masked adjustment layers.
5.   (Optional) Refine selected areas using local tools such as **Dodge**![Image 19](https://images.ctfassets.net/3p2fxa94bzao/5QPGu2iGfXQE4VUebZa70M/a46fe1835355d4da1b2ea6239caff901/dodge_tool.svg) **& Burn**![Image 20](https://images.ctfassets.net/3p2fxa94bzao/2SEF1Vp1gpr8Gtt7tb9MSy/4c01a454f9118170d31fb2ceb4bd07c0/burn_brush_tool.svg) , the **Tone Brush Tool**![Image 21: Tone Brush Tool](https://images.ctfassets.net/3p2fxa94bzao/5QTKKA3wxWlh9RBxHiJzvd/3fc00e66cc0e8b9c3058725bd5c8d774/toneBrushl_tool.svg) , or other brush-based methods.
6.   (Optional) For compositing workflows, harmonize layers using the **Live Tone Blend Group**![Image 22: Live Tone Blend Group](https://images.ctfassets.net/3p2fxa94bzao/4QwnwbtLzNdMFmosyTP9zQ/eba11ef9ff6694eff2139b714bc5cdd7/live_tone_blend_group.svg) or group-level adjustments.

The adjustments in Affinity come equipped with a number of ready-to-use presets which can offer a great starting point to your edits.

*   [Global tonal adjustments](https://www.affinity.studio/help/global-tonal-adjustments/)
*   [Editing tonality in Develop Studio (RAW)](https://www.affinity.studio/help/editing-tonality-develop-studio-raw/)
*   [Preserving and recovering highlights](https://www.affinity.studio/help/recovering-preserving-highlights/)
*   [Tonal adjustments in compositing](https://www.affinity.studio/help/tonal-adjustments-compositing/)
*   [Brush-based tonal adjustments](https://www.affinity.studio/help/brush-based-tonal-adjustments/)
*   [Editing tonality using Blend Options](https://www.affinity.studio/help/edit-tonality-blend-options/)
*   [Tonal Filters](https://www.affinity.studio/help/filters-tonal-filters/)

How would you rate the help you received from this article?
