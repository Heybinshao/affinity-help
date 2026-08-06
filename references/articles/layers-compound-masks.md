---
title: "Compound layer masks - Affinity Help Center"
source: https://www.affinity.studio/help/layers-compound-masks/
slug: layers-compound-masks
fetched: 2026-08-06
---

# Compound layer masks - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/layers-compound-masks/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Compound layer masks

Instead of working on a single mask layer, **compound masks** let you combine multiple mask layers non-destructively using Boolean operations (add, subtract, etc.), and then edit each 'component' mask layer independently of each other.

![Image 1: Compound mask](https://images.ctfassets.net/3p2fxa94bzao/7M1Zv9NRYlLYH8dGFbFs0H/0556e91ab89c96c825b77ab1a5d72628/compound_mask.jpg)

Compound mask (C-M1) made up of three separate mask layers (m1, m2 and m3); Add Boolean operations were used in the compound.

**Compound masks** offer powerful masking that uses the same Boolean operations used in vector-based graphic design (i.e., add, subtract, intersect or xor) but are instead applied to multiple mask layers non-destructively, i.e. without altering the individual mask layers.

Use compound masks for compositing and editing of complex textures, where you can combine more complex and diverse multiple masks. This gives a lot of flexibility as you can introduce different masking approaches and bring them together, e.g. a gradient mask layer combined with a painted mask layer.

Like other layers, any mask layer in the compound can be switched on/off, moved to another position on the layer stack or have its layer properties (e.g., opacity) altered.

Compound masks only work with more than one mask layer present.

Do one of the following:

*   On the **Layers** panel, **⌥**-click (Mac) / **right**-click (Windows) on **Mask Layer**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/r2qPaYMZu1PUwNoo8Bluy/10da3cdaad29dff22d89069363829214/mask_layer_type.svg) , then select **Compound Mask**.
*   On the **Pixel** menu, select **New Mask Layer > Compound Mask Layer**.

If there is a pixel layer previously selected, the compound mask will be clipped to that layer. When no layer is selected, it will be added to the top of your layer stack. You can drag the compound mask layer to a new position if needed.

*   On the **Layers** panel, drag the mask layer(s) over the compound mask layer entry and release.

The addition of multiple mask layers will create the compound, using an Add operation by default.

*   Create an empty compound mask as before.
*   Select a layer which you want make a pixel selection on, then create a pixel selection.
*   Select the compound mask layer, then select **Pixel > New Mask Layer > Mask Layer**.
*   Repeat to build up multiple masks in the same compound masks.

You can create masks from pixel selections made from channel information (e.g. targeting the Red channel) and add them to your compound mask as above. Similarly, you could target luminosity in your image for compound masking.

1.   On the topmost layer mask within the compound mask, click the mode icon.
2.   Select a different compound mode from the pop-up menu—choose from **Add**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/4te5ffuV7wlxfLHZjXBYE3/f298c15617667ceaccc59fc7dea44ef2/add.svg) , **Subtract**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/78M32Z31jTOkYaHWxegJxj/2a64fc0c16a52868678cbfe53c6f4a34/subtract.svg) , **Intersect**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/6G1NAmj6MzCJXPT8lRurlW/3a85ee7d014cb268e5c2a732cc8f9b19/interesect.svg)  or **Xor**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/5PMX28cvECFZr0WBI5g2Qw/cdaaf4d90c20d9ec601f121bf45ad9ae/combine.svg) .

Do one of the following:

*   Drag the mask layer out of the Compound Mask layer to another layer position.
*   **^(ctrl)**-click (Mac) / **right**-click (Windows) the compound mask layer, and from the menu, choose **Release**. 

The following modifier keys can be used on mask layers in the compound mask:

*   To view in isolation, hold down the **⌥** key (Mac) / **Alt** key (Windows) and click on the mask thumbnail of the layer in the **Layers** panel.

*   [Layer masks](https://www.affinity.studio/help/layers-layer-masks/)
*   [Creating compounds](https://www.affinity.studio/help/object-control-compound/)
*   [Using channels](https://www.affinity.studio/help/channels-using-channels/)

How would you rate the help you received from this article?
