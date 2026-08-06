---
title: "Books panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-books-panel/
slug: panels-books-panel
fetched: 2026-08-06
---

# Books panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-books-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Books panel

The Books panel allows you to manage multiple documents as a cohesive publication.

For Mac/Windows: On the **Window** menu, select **Layout > Books**.

Using the **Books** panel, you can:

*   Create books and add documents to them as chapters.
*   Specify the order of chapters.
*   Review and edit the page numbering (pagination) of all chapters.
*   Sync master pages, text styles, document palettes, and table formats from the Style Source Chapter to other chapters.
*   Open chapter documents for editing.
*   Review file and preflight statuses of all chapters.
*   Package/print/export selected chapters or the whole book. Exporting to a PDF, say, creates a single file.

The following options are available on the panel:

*   **Books**—if more than one book is open, select the one you wish to edit from the pop-up menu.
*   **Chapters list**—shows entries for all the chapters you've added to the selected book.
*   **Update Numbers**—updates **Page Numbers**, **List Numbers**, **Note Numbers** or **All Numbers** for continuity across chapters.
*   ![Image 1](https://images.ctfassets.net/3p2fxa94bzao/5bSSRhRZ5jBpy8T5G5BkkV/d975fb461415b6102a61156f6bad45c5/sync_chapters.svg) **Synchronize Chapters**—syncs data from the Style Source Chapter to the selected chapters.
*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/557PZwUf79x4CFvaBlDeZX/df4c79bc23760f650341a53295711e7e/add_chapter.svg) **Add Chapter**—opens a dialog in which you can select one or more documents to add to the book.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3m8ciDtLqf07Yrma1i0j4x/202c1d508104bbb0a1290c5be7725eae/trash_can.svg) **Remove Chapter**—removes the selected chapters from the book.

