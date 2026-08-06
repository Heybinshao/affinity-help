---
title: "Autoflowing images and documents - Affinity Help Center"
source: https://www.affinity.studio/help/media-place-images-autoflow/
slug: media-place-images-autoflow
fetched: 2026-08-06
---

# Autoflowing images and documents - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/media-place-images-autoflow/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Autoflowing images and documents

Autoflow allows you to place multiple images or documents in an instant.

It can be used to quickly place:

*   multiple images, framed or unframed.
*   multiple pages from one or more multi-page documents.

![Image 1: Page layout after autoflowing images ](https://images.ctfassets.net/3p2fxa94bzao/904almnFJCL90acFszP8m/50b4d80b974bff18556c60666f687f1c/autoflowImages_after.jpg)

Pages before and after autoflowing images from the Place panel.

![Image 2: Page layout before autoflowing images](https://images.ctfassets.net/3p2fxa94bzao/16CHOdJfbi3Ok1nfflXeDT/b47955b8a6f08966db8de6e766417a46/autoflowImages_before.jpg)

Pages before and after autoflowing images from the Place panel.

You can use autoflow to place images in repeating page layouts—either a single layout or a sequence of different layouts—such as for a lookbook or similar image gallery.

If there are insufficient pages in your document to accommodate all items, autoflow adds more pages. If you choose to place in picture frames, it clones the layout of picture frames from existing pages to the new pages as many times as needed. The pages remain fully and independently editable after autoflow.

Autoflow is available for text documents, but only when placed by clicking/tapping or dragging on a page, not by clicking/tapping on an existing text frame.

Autoflow is not available on master pages or for documents that contain artboards.

Autoflow is initiated by selecting multiple items on the **Place** panel and then interacting with the document view. The interaction you choose determines autoflow's behavior and results:

*   If you click or drag outside of a picture frame: 
    *   One item is placed per page.
    *   Items are placed on existing document pages, starting from where you dragged or clicked.
    *   If the document's last page is reached and there are still items to place, additional pages are appended, one per item.

*   If you click on a picture frame: 
    *   Affinity searches for empty picture frames, page by page, and from back to front on each page (bottom to top in the layer stack)1.
    *   The search stops at the first spread that contains no empty picture frames or, if no such spread is found, at the end of the document.
    *   One item is placed per picture frame.
    *   If there aren't enough empty picture frames to place all the items, picture frames found during the search will be cloned onto new pages until all items have been placed.
    *   New pages are inserted after the last page/spread on which an empty picture frame was found. In a document with facing pages, if this position is: 
        *   in the middle of the document, new pages are added as whole spreads.
        *   at the end of the document, new pages are added as individual pages.

    *   Each cloned page has the same master pages applied and picture frames as its corresponding source page but won't include other objects.

1 Picture frames on the starting page that are lower in the layer stack than the one clicked/tapped are ignored. To populate all empty picture frames on the starting page, ensure you click the one that is bottom-most in the layer stack.

1.   On the **File** menu, select **Place**. Alternatively, in the **Layout Studio**, select the **Place Tool**

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/47Z9iHInfnQl0IelWGJTdH/a235b375a151ad38f5a59edbf4183bba/place_image_tool.svg) . 
2.   On the pop-up dialog, navigate to the files you wish to place, select them, then click **Open**. The **Place** panel will appear, containing the items you selected.If the items you wish to autoflow are located in multiple folders, simply repeat steps 1 and 2 to add more items to the **Place** panel. 
3.   (Optional) If autoflowing pages from documents, on each document's entry on the panel, do one of the following: 
    *   On the pop-up menu, select the individual page/spread you wish to place.
    *   Click the filename to reveal entries for all the document's pages.

4.   To select items for autoflow, do one of the following: 
    *   To select all items, press **⌘A** (Mac) / **Ctrl**+**A** (Windows).
    *   To select an adjacent subset of items, hold the **⇧** key (Mac) / **Shift** key (Windows) and click the first and last required items.
    *   To select a non-adjacent subset of items, hold the **⌘** key (Mac) / **Ctrl** key (Windows) and click each required item.

5.   To autoflow the selected items, do one of the following: 
    *   Click to place each item at its default displayed size.
    *   Drag on the page to set the position and maximum size of placed items.
    *   Click on a picture frame to use as autoflow's starting point.

 The items are placed according to autoflow's defined behaviors. They are then removed from the panel. 
6.   If the panel contains no more items, it will close automatically. Otherwise: 
    *   repeat from step 3 to place additional items.
    *   press the **Esc** key to cancel further placement and close the panel.

Alternatively, **⌥**-drag / **Alt**-drag multiple image or document files from Finder (Mac) / File Explorer (Windows) and dropping onto a page in the document view adds them directly to the **Place** panel.

*   [Placing content](https://www.affinity.studio/help/media-place-images/)
*   [Place Tool](https://www.affinity.studio/help/tools-tools-placeimage/)
*   [Flowing text through frames](https://www.affinity.studio/help/text-flowing-text/)

How would you rate the help you received from this article?
