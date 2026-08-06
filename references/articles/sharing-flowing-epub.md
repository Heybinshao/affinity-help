---
title: "Reflowable EPUB - Affinity Help Center"
source: https://www.affinity.studio/help/sharing-flowing-epub/
slug: sharing-flowing-epub
fetched: 2026-08-06
---

# Reflowable EPUB - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/sharing-flowing-epub/

Disabling Generate CSS during export means no CSS is generated for any text styles, even if Emit CSS is enabled.

[Skip to main content](https://www.affinity.studio/help/sharing-flowing-epub/#_r_0_)

[![Image 1](https://content-management-files.canva.com/78303f82-4688-4614-99c7-ad7970d208a9/affinity_logotype_white_min.svg)](https://www.affinity.studio/)

*   Product    

*   Discover    

*   [Help](https://www.affinity.studio/help)

[Get Affinity](https://www.affinity.studio/get-affinity)

[![Image 2](https://content-management-files.canva.com/b916d6a5-3b78-490b-a56a-673b7dc606d0/affinity_symbol_white_min.svg)](https://www.affinity.studio/)

Submit Search

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Export, share, and publish](https://www.affinity.studio/help/export-share-publish/)
3.   Reflowable EPUB

# Reflowable EPUB

Use the Reflowable EPUB file format when you want content to adapt to the device or app your readers use.

If you're new to EPUB in Affinity, read the "About EPUB" topic first. It covers when to use each EPUB type, how to export, and how to test your files.

With a Reflowable EPUB, you need to take extra steps to prepare your content for a good reading experience.

[](https://www.affinity.studio/help/sharing-flowing-epub/#positioning-images)

## Positioning images

Make sure images appear in the correct place within your EPUB's text. Use the Pinning panel to set an image to float with text. Then drag the pin where you want the image to appear.

[](https://www.affinity.studio/help/sharing-flowing-epub/#navigating-a-reflowable-epub)

## Navigating a Reflowable EPUB

To help users navigate a Reflowable EPUB, Affinity can include your publication's table of contents (TOC) as a navigation document. The navigation document is an interactive TOC that readers can open at any time with a click or a tap.

To create one, use the Table of Contents panel as you would for a print document. Then set the TOC type to _EPUB: Primary_ so Affinity uses it to create a navigation document in your EPUB.

You can also add supplementary TOCs that list your EPUB's images and tables. Note that not all EPUB readers provide access to these.

[](https://www.affinity.studio/help/sharing-flowing-epub/#setting-a-reading-order)

## Setting a reading order

Check the order of items on the Reading Order panel and adjust as needed. This ensures all text and alt text is presented in a logical sequence for screen readers. The panel also lets you exclude objects you don't want presented, such as pull-quotes.

Reading order defaults to top-to-bottom on the page. Items can be reordered by dragging, or an item can be excluded by clicking the check mark on its entry.

[](https://www.affinity.studio/help/sharing-flowing-epub/#advanced-text-styling)

## Advanced text styling

When you export to Reflowable EPUB, Affinity encloses text in HTML tags based on its text style. This helps EPUB readers and assistive technologies to understand the structure.

Styles are applied to text in EPUBs using CSS classes. Affinity automatically translates your document's text styling to CSS on export unless instructed not to. You may want to use external CSS for Reflowable EPUB instead&#8212;for example, to adapt margins or spacing on smaller screens.

To apply further presentation rules, add your own CSS files through the EPUB panel. You can link these files or embed them in your Affinity document.

[](https://www.affinity.studio/help/sharing-flowing-epub/#how-to-export-a-reflowable-epub)

### How to export a Reflowable EPUB

Desktop app

1.   On the **File** menu, select **Export > Export**.
2.   On the dialog that appears: 
    1.   On the left, select an **EPUB (Fixed Layout)**or **EPUB (Reflowable)**preset.
    2.   (Optional) On the right, adjust settings.
    3.   (Optional) At the bottom right, enable **Show in Finder**(Mac) / **Show in Explorer**(Windows) to open the exported file's location.
    4.   Click **Export**.
    5.   Name the file, choose where to save it, then click **Save**.

[](https://www.affinity.studio/help/sharing-flowing-epub/#how-to-add-a-table-of-contents-or-list-of-images-tables-to-your-reflowable-epub)

### How to add a table of contents or list of images/tables to your Reflowable EPUB

Desktop app

With a TOC already inserted into your document's text:

1.   Create an insertion point within the TOC's text.
2.   On the **Table of Contents** panel, set **Type** according to how you want the TOC's content to be included in your EPUB's navigation document: 
    *   **EPUB: Primary**—to include as a table of contents.
    *   **EPUB: Images**—to include as a list of illustrations.
    *   **EPUB: Tables**—to include as a list of tables.

[](https://www.affinity.studio/help/sharing-flowing-epub/#how-to-set-html-tags-and-css-classes-for-your-text-styles)

### How to set HTML tags and CSS classes for your text styles

Desktop app

1.   On the **Text Styles** panel, click on the required style's options menu   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg)        and select **Edit "<style name>"**.
2.   On the dialog that appears: 
    1.   Select **Export Tags**.
    2.   Under **EPUB**: 
        1.   Set **Export Tag** as needed.  Affinity's built-in Heading 1 and Heading 2 styles export as _H1_ and _H2_. The Body style exports as _P_. Any style set to _[No change]_ gets its setting from the style it's based on.    
        2.   (Optional) Enable **Include class in HTML**, then do the following:
            1.   Set a **Class name**to add to HTML elements for this text style.
            2.   Disable **Emit CSS**if you plan to define the class in a separate CSS file via the EPUB panel.

    3.   Click **OK**.

Disabling **Generate CSS** during export means no CSS is generated for any text styles, even if **Emit CSS** is enabled.

[](https://www.affinity.studio/help/sharing-flowing-epub/#how-to-set-a-css-class-for-your-images)

### How to set a CSS class for your images

Desktop app

1.   Select one or more picture frames on the page.
2.   On the **Tags** panel, type the required class name in the **EPUB Class** box.

[](https://www.affinity.studio/help/sharing-flowing-epub/#how-to-add-custom-css-to-your-reflowable-epub)

### How to add custom CSS to your reflowable EPUB

Desktop app

On the **EPUB** panel:

1.   (Optional) Enable **Embed on add**to store a copy of your CSS file in your document.
2.   Click **Add CSS File**  ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/3ClTCf0TfFFNLrNypEgdf3/af78c7b52d68eea07490c39dffdcad50/add_item_list.svg)       .
3.   Select your CSS file, then click **Open**.

You can add more than one CSS file. The order they appear on the EPUB panel determines the order they are applied in the EPUB.

[](https://www.affinity.studio/help/sharing-flowing-epub/#see-also:)

#### SEE ALSO:

*   [About EPUB](https://www.affinity.studio/help/sharing-about-epub/)
*   [Pinning panel](https://www.affinity.studio/help/panels-pinning-panel/)
*   [Text Styles panel](https://www.affinity.studio/help/panels-text-styles-panel/)
*   [Tags panel](https://www.affinity.studio/help/panels-tags-panel/)
*   [Table of Contents panel](https://www.affinity.studio/help/panels-toc-panel/)
*   [EPUB panel](https://www.affinity.studio/help/panels-epub-panel/)
*   [Reading Order panel](https://www.affinity.studio/help/panels-reading-order-panel/)

How would you rate the help you received from this article?

Good

Not so good

*   
    *   Product

    *   [Get Affinity](https://www.affinity.studio/get-affinity)
    *   [Graphic design](https://www.affinity.studio/graphic-design-software)
    *   [Photo editing](https://www.affinity.studio/photo-editing-software)
    *   [Page layout](https://www.affinity.studio/page-layout-software)
    *   [Canva integrations](https://www.affinity.studio/canva-integrations)
    *   [Product integrations](https://www.affinity.studio/integrations)

*   
    *   Discover

    *   [Inspired.af](https://www.affinity.studio/blog)
    *   [Spotlight](https://www.affinity.studio/spotlight)
    *   [Learning resources](https://www.affinity.studio/resources)
    *   [Press](https://www.canva.com/newsroom/news/all-new-affinity)

*   
    *   Help

    *   [Help Center](https://www.affinity.studio/help)
    *   [Affinity V2](https://affinity.serif.com/v2/)
    *   [Affinity V2 account](https://store.serif.com/sign-in/)
    *   [April 2026 update](https://www.affinity.studio/blog/affinity-update-april-2026)
    *   [Release notes](https://www.affinity.studio/help/release-notes/)

*   
    *   Connect

    *   [About](https://www.affinity.studio/about)
    *   [Careers](https://www.lifeatcanva.com/)
    *   [Contact Sales](https://www.canva.com/contact-sales/affinity/)

*   Product 

    *   [Get Affinity](https://www.affinity.studio/get-affinity)
    *   [Graphic design](https://www.affinity.studio/graphic-design-software)
    *   [Photo editing](https://www.affinity.studio/photo-editing-software)
    *   [Page layout](https://www.affinity.studio/page-layout-software)
    *   [Canva integrations](https://www.affinity.studio/canva-integrations)
    *   [Product integrations](https://www.affinity.studio/integrations)

*   Discover 

    *   [Inspired.af](https://www.affinity.studio/blog)
    *   [Spotlight](https://www.affinity.studio/spotlight)
    *   [Learning resources](https://www.affinity.studio/resources)
    *   [Press](https://www.canva.com/newsroom/news/all-new-affinity)

*   Help 

    *   [Help Center](https://www.affinity.studio/help)
    *   [Affinity V2](https://affinity.serif.com/v2/)
    *   [Affinity V2 account](https://store.serif.com/sign-in/)
    *   [April 2026 update](https://www.affinity.studio/blog/affinity-update-april-2026)
    *   [Release notes](https://www.affinity.studio/help/release-notes/)

*   Connect 

    *   [About](https://www.affinity.studio/about)
    *   [Careers](https://www.lifeatcanva.com/)
    *   [Contact Sales](https://www.canva.com/contact-sales/affinity/)

English (US)

*   [![Image 5: Instagram](https://content-management-files.canva.com/42a74cd5-ccc1-43f4-847b-cfee15b387d6/social_instagram.svg)](https://www.instagram.com/affinity/)
*   [![Image 6: Facebook](https://content-management-files.canva.com/c0ee217b-1e52-423a-95cb-6674227da28c/social_facebook.svg)](https://www.facebook.com/affinity)
*   [![Image 7: Threads](https://content-management-files.canva.com/5a46d885-129b-44bc-9bb5-91a1cd24519a/social_threads.svg)](https://www.threads.com/@affinity)
*   [![Image 8: Discord](https://content-management-files.canva.com/4c86f6ba-0400-48aa-b33b-d1ac6e06406f/social_discord.svg)](https://affin.link/dc)
*   [![Image 9: TikTok](https://content-management-files.canva.com/c38ff714-7599-4dc5-869a-7bc1553075e5/social_tiktok.svg)](https://www.tiktok.com/@weareaffinity)
*   [![Image 10: X](https://content-management-files.canva.com/1c162bcb-f637-4d23-ac3f-909ebf33f8c0/social_twitter.svg)](https://x.com/Affinity)
*   [![Image 11: Youtube](https://content-management-files.canva.com/719b9b23-2ce5-4dcf-8487-d81d4fc52d81/social_youtube.svg)](https://www.youtube.com/AffinitySuite)

*   [Privacy](https://www.canva.com/policies/privacy-policy/)
*   [Terms & Conditions](https://www.canva.com/policies/)
*   © 2026 All Rights Reserved, Affinity 

Show main menu

Suggestions will appear below the field as you type

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

## Affinity Cookies

Affinity is a Canva product, and Canva uses essential cookies to make this site work. We'd like to use other cookies to improve and personalise your visit, tailor ads you see from us on Affinity and partner sites, and to analyze our website's performance, but only if you accept. Learn more about your choices in the [Canva cookies policy.](https://www.canva.com/policies/cookies-policy/)

Manage Cookies Accept All

![Image 12: Affinity Logo](https://cdn-au.onetrust.com/logos/3dbea99f-abc0-4dbd-bcd7-8f6dfcaea28d/019a2649-863c-7345-9b60-9a618abba327/5c38b3e1-3c43-4eda-b904-88377c9b9c2e/full-logo.png)

## Manage Cookies

Cookies and similar technologies collect certain information about how you’re using our website. Some of them are essential, and without them this affinity.studio website might not work. But others are optional, and you get to choose whether we use them or not. 

 Hungry for more? 

[Read our full Cookie policy here.](https://www.canva.com/policies/cookies-policy/)

Allow All

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work.

Cookies Details

#### Performance Cookies

- [x] Performance Cookies 

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Cookies Details

#### Targeting Cookies

- [x] Targeting Cookies 

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Cookies Details

### Learn More

Clear
*   - [x] checkbox label label 

Apply Cancel

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Reject All Confirm My Choices

[![Image 13: Powered by Onetrust](https://cdn-au.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
