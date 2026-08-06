---
title: "Expressions for field input - Affinity Help Center"
source: https://www.affinity.studio/help/workspace-expressions/
slug: workspace-expressions
fetched: 2026-08-06
---

# Expressions for field input - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/workspace-expressions/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Getting started](https://www.affinity.studio/help/getting-started/)
3.   Expressions for field input

Instead of adding absolute values into input fields, you can add expressions. These allow you create new values based on percentages, mathematical symbols, and another field's value.

You can mix units of measurement in an expression. Affinity handles conversion automatically.

The expression or variable presented after the comma can be used as alternative, often shortform, versions of the expression or variable.

When adding an expression into a field, the following colors may appear, providing feedback on the validity of the expression:

*   Red—this denotes an error (examples include unrecognized units, unexpected character, unexpected token, unknown keyword, incomplete argument)
*   Green—the variable has been recognized
*   Orange—valid input awaiting Return key

Use throughout the user interface but typically:

*   When resizing a document via **Document > Setup > Document Setup**.
*   Transforming one or more selected objects via the **Transform** panel*.
*   Increasing stroke width on one or more selected objects via the **Stroke** panel*.

* Individual objects in multiple selections will be sized based on their own values, not those of other objects.

| Input | Result |
| --- | --- |
| +=20 | Increase value by 20. |
| -=20 | Decrease value by 20. |
| *2 | Double size. |
| /2 | Divide in half. |
| 50%, *0.5 | Decrease by half. |
| 120%, *1.2 | 20% bigger. |

Use when resizing a document or transforming an object via the **Transform** panel.

| Input | Result |
| --- | --- |
| w+20 | Scales based on addition of other input value. _Example entered into Height box to set height as width plus 20 pixels._ |
| w-20 | Scales based on subtraction of other input value. _Example entered into Height box to set height as width minus 20 pixels._ |
| 2*w | Scaling based on a multiple of other input value. _Example is entered into Height box to set height to double the width._ |
| w/2 | Scaling based on a division of other input value. _Example entered into Height box to set height to half the width._ |
| w/3*2 | Scaling based on a division of other input values. _Example entered into Height box to divide the width of an object by 3 multiplied by 2. Good for resetting accidentally squashed images (from 35mm camera) or picture frames to 3:2 aspect ratio._ |
| w/4*3 | Scaling based on a division of other input values. _Example entered into Height box to divide the width of an object by 4 multiplied by 3. Good for resetting accidentally squashed images (from micro four-thirds/compact camera) or picture frames to 4:3 aspect ratio._ |
| sqrt(w) | Scales based on the square root of other input value. _Example entered into Height box to set height as the square root of the width._ |
| w^3 | Scales based on a power of other input value. _Example entered into Height box to set height as the width to the power of three._ |
| 12pt / x | Sets the text's x-height to 12pt. |

For general use throughout the user interface.

| Input | Constant |
| --- | --- |
| pi, π | For Pi |
| phi, gr, φ | For golden ratio |
| root2, rad, rt | For Pythagoras’s constant |
| e | Euler’s constant |

Use when moving, scaling, rotating or shearing objects via the **Transform** panel.

| Input | Variable |
| --- | --- |
| xposition, x | X position |
| yposition, y | Y position |
| width, w | Width |
| height, h | Height |
| rotation, r | Rotation |
| shear, s | Shear |

Use when setting dimensions using the New Document or Document Setup dialogs.

| Input | Variable |
| --- | --- |
| spreadwidth, w | Document width |
| spreadheight, h | Document height |
| marginleft, l | Left document margin |
| marginright, r | Right document margin |
| margintop, t | Top document margin |
| margin, b | Bottom document margin |

Use when setting the size of text.

| Input | Variable |
| --- | --- |
| xheight, x | X-height |
| ascent, a | Ascent |
| capheight, c | Cap height |

Use when sizing and positioning content using the **Transform** panel in relation to the document (i.e. page spread).

| Input | Variable |
| --- | --- |
| spreadwidth, sprw, sw | The width of the current spread |
| spreadheight, sprh, sh | The height of the current spread |
| spreadleft, sprl, sl | The position of the left edge of the current spread |
| spreadright, sprr, sr | The position of the right edge of the current spread |
| spreadtop, sprt, st | The position of the top edge of the current spread |
| spreadbottom, sprb, sb | The position of the bottom edge of the current spread |
| marginsizeleft, mgnszl, msl | The size of the left margin on the current spread |
| marginsizeright, mgnszr, msr | The size of the right margin on the current spread |
| marginsizetop, mgnszt, mst | The size of the top margin on the current spread |
| marginsizebottom, mgnszb, msb | The size of the bottom margin on the current spread |
| marginleft, mgnl, ml | The position of the left margin on the current spread |
| marginright, mgnr, mr | The position of the right margin on the current spread |
| margintop, mgnt, mt | The position of the top margin on the current spread |
| marginbottom, mgnb, mb | The position of the bottom margin on the current spread |
| designareawidth, areawidth, aw | The space between the left and right margins on the current spread |
| designareaheight, areaheight, ah | The space between the top and bottom margins on the current spread |

For general use throughout the user interface.

| Function/Usage | Notes |
| --- | --- |
| abs(x) | Absolute value |
| idiv(x,y) | Results in the integer (whole number) of _x_ divided by _y_ (no rounding is applied) |
| irem(x,y) | Results in the remainder of _x_ divided by _y_ |
| sin(a) | Sine |
| asin(a) | Inverse Sine |
| cos(a) | Cosine |
| acos(a) | Inverse Cosine |
| tan(a) | Tangent |
| atan(a) | Inverse Tangent |
| atan2(a, b) | Arctangent |
| average(a, b, ...) | Average of arguments |
| clamp(a, lo, hi) | a if it is between lo and hi, otherwise lo or hi |
| clampmin(n, min) | clamp values below minimum |
| clampmax(n, max) | clamp values above maximum |
| copysign(t, t sign) |  |
| dim(t x, t y) |  |
| fma(t a, t b, t c) | Computes (a*b) + c |
| fmod(t, t) |  |
| fraction(t) |  |
| lerp(a, b, f) | Linear interpolation (a + (b - a) f) |
| min(a, b, ...) | Smaller of values |
| max(a, b, ...) | Larger of values |
| mid(a, b) | Average of a and b |
| noise(seed / x, y) | Generate 1D noise either from a seed or based on X/Y input. |
| round(n) | Round to integer |
| roundup(b), ceil(n) | Round up to integer |
| rounddown(b), floor(n) | Round down to integer |
| trunc(t) | Shorthand for **truncate** |
| truncate(n) | Truncate **n** places after decimal point. |
| whole(t) |  |

*   [Document setup](https://www.affinity.studio/help/get-started-document-setup/)
*   [Transform panel](https://www.affinity.studio/help/panels-transform-panel/)
*   [Draw and edit geometric shapes](https://www.affinity.studio/help/curves-shapes-draw-geometric-shapes/)

How would you rate the help you received from this article?
