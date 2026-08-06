---
title: "Pixel selections from layers - Affinity Help Center"
source: https://www.affinity.studio/help/selections-pixel-selections-fromlayers/
slug: selections-pixel-selections-fromlayers
fetched: 2026-08-06
---

# Pixel selections from layers - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/selections-pixel-selections-fromlayers/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Pixel selections from layers

You can create pixel selections based on layers, layer groups or layer luminosity.

![Image 1: Selection from layer](https://images.ctfassets.net/3p2fxa94bzao/iv9H1wu7G5dIz16IhV2sI/3fb01aa44478029e5adee47b7766fcae/selection_from_layers.jpg)

Example of a pixel selection from layer intensity (luminosity).

If the layer or layer group contains areas which have an opacity lower than 100%, these are partially selected. This partial selection is based on the percentage of their opacity (i.e., the areas of 20% opacity will be selected by 20%). Transparent areas will not be included in the selection.

A pixel selection can also be created from a layer’s intensity, or luminosity. This uses the brightness values in the selected layer to determine the selection strength: lighter areas are selected more strongly, darker areas are selected less strongly, and black areas are not selected. This is useful when you want to target highlights, shadows, or tonal detail from an existing layer without manually painting or drawing a selection.

A selection marquee only appears around the areas which are selected by more than 50%. The areas selected by 50% or less will not display a marquee at their edges.

Pixel selections can be based on a number of factors. In Affinity, you can make selections based on:

*   Layer content.
*   Tonal Range.
*   Hue Range.
*   Transparency Range.

When you create a selection from layer intensity, Affinity analyses the brightness of each pixel in the layer and uses that to determine how strongly each pixel is selected. Brighter pixels are selected more strongly; darker pixels are selected less — or not at all.

To calculate brightness, Affinity uses a perceptual weighting that reflects how the human eye responds to color: green light appears much brighter to us than red, and red much brighter than blue. This means that a pure green pixel is treated as very bright (around 59% selected), a pure red pixel as moderately bright (around 30% selected), and a pure blue pixel as quite dark (around 11% selected) — even though all three colors appear equally "mid-toned" in standard color models like HSL.

The term _luminosity_ here refers to perceptual brightness — a weighted calculation based on how sensitive the human eye is to each colour channel. This is different from the Luminosity (L) value in HSL colour definitions, where pure red, green, and blue are all considered equally bright (50%). In this context, those three colours produce very different selection strengths.

Unlike a standard selection where pixels are either fully selected or not, an intensity-based selection can partially select pixels. A pixel selected at 50% is "half selected" — painting or erasing over it will apply your tool at half strength, and multiple passes are needed to fully affect it.

The marching ants outline only appears around areas where pixels are **50% selected or more**. Pixels below that threshold are still part of the selection — they just won't show the ants boundary. This can make it look as though only some areas were selected when others were actually included at a lower strength.

For example: if your layer contains pure green, red, and blue areas, the marching ants will appear around the green pixels only. But the red and blue areas are selected too — just at around 30% and 11% respectively.

Do one of the following:

*   On the **Layers** panel, select a layer. On the **Pixel** menu, select **Pixel Selection > From Layer**.
*    On the **Layers** panel, click the chosen layer's thumbnail while pressing the **⌘** key (Mac) / **Ctrl** key (Windows). 

Do one of the following:

*   On the **Pixel** menu, choose **Pixel Selection > From Layer Intensity**.
*    On the **Layers** panel, click the chosen layer's thumbnail while pressing the **⌥⌘⇧** keys (Mac) / **Alt**+**Ctrl**+**Shift** keys (Windows). 

*   On the **Layers** panel, click the chosen layer's thumbnail while pressing the **⇧⌘** keys (Mac) / **Shift**+**Ctrl** keys (Windows). 

*   On the **Layers** panel, click the chosen layer's thumbnail while pressing the **⇧⌥⌘** keys (Mac) / **Shift**+**Alt**+**Ctrl** keys (Windows). 

1.   On the **Layers** panel, select a pixel layer.
2.   On the **Pixel** menu, choose **Pixel Selection** and select an option.

*   [Creating pixel selections](https://www.affinity.studio/help/selections-selections-create/)
*   [Modifying pixel selections](https://www.affinity.studio/help/selections-selections-modify/)
*   [Refining pixel selection edges](https://www.affinity.studio/help/selections-selections-refine/)
*   [Range pixel selections](https://www.affinity.studio/help/selections-selections-range/)
*   [Sampled color pixel selections](https://www.affinity.studio/help/selections-selections-sampled/)

How would you rate the help you received from this article?
