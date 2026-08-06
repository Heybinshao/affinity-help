---
title: "Using Vectorscope (desktop only) - Affinity Help Center"
source: https://www.affinity.studio/help/design-aids-using-vectorscope/
slug: design-aids-using-vectorscope
fetched: 2026-08-06
---

# Using Vectorscope (desktop only) - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/design-aids-using-vectorscope/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Using Vectorscope (desktop only)

**Vectorscope** presents color and saturation data measured via the image signal. Its representation allows for accurate evaluation of color and thus aids workflows where it is challenging to judge the output by eye.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/6WJOBecuZoBKiqRZtinYc1/7bda5df8e0be3fba1846676c7fa3780f/usingVectorscope_after.jpg)

After skin color correction using Vectorscope as an aid.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/64MfdCKcE1HBI4MIkfEYro/1ee3a269afe04927d48bff30a4e8b6cc/usingVectorscope_before.jpg)

Before skin color correction using Vectorscope as an aid.

The Vectorscope pie chart, available in the Scope panel, is divided into six parts representing the main colors of the RGB color space (red, green, blue) as well as their inverse equivalents (cyan, magenta, yellow). The chart places signal information from the image according to where its value sits in relation to the color space. For example, if there is a significant amount of blue color in the image, its representation will appear in the region of the blue line.

Additionally, the chart includes the _I_ line, which may be used as an aid during correcting skin tones; the idea here is to adjust skin colors in such a way that their representation sits along this line.

To better understand the Vectorscope chart readout, on a new pixel layer, brush in strokes of the main RGB color space colors and observe how they are represented.

1.   On the **Window** menu, choose **Pixel > Scope**.
2.   In the panel, change the scope type to **Vectorscope**.

1.   Using the **Crop Tool**, crop into an area that is visibly inaccurate in the image, e.g. too saturated. Observe the representation of color on the Vectorscope chart.
2.   Undo the cropping action.
3.   Open the HSL adjustment and, from the dialog, use the **Color Picker Tool** to sample color from the skin area that needs correcting.
4.   Modify the Hue Shift slider to add a positive value (i.e. push it right slightly) while balancing the Saturation Shift with a negative value.
5.   Observe the Vectorscope chart's _I_ line and ensure that the color representation of the adjustment aligns with it.

The most effective outputs are achieved by small increments of adjustments. White Balance and Vibrance can also be used in addition to HSL to further tweak the correction.

To limit your edits to just the skin area of the subject, and to take things further, use non-destructive masking and selecting techniques.

*   [Scope panel](https://www.affinity.studio/help/panels-scope-panel/)
*   [Histogram panel](https://www.affinity.studio/help/panels-histogram-panel/)

How would you rate the help you received from this article?
