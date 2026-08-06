---
title: "Applying master pages - Affinity Help Center"
source: https://www.affinity.studio/help/pages-apply-master-pages/
slug: pages-apply-master-pages
fetched: 2026-08-06
---

# Applying master pages - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/pages-apply-master-pages/

Just like publication pages, a master page can be a single page or a spread with two or more pages. A master can be applied to all or some of another spread's pages.

When creating a new document, a **default master** can be created and applied to all your initial publication pages. After this, you can apply any new master at any time using the **Pages** panel.

You can apply one master to another. For example, a “parent” master containing just page numbering can be applied to several “child” masters. Each child master can show a different color for each section of your publication.

To change page numbering style across all sections, just update the parent master. When you apply the child master to pages, it adds the section color and inherits page numbers from the parent master.

![Image 1: Multiple masters](https://images.ctfassets.net/3p2fxa94bzao/7m6Gf5T6B44aqHHx60YC5E/c1b9110e7886723d84530292ad51006a/masterpages_multiple.jpg)

Parent Masters (top) with footer information and child masters (middle) with multi-color headers and their combined effect on publication pages (bottom).

You can drag and drop a master to apply it to existing pages, or to create new publication pages with it already applied.

| Positions and cursors | Action |
| --- | --- |
| ![Image 2: Master being applied to a left page, replacing existing masters](https://images.ctfassets.net/3p2fxa94bzao/6wAiZM0uPrHQ5mDPjP6lxU/ec51e332ce67ee2ad156142dbd4cd91e/apply_master_left_page.png) ![Image 3: Master being applied to a whole spread, replacing existing masters](https://images.ctfassets.net/3p2fxa94bzao/2FIghAtp01vv7EJXVXdgyu/1a522b05a546f4a9b68a1c8dbeeb2a2d/apply_master_whole_spread.png) ![Image 4: Master being applied to a right page, replacing existing masters](https://images.ctfassets.net/3p2fxa94bzao/626pRdvf1VfMeLf3QiuSID/f319279683f510963288e56d30d19e1e/apply_master_right_page.png) | Applies the master to the targeted pages, replacing any masters already applied to them. |
| ![Image 5: Master being added to a left page without replacing existing masters](https://images.ctfassets.net/3p2fxa94bzao/38V8FifX4honssIiFfL2Ut/87e2f898e3502503da22af794b1a641c/add_master_left_page.png) ![Image 6: Master being added to a whole spread without replacing existing masters](https://images.ctfassets.net/3p2fxa94bzao/4NkZ3nyLB1S7qj7HVp1eJV/3897dd45dde48769ea97e3da76cd1a91/add_master_whole_spread.png) ![Image 7: Master being added to a right page without replacing existing masters](https://images.ctfassets.net/3p2fxa94bzao/3lTm37P8msS3SpT4A8fmQv/d9b74a82ddf125bd8bf031e3365f2c98/add_master_right_page.png) | With the **⌥** key (Mac) / **Ctrl** key (Windows) held, applies the master to the targeted pages in addition to any masters already applied to them. |
| ![Image 8: Using a master to create a new spread before an existing one](https://images.ctfassets.net/3p2fxa94bzao/5kPsKmd23f4C1qnZWb7bNx/bdcfabac00c0dda1ddaa2b433790779e/create_spread_from_master_before.png) ![Image 9: Using a master to create a new spread after an existing one](https://images.ctfassets.net/3p2fxa94bzao/3uJm7Ca7bz0uQssEPQm0Xd/197ab1e968a7c81b09ecc2ee2c056916/create_spread_from_master_after.png) | Creates a new spread at the targeted position with the same page count as the master, and applies the master to the spread's pages. |

You can identify the masters applied to a page by hovering over the page's thumbnail on the **Pages** panel.

In multi-page spreads, the tooltip shows which master each page uses.

![Image 10: Thumbnail of a color-tagged master](https://images.ctfassets.net/3p2fxa94bzao/xgcwQgeCPS28cp7IETMUc/d6865484a3e98ef8f9057718162d9cb3/tooltip_one_applied_master.png)

A two-page spread with the same master applied to both pages.

![Image 11: Thumbnail of a color-tagged master](https://images.ctfassets.net/3p2fxa94bzao/5gNoYxrilJYou9ZAb16WmT/3da400e96534f4084b1a67aff14b191e/tooltip_two_applied_masters.png)

A two-page spread with different masters applied to each page.

Optionally, any master can be tagged with a color, which is indicated at the corner of the master's thumbnail.

![Image 12: Thumbnail of a color-tagged master](https://images.ctfassets.net/3p2fxa94bzao/78zFY3aZ37Hnw5zLY3ISg3/c1eb5652ec8bcc5d8e051929707f017e/tagged_master.png)

A two-page master that has been tagged red.

A master's tag color can be set when the master is created, or later via the master's thumbnail.

You'll see the tag color above the thumbnails of pages where that master is used.

![Image 13: Thumbnail of a two-page spread with a color-tagged master applied](https://images.ctfassets.net/3p2fxa94bzao/Qn5jzJcxYfdbisf4JlqRD/f93304dad1d984e5e9c0076f9d98d61c/applied_tagged_master.png)

A spread with different numbers of tagged masters applied to its pages.

An applied master appears as a layer on the **Layers** panel, marked by a solid turquoise line before its thumbnail.

You can expand the layer to show items from the master. These have solid turquoise markers next to them.

When an element of a master page is edited on a page where it's applied, that page's layer entries for the element and its master page display _dotted_ turquoise line.

By dragging a master's layer to the top of the layer stack, you can present its content in front of everything else on the page.

By selecting the master page's layer, the inherited content can be collectively transformed. Individual objects can only be transformed by detaching the master page. The content of text objects and picture frames can be edited, though.

To avoid accidentally editing inherited objects (except text frames or picture frames), select the master layer on the Layers panel and lock it.

Use the **Master Properties** dialog to control how the master is applied. You can set:

*   Which pages of the master are applied (**Master Start Page** and **Page Count**).
*   Where the master pages start in the spread (**First Applied Page**).
*   How the master is scaled to fit pages of different sizes and where it is anchored.
*   Whether line styles scale.

The following scaling behaviors are available:

*   **None**—places the master at its original size.
*   **Stretch**—stretches the master to fill the destination exactly. It may be noticeably distorted, depending on its relative proportions and those of the destination.
*   **Uniform to Fit**—scales the master uniformly to be completely visible within the page. There may be empty areas down the left and right or across the top and bottom of the page.
*   **Uniform to Fill**—scales the master uniformly to fill the entire page without distorting it. Some of its contents may be cropped.
