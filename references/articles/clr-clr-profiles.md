---
title: "Color management - Affinity Help Center"
source: https://www.affinity.studio/help/clr-clr-profiles/
slug: clr-clr-profiles
fetched: 2026-08-06
---

# Color management - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/clr-clr-profiles/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Color management

The color and tonal information in a digital document is stored as numbers. When we share these documents between devices, the device has to work out how to display the color. As not all devices can display the same color gamut it can lead to colors looking different on each device.

![Image 1: Color profiles](https://images.ctfassets.net/3p2fxa94bzao/wfD1LsMB9L4sYCPaq6X0a/bae474185568e8b61915e9270cff892d/clr_profiles_before.png)

Documents without color profiles (or with unsupported color profiles) may not look the same across each device.

To ensure that the color looks the same on each device, we use color profiles to tell the device how to display or render the color information.

![Image 2: Color profiles](https://images.ctfassets.net/3p2fxa94bzao/53IHe1WlHX8UHNx7VvszMu/c7fc6f94af92c761eca6b41507863afd/clr_profiles_after.png)

Documents with the correct profile for a calibrated device should closely match.

Affinity honors an opened file's color profile by default. You have the option to convert it to the current working color space. When placing images into an existing document, the image's embedded color profile will always be converted to the document's current working space.

On export, you can choose to embed the document's or a named color profile to ensure accurate color management. Alternatively, the exported file can be unprofiled by not embedding the document or named profile.

Affinity lets you choose global default color profiles, assign a color profile as you create a document, or at any point during your session.

Most commercial printers will accept sRGB as they'll be able to do their own profiling at the print stage to get the best results for your work.

For the CMYK color model, it's best to consult your print partner for an appropriate CMYK color profile recommendation.

*   From **Settings** (Color option), select an RGB, 32-bit RGB, CMYK, Grayscale or LAB color profile from the pop-up menus.
*   Choose a **Rendering intent** option and check **Black Point compensation** if needed.

*   As you create a new document, select an option from the **Color Profile** pop-up menu.

*   Prior to opening the file, from **Settings** (Color option), check the **Convert opened files to working space** option.

Options exist to warn that a file's working space will be converted, or that an unprofiled file will be assigned the current working space's profile.

1.   On the **File** menu, select **Document Setup**.
2.    From the dialog: 
    *   Select the **Color** tab.
    *   On the **Color Profile** pop-up menu, select a profile.
    *    Select **Assign** or **Convert**.**Assign** adopts the new profile but leaves the values of the colors/pixels as is. **Convert** converts each color from the old profile to the new one—color/pixel values may change as a result. 
    *   Click **OK**.

Common color profiles used in design include sRGB IEC61966-2.1 and Adobe RGB 1998, the former for on-screen display.

1.   On the **Document** menu, select **Setup > Convert Format / ICC Profile**.
2.   Select a profile from the list in the dialog.
3.   Click **Convert**.

1.   On the Slice Studio ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3vfODAvo895dTN5bFMTLNs/68e3d14904308a323dbf48d056fcf21d/persona_slice.svg) , choose your **Preset** in the Export Options panel.
2.   (Optional) Select a different **ICC profile** from the pop-up menu. Otherwise, the document's color profile will be embedded.
3.   Check **Embed ICC profile**.

You can also embed an ICC profile via **File > Export > Export** (in the **Advanced** section).

Related behaviors can be adjusted from [the app's settings](https://www.affinity.studio/help/workspace-settings/):

*   **Color > Color profiles**
*   **Color > Rendering intent**
*   **Color > Black point compensation**
*   **Color > Convert opened files to working space**

Soft proofing simulates output as you edit and design with respect to the color profile and the paper medium you intend to print on.

In Affinity, this can be done by applying a **Soft Proof** adjustment to your project. You can then preview how your output will appear, preventing any nasty surprises at print time.

Because soft proofing is applied as an adjustment you can apply multiple adjustments, and therefore produce soft proofs for multiple output devices.

As an example, if you want to create several different output types, you might want to start with a color profile on document creation with a wide gamut (e.g., Adobe RGB 1998), and then change the profile to match the output destination. However, color information may be thrown away if changing to a smaller color gamut—simply changing back to a profile with a wider gamut will not restore the additional color information. By applying a soft proof adjustment you prevent this, allowing you to work in a wider gamut until you are ready to change to your chosen output profile.

Affinity detects and can use ICC color profiles installed on your operating system when exporting files. No special steps have to be taken in the app to make profiles available for its use when exporting files; installed profiles are available from the ICC profile pop-up menu of the Export dialog.

Your operating system includes software to assign an installed profile to your printer.

*   Place the .icc file in /Library/ColorSync/Profiles at either the system or user level.

1.   In Finder, select **Go > Utilities** and open ColorSync Utility.
2.   Select the **Devices** tab.
3.   Select the printer with which to associate the profile.
4.   Select the profile from the pop-up menu next to **Current Profile**.

*   [Creating new documents](https://www.affinity.studio/help/get-started-new-document/)
*   [Slice Studio](https://www.affinity.studio/help/workspace-slice-studio/)
*   [Export Options panel](https://www.affinity.studio/help/panels-export-options-panel/)
*   [About exporting](https://www.affinity.studio/help/sharing-export/)
*   [Soft proof adjustment](https://www.affinity.studio/help/adjustments-adjustment-soft-proof/)
*   [Color models](https://www.affinity.studio/help/clr-clr-models/)

How would you rate the help you received from this article?
