---
title: "Export Settings - Affinity Help Center"
source: https://www.affinity.studio/help/sharing-export-settings/
slug: sharing-export-settings
fetched: 2026-08-06
---

# Export Settings - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/sharing-export-settings/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Export, share, and publish](https://www.affinity.studio/help/export-share-publish/)
3.   Export Settings

Affinity lets you control how your work looks in exported files.

The available settings are determined by your selected file format/preset.

Affinity provides presets for common needs. If none exactly fits your needs, pick the best fit, amend settings as required, and optionally create your own preset.

Custom presets you create on the **Export** dialog are then available on the **Quick Export** panel, as long as the corresponding file format is available.

Available for: PDF, SVG, EPS, Fixed-Layout EPUB, Reflowable EPUB

If raster elements exceed this DPI, they are downsampled to match. This option is available only if **Downsample images** is enabled.

Available for: SVG

When enabled, the exported code is formatted for readability. If disabled, the code is placed on a single line to reduce file size.

Available for: PSD

Controls how this design attribute is exported:

*   _Preserve accuracy_—the attribute will be rasterized to preserve its intended look.
*   _Preserve editability_—the attribute will be exported with its original settings to allow for easy editing.

Available for: PSD

Controls how this design attribute is exported:

*   _Preserve accuracy_—the attribute will be rasterized to preserve its intended look.
*   _Preserve editability_—the attribute will be exported with its original settings to allow for easy editing.

Available for: PDF

When enabled, all design features supported by the PDF file format are exported as vectors. If disabled, they are rasterized or converted to curves, depending on their type. These features include:

*   Artistic text which has been horizontally or vertically stretched.
*   Text which has an applied stroke.
*   Linear and radial gradients.
*   Non-solid transparencies.

If the **Allow advanced features** option is selected on export, opening the resulting PDF in another app may result in the advanced features being rasterized or rendered incorrectly. The third-party app may also display an error message on PDF import.

Available for: PDF

When enabled, anyone who can open the PDF can modify its content. If disabled, the PDF's content can be modified only by providing the permissions password.

Available for: PDF

When enabled, anyone who can open the PDF can print it. If disabled, the PDF can be printed only by providing the permissions password.

Available for: PDF, SVG, EPS, Fixed-Layout EPUB, Reflowable EPUB

When enabled, rasterized design elements will be compressed to decrease exported file size. If disabled, rasterized elements are exported without compression.

Available for: Reflowable EPUB

This setting is available when **Cover page** is set to _Rasterize first page_ or _Use image file_. In the box, type the text that will be presented by assistive technologies such as screen readers as an alternative to the rasterized image.

Available for: DWG, DXF

When enabled, the exported file uses the drawing scale. For example, a rectangle that is one inch wide with a scale of 1:10 will be exported at 10 inches wide.

Affinity allows multiple drawing scales within the same document, but DWG/DXF supports only one. The first or more common scale is used for export.

Available for: all formats.

You can export the full document or just part of it. Available options change depending on the document content.

*   _Whole document_—exports the entire document to a single PDF or multiple image files, depending on the selected file format. If the document contains artboards, each artboard is output as a separate PDF page or image file. 
*   **Artboard name**—exports the named artboard. If one or more artboards is selected in the document, this setting is automatically set to the first one that was selected, but you can choose another. (Available when the document contains one or more artboards.)
*   _Selection Area_—exports the selection with its background, meaning deselected layers within the area are included. (Available when one or more layers is selected.)
*   _Selection Only_—exports the selection without its background, meaning deselected layers within the area are excluded. (Available when one or more layers is selected.)
*   _All Spreads_—exports each spread as one PDF page or image file. The dimensions of each PDF page or image file are the same as its corresponding spread in Affinity. (Available when the document is page based, with at least one pair of facing pages.)
*   _Current Spread_—exports the active pages as one PDF page or image file. The dimensions of the PDF or image file are the same as the active pages. (Available when the document is page based, with at least one pair of facing pages.)
*   _All Pages_—exports each page as one PDF page or image file, i.e. in a document with facing pages, left and right pages are output as separate PDF pages or images. (Available when the document is page-based, with either ambidextrous or facing pages.)
*   _Current Page_—exports the active page as one PDF page or image file. (Available when the document is page-based, with either ambidextrous or facing pages.)

Available for: DWG, DXF

Determines what to do with object fills that have a bitmap fill applied, which DWG/DXF does not support. Available options are:

*   _Replace with solid_—replaces the bitmap fill with a solid fill of middle gray.
*   _Ignore_—removes the fill from the output.

