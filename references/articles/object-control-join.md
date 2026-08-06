---
title: "Joining with Booleans - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-join/
slug: object-control-join
fetched: 2026-08-06
---

# Joining with Booleans - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-join/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Graphic design](https://www.affinity.studio/help/graphic-design/)
3.   Joining with Booleans

Objects can be joined together to create an unlimited variety of shapes using Boolean operations. Joining operations are permanent.

There are various operations available (illustrated as before and after):

**Add**—creates a new object from the sum of the selected objects; the color of the lowest object is used.

![Image 1: Add](https://images.ctfassets.net/3p2fxa94bzao/s1xg8vbZCCqkiuCjQubxr/264762413608ab8204e17bcbd630045f/add_illus.png)

The **Add** operation can be applied to a single shape, where the resulting shape is the outline of the original shape.

**Subtract**—removes overlapped areas of the lowest object. All other selected objects are discarded.

![Image 2: Subtract](https://images.ctfassets.net/3p2fxa94bzao/1WlKgboZ71bargIOfic7GI/573488aef7acaa331643efd40e28fb4a/subtract_illus.png)

**Intersect**—creates a new object from the overlapping areas common to all selected objects.

![Image 3: Intersect](https://images.ctfassets.net/3p2fxa94bzao/4yDYfI55RAjkqDLFb8BqkL/d5b51ac76c26d70f3dc92e00745fd0dc/intersect_illus.png)

For more than two objects, all objects must intersect each other.

**Xor**—merges selected objects into a composite object with transparent area where filled regions overlap.

![Image 4: Xor](https://images.ctfassets.net/3p2fxa94bzao/5bNifkfkGzbX17ArBagWMp/1734d560e939566d4f3097985f5e290c/combine_illus.png)

**Divide**—splits object areas into separate objects; the object from the intersecting area retains the color of the upper object. The operation will be performed inside groups.

![Image 5: Divide](https://images.ctfassets.net/3p2fxa94bzao/2P7yNPGNL5GOe1rDotXQr0/8d5afb51ea45b2e9bd3df797f1859673/divide_illus.png)

![Image 6: Divide](https://images.ctfassets.net/3p2fxa94bzao/1vBXYkbDQ1SQdzlzsZBBVT/958afd7c06a4026e7376e19a633345fb/divide_illus_knockout.png)

Cut away of a fully overlapping object from the object below (the residual object can be deleted).

![Image 7: Divide](https://images.ctfassets.net/3p2fxa94bzao/qPm67f1Eku64k2lnxFsSn/fe3d1ada5beda23fb0570f36fd4c206e/divide_illus_bylines.png)

Object being be split by one or more straight lines or curves.

1.   Select multiple objects.
2.   Do one of the following: 
    *   In the Vector Studio ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg) , on the Toolbar, select **Add**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/4te5ffuV7wlxfLHZjXBYE3/f298c15617667ceaccc59fc7dea44ef2/add.svg) , **Subtract**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/78M32Z31jTOkYaHWxegJxj/2a64fc0c16a52868678cbfe53c6f4a34/subtract.svg) , **Intersect**![Image 11](https://images.ctfassets.net/3p2fxa94bzao/6G1NAmj6MzCJXPT8lRurlW/3a85ee7d014cb268e5c2a732cc8f9b19/interesect.svg) , **Xor**![Image 12](https://images.ctfassets.net/3p2fxa94bzao/5PMX28cvECFZr0WBI5g2Qw/cdaaf4d90c20d9ec601f121bf45ad9ae/combine.svg)  or **Divide**![Image 13](https://images.ctfassets.net/3p2fxa94bzao/01rSjRwpBCN0vFvVz1zEdP/6d2f80a42ab8db370c8f57338c8d2ed3/divide.svg) .
    *   Right-click on the selected objects and select one of the options from the **Geometry** category.
    *   On the **Vector** menu's **Geometry** submenu, select an operations command.

For Subtract operations, with objects selected, press the **⌥** key (Mac) / **Alt** key (Windows) and click a 'key' object to subtract from, instead of the lowest object. The key object shows with a strong outline colored blue by default or with the containing layer's layer color.

![Image 14: Subtract](https://images.ctfassets.net/3p2fxa94bzao/1kzsr59hleOZulMx1ex5Zw/84e6b0cfaf4dc842423aa658c5d1e811/subtract_illus_keyobject.png)

Holding down the **⌥** key (Mac) / **Alt** key (Windows) when selecting **Add**, **Subtract**, **Intersect** or **Xor** will create a non-destructive compound.

By default, the **Divide** operation will trim off any residual straight lines or curves extending beyond the shape’s outline, plus any lines/curves left over between object fragments.

With the **⌥** key (Mac) / **Alt** key (Windows) pressed during the operation, you can still retain the original curve(s) or line(s) instead (without trimming) but it will be split at every intersecting point.

**Vector > Fill holes** will remove any holes within one or more selected shapes, filling it with the surrounding shape’s fill.

*   [Creating compounds](https://www.affinity.studio/help/object-control-compound/)
*   [Adding by shape building](https://www.affinity.studio/help/object-control-join-shape-builder/)

How would you rate the help you received from this article?
