---
title: "Developing RAW images - Affinity Help Center"
source: https://www.affinity.studio/help/raw-raw/
slug: raw-raw
fetched: 2026-08-06
---

# Developing RAW images - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/raw-raw/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Developing RAW images

The Develop Studio is a dedicated non-destructive environment used for processing RAW images captured using a digital camera.

![Image 1: Develop Studio in Affinity for desktop.](https://images.ctfassets.net/3p2fxa94bzao/4MsDmOUeS7zbGGEupH7kMF/860d5a9b0b4c4ddb3ce499df248860e4/raw_develop_studio.jpg)

Develop Studio in Affinity for desktop.

If a [supported RAW file format](https://www.affinity.studio/help/appendix-fileformat/) is opened, it will automatically display in the Develop Studio. You can then process the image using the dedicated adjustments, panels and tools. Affinity lets you develop RAW images non-destructively, without affecting the original file.

Only **Affinity RAW Engine** can be used for non-destructive operation. The engine is selected by default when you open the app. If changed, swap to it by navigating to **Settings > Assistant > Develop Assistant** and then, from the **RAW Engine** pop-up menu, select **Affinity RAW**.

The Develop Studio gives you access to the following:

*   **Output** options that will retain your original RAW image as a non-destructive RAW layer, with the RAW file either embedded (copied into your document) or linked (left in its original file location).
*   **Develop Assistant Settings** to control RAW processing behavior on loading the RAW image. (See [Settings for desktop](https://www.affinity.studio/help/workspace-settings/).) 
*   Tonal adjustments using the [Basic](https://www.affinity.studio/help/panels-raw-panel-basic/) and [Tones](https://www.affinity.studio/help/panels-raw-panel-tones/) panels.
*   Sharpening and Noise adjustments using the [Basic](https://www.affinity.studio/help/panels-raw-panel-basic/) and [Detail](https://www.affinity.studio/help/panels-raw-panel-details/) panels.
*   Lens correction adjustments using the [Lens panel](https://www.affinity.studio/help/panels-raw-panel-lens/).
*   [Masks](https://www.affinity.studio/help/raw-using-masks-develop-studio/) for applying adjustments to specific brushed image regions.
*   Crop Tool for [cropping](https://www.affinity.studio/help/size-transform-cropping/) your image.
*   Blemish Removal Tool for [correcting image imperfections](https://www.affinity.studio/help/retouching-retouching-blemishes/).
*   [Focus panel](https://www.affinity.studio/help/panels-raw-panel-focus/).
*   [Scope panel](https://www.affinity.studio/help/panels-scope-panel/).
*   [Snapshots panel](https://www.affinity.studio/help/panels-raw-panel-snapshots/) for comparing different image processing settings.

At any point while working with an image or any selected pixel layer, you can switch to the Develop Studio to make use of its unique features.

The Develop Assistant Settings provides a choice between Apple (Core Image RAW) and Affinity engines for processing RAW images.

Apple's engine provides the benefits of predetermined behaviors for demosaicing, lens correction, noise reduction, cropping and more.

Affinity's engine allows for greater manual configuration. You can specify luma and chroma noise reduction separately or disable noise reduction altogether, override lens correction, and benefit from superior demosaicing.

Apple's engine crops to whatever aspect ratio was selected in camera and so was written into the image's metadata, even if the camera sensor's aspect ratio is different. Data outside of the crop area may be removed during RAW processing. The Affinity engine doesn't destructively crop images, so all sensor data remains available.

There are a variety of split view options available in the Develop Studio's View Tool which give you the opportunity of seeing how your processed image compares to the original raw data.

While applying adjustments, you can update the 'Before' and 'After' view to give you a more focused representation of the applied changes. Rather than comparing the processed image with the original raw data, you can sync the views so 'Before' adopts the current applied adjustments. The 'After' view continues to update as more adjustments are made.

An incorrect level of exposure within an image can lead to pixels 'falling out' of the viewable intensity range. This results in the loss of detail in areas of shadows, highlights, or midtones and is known as clipping.

In the Develop Studio, you have the ability to display **Clipped Shadows**, **Clipped Highlights** and/or **Clipped Tones** directly on the image. This can help you identify areas which need correcting as well as preventing overenthusiastic modifications which result in clipping. The Develop Studio remembers your choices for these options from the last time you used it, even when editing a different photo.

Focus Peaking provides a visual overlay that highlights areas of sharp focus in the image. By detecting contrast and edge detail, it allows you to quickly assess where focus has been achieved.

In the Develop Studio, you can enable **Focus Peaking**

![Image 2: Focus Peaking](https://images.ctfassets.net/3p2fxa94bzao/5MO22yxxotQ0LUieMia3K8/001c9db747c22fa865dd48af3611c1e2/focus_peaking.svg)

 to display colored overlays on regions of high detail. This helps confirm whether key subjects—such as eyes in portraits or important elements in a scene—are in focus before applying further adjustments.

Red, green, blue, yellow, and purple overlays are available from the feature’s drop-down. Choose a color that contrasts clearly with the image to help evaluate focus more accurately. The Develop Studio remembers your chosen overlay color for subsequent editing sessions.

This feature is only available in Affinity for desktop.

To develop RAW files faster, you may save previously modified panel settings as a **Preset** and then select it from the list in the panel. Each time you open a new RAW file, all panels reset to the **Default** state (no presets are applied).

Presets are available for the **Basic**, **Lens**, **Details** and **Tones** panels.

1.   Open a RAW image: the Develop Studio opens by default for RAW files. The studio will analyze the data and pre-process it, ready for editing.*
2.   On the context toolbar, activate your preferred view mode.
3.   Adjust the image using the various panel options and RAW tools.
4.   (Optional) Sync applied settings within the view and repeat the above step.
5.    On the context toolbar, select an **Output** option. Choose from: 
    *   **Pixel Layer**—output will be destructive; a pixel layer is created from your developed RAW image.
    *   **RAW layer (Embedded)**—when developed, an editable non-destructive raw layer is created; the RAW image is copied into your document.
    *   **RAW layer (Linked)**—when developed, an editable non-destructive raw layer is created; the RAW image is kept in its original file location.

6.   If redeveloping a RAW image, if **Show All Layers** is checked above your workspace then all layers (e.g., adjustments or filters) applied in the Pixel Studio will be displayed if the RAW image is redeveloped. Uncheck to hide other layers.
7.   On the context toolbar, select **Develop**.

You need to decide on the **Output** option when you open your RAW file for the first time. Once set, it cannot be modified when you return to the Develop Studio.

*To alter the pre-processing for a RAW image, change the develop options available in the **Develop Assistant Settings**. (See [Settings for desktop](https://www.affinity.studio/help/workspace-settings/).)

When adjusting settings, you can double-click each adjustment slider to reset it to its default value.

1.   From tools, select the **White Balance Tool**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3eLlasmxSbwxcGXOjVEP30/e5e435e9799956b354718603b31e23f1/white_balance_tool.svg) .
2.   Zoom in, as required, to locate an area in the image that is closest to white.
3.   Click on the area.

The white balance will be set accordingly.

If the colors in your image appear off still, navigate to the **Basic** panel and adjust Temperature and Tint further to suit the required outcome.

1.   On the **Layers** panel, select an image layer.
2.   Do one of the following:
    *   With the **Move Tool**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg) active, on the context toolbar click **Develop.**
    *   **^(ctrl)**-click (Mac) / **right**-click (Windows) an image on the page and select **Develop**.

1.   Modify your develop settings, as required (Basic, Lens, Details or Tones panel).
2.   At the top of the panel, click **Default** and select **Add Preset** from the list.
3.   On the pop-up window, type a name for the preset and click **OK**.

On the Toolbar, do one of the following:

*   Click **Single View**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/64YJgmKSUbLdSuf5GsGqvK/db4f634044988a695cc7da9cde6a964b/standard_view.svg)  to display the processed image in isolation.
*   Click **Split View**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/SWhhcyi7P9xZaJXlyOFDE/56a0c275bb369631b3c5564fb9f24c83/split_view.svg)  to display both processed and original RAW image on the same page. A sliding divider can be repositioned to view the image 'Before' and 'After' processing.
*   Click **Mirror View**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3oYRYc43vhHLh1fSgVmMxu/7a99e5a811f9fe9ef886c16980d7b95b/mirror_view.svg)  to display processed and original RAW image side-by-side on separate pages. Panning and zooming affects both pages simultaneously so the same area is always displayed in both pages.

The output will adopt all the settings as displayed in the 'None' or 'After' view. The 'Before' view is for comparison purposes only.

On the Toolbar, do one of the following:

*   Click **Sync Before**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/4qGnijHjcPbYBF6PKJWX6b/a031862fb862b695b89363215dd89307/sync_before_develop.svg)  to update the 'Before' view to the most recent applied settings, i.e. those in the 'After' view.
*   Click **Sync After**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/1E4pwiAUoGrHvqKLdfZknN/c2507c4494dd30ddeb078f66c40f344e/sync_after_develop.svg)  to revert the settings applied in the 'After' view back to the settings shown in the 'Before' view.
*   Click **Swap**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/eET9eah4IyOH6j2H0osAG/63d45fa80cf4b0a27beb537e5105dfba/swap_develop.svg)  to switch the applied settings between the views.

On the Toolbar, do one of the following:

*   Click **Show Clipped Highlights**![Image 11](https://images.ctfassets.net/3p2fxa94bzao/6yVmnnwjh0HjAeRiqo5Jh1/947997e1084e5316c0ae86468dbc84f9/show_clipped_highlights.svg)  to display all 'blown' highlights as a high-contrast red color.
*   Click **Show Clipped Shadows**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/hz1W7gRPMocIkJ7TGTlVY/7f1c40c1fe31feda5c0d0d0591761028/show_clipped_shadows.svg)  to display all clipped shadow areas as a high-contrast blue color.
*   Click **Show Clipped Tones**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/6EEyFmuUJU0GHlsO4oAGL3/e98b9226e7895b02cc6b23b4e55060b3/show_clipped_tones.svg)  to display all clipped midtone areas as a high-contrast yellow color.

1.   On the Toolbar, click the **Develop Assistant Settings**![Image 14](https://images.ctfassets.net/3p2fxa94bzao/3dblKCXI1Zhj399vpvDUpl/1db708c27e6856384ee0357289430132/assistant_options.svg)  to open its settings dialog.
2.   Choose from the list, as required.
3.   Restart the app for the changes to take effect.

The chosen RAW Engine will be remembered the next time a RAW image is loaded.

If you choose not to apply initial develop settings, your images will not undergo any processing. They may look flat, dull in tone and lacking contrast, but you will have absolute control in how the image is processed.

Related behaviors can be adjusted from the app's settings:

*   **Assistant > Develop Assistant**.

*   [Develop Studio](https://www.affinity.studio/help/workspace-develop-studio/)
*   [Assistant Settings](https://www.affinity.studio/help/workspace-settings/)
*   [Using Masks (Develop Studio)](https://www.affinity.studio/help/raw-using-masks-develop-studio/)
*   [White Balance Tool (Develop Studio)](https://www.affinity.studio/help/tools-tools-white-balance/)

How would you rate the help you received from this article?