Available for: DWG, DXF

Determines what to do with object strokes that have a bitmap fill applied, which DWG/DXF does not support. Available options are:

*   _Replace with solid_—replaces the stroke with a solid fill of middle gray.
*   _Ignore_—removes the stroke from the output.

Available for: Fixed-Layout EPUB, Reflowable EPUB

This setting is available when **Cover page** is set to _Use image file_. Click the setting's adjacent button, select the raster image file to use as the cover, then click **Open**.

Available for: WMF

When enabled, any transparent area around your content is absent in the exported file. If disabled, the transparent area is retained.

Available for: EXR

This is dependent on OpenColorIO. With a valid configuration, appending the filename during export will convert to that color space from scene linear. For example, name your file _output acescg.exr_ to convert to ACEScg if your OCIO configuration lists that as a valid color space.

Available for: PDF

Choose whether to use the document's current color space or export using a selected color space. Select from the pop-up menu.

Available for: PNG, GIF

Selects the number of colors available in the palette. Select from the pop-up menu.

Available for: PDF

Sets the version and type of PDF to be exported. Select one of the following:

*   _PDF 2.0 (ISO 32000-2)_
*   _PDF 1.7 (Acrobat 8)_
*   _PDF 1.6 (Acrobat 7)_
*   _PDF 1.5 (Acrobat 6)_
*   _PDF 1.4 (Acrobat 5)_
*   _PDF/X-1a:2003_
*   _PDF/X-3:2003_
*   _PDF/X-4_

Available for: PSD

When enabled, the exported file will be compatible with other apps which do not support some features (file size may also increase). If disabled, the exported file may not be readable by other apps (depending on the features used in the image).

Available for: TIFF, EXR

By default, this is set to ZIP. For TIFF, options to apply LZW compression or no compression are available. For EXR, options include RLE, PIZ and PXR24.

Available for: JPEG

When enabled, converts top level clipping curves to vector paths.

Available for: PDF

When enabled, all placed images will convert to the color space chosen on export (as set in the **Profile** option). If disabled, the exported file keeps the color space of each placed image.

Available for: Reflowable EPUB

When enabled, list item markers in bulleted lists will be converted to regular text.

Available for: Reflowable EPUB

When enabled, list item markers in numbered lists will be converted to regular text.

Available for: Fixed-Layout EPUB, Reflowable EPUB

Choose whether to include a cover page for your EPUB: _None_, _Rasterize (first) page_, or _Use image file_. The last two choices reveal additional settings that let you specify a page number, image file, and alt text where appropriate.

Available for: DWG, DXF

Determines what to do with object strokes with a dash pattern. DWG/DXF does support dash patterns; however, DWG/DXF dashes do not scale automatically with line weight, as they do in Affinity. Available options are:

*   _Keep_—approximates the dash pattern.
*   _Expand_—expands the dashed stroke. The dashes are then exported as a hatch.
*   _Make continuous_—the dashes are ignored and the Continuous line type is applied to the exported curve.

Available for: SVG

Determines the numerical accuracy of values in the exported file, with a precision range of 1 to 12 places.

Available for: Fixed-Layout EPUB

When enabled, layers that have been hidden while in the Slice Studio are excluded from the export file, even if they are shown on the page. When disabled, all objects on the page (and within the selected Area) will be exported regardless of their visibility in the Slice Studio.

Available for: PDF, SVG, EPS, Fixed-Layout EPUB, Reflowable EPUB

Select whether to downsample raster images within the design.

Available for: DWG, DXF

Determines the file format version that will be exported. Available options are:

*   _2000-2002_
*   _2004-2006_
*   _2007-2009_
*   _2010-2012_
*   _2013-2016_
*   _2018+_

Available for: PDF

Select an option for handling fonts used in the document.

*   _Text as Curves_—all text is converted to curves. This ensures the resulting exported file will display correctly regardless of the fonts installed on the viewing device.
*   _All Fonts_—any fonts used in the document are embedded in the exported file. This ensures the resulting exported file will display correctly regardless of the fonts installed on the viewing device.
*   _Uncommon Fonts_—fonts used are only embedded in the exported file if they are not part of the fonts traditionally installed on most devices. The viewing device must have the expected fonts to view any common fonts in the exported file.
*   _No Fonts_—no fonts are embedded in the exported file. A viewing device must have all the used fonts installed to accurately view the exported file. (Not available when PDF/X compatibility is used.)

Available for: PDF, PNG, JPEG, TIFF, JPEG-XL

