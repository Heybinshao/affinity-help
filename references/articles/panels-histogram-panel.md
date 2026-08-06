---
title: "Histogram panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-histogram-panel/
slug: panels-histogram-panel
fetched: 2026-08-06
---

# Histogram panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-histogram-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Histogram panel

The Histogram panel shows the distribution of Red, Green and Blue values for the image, layer, or current selection.

For Mac/Windows: On the **Window** menu, select **Pixel > Histogram**.

The panel gives a valuable 'heads up' of the colors present in your image, which is useful for deciding if color or tonal correction is needed.

The light blue values indicate the overlap of the RGB channels (not the luminosity). Purple represents where the red and blue channel representations overlap.

In LAB or CMYK color modes, channels for that mode are displayed instead of Red, Green and Blue (RGB).

Color distribution statistics can optionally be presented at the bottom of the panel to provide further color information. Your cursor can be moved around the histogram, displaying the pixel count at the color level (0-255) your cursor is currently placed at.

**Level** and **Percentile** readouts are particularly useful in recognising precise color and tonality values, and where precision editing is key. They are particularly useful when editing in the following example scenarios:

*   matching images in a series
*   preparing for print
*   working on calibrated displays

Level is the pixel's position on the tonal scale (0-255) with the readout value presenting how bright the current pixel is. Percentile shows what percentage of pixels are darker than the current one—in other words, where this pixel sits relative to the whole image.

Keep an eye out on very high and very low **Level** and **Percentile** readouts. For example, if Percentile is 99% and Level is near max, this may result in clipped highlights. Similarly, if the readouts are near min (0-2%), this may indicate crushed shadows.

Use the readouts to inform your next editing steps for these areas.

**Min/Max** inputs can also be presented at the bottom of the panel to constrain or expand the tonal range the histogram represents. This is especially useful for unbounded 32-bit documents where you may want to either represent more out of range information or clip it further.

The yellow triangle on the histogram can be clicked to display color distribution levels in finer detail.

Luminosity is displayed on the **Scope** panel's Intensity Waveform, providing both an IRE readout and an abstract visual representation of your image.

The following options are available on the panel:

*   **Channels**—presents data either for all or individual channel; select from the list.
*   **Layer**—when checked, presents data for the currently selected layer.
*   **Marquee**—when checked, and with a selection made with one of the Marquee tools in place, the histogram presents data for that region.

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 The following options are available on the Panel Preferences menu:

*   **Advanced**—when checked, the histogram will display additional readout data.
*   **Panels**—opens a dialog which allows quick access to displaying other panels.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

*   [Color models](https://www.affinity.studio/help/clr-clr-models/)
*   [Scope panel](https://www.affinity.studio/help/panels-scope-panel/)
*   [Customizing Studios](https://www.affinity.studio/help/workspace-customizing-studios/)

How would you rate the help you received from this article?
