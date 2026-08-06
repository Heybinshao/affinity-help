---
title: "Layer states - Affinity Help Center"
source: https://www.affinity.studio/help/object-control-layer-states/
slug: object-control-layer-states
fetched: 2026-08-06
---

# Layer states - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/object-control-layer-states/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Layer states

**Layer states**, or simply states, allow you to instantly set the visibility and layer effects of multiple layers.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/5XzmtdwW1clVXmTEFFSQmD/c631e8f1569aea160ab10169971a79e6/layer-states-designer-after.png)

After a query is applied: German and English version visibility.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/5Z1GfTmsYr9kro9EvQ8seJ/9e86a99da1ef416591a536c5c88cb6ab/layer-states-designer-before.png)

Before a query is applied: German and English version visibility.

There are two types of state:

*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/7zyFKBAERTQj8pdd7iAYoa/d05fa2946cc9a1be5d9dfc10cf012dc9/standard_layer_state.svg)  A regular **state** captures the visibility of and layer effects applied to layers at the time the state is added to a document.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/5x9LIAQZmQ02KKRk4TY867/cffd4679f1010251a92f277fb64cd675/add-smart-state.svg)  A **query** specifies criteria—any combination of a layer's tag color, type, name and lock status—that determine the visibility of layers. For example, you may want to hide all layers that have a tag color of red and show all other layers.

States of each type can be given a name.

With several states or queries added to the **States** panel, you can quickly compare different design choices for your document, such as alternative masks, adjustments, live filters and even entirely different layer content.

Entries on the States panel for each type of state provide different information about how they will affect your document's layers.

Each state entry displays:

*   A thumbnail representation of the state.
*   The state's name.
*   The number of layers for which information is captured in the state.

Each query entry displays the query's name, and specifies the criteria that must all be met in order to set your chosen layer visibility. You can specify any combination of the available attributes. Unselected attributes are ignored.

The application of states and queries can be used in a number of professional scenarios. Apart from language content previews above, more could include:

*   Switching the visibility of an underlying image on and off while tracing: particularly useful when learning how to draw.
*   Preparing a number of versions of mock-up designs for promotional campaigns.
*   Presenting variations of content layout options on artboards.

You can use regular expressions to match layer names that follow a pattern. For example:

*   The regular expression _A-[0-9]{3}-_ will match layers whose name starts with the letter A (in either case), a hyphen, a sequence of three numbers, and another hyphen, such as _a-230-_ but not _C-230-_ or _A-2300-_.
*   The regular expression _[.]*-M\_DOOR$_ will match all layers whose name ends with _M\_DOOR_, e.g. _A-325-M\_DOOR_ and _Z-124-M\_DOOR_ but not _A-325-M\_DOOR\_FRAME_.

Detailed information about the capabilities of regular expressions is available on the Web.

When adding or updating a state or applying a state or a query, use the **Scope** setting to determine how broadly information is captured from or affects the current visibility of your document's layers, respectively.

The scope can be the whole document, the current selection on the **Layers** panel, or an individual spread.

This allows you to focus your use of states on a specific portion of your work. For example, layers whose tag color is orange but only if they are nested within a selected layer.

1.   On the **Layers** panel, set the visibility of your document's layers as you want them to be captured.
2.   On the **States** panel, set the **Scope** of layers whose visibility and layer effects you wish to capture to either **Document**, **Spread** or **Selection**.
3.   (Optional) If the selected scope is either: 
    *   Spread—use the page navigation bar, at the bottom left of the workspace when editing a suitable document type, to navigate to the required spread.
    *   Selection—on the Layers panel, select the layers whose visibility you want to capture.

4.   Click **Add new captured state**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/7bMYNXlHZVU94q6Ujbgfuf/eed0ebb4767354c51fd3f47c53f5d23e/add-layer-state.svg) .

if artboards are in place, the **Spread** option for **Scope** (second point above) will reflect that and display **Artboard** instead.

1.   On the **States** panel, select **Add new query**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/5x9LIAQZmQ02KKRk4TY867/cffd4679f1010251a92f277fb64cd675/add-smart-state.svg) .
2.   On the query's entry: 
    *   Select only the attributes (**Layer tag**, **Layer type**, **Layer name** and **Lock status**) that you want to include as criteria.
    *   For each selected attribute, specify the values that layers must match.
    *   (Optional) Select **And show / hide others** if you wish to set the visibility of non-matching layers to the opposite of matching layers when the query is applied.

*   (Optional) On the **Layers** panel, select the layers whose visibility you wish to affect.
*   On the **States** panel: 
    *   Select the **Scope** for layers you wish to affect.
    *   Click **Apply**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/1CJRfVLRIvw9E1Xr9oIqf9/2aca19f44cb79ac4e2b093953da01285/apply_layer_state.svg)  on the state you wish to apply.

On the **States** panel:

1.   Select the **Scope** for layers you wish to affect.
2.   On the query you wish to apply: 
    1.   (Optional) Select or deselect **And show / hide others** according to whether you wish to affect non-matching layers.
    2.   On the query you wish to apply, click **Hide**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/7rY9o7BaMYaXIuO3e0XZeQ/aaf4a20d62a86e46e3524da1e71396c2/visibility_off_alternate.svg)  or **Show**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/9rstenG65qWb7jzhC83X9/df6defa0ca6b00f2d4f82ec5823bffa6/visibility_on.svg) .

*   On the **States** panel, click the **States Options**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/7e47FwYJ0eBW8yOWy3elSz/813ccca2419c99817334e5bb65c2a0db/cog_icon_2.svg)  menu and do the following: 
    1.   Select **Visibility changes** to allow layer visibility captured in the state to be applied, or deselect it to ignore captured layer visibility.
    2.   Select **Effects changes** to allow layer effects captured in the state to be applied, or deselect it to ignore captured layer effects.

1.   (Optional) On the **Layers** panel, select the layers you wish to include in the updated state. (Layers that were not captured when the state was added will be ignored even if they are selected.)
2.   On the **States** panel: 
    1.   Select the **Scope** of layers you wish to include in the updated state.
    2.   Click **Update**![Image 11](https://images.ctfassets.net/3p2fxa94bzao/5KDZbVOfTFnEfmyKXzDqtc/14a2f160b1a4f6d95149227f9c92dc7b/update_layer_state.svg)  on the state's entry.

*   [States panel](https://www.affinity.studio/help/panels-states-panel/)
*   [About layers](https://www.affinity.studio/help/layers-about-layers/)
*   [Layers panel](https://www.affinity.studio/help/panels-layers-panel/)

How would you rate the help you received from this article?
