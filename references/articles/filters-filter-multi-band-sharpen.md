---
title: "Multi Band Sharpen filter - Affinity Help Center"
source: https://www.affinity.studio/help/filters-filter-multi-band-sharpen/
slug: filters-filter-multi-band-sharpen
fetched: 2026-08-06
---

# Multi Band Sharpen filter - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-filter-multi-band-sharpen/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Multi Band Sharpen filter

The Multi Band Sharpen

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/7IrOc5Es7Em2TtEzNPG1xl/b2448ae54bfdd7bda374d4a9d5d6488e/multi_band_sharpen_live_filter.svg)

 filter performs accurate multi-pass detail enhancement. Each pass gradually increases detail enhancement and they're blended together to produce the final output.

![Image 2: After](https://images.ctfassets.net/3p2fxa94bzao/15iL6agN6TLLBtbYJmguie/fac061a9c4a04403205d30d00a9c5919/filter_multiband_after.jpg)

![Image 3: Before](https://images.ctfassets.net/3p2fxa94bzao/qGpjdg3sZpdhzbrXsUqUP/8096dd4852dc821a6f8fd70cdf3c7388/filter_multiband_before.jpg)

The method behind the **Multi Band Sharpen**

![Image 4](https://images.ctfassets.net/3p2fxa94bzao/7IrOc5Es7Em2TtEzNPG1xl/b2448ae54bfdd7bda374d4a9d5d6488e/multi_band_sharpen_live_filter.svg)

 filter delivers results that are much more pleasing to the eye, particularly when sharpening areas with fine edges, such as hairs, where a halo effect may be present when using other, more conventional sharpening techniques. The filter is particularly useful in portrait or astrophotography. In the former, it flattens facial features, especially small details such as skin pores, while in the latter it avoids over brightening the star details.

Since the filter uses multiple sub-pixel gaussian sampling passes, it can be more demanding on performance and so it is best to be applied as the last step of your editing, particularly if used as a live filter.

This filter can be applied as a destructive or non-destructive live filter.

Access the destructive version of the filter from the **Pixel > Filters > Sharpen** menu. The live version can be accessed from:

*   the **Layers** panel by clicking **Live Filters**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/2ALwfgZXKqtubPaMdMHvlC/d4901c280214d88174d57188a9c56e21/filters_studio.svg) .
*   the **Pixel > New Live Filter Layer > Sharpen** menu.

Multi Band Sharpen is also available as a tool in the Compositing Studio

![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3HLsf5xx2FlnBTmx7VwAkX/eb93eb77aa0dc236a5edfe2d6e7ef9f7/compositing_studio.svg)

.

The following methods can be selected:

*   **Standard**—uses the default multi-band sharpening approach to enhance detail across multiple frequency ranges. It produces balanced results by increasing clarity while minimising haloing, making it suitable for general-purpose sharpening across a wide range of images.
*   **Fine Detail**—uses an alternative detail enhancement method designed to emphasise very fine structures. It is particularly effective for imagery with subtle or undersampled detail—such as solar or lunar photography—but can also be used to enhance fine textures in other types of images.

The following settings can be adjusted:

*   **Base Radius**—from 0 to 2, determines the radius of the first pass, or “band”. Each subsequent pass will increase this value.
*   **Number of Bands**—determines the number of passes (bands). Larger numbers will introduce local contrast enhancement in addition to fine detail enhancement.
*   **Band Range**—controls the “gap” between each band value. Smaller deltas will use narrower gaps for finer detail enhancement while larger deltas will use larger gaps for broader detail enhancement.
*   **Contrast**—controls the contrast of each pass providing a slight boost to the overall sharpening effect.
*   **Hard Blend**—an option to blend the passes more aggressively, further increasing the sharpening effect.

*    Drag on the page to set radius. 

*   [Using live filters](https://www.affinity.studio/help/layers-livefilters/)
*   [Applying filters](https://www.affinity.studio/help/filters-filters-applying/)
*   [Sharpen filters](https://www.affinity.studio/help/filters-sharpen-filters/)
*   [Compositing Studio](https://www.affinity.studio/help/workspace-compositing-studio/)

How would you rate the help you received from this article?
