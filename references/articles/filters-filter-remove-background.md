---
title: "Remove Background filter (Astrophotography) - Affinity Help Center"
source: https://www.affinity.studio/help/filters-filter-remove-background/
slug: filters-filter-remove-background
fetched: 2026-08-06
---

# Remove Background filter (Astrophotography) - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-filter-remove-background/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Remove Background filter (Astrophotography)

An astrophotography filter that subtracts unwanted sky glow, light pollution, and gradient illumination from your image by sampling background colour. Use it to get rid of sky glow and light pollution, which tend to be exaggerated by tone-stretching.

This feature is only available in Affinity for desktop.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/MHyDPAnJIZASN9HkMWfUB/52fb25d3356258598e4531e7cbf668e7/filter_removebackground_after.jpg)

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/5gFcpEhVXmnPdqTLSppW6y/1f491b33120e80f4ab271e14b29250c4/filter_removebackground_before.jpg)

This filter can be found on the **Pixel > Filters > Astrophotography** menu.

The filter is destructive, so it is recommended to apply it to a merged pixel layer that is created after tone-stretching but before any other post-processing has been applied to your image.

A color-sampling handle is precreated at the center of the image. Drag it to reposition as needed to sample a background tone to be subtracted.

Use a single handle to remove a fairly uniform background. Click within the document view to create additional handles to remove gradients, e.g. caused by light pollution, sky glow or moon illumination.

Alternatively, specify your own gray and RGB levels for subtraction by selecting a handle and manually setting the filter's **Grey**, **Red**, **Green** and **Blue** values. Manually setting any of these values will cause **Sample color at handle** to become deselected for the selected handle.

The following settings can be adjusted in the filter dialog:

*   **Sample color at handle**—when selected (recommended), the gray and RGB levels for the selected handle are automatically read from the handle's position.
*   **Radius**—controls the distance from which color is sampled around the handle, up to a maximum of 20 px. Type directly in the text box or drag the slider to set the value.
*   **Grey**—controls the level of gray to be subtracted from the image. Type directly in the text box or drag the slider to set the value.
*   **Red**—controls the level of red to be subtracted from the image. Type directly in the text box or drag the slider to set the value.
*   **Green**—controls the level of green to be subtracted from the image. Type directly in the text box or drag the slider to set the value.
*   **Blue**—controls the level of blue to be subtracted from the image. Type directly in the text box or drag the slider to set the value.
*   **Output black level**—prevents darker tones being clipped and provides control over the background's aesthetic. Type directly in the text box or drag the slider to set the value.

*   [Remove Background (Canva AI)](https://www.affinity.studio/help/canva-ai-canva-ai-remove-background/)
*   [Applying filters](https://www.affinity.studio/help/filters-filters-applying/)
*   [About astrophotography stacking](https://www.affinity.studio/help/astrophotography-astro-about/)

How would you rate the help you received from this article?
