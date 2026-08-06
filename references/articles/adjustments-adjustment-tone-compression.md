---
title: "Tone Compression adjustment - Affinity Help Center"
source: https://www.affinity.studio/help/adjustments-adjustment-tone-compression/
slug: adjustments-adjustment-tone-compression
fetched: 2026-08-06
---

# Tone Compression adjustment - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/adjustments-adjustment-tone-compression/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Tone Compression adjustment

The Tone Compression adjustment

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/1lvZge9y27vIh7w8LGd7zk/aab2536a44955a983324b0ab8ef575c1/tone_compression.svg)

 groups together several settings for enhancing tone and color.

![Image 2: After](https://images.ctfassets.net/3p2fxa94bzao/1mvrYAZ7dMUNY925OGqQLx/3780f676b31a3d59a060377993e07493/adjustment_toneCompression_after.jpg)

![Image 3: Before](https://images.ctfassets.net/3p2fxa94bzao/6xqnHfCefxkLSRkoRW3mPq/142cbd3e3fdbe6d07b3b274aab927d3f/adjustment_toneCompression_before.jpg)

Contrary to how images are processed in the Tone Mapping Studio which uses spacial processing techniques, the Tone Compression adjustment uses non-spacial processing methods, which in return is much faster. The adjustment therefore renders results in real time, allowing you to preview the output instantly.

The adjustment is non-destructive, meaning it can be reworked at any point in time. It also provides and easy way of mapping HDR images to SDR.

32-bit HDR source imagery is required for the adjustment to work. This could be from:

*   HDR merging bracketed exposures. Make sure to toggle **Tone map image** off to avoid Affinity opening the Tone Mapping Studio as soon as merging has completed.
*   Developing RAW files straight to 32-bit linear unbounded float format. This can be achieved by changing an Assistant option in the app's Settings.
*   Opening HDR images from various sources such as EXR, Radiance HDR, JPEG-XL, HEIF etc.

*   **Method**—sets the tonal range type of compression. Choose from: 
    *   **Basic**—straightforward compression, producing a fairly neutral image with gradually compressed highlights.
    *   **Neutral**—produces a more natural roll off of color intensity as values get brighter.
    *   **Bright**—produces slightly brighter highlights.
    *   **Contrast**—creates a punchier compressed result.
    *   **Filmic**—exaggerates highlight bloom or glow in overexposed areas, similar to that of negative film.
    *   **Punchy**—produces more contrast between tones.
    *   **PBR Neutral**—primarily intended for 3D work that uses a PBR rendering pipeline.
    *   **Log**—transforms the image to log space, giving the user more freedom to shape the tones using various adjustments (e.g. Curves and LUTs).

*   **Exposure**—raises or lowers the overall exposure.
*   **Saturation**—increases or decreases color saturation. Drag the slider to the left to increasingly desaturate.
*   **Gamma**—controls the intensity of color compression.
*   **Color**—controls the level of tonal compression while targeting color pixels rather than luminosity.

Do one of the following:

*   On the Layers panel, click **Adjustments**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/4ZFx9I9M7MiUBPmytBqZrt/cad5a29a5e39b1b3faa42c5fa29402f3/add_adjustment_layer.svg)  and select **Tone Compression**.
*   On the **Adjustment** panel, select **Tone Compression**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/1lvZge9y27vIh7w8LGd7zk/aab2536a44955a983324b0ab8ef575c1/tone_compression.svg)  and then click on a preset to modify, as required.
*   On the **Pixel** menu, select **New Adjustment Layer > Tone Compression**.

The **Adjustment** panel is not visible by default. To enable it, navigate to the top menu and select **Window > Pixel > Adjustment**.

*   [Astrophotography adjustments](https://www.affinity.studio/help/adjustments-astro-adjustments/)
*   [Tonal adjustments](https://www.affinity.studio/help/adjustments-tonal-adjustments/)
*   [32-bit HDR editing](https://www.affinity.studio/help/hdr-hdr-editing/)
*   [Developing a RAW image](https://www.affinity.studio/help/raw-raw/)
*   [Applying adjustments](https://www.affinity.studio/help/raw-raw/)
*   [Assistant Settings](https://www.affinity.studio/help/workspace-settings/)

How would you rate the help you received from this article?
