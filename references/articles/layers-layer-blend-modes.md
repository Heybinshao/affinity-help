---
title: "Layer blend modes - Affinity Help Center"
source: https://www.affinity.studio/help/layers-layer-blend-modes/
slug: layers-layer-blend-modes
fetched: 2026-08-06
---

# Layer blend modes - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/layers-layer-blend-modes/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Layer blend modes

A layer's blend mode determines how the layer or object's pixels blend with the pixels on the layer beneath.

![Image 1: Blend Modes](https://images.ctfassets.net/3p2fxa94bzao/6bDF9Pgx9WWKlxKlsPvbOl/69587fd1582784b3560333a5905f705a/layer_blending.png)

Common blend modes: (A) Normal, (B) Multiply, (C) Screen, (D) Overlay, (E) Divide (F) Color Burn.

Affinity supports an impressive selection of different blend modes. They are organized in their respective groups, which initially inform of the effect they add. They are as follows:

The default and starting mode for layers. It results in fully opaque pixels appearing above the underlying pixels. Use to completely cover the underlying layer's content.

![Image 2: Normal blend mode](https://images.ctfassets.net/3p2fxa94bzao/jrVnaYU9MLP4aWoNA5KLW/6b6a04cbcaa162f5b408ea6c31c8f2cf/normal_triptych_test2.jpg)

This mode allows for natural and life-like preview of mixing primary colors. It is particularly useful in digital painting where faithful results are key.

![Image 3: Pigment blend mode after](https://images.ctfassets.net/3p2fxa94bzao/5Wv9VVFdekTkEKKkbRV5nW/27500cd3236f83f6129db386cdec836f/pigmentBlendMode_after.jpg)

After applying the Pigment blend mode to primary colors.

![Image 4: Pigment blend mode before](https://images.ctfassets.net/3p2fxa94bzao/41JsIXvwVQEk4WVcJSBWqa/184e931bd54675f4ebeee3f85ab315e0/pigmentBlendMode_before.jpg)

Before applying the Pigment blend mode to primary colors.

When using blend modes from the Darken group, the resulting colors and tones are typically darker than both the base and blend layers.

Compares pixels of the active vs the underlying layer(s) and leaves darker pixels visible. Use to create dramatic, moody atmosphere.

![Image 5: Darken blend mode](https://images.ctfassets.net/3p2fxa94bzao/7FrfdTyQESeQlh7m9XnvrP/0f4783c2f31343be25750cfebae698de/darken_triptych_test.jpg)

One of the most frequently used blend modes in the group. Each pixel of the active layer is multiplied with the pixels of the layer(s) below. Bright pixels are ignored while darker ones are intensified. This results in a darker overall output when compared to the Darken blend mode. Use to create darker outputs with increased contrast.

![Image 6: Multiply blend mode](https://images.ctfassets.net/3p2fxa94bzao/3aKNaoo9pRvFgLbZMCbXRB/94d5180dd32292c2d8b1871a44310999/multiply_triptych_test.jpg)

Results in more saturated mid-tones and reduced highlights by intensifying contrast and the underlying layer's colors. Use to exaggerate colors and create highly contrasting scenes.

Color Burn isn't available in LAB16 mode.

![Image 7: Color Burn blend mode](https://images.ctfassets.net/3p2fxa94bzao/1g8my7GEfOqVU1wGKaCEjl/eca9279e4f7507717af1665b6131300a/colour_burn_triptych_test.jpg)

Results in darker output than with Multiply blend mode, yet less saturated than Color Burn. Lighter pixels of the active layer(s) are unaffected. This mode is ideal for rendering darker tones in the shadows and mid-tones.

![Image 8: Linear Burn blend mode](https://images.ctfassets.net/3p2fxa94bzao/3BqFBeZnEu1QjmGArvHkps/3c74918b5005fbc357f22c9b27a00782/linear_burn_triptych_test.jpg)

Compares the color values of the active and underlying layer(s) and only retains the darker ones. Use to accentuate the darker tones from both layers.

![Image 9: Darken Color blend mode](https://images.ctfassets.net/3p2fxa94bzao/1b2safGxA5ZUNnPyVfhn4O/3b1fcc7d60f927f01f709a499ad67590/darker_clr_triptych_test.jpg)

When applying blend modes from the Lighten group, the resulting colors and tones are generally lighter than both the base and blend layers.

Results in only the brighter values being retained upon comparing the active and underlying layer(s). Use to add complimentary color tint to images.

![Image 10: Lighten blend mode](https://images.ctfassets.net/3p2fxa94bzao/cZpm6zujBnceBl5Z6lRLk/6ba00465e39f4352344159fdd2e0f9ec/lighten_triptych_test.jpg)

Inverts colors of the underlaying layer(s) and multiplies it with those of the active layer: this results in generating smooth results. It is one of the most commonly used blend modes due to its soft rendering.

![Image 11: Screen blend mode](https://images.ctfassets.net/3p2fxa94bzao/4Z9DLxwpjVpRZNL44wiIOb/2607578b361778a74997d7867a841b4e/screen_triptych_test.jpg)

Increases the luminosity of the underlying layer(s) while reducing contrast between both the active and underlying layer(s). It results in a stronger effect than the one produced by Screen with saturated mid-tones and intense highlights. Use to accentuate color and highlights.

Color Dodge isn't available in LAB16 mode.

![Image 12: Color Dodge blend mode](https://images.ctfassets.net/3p2fxa94bzao/39jckB7zq9aggDZJv8qSJ2/9f292ca61c44716f4620bdf76e4f3a79/colour_dodge_triptych_test.jpg)

Results in added color information to both the active and underlying layer(s) and increases overall brightness while not affecting the black tones. Use to reveal brighter tones in images.

![Image 13: Add blend mode](https://images.ctfassets.net/3p2fxa94bzao/5Yx3s3kUxnX361jFrDArCP/d0b591df4edacbbfddc1644a3b00ba41/add_triptych_test.jpg)

Rather than looking at individual color, this mode uses perceived luminosity from all color channels to determine which pixel is lighter. It acts as an inverted luminosity mask. Use for faded looks and smooth rendition of highlights in outputs.

![Image 14: Lighter Color blend mode](https://images.ctfassets.net/3p2fxa94bzao/5tUTN7eaAvMwvlD29NG6JZ/02ae26d88a7c5003af057810a98f536c/lighter_colour_triptych_test.jpg)

Contrast blend modes analyze the base layer to see if its colors are darker or lighter than 50% gray, then blend accordingly. Colors at exactly 50% gray remain unchanged.

Compares the active and underlying layer(s) and shifts to darker mid-tones if the colors are lighter than 50% gray. Results in darkening the darker pixels of the images and lightening the lighter ones. Use to enhance contrast and saturation.

![Image 15: Overlay blend mode](https://images.ctfassets.net/3p2fxa94bzao/IYrz1JL7fABCXmuQqUbmT/103063f258774fb41e777dd4930de576/overlay_triptych_test.jpg)

Results in a more diffused effect from comparing luminance and color values between the active and underlying layer(s). Use for subtle blending and faded looks.

![Image 16: Soft Light blend mode](https://images.ctfassets.net/3p2fxa94bzao/57Tp7gnlpdppnh2BUlImvJ/a78780c516a296ead12a020375210cb7/soft_light_triptych_test.jpg)

Results in a dramatic, high-contrast effect. The top layer is used to determine the calculation required for the evaluation of pixels. Its effect can be observed as the opposite of the Overlay blend mode. Use to enhance color contrast and reduce opacity, as required, to achieve best results.

![Image 17: Hard Light blend mode](https://images.ctfassets.net/3p2fxa94bzao/6VaJkMX6as6LaKIXafjy7G/3d70082ce27b519172935e52a5a4515b/hard_light_triptych_test.jpg)

This blend mode applies the effect of the Color Burn or Color Dodge blend mode based on the comparison of RBG channels in the active (top) layer and underlying layer(s). Color Dodge is applied when the top layer image's values are lighter than mid-gray; Color Burn is applied when the top layer image's values are darker than mid-gray. Mid-gray serves as a neutral color, so any pixels with a gray value of 50% are not affected.

Results in increased contrast and highly saturated colors. Use to enhance contrast and color intensity, though best results are achieved with reduced opacity.

![Image 18: Vivid Light blend mode](https://images.ctfassets.net/3p2fxa94bzao/31kvqYMJek5st1UawQuqw4/6c71887e5c60f457ecba423a59fb072d/vivid_light_triptych_test.jpg)

Brighter pixels receive lighter treatment while darker ones get darkened. Results in a stronger contrast in the mid-tones. Use to create a dramatic, enhanced effect.

![Image 19: Lineal Light blend mode](https://images.ctfassets.net/3p2fxa94bzao/4gXcR5dxWirWoyGwWyIsVb/5f1f2d96e301ea68facd28d5476b3d33/linear_light_triptych_test.jpg)

Results can be compared to a mix of those achieved with the Darken and Lighten blend modes. This blend mode creates distinct boundaries between the dark and light regions. Use to achieve pronounced, yet somewhat faded look.

![Image 20: Pin Light blend mode](https://images.ctfassets.net/3p2fxa94bzao/30KUa8ShNuWRgSjWev8Ul5/2c9297ceb1d0145dca379661a848dd2d/pin_light_triptych_test.jpg)

Results in a highly-contrasting effect between pixels (modified by either 0 or 1). The effects can be attributed to the output often observed in comic books or posters where the increase in contrast accentuates colors. Use to posterize or to maximize color contrast.

![Image 21: Hard Mix blend mode](https://images.ctfassets.net/3p2fxa94bzao/50WFBhFMu9LpRAjUmrDP23/a8a8a035dc1edf55be76edea0366bce6/hard_mix_triptych_test.jpg)

Inversion blend modes adjust the base layer’s luminance by inverting it according to the luminance values of the blend layer.

Calculates the absolute difference between the active and underlying layer(s). When using this blend mode, similar values cancel each other out. Use to find errors in images.

Difference isn't available in LAB16 mode.

![Image 22: Difference blend mode](https://images.ctfassets.net/3p2fxa94bzao/3ETT7rq7AlnwbsrpDS4hgc/990b3fb95faea64637502c7904fdcdcf/difference_triptych_test.jpg)

Results in similar output to the above (Difference) mode, however with a softer effect. Use for soft blending of images consisting of similar luminance values.

Exclusion isn't available in LAB16 mode.

![Image 23: Exclusion blend mode](https://images.ctfassets.net/3p2fxa94bzao/5w99NSPJ5JlcEyqaGlbJWh/4a57044f716b39c8cf2b6c71da94d720/exclusion_triptych_test.jpg)

Subtracts the top layer's pixel values from the underlying layer, which results in lighter areas becoming brighter whereas the darker areas seeing little to no change. Use to remove or fade the active layer's colors and/or luminosity.

![Image 24: subtract blend mode](https://images.ctfassets.net/3p2fxa94bzao/3HFhTAfbufMhwTQhmwAjsn/c8e4a1a985e3ea40ead94d8ee85b17f6/subtract_triptych_test.jpg)

The underlying layers' pixel values are divided by those of the active layer, which usually results in brighter images. The effect of this blend mode is the opposite of the Subtract mode; darker color values create brighter results while brighter color values see little to no change. Use to simulate film negative look.

Divide isn't available in LAB16 mode.

![Image 25: Divide blend mode](https://images.ctfassets.net/3p2fxa94bzao/1zryV73zluaThCS0WKJZHI/b504b0bdb2b38a45fd737d0d93baf85f/divide_triptych_test.jpg)

Component group blend modes combine primary color components by blending each pixel’s red, green, and blue values separately, rather than adjusting the overall color.

Combine the hue of the active layer with that of the underlying layer(s). Use to exaggerate or create intense colors and to produce vivid, often surreal scenes.

Hue isn't available in Grayscale mode.

![Image 26: Hue blend mode](https://images.ctfassets.net/3p2fxa94bzao/45SV2mKGwQVGcDwgz2H9Ku/50b432e95d12e846923a11e199e47356/hue_triptych_test.jpg)

Similar to the Hue blend mode, however here Saturation is the replaced component. Depending on your images' saturation and colors, use this blend mode, as an alternative to the above, and to intensify and exaggerate colors.

Saturation isn't available in Grayscale mode.

![Image 27: Saturation blend mode](https://images.ctfassets.net/3p2fxa94bzao/7x3rmISnROLutCe598d5jm/39595ba568ac2cb9a23c1b4159666b07/saturation_triptych_test.jpg)

Combines the hue and saturation values of the active layer with the brightness of the underlying layer(s). Additionally, only the brightest colors of the underlying layer(s) are retained. Use to stylize images to produce scenes with intensified hue and saturation levels.

Color isn't available in Grayscale mode.

![Image 28: Color blend mode](https://images.ctfassets.net/3p2fxa94bzao/27VQvIfJwQm40ngbow7dUn/28551be0153e411e4843db9243ab075f/colour_triptych_test.jpg)

Combines the brightness values of the active layer with the brightness of the underlying layer(s). This blend mode's effect is the opposite of the Color blend mode — it retains the hue and saturation of the underlying layer(s). Use to add detail and textures where color information of the added image layer is less important.

![Image 29: Luminosity blend mode](https://images.ctfassets.net/3p2fxa94bzao/5O6S6SH4j0Xc1LTCX2JA68/80df7a7c80626912da6514690e63641a/luminosity_triptych_test.jpg)

A unique set of blend modes available as alternatives to the ones listed above and producing a range of distinctive outputs.

Combines the color and luminance values of the active and underlying layer(s) in producing a mean average. The result is similar to the one achieved by setting the active layer's Opacity to 50%. Use to simulate simple double-exposure images.

Average isn't available in LAB16 mode.

![Image 30: Average blend mode](https://images.ctfassets.net/3p2fxa94bzao/h6PtcbGq5QfFORR0RMi1b/dc1f46429841b605861c038119e63c3d/average_triptych_test.jpg)

Similar in effect to the Difference blend mode (Inversion group), which may be used as its alternative. Use to produce more contrasting and intense scenes; particularly powerful when working with selections and masking.

Negation isn't available in LAB16 mode.

![Image 31: Negation blend mode](https://images.ctfassets.net/3p2fxa94bzao/2QzKxY312afrjeidrTzhc8/d99b9f2ada96aa389c2358329bf37da9/negation_triptych_test.jpg)

Combines the effects of the Hard Light and Hard Mix blend modes (Contrast group) and produces images with preserved darker tones while enhancing the lighter ones. Use as an alternative to control image contrast; the method is particularly useful when combined with manipulating the source layer's graph to reduce highlights output via Blend Options.

Reflect isn't available in LAB16 color mode.

![Image 32: Reflect blend mode](https://images.ctfassets.net/3p2fxa94bzao/3AcOnCmOgQssB0CLhJxhRU/43cd785bb553b823d9abc8ce319f8f03/reflect_triptych_test.jpg)

The opposite of the Reflect blend mode, which produces images with preserved lighter tones (while enhancing the darker ones). As above, use to manipulate contrast and combine it with Blend Options for best outcomes.

Glow isn't available in LAB16 mode.

![Image 33: Glow blend mode](https://images.ctfassets.net/3p2fxa94bzao/yWIWEwJyzqQk5pWgnmElC/4d2df5e0794a89535da534204b890e68/glow_triptych_test.jpg)

Inverts pixel values depending on those of the underlying layer's content versus the active layer. Use to create effects similar to those of a two-tone color grade and posterization.

![Image 34: Contrast Negate blend mode](https://images.ctfassets.net/3p2fxa94bzao/IOfy6uW9VG6GEe5GO6PIb/2ef2d6b9a5dc617c9377878a1a58003e/contrast_negate_triptych_test.jpg)

Excludes pixels of the underlying layer. Use in combination with layer Opacity to produce faded and transparent outputs or to hide pixels from the layer(s) below the active one.

![Image 35: Erase blend mode](https://images.ctfassets.net/3p2fxa94bzao/5LzKY5N1LHT25dkDWHC10A/665d3a26983ed6911dd626fe91453400/erase_triptych_test.jpg)

Erase blend mode set to shapes (from left) at 25%, 50% and 75% Opacity over the base image.

Any layer or object can have a blend mode assigned, including mask and adjustment layers. The default blend mode is 'Normal'—no special compositing is applied. For a group, the default is 'Passthrough'. When set, the group itself has no special blend properties of its own, and passes on the blend mode of its parent layer.

Layer blend modes applied to child layers produce isolated blending which will not affect the parent layer or any other layers in the layer stack.

The same blend modes can be utilized on layer effects and pixel brushes.

When adjusting blend opacity, some blend modes (listed below) work best by adjusting **Fill Opacity**, rather than the layer's **Opacity**. The Fill Opacity option is available from the **Layers** panel’s **Blend Options** option. Fill opacity is essential when using Hard Mix blending in particular.

*   Color Burn
*   Linear Burn
*   Color Dodge
*   Add (Linear Dodge)
*   Vivid Light
*   Linear Light
*   Hard Mix
*   Difference

1.   On the **Layers** panel, select a layer (or object).
2.   Choose a blend mode from the pop-up menu on the panel.

*   With the **Move Tool**active and a layer selected on the Layers panel, press **⇧ + / -**keys (Mac) / **Shift**+ **+ / -**keys (Windows) to shuffle through the blend modes.

*   [Layer blend options](https://www.affinity.studio/help/layers-layer-blend-options/)
*   [Live Tone Blend Group adjustment](https://www.affinity.studio/help/adjustments-adjustment-live-tone-blend-group/)

How would you rate the help you received from this article?
