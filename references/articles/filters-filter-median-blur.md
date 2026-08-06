---
title: "Median Blur filter - Affinity Help Center"
source: https://www.affinity.studio/help/filters-filter-median-blur/
slug: filters-filter-median-blur
fetched: 2026-08-06
---

# Median Blur filter - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-filter-median-blur/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Median Blur filter

The Median Blur

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/2J4POfCnK5LWE827R8IRmX/debcf574bf588cd707b94638115c0cad/median_blur_tool.svg)

 filter broadens color regions in the image. At low settings it’s useful for removing noise, especially as it retains edges better than Gaussian Blur. At much higher intensities it introduces flat areas of color and smoothes textures.

![Image 2: After](https://images.ctfassets.net/3p2fxa94bzao/54DdCpbGEhQ64iLw7QAM3S/97fc15c3a86c2b7a4403d7347b989d16/filter_medianblur_after.jpg)

![Image 3: Before](https://images.ctfassets.net/3p2fxa94bzao/UhY4sEOxm4A9kbMgMglaT/93cde7725031301e29b8fd2f81cab2c7/filter_medianblur_before.jpg)

Instead of averaging nearby pixels (as Gaussian or Box blur does), Median Blur filter examines a defined neighbourhood around each pixel, sorts the surrounding pixel values and replaces the original pixel with the middle (median) value. Because extreme balies (such as noise or speckles) are ignored, this approach removes unwanted detail while keeping edges relatively sharp.

This filter can be applied as a destructive or non-destructive live filter.

This filter, including its live filter equivalent, is not available for 32-bit RGB documents.

*   **Photo Restoration**—Use Median Blur to clean scanned photos, removing dust and imperfections before retouching.
*   **Pre-Masking Cleanup**—Apply it lightly before creating selections or masks to simplify complex textures.
*   **Stylized Smoothing**—At higher settings, Median Blur can create flat, poster-like surfaces while keeping outlines visible.
*   **Reducing Pattern Noise**—Useful for smoothing repetitive textures or digital artifacts without destroying texture.
*   **Edge-Friendly Background Softening**—Blur noisy backgrounds while preserving subject edges more effectively than with standard blur filters.

To use the destructive version of the filter, select it from the **Pixel > Filters > Blur** menu. The live version can be accessed from:

*   the **Layers** panel by clicking **Live Filters**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/2ALwfgZXKqtubPaMdMHvlC/d4901c280214d88174d57188a9c56e21/filters_studio.svg) .
*   the **Pixel > New Live Filter Layer > Blur** menu.

Median Blur is also available as a tool in the Compositing Studio

![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3HLsf5xx2FlnBTmx7VwAkX/eb93eb77aa0dc236a5edfe2d6e7ef9f7/compositing_studio.svg)

.

The following settings can be adjusted in the filter dialog:

*   **Radius**—controls intensity of the filter. At high levels it creates large, flat areas of color. Type directly in the text box or drag the slider to set the value. Dragging to the right on the page allows you to override the maximum value—values above 100 px may affect performance so use with care.

*   [Using live filters](https://www.affinity.studio/help/layers-livefilters/)
*   [Applying filters](https://www.affinity.studio/help/filters-filters-applying/)
*   [Gaussian Blur filter](https://www.affinity.studio/help/filters-filter-gaussian-blur/)
*   [Bilateral Blur filter](https://www.affinity.studio/help/filters-filter-bilateral-blur/)
*   [Compositing Studio](https://www.affinity.studio/help/workspace-compositing-studio/)

How would you rate the help you received from this article?
