---
title: "About EPUB - Affinity Help Center"
source: https://www.affinity.studio/help/sharing-about-epub/
slug: sharing-about-epub
fetched: 2026-08-06
---

# About EPUB - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/sharing-about-epub/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Export, share, and publish](https://www.affinity.studio/help/export-share-publish/)
3.   About EPUB

Affinity lets you export your publication to the EPUB file format, an open standard for electronic publications. It supports both EPUB types: Fixed-Layout and Reflowable.

EPUB can be viewed in many places, including:

*   Google Play Books (Android, iPhone, iPad)
*   Apple Books (Mac, iPad, iPhone)
*   Thorium (Mac, Windows, Linux)
*   Colibrio Reader (Android)
*   Rakuten Kobo devices

Amazon Kindle devices do not natively support EPUB. Some models allow EPUBs to be uploaded/sideloaded, but convert them to Amazon's own format. If your publication does not look as expected on a Kindle device, refer to Amazon's documentation for support.

Choose Fixed-Layout EPUB when you want to ensure the user sees your design as intended, regardless of the device they're using. On small devices like smartphones, they'll likely need to zoom in and pan around to read everything.

This type of EPUB is suited to publications that lean heavily on designed page layouts and imagery, such as:

*   Lookbooks
*   Manuals with complex diagrams
*   Comics and graphic novels
*   Magazines
*   Recipe books

