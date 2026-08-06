---
title: "Stacking Options panel (Astrophotography Stack Studio) - Affinity Help Center"
source: https://www.affinity.studio/help/panels-astro-panel-stacking-options/
slug: panels-astro-panel-stacking-options
fetched: 2026-08-06
---

# Stacking Options panel (Astrophotography Stack Studio) - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-astro-panel-stacking-options/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
4.   Stacking Options panel (Astrophotography Stack Studio)

When creating astrophotography, use the Stacking Options panel to control the stacking method that's used to process light and calibration frames.

This feature is only available in Affinity for desktop.

For Mac/Windows: On the **Window** menu, select **Stacking Options**.

The following options are available on the panel:

*   **Background calibration**—normalizes the background level of the light frames based on a reference frame. Recommended when using sigma clipping to avoid mistakenly clipping pixels.
*   **Stacking method**—the operator used to average the contents of the light frames and, separately, calibration frames, which can be: 
    *   **Mean**—averages pixel content across the stack of images.
    *   **Median**—removes pixel content that is not consistent in each image.
    *   **Sigma clipping**—clips pixels outside of a given range.

*   **Threshold (standard deviations)**—if the result of sigma clipping still contains hot pixels or other erroneous data, try lowering this to about 2. However, a lower value may result in banding/posterization around high-contrast star detail.
*   **Clipping iterations**—the number of passes performed during stacking. More passes may result in greater accuracy.

Sigma clipping is the default stacking method and generally a good choice if you have a lot of data. With very limited data—less than one hour's worth of exposures—the mean and median methods are suitable.

Sigma clipping is well suited to monochrome imagery from dedicated astronomy cameras with a CCD or CMOS sensor. Although temperature-regulated, these cameras may exhibit hot pixels, sensor defects and other erroneous pixel data that would show up in the end result.

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 The following options are available on the **Panel Preferences** menu:

*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

*   [About astrophotography stacking](https://www.affinity.studio/help/astrophotography-astro-about/)
*   [Creating an astrophotography stack](https://www.affinity.studio/help/astrophotography-astro-creating/)
*   [Files panel](https://www.affinity.studio/help/panels-astro-panel-files/)
*   [RAW Options panel](https://www.affinity.studio/help/panels-astro-panel-raw-options/)
*   [Compositing narrowband images](https://www.affinity.studio/help/astrophotography-astro-narrowband/)
*   [Customizing Studios](https://www.affinity.studio/help/workspace-customizing-studios/)

How would you rate the help you received from this article?
