---
title: "Picture frames - Affinity Help Center"
source: https://www.affinity.studio/help/media-picture-frames/
slug: media-picture-frames
fetched: 2026-08-06
---

# Picture frames - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/media-picture-frames/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Picture frames

A picture frame reserves space in your document for content—usually an image. You can scale, position, and rotate the content to control which part is shown.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/FsXFkHMLC412zppBG9ri5/7ee06c28666c537bfdf5c0eeb931dfb7/pictureframe_after.jpg)

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/1QPPlZ4pwfOAjOA0vb24gM/99dd51482de0d4daf875d915da9a627d/pictureframe_before.jpg)

After adding a picture frame, you can reposition it, resize it, add borders, and change its shape and style.

You can place an embedded or linked resource inside the frame. The resource can be an Affinity-compatible image file, a PDF, an InDesign (IDML) document, or an Affinity document.

The frame's contents can be scaled according to one of three automatic behaviors, or panned, scaled, and rotated manually:

*   ![Image 3: Scale to Max Fit icon](https://images.ctfassets.net/3p2fxa94bzao/7gvA9iuxlzrd9SCyEQAh0o/f82e251f27a4d68b427a53970a5fad9e/scaletomaxfit.svg) **Scale to Max Fit**—The image is automatically scaled to fill the entire frame without distorting it. Some of its contents may be cropped. This behavior is the default when content is placed in a picture frame.
*   ![Image 4: Scale to Min Fit icon](https://images.ctfassets.net/3p2fxa94bzao/UwVQhuhDLLJpFCXYgdtuE/a7c3d1cb6806d701e5e24370b1670f3b/scaletominfit.svg) **Scale to Min Fit**—The image is automatically scaled to be completely visible within the frame. There may be empty areas down the left and right or across the top and bottom of the frame.
*   ![Image 5: Stretch to Fit icon](https://images.ctfassets.net/3p2fxa94bzao/6nBqZ5ABwY758SC1UplYrX/b0e95478111bc3aba3f71d0c2da7f404/stretchtofit.svg) **Stretch to Fit**—The image is automatically scaled to be completely visible and fill the entire picture frame. It may be noticeably distorted, depending on the relative proportions of it and the frame.
*   ![Image 6: None icon](https://images.ctfassets.net/3p2fxa94bzao/25jF3hlK3b1iEsxx5FXYk/daaaf2cb1f9eaea758ba1575d6702c4e/noscale.svg) **None**—The frame's content is not scaled dynamically as the frame is resized. This behavior is selected automatically when you use the frame's rotation, scaling, or position controls, or by double-clicking the frame and transforming the content directly.

![Image 7: Scaling frame content](https://images.ctfassets.net/3p2fxa94bzao/3Ivx7Z550w21ssBA4wz7vY/51aba908e1e2ec300464e0043d2af561/framecontent_scaling.jpg)

Examples of the various scale/stretch behaviors.

When you choose an automatic scaling behavior, its effect updates automatically if you later resize the picture frame. When **None** is selected, the size, position, and rotation of the framed content become independent of the frame's dimensions. No further automatic scaling is applied, but you can still make manual changes.

Pictures frames whose scaling method is set to **None** display an extra control handle at their bottom-right corner. Dragging this handle scales the frame and its contents together.

A picture frame, like any other object, can act as a **parent** clipping object for any number of **child** objects. In the case of picture frames, only one child object can be flagged as the “framed content”. The framed content is indicated on the **Layers** panel by a box and diagonal cross at the lower-right corner of its thumbnail.

The framed content scales according to the picture frame's set behavior. Other child objects scale normally and can use standard constraints. For example, this allows you to set up a frame with adornments or a watermark.

To add an object as framed content, drag its layer onto the picture frame's name on the **Layers** panel and drop when the frame's row is highlighted.

If a child object flagged as the frame's content already exists, it is replaced by the new object. This is equivalent to selecting the frame and choosing **Replace Image** on the context toolbar.

To add an object as a regular child object, expand the target picture frame's row on the **Layers** panel, drag the object's layer just below the target picture frame's row, and drop when a highlight line appears beneath the frame's layer name. You can add as many child objects as you like.

In the **Layout Studio**

![Image 8](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg)

:

1.   Select the **Picture Frame Rectangle Tool**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/146bEWkL7iva3iAHK7wM3v/e4b3a2f7664d2112b708aa32ef7f1134/box_picture_frame_tool.svg)  or the **Picture Frame Ellipse Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/2lDKQgB6l6nqENkD0vFebd/150333d4803347a819b2f16202e5a0ba/circle_picture_frame_tool.svg) .
2.   Do one of the following: 
    *   For precise _Data Entry_: **⌘**-click (Mac) / **Ctrl**-click (Windows) on the page, then enter your frame dimensions on the dialog that appears. Optionally, set an anchor point to position the frame in relation to the new anchor position, rather than the default or previously set anchor point. The last used settings will be remembered.
    *   For sizing _'by eye'_: Drag on the page to set the size and position of the picture frame, holding the **⇧** key (Mac) / **Shift** key (Windows) to constrain the frame's proportions to a square or circle if needed.

In the **Layout Studio**

![Image 11](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg)

, with the picture frame selected, do one of the following:

*   Select the **Place Tool**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/47Z9iHInfnQl0IelWGJTdH/a235b375a151ad38f5a59edbf4183bba/place_image_tool.svg) . On the dialog that appears, select a compatible file to place inside the picture frame.
*   Select the **Picture Frame Rectangle Tool**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/146bEWkL7iva3iAHK7wM3v/e4b3a2f7664d2112b708aa32ef7f1134/box_picture_frame_tool.svg)  or the **Picture Frame Ellipse Tool**![Image 14](https://images.ctfassets.net/3p2fxa94bzao/2lDKQgB6l6nqENkD0vFebd/150333d4803347a819b2f16202e5a0ba/circle_picture_frame_tool.svg) . On the context toolbar, select **Replace Image**![Image 15](https://images.ctfassets.net/3p2fxa94bzao/4NjS8BeqgOJiVWgmPimsZO/0cf8b6b3bfbcf15b99b9be62bb44ef76/place_image_tool_2.svg) .
*   Drag a compatible file from your operating system's file manager or an image from the **Stock** panel and drop it on the frame.
*    For a pixel selection copied to the Clipboard, **^(ctrl)**-click (Mac) / **right**-click (Windows) on the picture frame and select **Paste as Content**. 

In the **Layout Studio**

![Image 16](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg)

, do one of the following:

*   Select the **Move Tool**![Image 17](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg) , **Picture Frame Rectangle Tool**![Image 18](https://images.ctfassets.net/3p2fxa94bzao/146bEWkL7iva3iAHK7wM3v/e4b3a2f7664d2112b708aa32ef7f1134/box_picture_frame_tool.svg) , or **Picture Frame Ellipse Tool**![Image 19](https://images.ctfassets.net/3p2fxa94bzao/2lDKQgB6l6nqENkD0vFebd/150333d4803347a819b2f16202e5a0ba/circle_picture_frame_tool.svg) . In the document view, click the picture frame.
*   On the **Layers** panel ![Image 20](https://images.ctfassets.net/3p2fxa94bzao/6pK4M8wQgQfeJA5iUukqFw/87a5ff80aed81e1449c90447fc8385c4/layers_studio.svg) , click on the layer entry for the picture frame.

In the **Layout Studio**

![Image 21](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg)

, do one of the following:

*   Select the **Move Tool**![Image 22](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg) , **Picture Frame Rectangle Tool**![Image 23](https://images.ctfassets.net/3p2fxa94bzao/146bEWkL7iva3iAHK7wM3v/e4b3a2f7664d2112b708aa32ef7f1134/box_picture_frame_tool.svg) , or **Picture Frame Ellipse Tool**![Image 24](https://images.ctfassets.net/3p2fxa94bzao/2lDKQgB6l6nqENkD0vFebd/150333d4803347a819b2f16202e5a0ba/circle_picture_frame_tool.svg) . In the document view, double-tap the picture frame.
*   On the **Layers** panel ![Image 25](https://images.ctfassets.net/3p2fxa94bzao/6pK4M8wQgQfeJA5iUukqFw/87a5ff80aed81e1449c90447fc8385c4/layers_studio.svg) , click Expand ![Image 26](https://images.ctfassets.net/3p2fxa94bzao/1Ddu0OMS1hpMeFSbSvSbT5/c2afd02a205615b19cbaa4ede913dacc/singlearrowright.svg)  on the picture frame's layer entry, then click on the entry for the framed content.

With the picture frame selected, do one of the following:

*   To scale the placed content as required, click **Properties**![Image 27](https://images.ctfassets.net/3p2fxa94bzao/6E6WUnfl7NeOCYHluZnc1A/8c9e479415e9d8dc213cf0166e5e6548/pictureframeproperties.svg)  on the context toolbar and choose one of the automatic scaling behaviors or **None**.
*   Use the Scaling slider below the frame to zoom in or out. The scaling percentage on the slider is relative to the image's native dimensions.![Image 28: Zooming frame content](https://images.ctfassets.net/3p2fxa94bzao/30PESNItrozERGnurtg8az/d3da1c264cc336b22118b8b1a4a4743e/framecontent_zooming.jpg) 
*   To reposition the content within the frame, drag the pan control (arrowed icon) that's shown in the center of the frame when you hover over it.![Image 29: Panning frame content](https://images.ctfassets.net/3p2fxa94bzao/6odhSaG5wa8FRl0sGmtW3X/f6935b5cc398b9d181ce07a88079b0ee/framecontent_panning.jpg) 
*   To rotate the framed content, drag left/right over the rotate icon (a circular arrow) that's shown near the top-center of the frame when you hover over it.![Image 30: Rotating frame content](https://images.ctfassets.net/3p2fxa94bzao/5hILHTyG6xUzBC5QD2W4gv/0efc8e7324f304ae9750da627f58c962/framecontent_rotating.jpg) 

After you reposition or rotate framed content, you may need to scale the content if its edge has been exposed in the frame.

Double-clicking the framed content will select it rather than the picture frame. This lets you resize the content using its bounding box's edge and corner handles, and reposition it by dragging.

Do one of the following before resizing the frame:

*   Select the picture frame and then check **Lock Children** on the context toolbar.
*   Select the picture frame, select **Properties** on the context toolbar, and then choose **None**, ensuring the anchor point is set as needed.

To match a common aspect ratio, enter an expression on the **Transform** panel. For example, to size a frame to 3:2 aspect ratio, select it, ensure the adjacent Link symbol is disabled, then enter w/3*2 into the panel's **H** (Height) field.

1.   Select the picture frame.
2.   On the context toolbar, select **Size Picture Frame to Content**![Image 31](https://images.ctfassets.net/3p2fxa94bzao/5sRu6KkKgkCGsoZOgJzL33/b4345dc2eb42874209e634937cfb4569/pictureframesizetocontent.svg) .

1.   Select the shape or path.
2.   On the **Layer** menu, select **Convert > To Picture Frame**.

As well as standard shapes, you can also convert abstract shapes created from Boolean geometry operations to picture frames.

With the **Move Tool**

![Image 32](https://images.ctfassets.net/3p2fxa94bzao/3oigj5SSoPtnSw21egHEvD/b6ac975f2be7b3feb8e3e9867b378345/move_tool.svg)

 selected:

1.   Double-click the framed content to select it.
2.   On the context toolbar, click **Edit Image**.

Applies only to images that are linked resources.

*   [Picture Frame Rectangle Tool](https://www.affinity.studio/help/tools-tools-picture-frame-rectangle/)
*   [Picture Frame Ellipse Tool](https://www.affinity.studio/help/tools-tools-picture-frame-ellipse/)
*   [Place Tool](https://www.affinity.studio/help/tools-tools-placeimage/)
*   [Embedding vs linking](https://www.affinity.studio/help/media-embedding-vs-linking/)
*   [Color management](https://www.affinity.studio/help/clr-clr-profiles/)

How would you rate the help you received from this article?
