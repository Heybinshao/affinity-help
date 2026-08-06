---
title: "Preflight - Affinity Help Center"
source: https://www.affinity.studio/help/sharing-preflight/
slug: sharing-preflight
fetched: 2026-08-06
---

# Preflight - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/sharing-preflight/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Export, share, and publish](https://www.affinity.studio/help/export-share-publish/)
3.   Preflight

Use Affinity's Preflight feature to make sure your document will print or export as intended. A preflight check can be run on demand—e.g. prior to output—or “live” on a continual basis.

When you open an .af file or an old Affinity .afpub file, preflight checking is set to **Live** by default. When you open a PDF or an old Affinity .afdesign or .afphoto file, preflight checking is set to **Never** by default, but you can adjust this manually via the **Preflight** panel.

With preflight enabled, the color of the preflight indicator in the status bar shows whether warnings or errors have been detected in the document.

*   ![Image 1](https://images.ctfassets.net/3p2fxa94bzao/01pC51p7ZPIbHUK8gnSAug/112cd635cbb62145d0a82cac5ebd90e8/preflightIndicatorDisabled.svg)  Grey indicates that preflight is not enabled, i.e. live checks are not being performed.
*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/5XBDfkelnVWfrlc2KiB4uI/f36d68ae1b187298a4be7646179b3bdf/preflightIndicatorOk.svg)  Green indicates that preflight is active and no errors or warnings have been found.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2axPIQLiNiyKGG7Zho9DUg/abde989542aecad1fe24b17f6b1b00ee/preflightIndicatorErrors.svg)  Red indicates that preflight is active and errors that will interrupt export have been found.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/49XOrTHfzsgcrwGNEZFUWN/f254336b0aa74708d67583b31bf24921/preflightIndicatorWarning.svg)  Yellow indicates that preflight is active and issues that won't prevent export have been found.

Hovering over the red or yellow indicator shows the number of errors or warnings found. Selecting the indicator takes you directly to the **Preflight** panel.

The **Preflight** panel uses a default set of checks, which can be customized to your needs using the **Edit profile** function. You can choose the severity level for each issue type, define limits that trigger warnings and errors, and manage how placed documents (e.g. PDFs) are checked.

The **Preflight** panel lists all warnings and errors it finds, allowing you to pinpoint and correct issues where they appear in your document.

The types of items that are listed are determined by the active preflight profile's settings. Two different icons may be shown to indicate severity:

*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/2YKwk3FZYGsWZ8z6wjMKDV/dbdcbf346712ec649f7d4cdcc276790d/preflightWarning.svg)  A yellow icon to the left of an entry is a **warning** of an issue that will not prevent export.
*   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/2Pliq5AJ1KXiiPy32gKszN/080134b9100c8eaf63848a4fd7db05b8/preflightError.svg)  A red icon to the left of an entry indicates an **error** in the document that will interrupt export.

The full list of preflight warnings and errors is as follows:

*   Accessibility Metadata—a series of preflight messages related to the preflight profile's **EPUB (Reflowable)** checks. When **Check accessibility metadata** is enabled, these messages may appear if required information has not been specified on the **Document Metadata** dialog, available on the **File** menu. At least one **Access Mode** item and one **Access Mode Sufficient** item must also be specified. The messages include:
    *   **Document has no accessibility metadata**.
    *   **Flashing hazards are unspecified**.
    *   **Motion hazards are unspecified**.
    *   **No access modes are specified**.
    *   **No access modes sufficient are specified**.
    *   **Sound hazards are unspecified**.