![Image 1: Example of exporting a Fixed-Layout EPUB.](https://images.ctfassets.net/3p2fxa94bzao/7gXZBhlVxBeLJrAe39FhSB/bd38cfea38194eb5cb3de13a5f74104a/epubFixedLayoutConcept.png)

Fixed-Layout EPUB maintain your layout, but readers may need to zoom and pan to read.

Consider the devices your audience will use. Page proportions, rather than physical dimensions, matter most—layouts scale to fit the screen or window while maintaining their aspect ratio. Single pages fit well in portrait mode on tablets, while Fixed-Layout EPUB spreads work well in landscape on laptops and monitors. When exporting, set appropriate dimensions to balance image quality and file size..

Fixed-Layout EPUB is sometimes referred to as EPUB FXL.

Choose Reflowable EPUB when your content is text-heavy. For reflowable content, instead of your content being presented on fixed pages, it will automatically adapt to the screen size and the reader's settings. Text and images reflow to fill the screen.

This type of EPUB is suited to:

*   Novels
*   Reports, such as in academia and business
*   Manuals that are mostly textual

Affinity can embed your choice of fonts, but bear in mind that the reader may override them, due to personal preference or accessibility needs. For example, in Apple Books, the user can choose a different font family, font size, leading, and margins.

Images that you pin to text in Affinity will appear as inline images at the same position in your EPUB.

Bear in mind that what's on page 50 for one person may be on a different page for another. This may affect things like the phrasing of cross-references. If your content needs adapting for reflowable EPUB, you may need to work on a copy of your document separate from your print edition.

Page markers are also added to EPUB output to improve accessibility—readers using assistive technology such as screen or braille readers can match their position to the printed book.

![Image 2: Example of a reflowable EPUB.](https://images.ctfassets.net/3p2fxa94bzao/11wHzpg8CLzbLgD2XuEdzq/31a0857a827bf6f72bde8c4f486a083e/epubReflowableConcept.png)

A reflowable EPUB as it might appear on two different devices.

Reflowable EPUB is sometimes referred to as _Reflowing_ EPUB.

You don't need to do anything special to be able to export an Affinity document to EPUB, but you'll get better results by making use of the following Affinity features.

For Fixed-Layout and Reflowable EPUB:

*   **Text Styles** panel—to apply formatting in a way that's easy to maintain (just like in any document) and results in efficient CSS in EPUB output.
*   **Tags** panel—to set alt (alternative) text on design elements other than text so assistive technologies can describe it.
*   **Fields** panel—to set metadata: title, author, publisher, ISBN, subject, illustrator, revision, copyright, and comments. These values are written to the EPUB's package metadata and may be displayed by EPUB readers or used by publishing platforms. For example, Apple Books uses the **Revision** value as the version identifier when submitting updates.
*   **Document Metadata** dialog—to set metadata that declares your EPUB's accessibility support, hazards, access modes, and certification. (Available on the File menu.)
*   **Reading Order** panel—to define the logical reading order of content (both text and alt text descriptions) for use by assistive technologies. You can also choose to omit content, such as pull-quotes.

For Reflowable EPUB:

*   **EPUB** panel—to add custom CSS (cascading stylesheet) files to your EPUB output.

Affinity exports EPUB 3.0 files. Many modern readers support this format. The Export dialog includes presets for Fixed-Layout and reflowable EPUBs. You can also adjust a range of settings.

Before publishing, check your document and export settings carefully. Make sure you've specified metadata, a reading order, and accessibility information.

Choose whether to include a cover page. The page can be a rasterized copy of a document page, or it can be a pre-prepared image.

Reflowable EPUB has settings that affect how your document's text and formatting are handled, such as whether list formatting is converted to regular text.

Make sure your exported EPUB meets the requirements of your chosen publishing platform. Apple Books, for example, limits each image to 5.6 million pixels. If your images are larger, downsample them during export.

For a complete reference to available EPUB export settings, refer to the Export settings topic.

EPUB exports include the fonts you've used. They are lightly encrypted, which stops them being used outside the EPUB.

Check your compliance with the licensing terms of all fonts used in your document. Many fonts and vendors require you to purchase a specific license to allow fonts to be included in ebooks.

EPUB files you export do not use DRM (Digital Rights Management).

Some publishing platforms add DRM when you upload.

Test EPUBs thoroughly before publishing:

*   Preview on at least two devices that use different rendering engines (e.g. Apple Books and Thorium).
*   Use EPUBCheck (https://www.w3.org/publishing/epubcheck/), the official W3C tool, to validate your EPUBs. Many platforms require a pass before publishing. EPUBCheck is a command-line tool. If you prefer a graphical interface, the W3C lists several options, including the popular Pagina EPUB-Checker (https://www.w3.org/publishing/epubcheck/docs/apps-and-tools/#epubcheck-apps).
*   Follow WCAG (Web Content Accessibility Guidelines, https://www.w3.org/WAI/standards-guidelines/wcag/) for alt text and use of color, and check accessibility with Ace by DAISY (https://daisy.org/activities/software/ace/).

You can also preview EPUB files in a web browser using tools such as Colibrio Vanilla Reader (https://demo.colibrio.com/), which demonstrates EPUB rendering and accessibility features.

1.   On the **File** menu, select **Export > Export**.
2.   On the dialog that appears: 
    1.   On the left, select a preset from the **EPUB (Fixed Layout)** or **EPUB (Reflowable)** section.
    2.   (Optional) On the right, adjust settings as needed.
    3.   (Optional) At the bottom right, if you want to open the file's location after export, enable **Show in Finder** (Mac) / **Show in Explorer** (Windows).
    4.   Click **Export**.
    5.   Name the file, choose where to save it, then click **Save**.

1.   On the **File** menu, select **Document Metadata**.
2.   On the dialog that appears: 
    1.   Enable or disable options as needed to inform EPUB readers about accessibility features, hazards, and certification of your publication: 
        *   **Accessibility Features**—declares support your content provides. For example, you might include **Table of Contents**, **Index**, and **Reading Order** if the corresponding Affinity features were used in your publication.
        *   **Accessibility Hazards**—declares risks that your content might present for some users. For example, you might include _Flashing_ if fine detail in a raster image might produce a flickering effect when scrolled.
        *   **Access Modes**—declares the default nature of the content as designed. Enable all that apply. For example, **Textual** for text content and **Visual** for images.
        *   **Access Modes Sufficient**—declares the mode (or combination of modes) that's _enough_ for the reader to grasp the full meaning. For example, if you've added alt text, someone using a screen reader can still understand the content without seeing the pictures.
        *   **Accessibility (General)**—declares your publication's conformance level, the organization that certified it, and a link to the certificate. You can also include a human-readable **Accessibility Summary** for supplementary plain-language notes.

    2.   Click **OK**.

On the Text Styles panel, for each text style that's used in your document:

1.   On the text style's **Options** menu![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg) , select **Edit <style name>**.
2.   On the dialog that appears: 
    1.   On the left, select **Export Tags**.
    2.   On the right, under **EPUB**: 
        1.   Set **Export Tag** to the HTML tag that best represents the styled text's hierarchical place. Affinity's built-in Heading 1 and Heading 2 styles export as _H1_ and _H2_. The Body style exports as _P_. Any style set to _[No change]_ gets its setting from the style it's based on.You can enter a different valid HTML tag to indicate the meaning of text in this style, e.g. _abbr_ for abbreviations or acronyms, or _cite_ for short citations such as book titles. 
        2.   (Optional) To add a custom CSS class name to the text's HTML, enable **Include class in HTML**, then set the **Class name** to use. This is useful when working with custom CSS added with the **EPUB** panel.
        3.   (Optional) If you added a CSS class name, enable **Emit CSS** to generate a CSS rule-set from your text style's settings. Disable it if you'll style it using a CSS file added to the EPUB panel.

*   [Fixed-Layout EPUB](https://www.affinity.studio/help/sharing-fixed-layout-epub/)
*   [Reflowing EPUB](https://www.affinity.studio/help/sharing-flowing-epub/)
*   [Pinning panel](https://www.affinity.studio/help/panels-pinning-panel/)
*   [Text Styles panel](https://www.affinity.studio/help/panels-text-styles-panel/)
*   [Tags panel](https://www.affinity.studio/help/panels-tags-panel/)
*   [Fields panel](https://www.affinity.studio/help/panels-fields-panel/)
*   [EPUB panel](https://www.affinity.studio/help/panels-epub-panel/)
*   [Reading Order panel](https://www.affinity.studio/help/panels-reading-order-panel/)
*   [Export settings](https://www.affinity.studio/help/sharing-export-settings/)

How would you rate the help you received from this article?
