---
title: "Importing Adobe Photoshop and Illustrator documents - Affinity Help Center"
source: https://www.affinity.studio/help/get-started-import-adobe/
slug: get-started-import-adobe
fetched: 2026-08-06
---

# Importing Adobe Photoshop and Illustrator documents - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/get-started-import-adobe/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Getting started](https://www.affinity.studio/help/getting-started/)
3.   Importing Adobe Photoshop and Illustrator documents

You can import Adobe Illustrator and Adobe Photoshop files into Affinity.

The importing of Adobe documents is a one-way process. You cannot overwrite the original file once it has been imported, instead saving it as an Affinity document.

Some important aspects are as follows:

*   When importing Adobe Illustrator files, Affinity uses the embedded PDF in the file rather than the raw Illustrator data. The PDF data is embedded by enabling Illustrator’s **Create PDF Compatible File** option in the **Illustrator Options** dialog when the document is saved using **File > Save As**.
*   Files are imported with layers intact and ready for editing.
*   For Adobe documents containing artboards, each artboard is created as its own layer in Affinity.
*   Consistency is ensured for adjustment layers, which are mapped appropriately for Affinity.
*   Adobe Photoshop Large Document Format files (PSB) can be imported.
*   Smart objects can be edited within Affinity.

1.    Do one of the following: 
    *   On the **File** menu, click **Open**, then select the file you want and click **Open**.
    *   Open the file containing folder and drag the Adobe file to an off-page area of your workspace.

2.   For Illustrator files, from the PDF Options dialog, you can control page import choice, print resolution (DPI), color space, text editability and missing fonts. If the PDF stream contains bitmap data, the DPI and color space values are taken from the first encountered bitmap, otherwise 300DPI is used if no bitmaps are present. See [Importing PDF documents](https://www.affinity.studio/help/get-started-import-pdf/).

Photoshop and Illustrator files can be easily placed into an existing document via the **File** menu (**Place**). For multi-page files, each page is placed on its own artboard.

On opening, a file's color space is preserved by default, but you can convert it to the default working color space via **Settings** (**Color** option) using **Convert opened files...**. The document's current color profile is displayed at the top left of your workspace.

Smart objects reside on layers with similar pixel information as typical layers, however, they may be edited as stand-alone objects which aids non-destructive workflows. Adjustments, filters, transformations and more can be performed on smart objects in Affinity.

When importing Adobe Photoshop files containing smart objects, you can choose to import them and retain their editable functionality. This is instead of them being rasterized on import. When duplicated (or copied), layers containing smart objects retain their editable functionality.

1.   Access the app's **Settings**.
2.   In the **General** section, enable **Import PSD smart objects where possible**.

It is possible to save Affinity files as a PSD document type via the **File** menu by selecting **Export > Export**.

1.    Select the **Move Tool**, then do one of the following: 
    *   On the **Layers** panel, double-click the layer containing the smart object.
    *   On the context toolbar, select **Edit Document** or **Replace Document**.

It is possible to save Affinity files as a PSD document type via the **File** menu by selecting **Export > Export**.

Related behaviors can be adjusted from [the app's settings](https://www.affinity.studio/help/workspace-settings/):

*   **General > Import PSD text as text rather than bitmap**
*   **General > Import PSD smart objects where possible**
*   **General > Enable "save" over imported PSD files**. This is recommended only for users who need to use PSD as an interchange format with their Digital Asset Management (DAM) app.

*   [Opening documents and images](https://www.affinity.studio/help/get-started-open-document/)
*   [Importing PDF documents](https://www.affinity.studio/help/get-started-import-pdf/)
*   [Importing CAD documents](https://www.affinity.studio/help/get-started-import-cad/)
*   [Color management](https://www.affinity.studio/help/clr-clr-profiles/)
*   [Supported file formats](https://www.affinity.studio/help/appendix-fileformat/)

How would you rate the help you received from this article?
