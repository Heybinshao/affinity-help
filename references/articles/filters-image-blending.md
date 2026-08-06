---
title: "Apply Image filter - Affinity Help Center"
source: https://www.affinity.studio/help/filters-image-blending/
slug: filters-image-blending
fetched: 2026-08-06
---

# Apply Image filter - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-image-blending/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Apply Image filter

Apply Image filter lets you composite images together on the same layer and use a number of expressions for advanced channel blending.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/3cYHNjsxuLyztDIxn4brJS/22ae8a018d659459888927f6e5d904f9/filter_applyimage_channel_after.jpg)

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/5zzWFFfVFBTpd2v60lEhF6/58fbe05f72675eae78106389290f071a/filter_applyimage_channel_before.jpg)

Apply Image filter lets you blend a layer from a source image into a target image's layer. The images are composited into a single layer. Channel expressions and blend modes are available to composite the layers.

The source image can be scaled automatically to the target image horizontally, vertically or both, avoiding having to size the images equally first.

Apply Image is also available as a tool in the Color Grading Studio.

1.   On the **Layers** panel, select the layer that you want to blend the source image with.
2.   On the **Pixel > Filters** menu, select **Apply Image**.
3.   Click **Load Image** and navigate to, then select the source image to import. If the image is another layer within your document, you can also drag it onto the dialog box to use it.
4.   (Optional) Check the **Equations** option in order to enable channel blending.
5.   (Optional) Set the **Opacity** level to control how transparent the imported image appears.
6.   (Optional) Select a **Blend Mode** to alter how the source image's colors blends with the target image. Select from the pop-up menu.
7.   (Optional) Uncheck **Scale Horizontal To Fit** to retain the imported images native width. When checked, the image is stretched/shrunk to the main image. Uncheck **Scale Vertical To Fit** to retain native height.
8.   Click **Apply**.

1.   With the **Apply Image** dialog open, either load an image or choose **Use Current Layer As Source** to blend the image with itself.
2.   Check the **Equations** option in order to enable channel blending.
3.   Choose a color space to blend in with the **Equation Color Space** pop-up menu.
4.    Now use the available expressions to blend channel information. Some expressions include: 
    *   Use **D**+**Channel** to specify a destination image channel (the original layer). E.g., **DB** for **Destination Blue** channel.
    *   Use **S**+**Channel** to specify a source image channel (the image you have loaded in). E.g., **SR** for **Source Red** channel.
    *   Use +, -, *, / to add, subtract, multiply or divide respectively. E.g., **SR/SG*SB** to divide **Source Red** by **Source Green** and then multiply by **Source Blue**.

*   [Applying filters](https://www.affinity.studio/help/filters-filters-applying/)
*   [Layer blend modes](https://www.affinity.studio/help/layers-layer-blend-modes/)
*   [Color Grading Studio](https://www.affinity.studio/help/workspace-color-grading-studio/)

How would you rate the help you received from this article?
