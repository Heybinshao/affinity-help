---
title: "Importing InDesign (IDML) documents - Affinity Help Center"
source: https://www.affinity.studio/help/get-started-import-in-design/
slug: get-started-import-in-design
fetched: 2026-08-06
---

# Importing InDesign (IDML) documents - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/get-started-import-in-design/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Getting started](https://www.affinity.studio/help/getting-started/)
3.   Importing InDesign (IDML) documents

You can import Adobe InDesign documents exported in IDML format into Affinity. The proprietary INDD file format cannot be imported.

The importing of these documents is a one-way process. You cannot overwrite the original file once it has been imported. Imported documents must be saved as an .af file.

InDesign files that have been saved in IDML (InDesign Markup Language) format can be imported, which is available in InDesign CS4 and later. With earlier versions of InDesign, you can export documents to PDF and then import that format directly into the app.

The dpi (dots per inch) setting of the resulting document is decided as follows:

*   If the imported IDML file does not contain linked or embedded raster resources with their own dpi settings, the document is set to 300 dpi if it's a CMYK document or 72 dpi if it's an RGB document.
*   If the imported IDML file contains linked or embedded raster resources, the document is set to whichever of 72, 96, 144, 192, 300, 400 and 600 dpi is closest to the highest dpi setting of all those resources.

IDML files can also be placed into an existing document rather than opened.

1.   On the **File** menu, select **Open**.
2.   Select an IDML file and click **Open**.
3.    If linked resources are not found, you'll be asked whether you want to locate them. You can click: 
    *   **Yes** to locate missing resources one at a time.
    *   **Resource Manager** to review missing resources and locate only those required at this time.
    *   **No** to open the document without locating anything. Items can be located later by selecting **Window > Resource Manager**.

If the document uses fonts that are unavailable, you'll be warned of this and provided a shortcut to Font Manager, where you can make substitutions.

IDML files can be easily placed via **File > Place**. When placing multi-page documents, you can choose which page you wish to display using the context toolbar.

A document's dpi setting can be changed at any time in **Document > Setup > Document Setup**.

*   [Opening documents and images](https://www.affinity.studio/help/get-started-open-document/)
*   [Importing PDF documents](https://www.affinity.studio/help/get-started-import-pdf/)
*   [Importing other Adobe documents](https://www.affinity.studio/help/get-started-import-adobe/)
*   [Managing fonts](https://www.affinity.studio/help/text-managing-fonts/)
*   [Placing content](https://www.affinity.studio/help/media-place-images/)

How would you rate the help you received from this article?
