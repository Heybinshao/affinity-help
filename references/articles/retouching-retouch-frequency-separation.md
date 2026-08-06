---
title: "Frequency separation - Affinity Help Center"
source: https://www.affinity.studio/help/retouching-retouch-frequency-separation/
slug: retouching-retouch-frequency-separation
fetched: 2026-08-06
---

# Frequency separation - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/retouching-retouch-frequency-separation/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Frequency separation

Frequency separation allows you to retouch texture and tone/color independently for powerful portrait retouching.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/6DGFvlCOJsScCbf5NnQzQW/eb9ab0b0d38cd132c14f80d85c4882d7/frequency_separation_after.jpg)

After retouch on high and low frequency layers.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/6UBRqaKQfzMdgd8pTNA0Vs/7e1a222671e34ba029f615c54c096604/frequency_separation_before.jpg)

Before retouch on high and low frequency layers.

Although the term frequency separation is initially intimidating, the concept is straightforward. By automatically separating your image color/tone and texture into separate low and high frequency layers, respectively, you'll be able to retouch color/tone and texture independently. This means you can target skin imperfections, such as uneven color, blemishes and texture.

*   _Skin tone and color_ (shadows, blotches, etc.) are made smoother by blurring with the Dodge or Blur Brush Tool. The Healing Brush Tool also works well here.
*   _Unwanted textures_ (spots, stray hair, blemishes, dimples, and wrinkles) can be removed with the Clone Brush Tool or Blemish Removal Tool.
*   Blown out highlights can be treated by painting over using a sampled skin color.

In frequency separation, a blur filter and High Pass filter (Linear Light blend mode) are applied to created low and high frequency layers, respectively.

Frequency separation is also available as a tool in the Retouching Studio

![Image 3: Retouching Studio](https://images.ctfassets.net/3p2fxa94bzao/55Tejv2qP2VzWf3iD9YFZT/7c2a5b825dd1a0d393aa1c9073992306/retouching_studio.svg)

.

1.   On the **Pixel** menu, select **Filters >****Frequency Separation**.
2.   Drag on either high or low pass preview panes, to set the **Radius** (or use the slider in the dialog); this sets the balance between texture and tone. Set the value so the image's Low Frequency preview blends image color and tone but without losing major features within it.
3.    (Optional) From the dialog, choose a **Method** to blur the low frequency layer: 
    *   Gaussian (Default): this offers a smooth blur using a weighted average.
    *   Median: this blurs by broadening color regions; it retains edges better than Gaussian blur.
    *   Bilateral: this blurs while retaining areas of high contrast at image edges. Use the **Tolerance** slider with this blur to control how much major features are preserved when applying subsequent brush strokes.

Use selection tools and masking on both frequency layers just as with other layers.

Press the **F** key to switch from the High frequency layer to the Low frequency layer (and vice versa).

1.   On the **Layers** panel, select the Low Frequency layer.
2.   Apply retouch tools to the layer as appropriate.

1.   On the **Layers** panel, select the High Frequency layer.
2.   Apply retouch tools to the layer as appropriate.

1.   On the **Layers** panel, select the Low Frequency layer.
2.   From tools, select the **Paint Brush Tool** and set its blend mode to **Darker Color** and a low **Flow**.
3.   Sample a skin color to apply onto the clipped tones.
4.   Paint over the areas of clipped tones.

*   [Retouching](https://www.affinity.studio/help/retouching-retouch/)
*   [Retouching Studio](https://www.affinity.studio/help/workspace-retouching-studio/)

How would you rate the help you received from this article?
