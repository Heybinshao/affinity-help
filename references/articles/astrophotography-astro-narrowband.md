---
title: "Compositing narrowband astrophotography - Affinity Help Center"
source: https://www.affinity.studio/help/astrophotography-astro-narrowband/
slug: astrophotography-astro-narrowband
fetched: 2026-08-06
---

# Compositing narrowband astrophotography - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/astrophotography-astro-narrowband/

Narrowband astrophotography uses astronomical filters to capture images of light from specific wavelength bands. It is often used to produce images of nebulae. A dedicated astronomy camera tends to be used.

The resulting frames are monochromatic but can be processed by the Astrophotography Stack Studio just like full-color frames.

Several mono images, each taken with a different filter, can be manually composited into a full-color image.

The most commonly used filters detect Hydrogen-alpha (Ha), Oxygen-III (O-III) and Sulfur-II (SII).

![Image 1: A composited full-color image](https://images.ctfassets.net/3p2fxa94bzao/7oGt9Y0jGSyNsl0uTBON5Y/9c4249af09c10a36f9d475c9886fbd2d/astroComposited.jpg)

An example of composited, full-color narrowband astrophotography.

Before compositing, use the [Astrophotography Stack Studio](https://www.affinity.studio/help/astrophotography-astro-creating/) to create three separate images, each from a different astronomical filter's frames.

To ensure you start with a document of the correct properties, including resolution and color format, use one of your already-stacked monochromatic documents as the base on which to perform the following procedure.

1.   Copy and paste a flattened version of each of the other two mono images onto a separate pixel layer in the new document.
2.    For each pixel layer in turn: 
    1.   Select **Pixel > New Adjustment Layer > Recolor**.
    2.   Clip the adjustment layer to the pixel layer. (See [Layer Clipping](https://www.affinity.studio/help/layers-layer-clip/).)
    3.   Set the adjustment layer's hue uniquely to red (0°), green (120°) or blue (240°).

3.   Set each pixel layer's blend mode to **Add**.
4.   Perform additional post-processing work as necessary

There is no universally accepted color assignment for each chemical element, so experiment. For example, the Hubble palette assigns red to S-II, green to Ha, and blue to O-III.

Use your artistic judgment in post-processing. For example, you might:

*   Perform tone-stretching by applying Brightness/Contrast, Curves and Levels adjustment layers or a dedicated Tone Stretch adjustment.
*   Remove distractions with noise reduction filters and retouching tools.
*   Use a Fill layer with the Subtract blend mode applied to remove a color cast.

*   [About astrophotography stacking](https://www.affinity.studio/help/astrophotography-astro-about/)
*   [Creating an astrophotography stack](https://www.affinity.studio/help/astrophotography-astro-creating/)
*   [Files panel](https://www.affinity.studio/help/panels-astro-panel-files/)
*   [Stacking Options panel](https://www.affinity.studio/help/panels-astro-panel-stacking-options/)
*   [RAW Options panel](https://www.affinity.studio/help/panels-astro-panel-raw-options/)
*   [Tone Stretch adjustment](https://www.affinity.studio/help/adjustments-adjustment-tone-stretch/)