*   **Bleed Hazard**—appears when an object is positioned outside of the bleed zone. You can adjust the safe zone edge via the panel, which will change what preflight checking will identify as a bleed hazard.
*   **Check copy**—appears if a preflight user comment has been attached to an object. Can be used as a reminder to, for example, check final text copy or to check image copyright.
*   **Cross-reference out of date**—appears after making certain changes to your document that require a cross-reference's value to be manually updated. Click **Fix** to update the cross-reference.
*   **Cross-reference target is missing**—appears if the target of a cross-reference has been deleted from the document, e.g. an anchor has been removed.
*   **Cross-reference book target is missing**—appears if the target is in a book chapter that is not open for editing, and so nothing more about the target is known.
*   **Cross-reference target is not a list**—a cross-reference contains a **List Number** subfield but its target is not an item in a numbered or bulleted list.
*   **Cross-reference target is not a note**—a cross-reference contains a **Note Number** subfield but its target is not a footnote, sidenote or endnote.
*   **Cross-reference target is not in a book**—a cross-reference contains a **Chapter Name** subfield but its target is not a book chapter.
*   **Cross-reference expansion includes itself**—a cross-reference contains a **Paragraph Body** or **Numbered Paragraph** subfield whose value includes the cross-reference's text.
*   **Cross-reference target is not in text**—a cross-reference contains a text-based subfield, such as **Paragraph Body**, but its target is not text. For example, the cross-reference is linked to an anchor on a shape or image.
*   **Cross-reference has no string for language**—a cross-reference contains an **Above/Below** subfield but translations have not been set for the text's language. Translations can be set via **Edit Strings** on the **Cross-References** panel's **Panel Preferences** menu.
*   **Cross-reference value is empty**—a cross-reference contains a subfield for which its target provides no value, e.g. a **Paragraph Body** subfield when the cross-reference's target is an empty paragraph. This check is optional and can be disabled by editing the preflight profile, selecting **Cross-References**, and then unchecking **Check for empty values**.
*   **Data Merge has source errors**—appears when there are problems opening or parsing the data source, or when an error in the **Script** section of the **Data Merge Data Viewer** prevents the JavaScript from running.
*   **Data Merge has validation warnings**—appears when criteria defined in the **Process** section of the **Data Merge Data Viewer** trigger a warning. Open the viewer for details.
*   **Data merge sources need updating**—appears when a data record(s) in the external data source has been edited. Click **Fix** to update to the latest records.
*   **The document index needs updating**—can be resolved by using the **Index** panel to update the index.
*   **Field (field name) not found in source (data source file name)**—appears when a row or column in the external data source has either been renamed or deleted.
*   **Fill ink density too high (<Percentage>)** / **Stroke ink density too high (<Percentage>)** / **Text ink density too high (<Percentage>)**—appears when an object uses a color with an ink density over a specified threshold.
*   **Fill uses too rich black (<Percentage>)** / **Stroke uses too rich black (<Percentage>)** / **Text uses too rich black (<Percentage>)**—appears when an object uses a rich black ink density over a specified threshold.
*   **Fill uses CMY** / **Stroke uses CMY** / **Text uses CMY**—appears when an object's Cyan, Magenta or Yellow levels do not conform to the document's expectation of only gray and spot colors.
*   **Frames in flow have mismatched scales**—appears when one or more of a story's text frames has been scaled. To go to the first frame in the linked sequence, double-click the warning, then follow the text flow to locate any frames on which the lower-right handle is solid. To reset the frame's scale, double-click the handle.
*   **Hidden Object**
*   **Hyperlink to Invalid Anchor <anchor name>**—appears where a hyperlink's anchor is missing or has been deleted.
*   **Hyperlink to Invalid Page**—appears where a hyperlink's target page is missing or has been deleted.
*   **Linked resource is missing/Linked resource is out of date**
*   **Mismatched color space (RGB)**
*   **Missing characters (character)**—appears when text uses a glyph that is not present in the currently applied font.
*   **Missing Font**—appears if the document is opened on a device that does not have the used fonts available.
*   **Non-Proportional Scaling**—appears when an object is not proportionally scaled, e.g. when an image has been accidentally squashed.
*   **Object missing Alt Text**—appears when alt text has not been specified for an object and the object has not been marked as decoration. The issue can be resolved using the **Tags** panel.
*   **One or more table of contents entries need updating**—appears when the TOC is out of date because referenced text in the document has been added to, modified or deleted. Click **Fix** to update the TOC and resolve.
*   Optional Metadata—a series of preflight messages related to the preflight profile's **EPUB (Reflowable)** checks. When **Check optional metadata** is enabled, these messages may appear if information has not been specified on the **Fields** panel, under **General** The messages include:
    *   **Document has no author set**.
    *   **Document has no comments set**.
    *   **Document has no copyright terms set**.
    *   **Document has no publisher set**.
    *   **Document has no subject set**.

*   **Overflowing path text**—appears where there is overset text on a path.
*   **Overflowing text frame**—appears where there is overset text within a text frame.
*   **PDF passthrough**—a series of different preflight checks for PDF passthrough. These issues include: 
    *   **Placed PDF has image adjustments applied. The PDF will be rasterized on export.**
    *   **Placed PDF has effects applied. The PDF will be rasterized on export.**
    *   **Placed PDF has transparency applied. The PDF will be rasterized on export.**
    *   **Placed PDF Version (version) is not compatible with the PDF export version. The PDF will be rasterized on export.**
    *   **Placed PDF has objects of a color not compatible with the PDF export version. The PDF will be rasterized on export.**
    *   **Placed PDF is missing or broken.**
    *   **Placed PDF has unsupported page box. The PDF will be rasterized on export.**
    *   **Placed PDF has objects of a color different to the document colorspace. The PDF will still pass through.**

