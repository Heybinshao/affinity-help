---
title: "Canvas not white, colors appear incorrectly, or UI not rendering as expected - Affinity Help Center"
source: https://www.affinity.studio/help/canvas-not-white/
slug: canvas-not-white
fetched: 2026-08-06
---

# Canvas not white, colors appear incorrectly, or UI not rendering as expected - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/canvas-not-white/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Installation and setup](https://www.affinity.studio/help/installation-setup/)
3.   Canvas not white, colors appear incorrectly, or UI not rendering as expected

Affinity performs document-to-screen colour profile conversion, which translates initial document colour values based on the current display profile. This differs from other apps that do not perform such conversions, meaning colour discrepancies may only be visible within Affinity.

If your Affinity app displays an off-white canvas, incorrect colours, or unexpected UI rendering, the issue is typically rooted in the colour profile (ICC profile) applied to your display or device. These profiles can be automatically applied by the manufacturer or manually created through third-party colour calibration tools.

To resolve these display issues in your Affinity app, we suggest changing your display's colour profile to sRGB IEC61966-2.1.

1.   Press **Windows Key** + **R**to open the Run dialog.
2.   Type **colorcpl** and click **OK**. This will open the**Color Management**window**.**
3.   Under the Devices tab, select the current monitor from the **Device** dropdown menu.Make sure **Use my settings for this device** is selected.
4.   **If there’s a ICC Profile already listed:**
    *   Select the profile and click **Remove**. You will be prompted to confirm, please select **Continue**.

5.   **If there’s no ICC Profile is listed:**
    *   Proceed to the next step.

6.   Click **Add...** and select **sRGB IEC61966-2.1** from the list and click **OK**. Do not use the 'virtual' sRGB profile**.**
7.   The **sRGB IEC61966-2.1** profile should now appear in the **Profiles associated with this device** section.
8.   Select the **sRGB IEC61966-2.1** profile and click **Set as Default Profile** to make it the default.
9.   If you have multiple monitors, please repeat the steps above by selecting your other monitor(s) from the **Device** dropdown menu.
10.   Close the **Colour Management**window and restart your Affinity app.

1.   Navigate to **Apple**>**System Settings**>**Displays**
2.   Select your main device/display from the top of the dialog, if multiple displays are connected.
3.   Change the **Colour Profile** dropdown menu to **sRGB IEC61966-2.1**
4.   If you have multiple devices, please repeat the steps above by selecting your other display(s).
5.   Close the **System Settings** window and restart your Affinity app.

How would you rate the help you received from this article?
