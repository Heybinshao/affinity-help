---
title: "32-bit Preview panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-32bit-panel/
slug: panels-32bit-panel
fetched: 2026-08-06
---

# 32-bit Preview panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-32bit-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   32-bit Preview panel

The 32-bit Preview panel provides configurable exposure and gamma controls to preview the vast tonal range of a 32-bit document without tonally modifying it.

For Mac/Windows: On the **Window** menu, select **Pixel > 32-bit Preview**.

The following options are available on the panel:

*   **Enable EDR**—enables _Extended Dynamic Range_ mode to allow peak brightness values greater than diffuse/paper white to be displayed, increasing the dynamic range of the document view. To enable EDR mode for .heif, .heic, and .jpeg files containing gain maps, select **Apply gain maps** in **Settings > General**. 
*   **Show EDR Clipping**—displays overexposed areas while in EDR mode. These are areas outside of the peak brightness value that the display is capable of (e.g. 1000 nits).
*   **Clip to maximum**—prevents the display from tone mapping while in EDR mode. Ordinarily, the display will tone map brightness values above its peak brightness threshold, but with this option enabled those values will instead be clipped.

*   **Enable HDR**—enables _High Dynamic Range_ mode to allow peak brightness values greater than diffuse/paper white to be displayed, increasing the dynamic range of the document view.
*   **Clip warning**—displays overexposed areas while in HDR mode. Choose between **average** or **peak** brightness, measured in nits. These values are obtained from the display's metadata.
*   **Monitor reference white (nits)**—used in conjunction with clipping. Set this value to the diffuse/paper white brightness value you have calibrated your display to (if using a profiling device, this may be measured in _cd/m2_ which is equal to _nits_). This ensures accurate clipping information is displayed.
*   **Clip to Max (Peak)**—prevents the display from tone mapping while in HDR mode. Ordinarily, the display will tone map brightness values above its peak brightness threshold, but with this option enabled those values will instead be clipped.

*   **Preview Exposure**—increases or decreases the preview exposure of the image, allowing you to better visualize the highlight or shadow tonal ranges for editing.
*   **Preview Gamma**—alters the gamma correction value.
*   **Display Transform**—allows you to switch between a non-linear view using the current display profile, linear light or an OCIO transform: 
    *   **ICC Display Transform**—non-linear transform using the current display profile.
    *   **Unmanaged**—a linear light view where no transform is applied.
    *   **OCIO Display Transform**—choose a device transform and a view transform to preview your document using OpenColorIO. The options presented for both pop-up menus will differ depending on your current OpenColorIO configuration.

In order to use the **Display Transform** options, you must have a valid **OpenColorIO** configurable file and directory defined. See [Using OpenColorIO](https://www.affinity.studio/help/clr-ocio/) for more information.

If you intend on tone mapping or tonally modifying your image to compress its tonal range, you will likely not need to use this panel.

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 The following options are available on the **Panel Preferences** menu:

*   **Panels**—opens a dialog where you can quickly set the visibility of all panels in the current Studio.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

*   [Using OpenColorIO](https://www.affinity.studio/help/clr-ocio/)
*   [Customizing Studios](https://www.affinity.studio/help/workspace-customizing-studios/)

How would you rate the help you received from this article?
