---
title: "About astrophotography stacking - Affinity Help Center"
source: https://www.affinity.studio/help/astrophotography-astro-about/
slug: astrophotography-astro-about
fetched: 2026-08-06
---

# About astrophotography stacking - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/astrophotography-astro-about/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
4.   About astrophotography stacking

The Astrophotography Stack Studio is used to create high-quality celestial images.

This feature is only available in Affinity for desktop.

It requires light frames, which are long exposures of the night sky, and several kinds of calibration frame. Stacking of the light frames increases the SNR (signal-to-noise ratio).

The stacking process is performed to 32-bit linear unbounded floating point precision throughout, which maximizes your options for tone-stretching and other post-processing you might perform.

When creating your astrophotography stacks, Affinity lets you choose the **Default tone curve** for the process. The options can be found in **Settings > Assistant > Develop Assistant**.

Calibration frames help to clean up imagery, by identifying and removing noise from the light frames—the excess of it, at least—as well as dust spots, vignetting and other artefacts.

The use of calibration frames is optional but strongly recommended.

Noise is inherent in the shooting environment and is influenced by several factors, including: overall thermal conditions, which can vary over time; background electrical interference in the camera; and hot pixels in the camera sensor. For example, hot pixels could be misidentified as stars, affecting alignment during stacking.

Four kinds of calibration frame can be processed, each of which identifies different noise.

*   **Dark frames**—identify hot pixels and thermal noise, arising from long exposure times, to be cleaned from the light frames. Taken during the same session and at the same shutter speed as light frames but with the lens cap on.
*   **Bias frames**—identify electrical read noise from the camera. Taken at the fastest shutter speed available with the lens cap on.
*   **Flat frames**—identify artefacts such as dust specks and lens vignetting, ensuring evenly illuminated images. Captured during the same session as light frames.
*   **Dark flat frames**—to pre-process the flat frames by cleaning noise from them, like dark frames do for light frames. Taken at the same shutter speed as the flat frames.

![Image 1: Light](https://images.ctfassets.net/3p2fxa94bzao/6BkfWt9HZ7j8KEFfFVihv/aa8d73f98aefe128ef5aa436d07b79f1/astroLight.jpg)

![Image 2: Bias](https://images.ctfassets.net/3p2fxa94bzao/18Y4sr2s6a6Yyq9AldiJ7E/ccb8c536c0f5b5423509fdb1e96182bf/astroBias.jpg)

![Image 3: Dark](https://images.ctfassets.net/3p2fxa94bzao/4TxAv98oujp1H5Zbix6Xb0/3bc50bf39f44e5b3f71d383a097c9a3f/astroDark.jpg)

![Image 4: Flat](https://images.ctfassets.net/3p2fxa94bzao/4twtA4KBR6fFZOfr6DZfnn/ac48ad6b8f3f9359af42439151b31182/astroFlat.jpg)

![Image 5: Dark flat](https://images.ctfassets.net/3p2fxa94bzao/7mDInrmI2G3HOpH4eXqMSd/8cf8bfc48a81ceac28b5ae7ca9c74e78/astroDarkFlat.jpg)

![Image 6: An example end result from the Astrophotography Stack Studio with additional post-processing applied](https://images.ctfassets.net/3p2fxa94bzao/5wjoS6C5bMKDzJHQC8qccL/6797c1463a4e0215d00b7bf226af71b8/astroEndResult.jpg)

In practice, multiple frames of each type are used to improve the SNR ratio and improve the end result.

Light frames and calibration frames should be RAW or FITS (Flexible Image Transport System) files from a DSLR or astronomy camera, respectively.

They must be unprocessed for best results to avoid assumptions being made about white balance and tonality, which are approximated later in the compositing process.

FITS (Flexible Image Transport System, https://fits.gsfc.nasa.gov) is a file format commonly used in astrophotography that can contain extra metadata not found in RAW files. It is usually captured by CCD and CMOS astronomy cameras used with telescopes. Affinity recognizes FITS files with a .fit or .fts file extension.

In the Pixel Studio, opening an individual FITS file that contains Bayer pattern metadata displays the **Develop FITS** dialog.

You might do this with individual FITS files from a photo shoot to inspect their quality, or with master FITS files containing calibrated and stacked data to manually combine, align and process them.

The dialog's **FITS Bayer Pattern** setting infers the Bayer pattern of the camera's color sensors by default, but can be manually set to a specific pattern if the results look incorrect.

*   [Creating an astrophotography stack](https://www.affinity.studio/help/astrophotography-astro-creating/)
*   [Files panel](https://www.affinity.studio/help/panels-astro-panel-files/)
*   [Stacking Options panel](https://www.affinity.studio/help/panels-astro-panel-stacking-options/)
*   [RAW Options panel](https://www.affinity.studio/help/panels-astro-panel-raw-options/)
*   [Compositing narrowband images](https://www.affinity.studio/help/astrophotography-astro-narrowband/)
*   [Tone Stretch adjustment](https://www.affinity.studio/help/adjustments-adjustment-tone-stretch/)
*   [Settings](https://www.affinity.studio/help/workspace-settings/)

How would you rate the help you received from this article?
