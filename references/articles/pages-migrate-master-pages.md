---
title: "Migrating edited master page content - Affinity Help Center"
source: https://www.affinity.studio/help/pages-migrate-master-pages/
slug: pages-migrate-master-pages
fetched: 2026-08-06
---

# Migrating edited master page content - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/pages-migrate-master-pages/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Migrating edited master page content

If you've added content to text or picture frames that are master page objects, it will be migrated by default when replacing your master page(s) with a new master page.

These master pages are considered 'smart' because they help retain your valuable content when you replace them—for example, after a design change to the master page that shouldn't affect page content.

![Image 1: Migrate master pages](https://images.ctfassets.net/3p2fxa94bzao/6qBHZXLdkSwsG1QkKh82Zh/494f095267e17403683dedd017bd307d/masterpages_migrate.jpg)

Top: Master page with placeholder content Bottom Left: Publication page showing edited master page frame content (turquoise) and static master page content (dark gray) Bottom right: New master page's objects (blue) have replaced old master page objects (gray); edited master page frame content is migrated and retained (red).

Smart master page layouts affect where and how images and text are arranged on a page or spread. Master page objects can be arranged to fit a new layout when master page content is migrated, as shown below.

![Image 2: After migration](https://images.ctfassets.net/3p2fxa94bzao/6Sz0pNxNU5ROpXqb70GTup/c954d2cb733c3a6ba37f3c767692616c/smartmaster_after.png)

Master page layouts (shown above) can completely change how master page content (shown below) is arranged on migration. This allows you to easily revamp the look of your pages and spreads while retaining all of your valuable content.

![Image 3: Before migration](https://images.ctfassets.net/3p2fxa94bzao/6mECGgkOTMYUKgZWFlLchR/4025e1ecca5d33e9267ef6aeaf01031d/smartmaster_before.png)

Master page layouts (shown above) can completely change how master page content (shown below) is arranged on migration. This allows you to easily revamp the look of your pages and spreads while retaining all of your valuable content.

Empty or unedited master page frames will not be migrated.

When a new master page replaces an already applied master page, and content has been added to frames from the existing master, Affinity determines the best destination for each piece of content.

*   To determine the best match between frames, it considers these attributes in order: 
    *   A frame from the same master. (This happens if you have nested masters.)
    *   A frame whose layer has the same name.
    *   The frame that is closest in size and position.

*   Frames are ignored if their layers—or their parent layers—are locked. So, if you have fixed text in a logo or footer, it's recommended to lock the corresponding layers to prevent them being considered.
*   It also skips pairings where both frames' layers are named but the names don't match.
*   If there aren't enough frames on the new master to transfer everything, any frames from the old master that can't be matched are converted to page content.

When performing an action that will move pages, you can choose one of several options to determine how applied master pages and content migration are affected.

For example, you might insert a new single page into a document with facing pages, causing later left pages to become right pages and vice versa.

Some edits you perform will affect all pages after the pages being moved. You can avoid unwanted consequences, such as losing detached edits, by disabling **Reflow Pages**.

The relevant options are on the Pages panel's preferences menu, under **Page Move Options**:

*   **Split Masters**—Any publication page that is moved retains the specific page of its master for its previous position within a spread.For example, a left page that becomes a right page will continue to have its master's left page applied to it, and vice versa.This option is helpful when you will be performing several actions that may temporarily result in pages changing position within spreads.
*   **Move Master Content**—Any publication page that is moved has the page of its master for its new position within a spread applied to it.Affinity will try to preserve content but you may end up with clashes, such as when you have detached the master to make local edits to an object's attributes.Modified inherited objects—e.g. a frame you've added content to—are moved with the page, along with any other content not from the master. Inherited objects that weren't modified are replaced with the 'correct' master page content for the spread page they end up on.For example, after a page is moved, it may contain a copy of an inherited text frame with content that was edited at the page's previous position, and a copy of the unmodified text frame from its applied master. In such situations, you'll need to manually remove the one you don't want.This option matches Affinity's behavior in old versions.
*   **Reapply Masters**—Any publication page that is moved has the master page that corresponds to its new position within a spread applied to it.Local edits to text and framed pictures are always retained but edits to object attributes, such as strokes, may be lost.This option works best with masters that contain alternative layouts for the same content on each of their pages.
*   **Anchor Toward Spine**—This complementary option controls the positioning of objects when a page moves from one side of the spine to the other. The option is located alongside the migration behaviors on the Page Move Options menu.When enabled, objects maintain their distance from the spine. When disabled, objects maintain their absolute position on the page.If your document has symmetrical margins about the spine but different values for Inner and Outer, Anchor Towards Spine helps keep things aligned with those margins.

If objects aligned to an outer page edge unexpectedly move to align to the opposite edge, pin the object to maintain the required alignment. 

1.   On the Pages panel's **Panel Preferences** menu ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg) , hover over **Page Move Options**.
2.   On the menu that appears, choose options that best fit your needs, based on the page operation you will perform and your document content: 
    *   Select the required master migration behavior: **Split Masters**, **Move Master Content**, or **Reapply Masters**.
    *   (Optional but recommended) Disable **Reflow Pages** to protect spreads, such as to prevent the loss of any detached edits you've made to applied masters.
    *   (Optional) If the page operation you perform will cause objects to move to the other side of the spine: 
        *   Enable **Anchor Toward Spine** to maintain their distance from the spine.
        *   Disable Anchor Toward Spine to maintain their absolute positions.

1.   On the **Pages** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) a publication page and choose **Apply Master**.
2.    On the dialog that appears: 
    1.   Select the master page to apply and the pages to apply it to.
    2.   Enable **Replace Existing**.
    3.   Set **Content** to **Migrate** to retain content.
    4.   Select **OK**.

If you drag and drop a replacement master page, any edited frame content will be migrated automatically.

For frames of the same type that will overlap, the position and size of the new master page frames are used, but the edited frame content is retained and will populate the new frames.

1.   On the **Pages** panel, **^(ctrl)**-click (Mac) / **right**-click (Windows) a publication page and select **Apply Master**.
2.    On the dialog that appears: 
    1.   Select the master page to apply and the pages to apply it to.
    2.   Enable **Replace Existing**.
    3.   Set **Content** to **Clear** to remove content.
    4.   Select **OK**.

*   [About master pages](https://www.affinity.studio/help/pages-master-pages/)
*   [Applying master pages](https://www.affinity.studio/help/pages-apply-master-pages/)
*   [Detaching and linking master pages](https://www.affinity.studio/help/pages-detach-link-master-pages/)
*   [Pages panel](https://www.affinity.studio/help/panels-pages-panel/)
*   [Locking](https://www.affinity.studio/help/object-control-locking/)

How would you rate the help you received from this article?