![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 The following options are available on the **Panel Preferences** menu:

*   **New Book**—creates a new, empty book that is initially unsaved.
*   **Open Book**—allows you to browse to an existing .afbook file and open it.
*   **Save Book**—saves the selected book as an .afbook file, keeping its chapter list and order. (Modified chapters must be saved separately.)
*   **Save Book As**—saves the selected book's state to a new file, which becomes the destination for further saves.
*   **Close Book**—asks whether to save changes to the selected book, if there are any, and closes the book.
*   **Add Chapter**—opens a dialog in which you can select one or more documents to add to the book. (When a document is added, its file is modified. See [Creating Books](https://www.affinity.studio/help/advanced-creating-books/) for more information.)
*   **Open Chapter**—opens the selected chapters for editing.
*   **Remove Chapter**—removes the selected chapters from the book.
*   **Replace Chapter**—with a chapter selected, allows you to swap its document for a different one.
*   **Set Style Source Chapter**—with a chapter selected, sets it as the style source for sync operations.
*   **Synchronize**—syncs data from the Style Source Chapter to the selected chapters.
*   **Synchronize Settings**—choose which data will be synced from the Style Source Chapter: any or all of **Swatches**, **Text Styles**, **Table Formats**, and **Master Pages**.
*   **Save Open Chapters**—saves all open chapters that have unsaved changes.
*   **Close Open Chapters**—closes all open chapters. If any have unsaved changes, for each one you will be asked whether to save before closing.
*   **Page Number Options**—sets the selected chapter's page numbering to either continue from the previous chapter or start at a specific number
*   **Update Numbers**—updates numbering of pages, lists, endnotes (or all three) through your book for continuity across chapters. 
    *   **Scope**—for the selected chapters, choose to update **Page Numbers**, **List Numbers**, **Note Numbers** or **All Numbers**.
    *   **Update Numbers Before Output**—when checked, page, list and note numbers are automatically updated before exporting or printing. When unchecked, numbers must be manually updated by selecting a Scope option.
    *   **Update Tables of Contents Before Output**—when checked, Affinity updates tables of contents before export or print. When unchecked, you must manually update tables of contents.
    *   **Update Index Before Output**—when checked, the book's index is automatically updated before exporting or printing. When unchecked, the index must be manually updated.
    *   **Update Page Numbers Automatically**—when checked, Affinity will auto-update a book's page numbering as chapters and pages are added to or removed from it, for example. When unchecked, page numbers can be manually updated when needed.

*   **Endnotes**—manages endnote bodies whose position is set to **End of Book** in a text frame of your choice. 
    *   **Insert Endnotes**—inserts relevant endnote bodies from all chapters in order at the text insertion point.
    *   **Update Endnotes**—updates endnote bodies from their chapters. Create an insertion point or select the consolidated bodies first.
    *   **Update Endnotes Before Output**—when checked, endnote bodies will be auto-updated before exporting or printing. When unchecked, endnote bodies can be manually updated when needed.

*   **Cross-References**—update cross-references in all chapters of the selected book to display the correct values. 
    *   **Update Cross-References**—immediately updates cross-references.
    *   **Update Cross-References Before Output**—when selected, Affinity will update a book's cross-references when it is printed or exported. When unselected, cross-references are not automatically updated and so may have incorrect values.

*   **Stray Pages**—manage how stray pages are handled in facing-pages books. Choose from the following behaviors: 
    *   **Merge Where Possible**—when checked, where adjacent chapters end and begin with trailing and leading pages, respectively, those pages become a facing-pages spread in the output. When unchecked, the pages are kept separate; they may be single- or facing-page spreads depending on the **Pad** setting.
    *   **Pad**—when checked (and if **Merge Where Possible** does not apply), blank pages may be added to the output, opposite chapters' leading and trailing pages that aren't at the book's start or end, to maintain facing-page spreads throughout. When unchecked (and Merge Where Possible does not apply), single-page spreads are allowed in the output.

*   **Preflight**—runs preflight checks on the selected chapters' documents or, if none are selected, all chapter documents, and updates Preflight Status icons accordingly.
*   **Export**—displays the **Export** dialog to output the current book or the selected chapters, e.g. as a PDF.
*   **Print**—displays the **Print** dialog to output the current book or the selected chapters as a hard copy.
*   For Mac: **Reveal in Finder**—with a chapter selected, opens a Finder window with the corresponding file selected.
*   For Windows: **Show in Explorer**—with a chapter selected, opens a File Explorer window with the corresponding file selected.
*   **Panels**—opens a dialog where you can quickly set the visibility of all panels in the current Studio.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

The following information is displayed, from left to right, on each chapter's entry:

*   **Chapter name**—the name of the chapter's corresponding document.
*   **Page range**—the page numbers of the chapter's first and last pages.
*   **Chapter file status**—an icon that indicates whether the chapter's file is: 
    *   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/jhIj9kApCcix9gX2s5NxE/95ba9f8d2bb41fa78338195e05959bca/ChapterOpen.svg) **Open for edit**—the file is currently open for editing.
    *   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/UUttZRdDkGaJYnXPXyeBS/1b173e5dba229d90922d13459713c81a/chapter_missing.png) **Not found or accessible**—the file may have been moved or deleted, or is stored in a currently unavailable location, open in another app, or marked as read-only.
    *   ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/6FbwEuptwxkjA0snMDE8dh/adac31db318dafe298dd8a6f0e211139/chapter_out_of_date.png) **Out of date**—its timestamp has changed since it was last opened via the Books panel, e.g. it was opened directly.
    *   ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/4J4N1sNgpAZ0c4mZ8OkvXv/78892b49ed4baf604d8762c797327d22/chapter_restricted.png) **Restricted**—the file is a sample document that cannot be printed or exported.
    *   ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/1WvVrJyKvv82XSAGVbVrDO/800efba6eafcea2966edba4c558d572d/chapter_ok.png) **OK**—none of the other statuses currently apply to the file.

*   **Preflight status**—an icon that indicates the chapter has passed preflight checks (green), checks have not yet been performed (gray), or that there are warnings (yellow) or errors (red).

![Image 10](https://images.ctfassets.net/3p2fxa94bzao/1a1tPbg7IwJxO34CMN5zNO/22a12b57c98168a6d0adbca3bd746284/KeyChapter.svg)

 A key icon to the left of one chapter's name indicates it is the **Style Source Chapter** for the purpose of syncing styles and master pages between chapters. The Style Source Chapter is your book's first chapter by default, but you can make it any chapter you wish via the **Panel Preferences** menu 

![Image 11](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

.

*   [About books](https://www.affinity.studio/help/advanced-about-books/)
*   [About pages](https://www.affinity.studio/help/pages-about-pages/)
*   [About master pages](https://www.affinity.studio/help/pages-master-pages/)
*   [Customizing Studios](https://www.affinity.studio/help/workspace-customizing-studios/)

How would you rate the help you received from this article?
