---
title: "Placing content - Affinity Help Center"
source: https://www.affinity.studio/help/media-place-images/
slug: media-place-images
fetched: 2026-08-06
---

# Placing content - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/media-place-images/

Many industry-standard file formats can be placed in Affinity documents, including popular raster and vector files, and Photoshop, Illustrator, Freehand and PDF documents.

*    Documents 
    *   Affinity (.af, .afphoto, .afdesigner, .afpub)
    *   Adobe Illustrator (AI)
    *   Adobe Freehand (10 and MX)1
    *   Adobe Photoshop (PSD)
    *   Adobe InDesign (IDML)
    *   Microsoft Excel (XLSX)
    *   Microsoft Word (DOCX)5
    *   PDF
    *   DWG/DXF
    *   RTF 5
    *   Plain text 5

*    Images 
    *   BMP
    *   EPS
    *   GIF
    *   HEIF/HEIC/HIF 4
    *   JPEG
    *   J2K,JP2
    *   JPEG-XR/JXR (WDP/HDP)
    *   PNG
    *   RAW 2
    *   SVG
    *   TGA 3
    *   TIFF
    *   WEBP
    *   OpenEXR
    *   Radiance HDR

1 Multi-page Freehand files open with each page concatenated onto a single page. Add file extension .fh10 or .fh11 to import. Text import is not supported.

2 Raw images are processed automatically.

3 Supports transparency.

4 For iPhone images, the HEIC file may include an upsampled depth map, loaded as an editable second layer. For Canon EOS models (1 DX MkIII, R5 and R6), HIF files (HDR 10-bit PQ-encoded) are supported.

5 See [Importing text](https://www.affinity.studio/help/text-import-text/) for information about placing textual documents.

*   Placed images are added as image layers rather than pixel layers. This allows the original image data (e.g., the native resolution, color space, and color profile) to be kept. On export to PDF, this data is re-embedded into the PDF file.
*   Use the context toolbar's scaling controls to ensure correct sizing of CAD-derived PDFs or PDF/PSD adverts on placement.
*   Placed documents offer a **Page Box** option to choose how the page displays (e.g., with/without bleed, objects only).
*   Placed content can be rasterized at any time.
*   A file's embedded color profile will always be converted to the Affinity document's current working space.
*   For unprofiled placed images, the color space is assumed to be RGB.
*   Some brush operations (e.g. retouching) will automatically rasterize image layers to the document resolution. Inpainting or selection manipulation on an image layer requires manual rasterization. You can control automatic rasterization behavior using [Settings](https://www.affinity.studio/help/workspace-settings/).
*   Modifications made by using sliders in the **Quick Adjustments** panel create corresponding layers. This is also true for the auto adjustment options available for Levels, Contrast, Color and White Balance, which are available from the bottom of the panel.

Once content is placed in your document, you can replace it or edit it without changing its position.

The context toolbar contains an **Artboard** option so you can choose which artboard is displayed.

You can hover over the layer type icon on one of these resources' entries on the **Layers** panel to confirm whether it's an **Embedded document** or a **Linked document**.

A bitmap representation of the file will be displayed; the file content will not be interpreted. This will generally give better results on output and also negates the requirement to have correct fonts installed.

You can still edit the layers of the placed PSD, although if edits are made the file will be interpreted again and its appearance may change—e.g. if a font is missing.

Affinity converts Smart Objects in Photoshop documents to pixel layers by default. To convert to embedded documents instead, turn on **Import PSD smart objects where possible** in the app's **General** settings.

Smart Objects that are linked (i.e. to an external file) are not converted to embedded documents.

If these are placed as embedded documents, you can edit them within Affinity. If edits are made, these files will be converted to Affinity documents and the original data will not be retained; you will not be able to write the embedded file out to its native file format and make it linked. Other features such as using PDF Passthrough will also then be lost.

Please note that the Resource Manager will always display the original file's source filename and location should you need to refer back to it.

If these are placed as linked documents, you will not be able to edit them directly within Affinity. However, any edits made to the files will be picked up by Affinity and will be reported as **Modified** in the Resource Manager.

You can then use the Resource Manager to update the files to match the external changes that were made.

Alternatively, you might prefer to enable **Automatically update linked resources when modified externally** in the app's **General** settings.

You can choose which page or spread you want to display by using **Spread** on the context toolbar.

For PDF, only one page is displayed, although you can simulate a spread by duplicating the placed object and choosing a different page to show.

With a placed RAW image selected, select **Develop Image** on the context toolbar to open a dedicated develop area. Edits are reflected live on the page. Select **Develop** on the context toolbar to apply them. You can re-develop the image too, as required.

These offer a **Passthrough** setting on the context toolbar.

The setting defaults to _Passthrough_ for exact reproduction of a PDF. If that's not possible, the _Interpret_ option is selected.

A bitmap preview of the PDF’s contents is displayed while editing your Affinity document.

Placing a password-protected PDF will prompt you to enter the file's password. The password is then requested whenever you open the parent document.

When the parent document is exported, the resulting PDF does not have to be password-protected. If you wish to protect the exported PDF, ensure you set the required password(s) and restrictions on Affinity's **Export** dialog.

If a PDF includes layers, you can choose which of them are visible in your Affinity document. With the PDF placed and selected, specify each layer's visibility from the context toolbar's **Layers** setting. Note that doing so will automatically set **PDF Passthrough** to _Interpret_.

These can be placed directly on the page as tables, which you can edit using the **Table Tool** and **Table** panel. When placing, click on the page (instead of dragging) to preserve the original appearance of the file.

Usually, placing one of these files imports its content into your Affinity document. These files can be placed as linked resources by enabling **Import text files as linked** during document creation or later in **Document Setup**.
