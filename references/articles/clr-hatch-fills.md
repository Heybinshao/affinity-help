---
title: "Hatch patterns - Affinity Help Center"
source: https://www.affinity.studio/help/clr-hatch-fills/
slug: clr-hatch-fills
fetched: 2026-08-06
---

# Hatch patterns - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/clr-hatch-fills/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Hatch patterns

A hatch pattern consists of a series of lines applied as an object's fill or stroke, which repeat in a tiled arrangement.

![Image 1: Example hatch patterns applied to the stroke and fill of an object.](https://images.ctfassets.net/3p2fxa94bzao/3zVJL27i1T3zXA15h1dMCK/e98ae9c3d3fa5a8bef667c02a4bf4f49/hatchPatternExample.png)

Hatch patterns applied to the stroke and fill of basic shapes.

Common uses of hatch patterns include adding shading and texture to illustrations and indicating building materials in CAD documents.

Affinity includes a _Hatches_ palette that contains a selection of useful patterns. It also has a built-in hatch pattern editor, which you can use to add and remove lines and control each line's position, angle, and line style.

Hatch patterns can be imported from AutoCAD .pat files. Each file creates a new palette on the Swatches panel.

Raster pattern libraries, which also use the .pat file extension, cannot be imported.

The Fill Tool’s context toolbar lets you adjust a hatch pattern’s scale, rotation, and line width. You can also change its fill and stroke colors, and reverse them instantly.

Anchoring a hatch pattern to the page lets you transform the object it's applied to, without affecting the pattern's position, rotation, and scale.

You can apply multiple hatch patterns to an object via the Appearance panel. To reveal background patterns, set any foreground patterns to have no Hatch fill color on the Fill Tool's context toolbar.

As well as layering hatch patterns in the panel, you can use a shortcut to rotate, scale, and set line widths for all patterns in one operation instead of affecting each pattern individually.

1.   Use the **Fill Tool**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/4AbVamuwkW3QLOJP3GQiV1/254daa0b4c76a58d6ef299e8068f0519/fill_tool.svg)  to select an object.
2.   On the context toolbar: 
    1.   Set **Context** to _Stroke_ or _Fill_ as needed.
    2.   Set **Type** to _Hatch_.
    3.   Do one of the following to set a hatch pattern: 
        1.   On the **Swatches** panel, select a built-in or imported hatch pattern. A Hatches palette is available to select from.
        2.   On the context toolbar, click the swatch, then use the hatch pattern editor to create a custom pattern.

If your fill doesn't display as you'd expect try adjusting the **Hatch scale** setting as it may be scaled up by default.

1.   To open the hatch pattern editor, do one of the following:
    *   Use the **Fill Tool**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/4AbVamuwkW3QLOJP3GQiV1/254daa0b4c76a58d6ef299e8068f0519/fill_tool.svg)  to select an object that uses a hatch pattern. On the context toolbar, set **Context** to _Stroke_ or _Fill_ as needed, then click the swatch.
    *   On the **Swatches** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) a hatch pattern swatch and select **Edit Fill**.

2.   On the editor, do any of the following: 
    *   To add a new line to the pattern, click **Add Line**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/665YKq8jcBR3ikEaRtacni/a988199c33634ac644564cddad8df35e/add_item.svg) .
    *   To select a line and highlight it on the preview, click it in the list.
    *   To edit a line's rotation, change the value in the **R** box, then press the **⏎** key (Mac) / **Return** key (Windows).
    *   To edit a line's position, change a value in the **X** or **Y** box, then press the **⏎** key (Mac) / **Return** key (Windows).
    *   To edit a line's style, click the arrow at the left of its list entry and change the following: 
        *   **Shift**—to adjust the relative starting position of each repeated line, for a staggered effect.
        *   **Spacing**—to adjust the spacing at which parallel lines repeat in the pattern. The value must be greater than zero.
        *   **Dash** / **Space**—to give the line a dot/dash line style. Use the summary below to edit the line style.

    *   To remove a line from the pattern, select it in the list, then click **Delete Line**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/3m8ciDtLqf07Yrma1i0j4x/202c1d508104bbb0a1290c5be7725eae/trash_can.svg) .

1.   Use the **Fill Tool**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/4AbVamuwkW3QLOJP3GQiV1/254daa0b4c76a58d6ef299e8068f0519/fill_tool.svg)  to select an object that uses a hatch pattern.
2.   On the context toolbar: 
    1.   Set **Context** to _Stroke_ or _Fill_ as needed.
    2.   Click **Reverse Gradient**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/0Z612ulJ7GvxqlmYLuqya/1b678b199f3a9148bdaefe9182deb1c5/fill_-_reverse_gradient.svg)  to swap the **Fill** and **Stroke** settings.

1.   Use the **Fill Tool**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/4AbVamuwkW3QLOJP3GQiV1/254daa0b4c76a58d6ef299e8068f0519/fill_tool.svg)  to select an object that uses a hatch pattern.
2.   On the context toolbar, set **Context** to _Stroke_ or _Fill_, as needed.
3.   Do one of the following: 
    *   To rotate by an arbitrary amount, either: 
        *   In the document view, drag an on-object rotation handle.
        *   On the context toolbar, type a value in the **Rotation** box, then press the **⏎** key (Mac) / **Return** key (Windows).

    *   To rotate in 90° intervals, click **Rotate**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/55L4Wf8nuqMLfvn64sMJ1r/b2a90b752d4dc14d3b56954753b4b490/fill_-_rotate_gradient.svg)  on the context toolbar.

When editing a hatch pattern, the following shortcuts can be used:

*   To rotate in 45° intervals, hold the **⇧** (Mac) / **Shift** key and drag an on-object rotation handle.

When working with multiple hatch patterns in the Appearance panel, use the following shortcuts:

*   To scale all fills simultaneously about the hatch origin, switch the **Caps lock** on and adjust **Hatch scale** on the Fill Tool's context toolbar.
*   To rotate all fills simultaneously about the hatch origin, switch the **Caps lock** on and adjust **Hatch rotation**.
*   To change all line weights simultaneously, switch the **Caps lock** on and adjust **Hatch line weight**.
*   Use **⌘⇪**(Mac) / **Ctrl+Caps lock** (Windows) to scale or rotate all fills about the currently selected fill's origin in the Appearance panel.
*   Use **⌥⇪**(Mac) / **Alt+Caps lock** (Windows) to set each hatch's scale or rotation to the same absolute value, scaled or rotated about its own origin.
*   Use the **⌘** key (Mac) / **Ctrl**key (Windows) to bake one line per hatch line with a dash pattern applied. Applies to a single hatch fill.
*   Use the **⇧** key (Mac) / **Shift** key (Windows) to bake one line per hatch line with a dash pattern applied, but to all selected objects.

*   [Fill Tool](https://www.affinity.studio/help/tools-tools-gradient/)
*   [Selecting colors](https://www.affinity.studio/help/clr-selecting-clr/)
*   [Transparency](https://www.affinity.studio/help/clr-transparency/)
*   [Dot/dash line styles](https://www.affinity.studio/help/curves-shapes-dot-dash-lines/)

How would you rate the help you received from this article?
