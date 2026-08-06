---
title: "States panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-states-panel/
slug: panels-states-panel
fetched: 2026-08-06
---

# States panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-states-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   States panel

The States panel lets you save the current visibility and effects of layers as layer states. You can also create queries that control layer visibility based on properties like tag color, type, name, and lock status.

For Mac/Windows: On the **Window** menu, select **General > States**.

Any state or query can be instantly applied to all or some of your document's layers, allowing you to easily compare different directions for your work. To learn more about the application of states and queries, view the [Layer states](https://www.affinity.studio/help/object-control-layer-states/) topic.

It is helpful to add a state that represents the starting configuration of your document's layers before adding or applying other states, so you can easily return to it.

Updating or deleting a state is not recorded in your document's History, i.e. you cannot simply undo or redo these actions.

The following options are available on the panel:

*   **Scope**—determines whether adding, updating or applying a state captures/affects the visibility of layers throughout the whole **Document**, only the current **Selection** on the **Layers** panel, or (for specific document types such as .afpub) only layers on the current **Spread**. If artboards are in use, then a Scope of just the currently selected **Artboard** can be set (replaces the **Spread** option).
*   **Add new query**—creates a new query, with your choice of name, that can be configured to affect layers' visibility according to their tag color, type, name and lock status.
*   **Add new captured state**—creates a new state, with your choice of name, that captures the current visibilities of and effects applied to layers in the selected **Scope**.
*   **Delete state**—deletes the selected state.

The following options are available on the **Panel Preferences** menu:

*   **Panels**—opens a dialog where you can quickly set the visibility of all panels in the current Studio.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

The following options are available on a state's entry on the panel:

*   **Update**—updates the state with current information about layers that were in scope when it was originally added and which are currently in scope. (Other layers that are currently in scope are ignored.)
*   **Apply**—the visibilities of layers are set to the values captured in the state. Affects only layers and layer effects captured in the state and which are in the selected **Scope**, and depending on your choices on the state's options menu.

The following options are available on the **State Options** menu:

*   **Visibility changes**—when selected, the state is allowed to affect layer visibilities when it is applied. When unselected, the state will not affect layer visibilities when it is applied.
*   **Effects changes**—when selected, the state is allowed to affect layer effect visibilities when it is applied. When unselected, the state will not affect layer effect visibilities when it is applied.

The following options are available from a query's entry on the panel:

*   **Select**—when clicked, relevant layers are selected according to the visible query.
*   **Hide**—when clicked, layers within the selected **Scope** that meet the query's criteria are hidden.
*   **Show**—when clicked, layers within the selected **Scope** that meet the query's criteria are shown.
*   **Criteria**—describes attributes that layers must match for their visibility to be affected when Hide or Show is clicked. Unselected attributes are ignored. All selected attributes must be matched. 
    *   **Layer tag**—select one or more tag colors (including no color). For example, layers with a red tag color, or layers with either a red tag color _or_ an orange tag color. Turn on the switch to match layers whose tag color **is** one of your selection, or turn it off to match layers whose tag color **is not** one of your selection.
    *   **Layer type**—select one or more layer types. For example, only adjustment layers, or adjustment layers _and_ live filter layers. Turn on the switch to match layers whose type **is** one of your selection, or turn it off to match layers whose type **is not** one of your selection.
    *   **Layer name**—enter a layer name that layers must match exactly, or, with **Regular expressions** selected, a pattern for matching layer names, then press the **⏎** key (Mac) / **Return** key (Windows). Turn on the switch to match layers whose name **is** as specified, or turn it off to match layers whose tag color **is not** as specified. 
    *   **Lock status**—turn on the switch to match only locked layers. Turn it off to match only unlocked layers.

*   **And show / hide others**—when selected, layers in the selected **Scope** and which do not meet the criteria are set to the opposite visibility when you click Hide or Show.

*   [Layer states](https://www.affinity.studio/help/object-control-layer-states/)
*   [About layers](https://www.affinity.studio/help/layers-about-layers/)
*   [Viewing](https://www.affinity.studio/help/design-aids-view/)
*   [Layers panel](https://www.affinity.studio/help/panels-layers-panel/)

How would you rate the help you received from this article?
