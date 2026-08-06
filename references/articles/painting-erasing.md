---
title: "Erasing - Affinity Help Center"
source: https://www.affinity.studio/help/painting-erasing/
slug: painting-erasing
fetched: 2026-08-06
---

# Erasing - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/painting-erasing/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Erasing

You can erase areas of a pixel or container layer using a combination of the Erase Brush Tool, the Brushes panel and the tool's context toolbar.

Alternatively, you can use the [Background Erase Brush](https://www.affinity.studio/help/tools-tools-background-erase-brush/) or the [Flood Erase Tool](https://www.affinity.studio/help/tools-tools-flood-erase/) to remove pixels from a layer.

![Image 1: Erasing examples](https://images.ctfassets.net/3p2fxa94bzao/S5IFOaeNmscWoToBstcyO/59e325e56dcb8bf89789fc8008bf5422/pixelerasing.png)

Use of Erase Brush Tool, Background Erase and Flood Erase Tools.

If you're working on a pixel layer, you can use the **Erase Brush Tool** to erase unwanted pixels directly on the layer.

The **Background Erase Brush Tool** takes a sample of the color under the cursor when you begin to erase, and will remove all closely matching colors along the stroke.

The **Flood Erase Tool** removes areas of the layer based on the color selected using a powerful tolerance setting.

The **Flood Erase Tool** is only available in Affinity for desktop.

1.   In the Pixel Studio ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Erase Brush Tool**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/1JePHOcZPgb6CwwmJi5c2b/14ccdc5a1fa7208f58fb9d35b264b302/eraser_tool.svg) .
2.   From the Brushes panel, select a brush of your choice.
3.   Adjust the brush size and other brush-related properties from the context toolbar above your workspace.
4.   Paint on the page in the direction that you want the erase brush stroke to follow.

1.   On the **Layers** panel, select a layer. (If you select a vector object or container layer, it will be automatically rasterized when the tool is used.)
2.   In the Pixel Studio ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Background Erase Brush**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/qVXPS6ANyBsLqEXAcfKu2/b978da6518719f8dba41410aaeb85237/background_eraser_tool.svg)  from the **Erase Brush Tool** flyout.
3.   On the **Brushes** panel, select a brush of your choice.
4.   Adjust the context toolbar settings.
5.   Place the cursor over the color you want to erase in the image and drag within the image to erase the targeted color beneath the brush cursor.

1.   On the **Layers** panel, select a pixel layer.
2.   In the Pixel Studio ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select **Flood Erase Tool**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/3Ojlm9AUrsMcrOb267zl70/ff4cce0f7f55874521811253d0e415f7/flood_eraser_tool.svg)  from the **Erase Brush Tool** flyout.
3.   Adjust the context toolbar's **Tolerance** setting to control the extent of flood erasing across pixels. Experimenting will produce labor saving results.
4.   Click on the image to select the target pixel.

Pixels don't exist on a vector layer so a pixel mask is created and applied to the vector layer instead; the vector layer remains unaffected. By painting with raster brushes directly on the mask, you can decide what can be shown or hidden on the underlying vector layer.

1.   From the Layers panel, select the container layer (containing vector objects), a group or vector object contained within it.
2.   In the Pixel Studio ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , select the **Erase Brush Tool**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/1JePHOcZPgb6CwwmJi5c2b/14ccdc5a1fa7208f58fb9d35b264b302/eraser_tool.svg) . The tool uses a soft-round brush by default.
3.   To use a different brush style, choose one from the **Brushes** panel.
4.   On the context toolbar, change the brush values as desired.
5.   Paint on the container layer, group or vector object to erase.

On the Layers panel, you'll notice a vector mask thumbnail appear next to the layer, group or object. While this remains selected you can continue erasing.

If you're working with vector brush strokes created using the [Vector Blob Brush Tool](https://www.affinity.studio/help/tools-tools-vector-blob-brush/)

![Image 10: Vector Blob Brush Tool](https://images.ctfassets.net/3p2fxa94bzao/nrJCkCoRO79eiVU2vINfL/08fa9f4d8368f2ed3df19b6b872cf36e/vector_blob_brush_tool.svg)

, you can erase directly from the resulting vector shapes using the **Vector Erase Brush Tool**

![Image 11: Vector Erase Brush Tool](https://images.ctfassets.net/3p2fxa94bzao/3pjH11yVYnAbdb0ndZSITM/5a997ebe1936da03c279ccd4fcf2bdd5/vector_erase_brush_tool.svg)

. Unlike the Erase Brush Tool, this approach removes vector content without creating a pixel mask, so your artwork remains fully vectorized.

1.   On the **Layers**panel, select the layer containing your vector brush strokes.
2.   Select the **Vector Erase Brush Tool**![Image 12: Vector Erase Brush Tool](https://images.ctfassets.net/3p2fxa94bzao/3pjH11yVYnAbdb0ndZSITM/5a997ebe1936da03c279ccd4fcf2bdd5/vector_erase_brush_tool.svg) .
3.   Adjust the brush size and other settings from the context toolbar.
4.   Paint over the vector brush strokes you want to remove.

The erased areas are removed directly from the vector shapes — no mask is created and the artwork remains fully vectorized.

*   **Assistant > Erasing from vector layers**—optionally rasterizes the layer, group or object completely (flattening the layer) and erases or takes no action (preventing erasing from occurring).

*   [Erase Brush Tool](https://www.affinity.studio/help/tools-tools-erase-brush/)
*   [Background Erase Brush](https://www.affinity.studio/help/tools-tools-background-erase-brush/)
*   [Vector Erase Brush Tool](https://www.affinity.studio/help/tools-tools-vector-erase-brush/)
*   [Vector Blob Brush Tool](https://www.affinity.studio/help/tools-tools-vector-blob-brush/)
*   [Brushes panel](https://www.affinity.studio/help/panels-brushes-panel/)
*   [Painting pixel brush strokes](https://www.affinity.studio/help/painting-raster-painting/)
*   [Assistant Settings](https://www.affinity.studio/help/workspace-settings/)

How would you rate the help you received from this article?
