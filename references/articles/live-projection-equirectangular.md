---
title: "Equirectangular projection - Affinity Help Center"
source: https://www.affinity.studio/help/live-projection-equirectangular/
slug: live-projection-equirectangular
fetched: 2026-08-06
---

# Equirectangular projection - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/live-projection-equirectangular/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Equirectangular projection

Equirectangular images, typically 360x180 panoramas, can be mapped to a live projection in Affinity and edited while they are being projected. This allows for instant feedback of detailed retouching, brush work and masking—all operations that would be difficult on an unmapped equirectangular image.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/6V1uOF6cBELSuFNu58JsD0/b8b41e4420e3e06693c394a7a371f282/feature_360_mapped01.jpg)

Projected image.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/3y1ClfENgPsmfrzIej7dIo/24a1659cab02de8e0d70d1971bf60b52/feature_360_unmapped01.jpg)

Unmapped equirectangular image (360x180).

360x180 imagery is often obtained either from dedicated 360 cameras, or by stitching a series of shots together using dedicated 360 stitching software.

1.   In the Pixel Studio ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , with an equirectangular image layer selected, from the **Pixel** menu, choose **Live Projection > Equirectangular**. The image layer will then enter live projection.
2.   Use the **Move Tool**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg) to pan around the image until you settle on an area you wish to edit.
3.   (Optional) Using the appropriate tools, make your edits.

1.   Do one of the following:

*   Select the **Move Tool**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg) , then from the context toolbar, select **Edit Live Projection**.
*   On the **Pixel** menu, choose **Live Projection > Edit.**

1.   While in live projection view, you can add content to the projected image such as text, images and brush work on new layers.
2.   Add your new layer content. For example, you could add some Text at the Nadir (bottom pole) with a copyright notice.
3.   Position and rotate the layer as you wish using the **Move Tool**. You can also match perspective by using the **Perspective Tool**.
4.   With the new layer selected, from the **Layer** menu, choose **Merge Down**. This will merge and rasterize the layer into the main equirectangular image layer.
5.   Once the content is merged, you can pan around the live projection by choosing the **Move Tool**, then selecting the **Edit Live Projection** from the context toolbar.

1.   In the Pixel Studio ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , while in live projection view, you will see **Straighten** on the context toolbar.
2.   To straighten the horizon of the the equirectangular image, either click inside the **Straighten** value box to set it manually, or use the slider.

1.   In the Pixel Studio ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , while in live projection view, you will see **Center Coordinate System** on the context toolbar.
2.   To change the middle origin point of the unmapped image, pan the view around and choose a new view point. Click **Center Coordinate System**, then from the **Pixel** menu, choose **Live Projection > Remove**.

The unmapped image's center point will now have changed.

This feature is only available in Affinity for desktop.

1.   Converting your image layer back to its original equirectangular mapping will allow you to export and share it—some image hosts support 360 image projection, or alternatively you can implement a Javascript/WebGL-based viewer on your own web pages if you wish.
2.   To clear the live projection, select your image layer, then from the **Pixel** menu, choose **Live Projection > Remove**.

How would you rate the help you received from this article?