*   **Placed image DPI too low**—appears when an image's DPI is too low for the file, with the image's DPI listed in brackets beside the error.
*   **Spelling Mistake**
*   **Stroke has too complex dash pattern**—appears when a line's dash pattern contains more than 12 entries. For PDF export, dash patterns must have 12 or fewer entries.
*   **Stroke too narrow (Stroke width)**—appears when the stroke width is too narrow.
*   Text patterns—a series of different preflight checks for text patterns that are commonly found in edited or imported copy which may cause inconsistency. These will report as: 
    *   **Multiple spaces**.
    *   **Space after Tab**.
    *   **Space after break**.
    *   **Consecutive breaks**.
    *   **Straight quotes**.
    *   **Ellipsis with full stops**.
    *   **Double hyphen for dash**.

*   **Styles <style> and <style2> both use class name <class>**—appears when two text styles use the same **Class name**in their **Export Tags**settings.
*   **Unnamed Anchor**—appears when an unnamed anchor has been generated, e.g. as a consequence of document content with a text style applied that is used to generate a table of contents.
*   **Unpinned object isn't included in reading order**—relates to the preflight profile's **EPUB (Reflowable)** checks. When **Check unpinned objects** is enabled, this message appears if an image is not pinned and has no tags, meaning it will not be included in the EPUB's reading order. This check acts as a safety net in case the omission is unintended, ensuring images are not accidentally excluded from the output.
*   **Unsupported absolute leading <in style>**—appears when local formatting or a text style has a **Leading override**setting that Flowing EPUB doesn't support.
*   **Unsupported cell pen**—appears when a table cell border has an **Edge Fill**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported cell stroke**—appears when a table cell border has an **Edge Stroke**setting that Flowing EPUB doesn't support. Borders must be solid or use a simple dot or dash pattern for use in EPUB.
*   **Unsupported cell brush**—appears when a table cell has a **Fill**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported decoration fill <in style>**—appears when local formatting or a text style has a **Decoration**with a **Fill**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported decoration pen <in style>**—appears when a **Decoration**has a **Stroke**fill setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported decoration transparency <in style>**—appears when local formatting or a text style uses transparency in a **Decoration**. Transparency is not supported in Flowing EPUB.
*   **Unsupported decoration line style <in style>**—appears when local formatting or a text style has a **Decoration**stroke that Flowing EPUB doesn't support. EPUB supports only solid, dash-dash, and dot-dot line styles, with butt caps and round joins.
*   **Unsupported fill <in style>**—appears when local formatting or a text style has a **Font color**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported highlight <in style>**—appears when local formatting or a text style has a **Background color**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported hyphenation min length <in style>**—appears when local formatting or a text style has a **Minimum word length**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation min prefix <in style>**—appears when local formatting or a text style has a **Minimum prefix**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation min suffix <in style>**—appears when local formatting or a text style has a **Minimum suffix**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation score <in style>**—appears when local formatting or a text style has a **Minimum score**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation zone <in style>**—appears when local formatting or a text style has a **Hyphenation zone**setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation zone capitals <in style>**—appears when local formatting or a text style has a **Capital zone**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation zone column end <in style>**—appears when local formatting or a text style has a **Column end zone**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported hyphenation zone paragraph end <in style>**—appears when local formatting or a text style has a **Paragraph end zone**hyphenation setting that Flowing EPUB doesn't support.
*   **Unsupported keep with previous <in style>**—appears when local formatting or a text style has a **Keep with previous paragraph**setting that Flowing EPUB doesn't support.
*   **Unsupported keep with next <in style>**—appears when local formatting or a text style has a **Keep with next paragraph**setting that Flowing EPUB doesn't support.
*   **Unsupported last line outdent <in style>**—appears when local formatting or a text style has a **Last line outdent**setting that Flowing EPUB doesn't support.
*   **Unsupported leading <in style>**—appears when local formatting or a text style has a **Leading**setting that Flowing EPUB doesn't support.
*   **Unsupported letter spacing <in style>**—appears when local formatting or a text style has a **Tracking**setting that Flowing EPUB doesn't support.
*   **Unsupported manual kerning <in style>**—appears when local formatting or a text style has a **Kerning**setting that Flowing EPUB doesn't support.
*   **Unsupported max consecutive hyphens <in style>**—appears when local formatting or a text style has a **Max consecutive hyphens**setting that Flowing EPUB doesn't support.
*   **Unsupported optical alignment <in style>**—appears when local formatting or a text style has an **Optical Alignment**setting that Flowing EPUB doesn't support.
*   **Unsupported outline <in style>**—appears when local formatting or a text style has an **Outline fill**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported scale <in style>**—appears when local formatting or a text style has a **Horizontal scale**or **Vertical scale**setting that Flowing EPUB doesn't support.
*   **Unsupported shear <in style>**—appears when local formatting or a text style has a **Shear**setting that Flowing EPUB doesn't support.
*   **Unsupported strikeout fill <in style>**—appears when local formatting or a text style has a **Strikethrough fill**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported tab stops <in style>**—appears when local formatting or a text style has a **Tab Stops**setting that Flowing EPUB doesn't support.
*   **Unsupported transparency <in style>**—appears when local formatting or a text style has an **Opacity color**setting that Flowing EPUB doesn't support.
*   **Unsupported underline fill <in style>**—appears when local formatting or a text style has an **Underline fill**setting that Flowing EPUB doesn't support. Fills must be solid for use in EPUB.
*   **Unsupported word spacing <in style>**—appears when local formatting or a text style has a **Word spacing**setting that Flowing EPUB doesn't support.

