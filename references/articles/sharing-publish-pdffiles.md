---
title: "Publishing PDF files - Affinity Help Center"
source: https://www.affinity.studio/help/sharing-publish-pdffiles/
slug: sharing-publish-pdffiles
fetched: 2026-08-06
---

# Publishing PDF files - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/sharing-publish-pdffiles/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Export, share, and publish](https://www.affinity.studio/help/export-share-publish/)
3.   Publishing PDF files

You can output your publication to PDF, Adobe's cross-platform file format that preserves layout and appearance across platforms.

![Image 1: PDF publishing](https://images.ctfassets.net/3p2fxa94bzao/4HS4AUxStM8l0jYGaJZg2s/308dc0bb90999d6d742a199bf587f142/pdfpublish.png)

PDF files are perfect for web distribution and professional printing.

*   **For web**—PDF files for web use (and other methods of digital distribution) are optimized for screen use, i.e. with downsampled images but without pre-press printer's marks and bleed. Downsampling images leads to smaller documents for quicker loading.
*   **For professional printing**—PDF files for professional printing are high-quality copies of your publication, sent to a print partner that's normally external to your company. These usually require a CMYK document, printer's marks, bleed, high-resolution images (over 300dpi), and PDF/X-1a, PDF/X-3, or PDF/X-4 compatibility.PDF/X compatibility ensures your publication's colors are output in CMYK. It also embeds the fonts you've used. A single PDF/X file contains all the information (fonts, images, graphics, and text) your print partner needs. 

If your exported file contains fewer pages than expected, check the _Area_ export setting is set to _Whole document_, _All Pages_, or _All Spreads_.

For professional printing, you can include registration marks using registration black (100% for all CMYK components). This color appears on printing plates including PANTONE and other spot colors. You can add registration black as a swatch and apply it to an object on the page to create a custom registration mark.

You may see a warning about overflowing text. Use the **Preflight** panel to find and fix text frames with too much content.

All layers and hyperlinks export to PDF. If you add a TOC or index and export with hyperlinks, they'll include links.

The **Soft Proof** adjustment provides an in-app preview of CMYK PDF output to ensure your publication appears exactly as intended before export.

For better search engine indexing of the document, you can add document metadata such as Title, Subject, and Keywords to your publication via the **Fields** panel's **Document Information** section. Your exported PDF will then include these details.

When exporting a PDF, you can choose to give it two types of password: an **open password** and a **permissions password**. Password options are available when **Compatibility** is set to PDF 1.6 or above. You can add either or both types. Adding a password encrypts the PDF.

A PDF with an open password can be viewed by providing the open password _or_ the PDF's permissions password, if set.

When a PDF has only an open password, there are no restrictions on what can be done with its content. It can be printed or placed in an Affinity document, its content can be modified and selectively copied, and pages can be extracted to create new PDFs.

A permissions password limits what can be done with the PDF unless it is provided.

You can choose to allow specific actions to be performed without the permissions password. So, you might allow opening and printing, but not modification or selective copying of content.

A permissions password _always_ blocks page extraction, which could be used to extract content as is from your PDF. This is independent of the **Allow Copying of Content** setting, which determines whether smaller amounts of content, such as images and text, are copyable.

1.   On the **File** menu, select **Export > Export**.
2.   On the dialog that appears: 
    1.   Select your required **PDF** preset. Refer to 'PDF export presets' for details of each preset's PDF version, color space, resolution and other settings.
    2.   Set a **Raster DPI** value to set the resolution for rasterization of effects.
    3.   Check **Preview export when complete** to open the PDF in your default viewer.
    4.   Select the **Area** to export. To export the whole document or multiple specific pages, choose _Whole document_, _All Pages_ or _All Spreads_. _Current Page_ and _Current Spread_ export only the active page or spread.
    5.   (Optional) If you selected _All Pages_ or _All Spreads_, you can type the specific page numbers or page ranges you want in the _Pages_ box.
    6.   Choose whether to **Include bleed** in pages. Use with PDF/X for professional printing.
    7.   Adjust other settings as needed. Refer to the [Export Settings](https://www.affinity.studio/help/sharing-export-settings/) topic for descriptions.
    8.   Click **Export**.
    9.   Name the file, navigate to where you want to save it, then click **Save**.

*   On the **Swatches** panel, click the **Panel Preferences** menu ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg) , then select **Add Registration Color**.

You can then apply the swatch to an object on the page.

On the **Export** dialog, when exporting to PDF:

1.   Make sure **Compatibility** is set to PDF 1.6 or above.
2.   Select **Require password to open**.
3.   Click in the **Open password** box and type your required password.

On the **Export** dialog, when exporting to PDF:

1.   Make sure **Compatibility** is set to PDF 1.6 or above.
2.   Select **Require password for Modification and Printing**, click in the box below, then type the required password.
3.   Select **Allow Document Printing**, **Allow Content Modification**, and **Enable Copying of Content** as needed.

*   [Compare PDF export presets](https://www.affinity.studio/help/sharing-pdf-presets/)
*   [About exporting](https://www.affinity.studio/help/sharing-export/)
*   [Export dialog](https://www.affinity.studio/help/sharing-export-dialog/)
*   [Export Settings](https://www.affinity.studio/help/sharing-export-settings/)
*   [Setting bleed](https://www.affinity.studio/help/sharing-bleed/)
*   [Preflight](https://www.affinity.studio/help/sharing-preflight/)
*   [Overprinting](https://www.affinity.studio/help/clr-overprint/)
*   [Spot colors](https://www.affinity.studio/help/clr-spot-clr/)
*   [Soft Proof adjustment](https://www.affinity.studio/help/adjustments-adjustment-soft-proof/)

How would you rate the help you received from this article?