When enabled, the ICC profile is included within the exported image's data, allowing the image to be viewed using the correct profile on any device. If disabled, the viewing device must have the ICC profile, or a substitute will be used.

Available for: PNG, JPEG, TIFF, PSD, EPS

When enabled, any raster image's original metadata is preserved in the exported file. If disabled, all original metadata is removed; use this for privacy reasons or to reduce file size (for web use).

Available for: JPEG

When enabled, for exporting HDR images, the export process adds high-dynamic-range brightness data to a standard SDR image by storing it in a special gain map. This lets the image display normally on any device, while unlocking enhanced brightness, contrast, and color on screens that support HDR.

Available for: PDF

When enabled, anyone who can open the PDF can selectively copy content from it. If disabled, content can be copied only by providing the permissions password.

Available for: PDF

Indicates the type of encryption that will be applied to the PDF, if you have chosen to require an **Open password** or a **Permissions password**. The encryption type is determined by the **Compatibility** setting.

Available for: WMF

When enabled, the exported file will be in EMF format. If disabled, the export file will be in WMF format.

Available for: all formats

Shows an estimate of the amount of space that will be required for the export. Its value is determined by your chosen preset/settings. It helps guide your choices when optimizing file size is important.

Available for: SVG, WMF

When enabled, the text in the resulting file will be drawn as curves (therefore displaying precisely as intended, even if viewed on a device without the used fonts installed). However, this option will increase file size, and text won't be editable or usable with text-to-speech features. If disabled, text will be exported as text and the viewing device will need the used fonts installed for it to be displayed correctly.

Available for: SVG

When enabled, transformed objects are 'fixed' in the exported file. This allows for the file to be viewed more accurately across apps. If disabled, objects remain dynamically transformed to allow for more flexible editing.

Available for: PNG

When checked, the entire dynamic range is used for the PNG, rather than being compressed.

Available for: Reflowable EPUB

When enabled, each text style that has **Emit CSS** enabled is translated to a CSS rule-set in the EPUB output. When disabled, CSS is not generated for your document's text styles, but CSS files added to the EPUB panel will be included in the output.

Available for: DWG, DXF

Determines what to do with object fills that have a gradient fill applied. Available options are:

*   _Simplify_—applies a simplified gradient.
*   _Replace with solid_—replaces the gradient with a solid fill of the color of the gradient's first stop.
*   _Ignore_—removes the fill from the output.

Available for: DWG, DXF

Determines what to do with object strokes that have a gradient fill applied, which DWG/DXF does not support. Available options are:

*   _Simplify_—applies a simplified gradient.
*   _Replace with solid_—replaces the gradient with a solid fill of the color of the gradient's first stop.
*   _Ignore_—removes the stroke from the output.

Available for: PSD

Controls how this design attribute is exported:

*   _Preserve accuracy_—the attribute will be rasterized to preserve its intended look.
*   _Preserve editability_—the attribute will be exported with its original settings to allow for easy editing.

Available for: Reflowable EPUB

When enabled, page numbers are not shown in the table of contents within the document content. When disabled, page numbers are shown, but they may not match the page numbers displayed by the reading device due to layout and user settings.

Available for: PDF

When enabled, spot colors within the design are exported as spot colors. If disabled, spot colors are converted to an equivalent color within the exported file's color space.

Available for: PDF, PNG, JPEG, GIF, TIFF, TGA, WEBP, JPEG-XL

By default, this is set to the ICC profile of the project (document). However, the project's ICC profile can be overwritten for this export area. Select from the pop-up menu.

Available for: EXR

Choose whether to encode Image channels (**RGBA** etc) as 16-bit (half float) or 32-bit (full float).

Available for: PNG, JPEG, GIF, TIFF, PDF, SVG, EPS, TGA, WEBP, JPEG-XL

