---
title: "Fixed-Layout EPUB - Affinity Help Center"
source: https://www.affinity.studio/help/sharing-fixed-layout-epub/
slug: sharing-fixed-layout-epub
fetched: 2026-08-06
---

# Fixed-Layout EPUB - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/sharing-fixed-layout-epub/

Use the Fixed-Layout EPUB file format when you want readers to see your page layouts exactly as you designed them.

If you're new to EPUB in Affinity, read the "About EPUB" topic first. It covers when to use each EPUB type, how to export, and how to test your files.

With Fixed-Layout EPUB, you control every part of your design. Tables of contents, an index, notes, and other references are presented just as they would be in a print edition.

The reader can't control presentational attributes that can assist with readability, such as font settings. Pages work best on larger screens, but on smaller devices, such as smartphones, users may need to zoom and pan to read.

Fixed-Layout EPUB works well for image-heavy publications, but such content increases file size.

Built-in presets are provided for exporting Fixed-Layout EPUB files: high quality, small size, and document settings.

| Preset | Raster DPI | Above DPI | JPEG Quality |
| --- | --- | --- | --- |
| EPUB (small size) | 72 | 90 | 85 |
| EPUB (high quality) | 300 | 375 | 98 |

Check whether your chosen publishing platform sets a maximum EPUB file size. After selecting a preset, check the estimated file size shown on the Export dialog.

If the presets don't meet your needs, try adjusting the export settings. The key settings to consider, which are explained in the Export Settings topic, are:

*   **Raster DPI**
*   **Downsample images**
*   **Above DPI**
*   **Allow JPEG compression**
*   **Quality**

Remember, you can save your choices as a new preset.

You can improve accessibility of Fixed-Layout EPUBs with a few steps to prepare your content for a good reading experience.

Make sure assistive technologies announce images in the correct place by setting their position on the Reading Order panel.

As you add new content to the page, it is added to the reading order in an assumed position from top to bottom on the page.

Any content on a publication page that you do not want to be announced by assistive technologies can be disabled by clicking the checkmark on its entry on the panel. The content is still listed in case you change your mind, but it is not included in the reading order

If you import or open an existing document, pay attention to the reading order. Drag content into the most logical order for the reader.

To help users navigate a Fixed-Layout EPUB, Affinity can include your publication's table of contents (TOC) as a navigation document. The navigation document is an interactive TOC that readers can open at any time and from anywhere while reading.

To create one, use the Table of Contents panel as you would for a print document. Set your TOC's type to _EPUB: Primary_ so Affinity uses it to create a navigation document in your EPUB.

Running headers and page numbers are useful for sighted readers to find their place in a long document, but they can be disruptive for some readers, e.g. those listening via text-to-speech or using a Braille reader. By placing these repeating elements on master pages, you can ensure they still appear visually on pages, but are not repeatedly announced by assistive technologies.

When you export to Fixed-Layout EPUB, Affinity encloses text in HTML tags based on its text style. This helps EPUB readers and assistive technologies to understand the structure.