Some issue types have a **Look inside placed documents** option. Some warnings/errors about placed documents, such as PDF version compatibility, can be fixed from the parent document but others, such as missing fonts in a placed PDF, require you to have access to the placed document's source file.

If enabled, preflight checks are performed on print and export. If the document has errors (not warnings), a dialog lets you cancel the process so you can review the errors on the **Preflight** panel.

This feature is only available in Affinity for desktop.

Preflight user comments can be added to objects in your publication, creating a custom check to be made prior to print or export. This has many uses:

*   Check specific layers are hidden or visible at export.
*   Check text and picture frames are populated.
*   Check text frames with placeholder text that may need replacing.
*   Check images that need copyright checking or creative approval.
*   Check images using temporary colors.
*   Check that copy is accurate.
*   Verify that copy is approved.

When a user comment is added, it is listed on the **Preflight** panel to be checked later. It can be ignored or cleared if it's no longer needed.

*   On the **Preflight** panel, set the **Check** option to when you want preflight checks to be performed: 
    *   **Never**—Only when you click **Check Now** on the panel.
    *   **Export**—Just prior to export.
    *   **Live**—Actively while you work.

*   On the **Preflight** panel, click **Check Now**.

*   On the **Preflight** panel, click **Profile**![Image 7](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg) , then select **Edit profile**.
*   On the dialog that appears: 
    1.   For each issue type, set the **Warning Level** and other options as needed.
    2.   Click **Close**.

The panel's **Profile** option will show _Custom_.

*   On the **Preflight** panel, click **Profile**![Image 8](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg)  and select **Create preset**.
*   On the dialog that appears: 
    1.   Type a name for the preset.
    2.   Click **OK**.

The panel's **Profile** option will show the name of your preset.

*   On the **Preflight** panel, click **Profile**, then select **Edit profile**.
*   On the dialog that appears: 
    1.   Select **Bleed Hazard**.
    2.   Set **Safe Zone Edge** to _Trim Box_, _Mirror Bleed_, or _Custom_.
    3.   (Optional) If you selected Custom, set **Custom Safe Zone** as needed.
    4.   Click **Close**

*   Hover over the issue on the **Preflight** panel.
*   (Optional) To go to the issue's location in the document, double-click its entry on the panel.
*   (Optional) If an issue displays a **Fix** button—only some issue types do—click it to resolve the issue immediately.

In the document view or on the **Layers** panel:

1.   On the object or layer group you want to comment on, **^(ctrl)**-click (Mac) / **right**-click (Windows), then select **Preflight Comment > Set**.
2.   On the dialog that appears: 
    1.   Type a comment in the box.
    2.   Click **OK**.

In the document view or on the **Layers** panel:

1.   On the object or layer group that has the unwanted user comment, **^(ctrl)**-click (Mac) / **right**-click (Windows), then select **Preflight Comment > Clear**.

*   [Creating new documents](https://www.affinity.studio/help/get-started-new-document/)
*   [Publishing PDF files](https://www.affinity.studio/help/sharing-publish-pdffiles/)

How would you rate the help you received from this article?
