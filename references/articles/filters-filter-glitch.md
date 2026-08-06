---
title: "Glitch filter - Affinity Help Center"
source: https://www.affinity.studio/help/filters-filter-glitch/
slug: filters-filter-glitch
fetched: 2026-08-06
---

# Glitch filter - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-filter-glitch/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Glitch filter

The filter simulates a number of realistic and creative glitches including chromatic aberration, static noise, pixelation, pixel displacement, light leaking, warping and more.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/6VWsPz6L9Rb5YSpKDo9KtH/f7d44462b295d97d14e11a4537a13095/filter_glitch_after.jpg)

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/6bfIpiw1yLmV8lZuFNdgb2/969a76005c445136cedbb04c9b81328f/filter_glitch_before.jpg)

The **Glitch**

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2UqsbjdwlwsZOmQPgjApA6/31bb87be2d8dd6f9885f5662f7c7b00d/glitch_live_filter.svg)

 filter simplifies a complicated process of editing channels, selections and other distortion filters to achieve the effect. The output is previewed in real time, without the need to render the effect.

Stack multiple glitch filters of either the same or different types for an even more intense and varied effect.

This filter can be applied as a destructive or non-destructive live filter.

For filter methods that use channel ordering (RGB, GRB, etc.), the in-dialog Number of Channels set represents the channels mix from the order. For example, if set to RGB and two channels, the color mix will take the Red and Green channel values into the calculation.

For negative Glitch Strength values, the result is inverted mixtures from the color spectrum set.

To use the destructive version of the filter, select it from the **Pixel > Filters > Distort** menu. The live version can be accessed from:

*   the **Layers** panel by clicking **Live Filters**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/2ALwfgZXKqtubPaMdMHvlC/d4901c280214d88174d57188a9c56e21/filters_studio.svg) .
*   the **Pixel > New Live Filter Layer > Distort** menu.

Glitch is also available as a tool in the Compositing Studio

![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3HLsf5xx2FlnBTmx7VwAkX/eb93eb77aa0dc236a5edfe2d6e7ef9f7/compositing_studio.svg)

.

The following glitch types can be applied from the filter dialog:

*   **Aberration (Distortion)**—simulates wavelengths of light being displaced (fringing/chromatic aberration). Drag on the document view to set the origin.
*   **Aberration (Offset)**—simulates chromatic aberration/fringing based on a simple X/Y offset. Drag on the document view to set X/Y offset.
*   **Shred**—splits the image apart into segments with the ability to control both horizontal and vertical offsets separately. Use the pixel spacing slider to control the size of each row/column.
*   **Blast**—control the horizontal and vertical offsets separately, and use the Stagger option to randomise which columns/rows are affected (preserving some of the underlying image).
*   **Slice**—creates visible “slices” in the image (horizontal and vertical, controllable separately). The Offset slider can be used to control the amount of slice displacement.
*   **Sawtooth**—similar to slice, producing a visible “sawtooth” edge effect. This could be combined with other glitches to simulate an analog television signal.
*   **Distort**—applies uneven pixel or channel shifts to create a fragmented appearance, mimicking digital signal errors or data corruption.
*   **Ripple**—separable channel method. Distorts the image with small ripples.
*   **Waves**—separable channel method. Distorts the image in a wave shape. Use Wave Loops to go from a very broad wave to many smaller waves.
*   **Shred (Color)**—a separable channel version of Shred. Creates a more intense channel split effect.
*   **Blast (Color)**—a separable channel version of Blast.
*   **Slice (Color)**—a separable channel version of Slice.
*   **Sawtooth (Color)**—a separable channel version of Sawtooth.
*   **Distort (Color)**—a separable version of Distort.
*   **Ripple (Color)**—a separable version of Ripple.
*   **Waves (Color)**—a separable version of Waves.
*   **Quantisation**—separable channel method. Pixelates each channel with different values.
*   **Scramble**—pixelates the image in a random, noisy fashion.
*   **Fuzz**—separable channel method. Produces diffuse noise with the strength varying for each channel. Set the number of channels (1-3) and use channel ordering to control the order in which the strength values are applied.
*   **Ripple**—separable channel method. Distorts the image with small ripples.
*   **Waves**—separable channel method. Distorts the image in a wave shape. Use Wave Loops to go from a very broad wave to many smaller waves.
*   **Warp**—distorts an image, with controllable horizontal and vertical distortion. Use the Turbulence slider to go from a broader distortion to many smaller waves of distortion.
*   **Light Streaks**—applies a “light leak” type effect, controllable for both horizontal and vertical directions.
*   **Channel Flip**—inverts one color channel with strength controlling the contrast. Use with opacity and blend modes for optimum results.
*   **Data Blocks**—adds colorful, square-shaped blocks; their size and color contribution can be edited.

For Distortion, Offset, Shred Color, Blast Color filter types, the following option will become available:

*   **Bidirectional**—when enabled, the glitch effect applies pixel or color-channel displacement in both directions (e.g., left and right) along the chosen axis. This creates a more balanced, mirrored distortion compared to a one-sided (unidirectional) glitch.

*   [Using live filters](https://www.affinity.studio/help/layers-livefilters/)
*   [Applying filters](https://www.affinity.studio/help/filters-filters-applying/)
*   [Chromatic Aberration filter](https://www.affinity.studio/help/filters-filter-chromatic-aberration/)
*   [Compositing Studio](https://www.affinity.studio/help/workspace-compositing-studio/)

How would you rate the help you received from this article?