When enabled, the bleed area of your document, if set, will be included in the output. See also **Include printers marks** and the [Setting bleed](https://www.affinity.studio/help/sharing-bleed/) topic. (A bleed area can be added in **Document Setup**.)

Available for: PDF

When enabled, bookmarks defined on the **Anchors** panel are included in the output.

Available for: PDF

When enabled, the PDF output will include all hyperlinks in your document—manually created or automatically generated by a table of contents or index.

Copies of linked files will be created alongside the PDF if the corresponding hyperlink's **Include File on Export** setting is checked.

Available for: PDF

When enabled, layers at the top hierarchical level that are hidden and contain child layers that are not hidden will be included in the PDF output as invisible layers.

Available for: PDF

When enabled, the PDF output will include all created layers (except invisible/hidden layers unless the corresponding setting is also selected).

Only named layers are included. Affinity layers without a name are not exported as PDF layers.

Available for: PDF

When enabled, the PDF output will show printer's marks around the page edge. All printer's marks are added by default. However, particular types of printer's marks can be switched off, depending on your preference. These include:

*   Crop marks
*   Registration marks
*   Color and grayscale bars
*   Page information

Professional printing services often print on larger sheets and trim them to your page design's size. To ensure movement during printing does not result in white edges, make your design fill the document's bleed area, turn on **Include bleed** to add this information to your PDF file, and turn on **Include printers marks** to assist with trimming. For more details, see [Setting bleed](https://www.affinity.studio/help/sharing-bleed/).

Available for: EXR

When checked, channels whose type cannot be determined will still be exported as a single luminance-based channel.

Available for: PSD

Controls how this design attribute is exported:

*   _Preserve accuracy_—the attribute will be rasterized to preserve its intended look.
*   _Preserve editability_—the attribute will be exported with its original settings to allow for easy editing.

Available for: DWG, DXF

Determines how Affinity objects and layers are mapped to DWG/DXF layers, and so which DWG/DXF layer an exported item belongs in. (The DWG/DXF format does not allow for nested layers, so all exported layers are at the top level of the resulting file.)

Objects at the top of Affinity's layer stack, i.e. not belonging to an Affinity layer, are always mapped to Layer 0 of the exported DWG/DXF file.

Objects on top-level, unnamed Affinity layers are always mapped to Layer 0.

Objects on nested, unnamed Affinity layers and on named Affinity layers, however deeply nested, are mapped according to which of the following options is selected:

*   _None_—objects are mapped to Layer 0. (Your Affinity document is flattened onto a single layer.)
*   _Top Level Only_—objects are mapped to their top-level containing layer. Nested layers are then empty and not included in the exported file.
*   _Any_—objects on named Affinity layers are mapped to their nearest named containing layer. Objects on unnamed layers are mapped to Layer 0.
*   _Any named_—objects are mapped to their nearest named containing layer, or Layer 0 if there isn't one.

Available for: PSD

Controls how stroked vector paths (line strokes) are exported, particularly when stroke styling may not be fully supported in PSD—for example, dashed or variable-width strokes.

*   _Preserve accuracy_—Line strokes that PSD cannot reliably represent are rasterised to preserve their appearance.
*   _Preserve editability_—Line strokes are exported as editable vectors using the closest supported PSD stroke settings, which may simplify or alter some stroke styling.

Available for: SVG

When enabled, text is placed relative to previous lines of text (therefore producing smaller file sizes and simpler file structures). If disabled, text is placed with absolute coordinates.

Available for: WEBP

When checked, the newer, lossless WebP compression algorithm is used.

Available for: PNG, JPEG, GIF, TIFF, EXR, HDR, TGA, WEBP, JPEG-XL

Sets the background color for the exported image. Select from the pop-up panel.

Available for: EPS

When enabled, the exported file will be compressed to create the smallest file size possible.

Available for: EXR

When exporting to OpenEXR format, converts layers with affixes—e.g. .RGB or .RGBA after the layer's name—back to multi-channel data.

Available for: PDF

If **Require password to open** is enabled, type the password that will be required to decrypt and view the PDF.

In the box, click the eye icon to show or hide the open password. Click the clipboard icon to insert the contents of the Clipboard into the box.

Available for: EXR

Choose whether to encode other/undetermined channels as 16-bit (half float) or 32-bit (full float).

Available for: PDF

When enabled, design elements which use CMYK black are set to overprint. If disabled, CMYK black elements are set to be indistinguishable to other colors during printing.

Available for: DWG, DXF

Determines what to do with object strokes with a line weight greater than 2.11 mm, which DWG/DXF does not support. Available options are:

*   _Expand_—expands the stroke. The expanded stroke is then exported as a hatch.
*   _Clamp_—clamps the line weight to a maximum of 2.11 mm.

Available for: Fixed-Layout EPUB

This setting is available when **Cover page** is set to _Rasterize page_. Select the page number from which to generate the cover page.

Available for: Fixed-Layout EPUB

Controls the overall output pixel dimensions. While DPI is familiar from print, pixel dimensions are the more relevant measure here. Adjust either the Width and Height pixel values or the Page DPI to resample and scale attributes for the best balance between file size and quality.

Available for: PNG, JPEG, GIF, TIFF, PDF, DWG, DXF, PSD, SVG, WMF, EPS, EXR, HDR, TGA, Fixed-Layout EPUB, WEBP, JPEG-XL

This setting is available when the document is page-based, with either ambidextrous or facing pages. Enter the page number(s) you would like to include in the export. For example, _1-3, 8_ will include pages 1 to 3 inclusive and page 8 in the output. Available only when **Area** is set to _All Pages_ or _All Spreads_.

*   Exporting a PDF creates one file with the specified pages. Page numbers stay the same as in the full document.
*   Exporting other file formats, e.g. PNG or JPEG, produces a separate graphic file for each specified page.

Available for: Reflowable EPUB

Use this setting to tell reading systems where your EPUB's page break markers come from. Choose from:

*   _None_—when your EPUB uses digital-only pagination.
*   _ISBN Number—_ type a URN (Uniform Resource Name) to use pagination that matches a print edition.
*   _Other_—type custom text, such as the name of a source document.

Specifying a source ensures consistent page numbers for citations, accessibility tools, and page navigation.

Available for: PNG, GIF

By default, this is set to be automatically determined. However, you can specify an encoding palette yourself. Select from the pop-up menu.

Available for: PNG, GIF

When enabled, encodes the exported image by mapping it to the **Palette** and **Colors** settings. (This option cannot be switched off for GIF images.)

Available for: PDF

If **Require password for modification and printing** is enabled, type the permissions password for the PDF.

In the box, click the eye icon to show or hide the permissions password. Click the clipboard icon to insert the contents of the Clipboard into the box.

Available for: PNG, JPEG, GIF, TIFF, TGA, WEBP, JPEG-XL

Sets the color mode for the exported image. Select from the pop-up menu.

Available for: EPS

Sets the version of the exported PostScript file. Select from the pop-up menu.

Available for: Reflowable EPUB

When enabled, local formatting in text generates CSS classes that are applied to the relevant text ranges in the EPUB output. When disabled, local formatting is ignored and the relevant text in the EPUB output uses the same style as its containing paragraph.

Available for: DWG, DXF

Determines what to do with object strokes with a pressure profile applied, which DWG/DXF does not support. Available options are:

*   _Expand_—expands the stroke with its pressure profile. The expanded stroke is then exported as a hatch.
*   _Ignore and clamp_—drops the pressure profile from the stroke. The line weight is then clamped to the DWG/DXF maximum of 2.11 mm.

Available for: PDF

Opens the exported file in your default PDF viewer.

Available for: PNG

Provides a full set of WCG primaries (P3-D65 plus a choice of BT primaries).

Available for: PDF

Choose whether the export uses the document's current color profile or a specific one. Select from the pop-up menu.

Available for: JPEG

When enabled, the exported image is progressively compressed for optimized viewing when downloading.

Available for: JPEG, PDF, SVG, EPS, WEBP, JPEG-XL, Fixed-Layout EPUB, Reflowable EPUB

Sets the resulting quality of rasterized design elements in the exported image—or the overall image in the JPEG format's case. Higher quality may result in significantly larger file sizes.

For the JPEG format, this is an independent setting. For the other formats, this option is available only if **Allow JPEG compression** is enabled.

Available for: PDF, SVG, EPS, Fixed-Layout EPUB, Reflowable EPUB

This option lets you choose the resolution for effects which will be rasterized on export.

Available for: PDF, SVG, EPS

Select an option for rasterizing design elements which are unsupported by the file format:

*   _Nothing_—no elements within the design are rasterized on export, therefore unsupported elements are not included in the exported file.
*   _Everything_—all elements within the design are rasterized for a resulting exported file which perfectly matches your original design.
*   _Unsupported properties_—only unsupported elements are rasterized in the exported file.

Available for: PSD

When enabled, layer content is rasterized in the exported file (the layer structure is retained). If disabled, no rasterization takes place on export.

Available for: Fixed-Layout EPUB

Text that uses special typographic features, e.g. complex ligatures, is rasterized to ensure your design looks as intended on devices that don't support those features. When enabled, the text is rasterized at a very high quality. When disabled, the text is rasterized at a lower quality and might exhibit pixelation.

Available for: Reflowable EPUB

When enabled, soft returns—line breaks that don't start a new paragraph—are replaced with spaces in the EPUB export. When disabled, they are retained, meaning users may observe unexpected gaps within paragraphs as the text reflows.

Available for: PDF

When enabled, the **Permissions Password** will be required to perform actions that you have chosen not to openly allow for the PDF, and to place the PDF in Affinity documents. If disabled, anyone can print, modify, copy from, and place the PDF.

Available for: PDF

When enabled, the **Open password** will be required to open the PDF. If disabled, anyone can open the PDF.

Available for: PNG, JPEG, GIF, TIFF, PDF, PSD, SVG, EPS, EXR, HDR, TGA, WEBP, JPEG-XL, Fixed-Layout EPUB

Select which resampling method to use if the image is to be upsampled or downsampled on export. For the PDF, SVG and EPS file formats, this setting is available in the dialog's **Advanced** section.

The following resample settings are available:

*   _Nearest Neighbor_—simple resampling which has the fastest processing time. Use for hard-edge images.
*   _Bilinear_—algorithmic resampling for use when shrinking images.
*   _Bicubic_—algorithmic resampling for use when enlarging images. Resampling is smoother than Bilinear but has a slower processing time.
*   _Lanczos 3_—complex algorithmic resampling which gives the best results but with the longest processing time. Available as 'separable' and 'non-separable'; the latter gives marginally better results, but is slightly slower than 'separable'.

Available for: TIFF

The exported TIFF keeps all layers from the Affinity document. These layers are only readable when the file is opened in Affinity.

Available for: DWG, DXF

Lets you choose how object strokes respond when line weight is adjusted on export, e.g. if a stroke is clamped to the 2.11 mm maximum.

When enabled, the length of dashes scales automatically, like in Affinity. If disabled, dashes stay the same length, similar to AutoCAD's behavior.

Available for: SVG

When enabled, the exported file includes coordinates and dimensions that define the image's view box. If disabled, no view box data is included. The view box matches the export area.

Available for: PNG, JPEG, GIF, TIFF, EXR, HDR, TGA, WEBP, JPEG-XL

By default, displays the native dimensions of your image. Type an alternative width and/or height for the exported image.

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/2Of9JkA5iBiu59zsYBPs12/624225bbbadd88dd99b8ebb8809ce2f7/locked.svg)

![Image 2](https://images.ctfassets.net/3p2fxa94bzao/UvEnvWAPVBpNWYA5Z5r9T/a84b0fe57ee4b92096115fef76957e2a/unlocked.svg)

**Lock aspect ratio**—when enabled, the image's native aspect ratio is honored. If disabled, the exported image's width and height can be set independently.

If your exported design exceeds the maximum dimensions for the file format to which you are exporting, the design will be scaled on export to fit the maximum dimensions. The Export dialog will warn you about this before you proceed.

Available for: PSD

When enabled, the exported file will be compressed where possible but may not be readable by other apps. If disabled, no compression will take place for the exported file.

Available for: EXR

Choose whether to encode Spacial channels (**XYZ** etc) as 16-bit (half float) or 32-bit (full float).

Available for: PDF

When enabled, embedded fonts will only include the glyphs used in the document. If disabled, all glyphs for the used fonts are embedded in the exported file, regardless of whether they appear in the document or not.

Available for: PDF

When enabled, alt text added to objects using the **Tags** panel will be included in the exported file.

Available for: PNG

HDR formats such as PQ, HLG and BT.709 are supported.

32-bit HDR PNGs (PNG specification - Third edition, https://www.w3.org/TR/png-3/) are used for interchanging HDR broadcast imagery in a lossless format. A growing range of video editing apps now support this PNG file format, as well as the Google Chrome web browser.The cICP chunk in this format allows the image to be tagged and processed with various video-centric color spaces (**Primaries**), which is more robust for broadcast workflows where the imagery needs to integrate seamlessly with video content.

Available for: PDF, SVG, EPS, Fixed-Layout EPUB, Reflowable EPUB

Ensures the exported file matches your project's DPI setting.

Available for: PDF, SVG, EPS

Overrides the current document's resolution setting for the export. Set the DPI using the adjacent input box.

Available for: SVG

When enabled, colors in the exported file are expressed as RGB Hex values (therefore reducing file size but less human-readable). If disabled, colors are exported as standard RGB values.

Available for: SVG, EPS

When enabled, objects in the exported file have relative positions for maximum editability. If disabled, object positions are fixed to create a file which is optimized for viewing.

Available for: SVG

When enabled, rasterized areas may be converted to a vector shape with a filled bitmap to give smoother, sharper edges. However, this might not be supported by some apps. If disabled, objects will exist as singular elements within the exported file.

*   [About exporting](https://www.affinity.studio/help/sharing-export/)

How would you rate the help you received from this article?
