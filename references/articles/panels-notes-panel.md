---
title: "Notes panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-notes-panel/
slug: panels-notes-panel
fetched: 2026-08-06
---

# Notes panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-notes-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Notes panel

The Notes panel allows you to insert footnotes, sidenotes and endnotes into your documents.

For Mac/Windows: On the **Window** menu, select **References > Notes**

The Notes panel also allows you to customize visual attributes of references and note bodies, including the character and paragraph styles applied to them.

Each note has a reference where it's inserted and a note body with the same label. The position of the body in your publication depends on the note type and your chosen settings.

The following options are available on the panel:

*   ![Image 1](https://images.ctfassets.net/3p2fxa94bzao/5UDv4vd3UuwclUaQA7oFjb/c4457d5fb770ac89006f17adb429f42e/note_insert.svg) **Insert Note**—creates a note of the selected type at the insertion point or after selected text.
*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/2LEdEWISNEgqTMz0SIyMg9/605121ec9c8aa014404f85de6dc0fc26/GoToNoteReference.svg) **Go to Reference**—refocuses the document view on the reference for the note body at the insertion point/in which text is selected.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/5mgQeQhvViPsy8sKUFvtzR/2bd356bd9bff492cdbd55f9261c073b3/GoToNoteBody.svg) **Go to Body**—refocuses the document view on the note body for the reference at the insertion point/within the selected text.
*   **Type**—selects the type of note to be inserted or styled: **Footnote**, **Sidenote** or **Endnote**
*   **Scope**—controls the extent to which settings are applied: 
    *   **Document-wide**—applies to all notes of the selected type in the document.
    *   **Custom**—applies only to the note at the insertion point, or to notes in the selection or selected frames.

If a text selection encompasses multiple note references or several endnote bodies, the first one is used when you select **Go to Body** or **Go to Reference**.

*   **Number format**—choose the letters, numbers, or symbols used for note serialization.
*   **Start numbering at**—sets the starting index for note serialization. For example, for the number format _*, †, ‡, …_, setting this to 1 means begin with *, 2 means begin with †, and so on.
*   **Restart every**—sets whether note serialization resets to the first index after each **Frame**, **Page**, **Story**, **Section**, **Document** or **Book**.
*   **Restart numbering now**—begins with the note at the insertion point/the first note in the selection and uses the index you set in **Start numbering at**. (Available when **Scope** is set to _Custom_.)

Notes for which **Restart every** is set to **Book** are numbered as a continuous series across all of a book's chapters. For example, if notes in the first chapter are numbered 1 to 4, notes in the second chapter would start from 5.

*   **In main text**—the following options control the appearance of references in story text: 
    *   **Number text**—sets the sequence of characters used to present note references in main (story) text.
    *   **Number style**—sets the character style applied to note references in main (story) text. From this option, you can also create a new character style or edit the currently selected one.
    *   **Superscript**—sets whether note references are set above the text baseline and at a reduced size.

*   **In note body**—the following options control the appearance of note bodies and their prefixed references: 
    *   **Number text**—sets the sequence of characters used to present note references as a prefix to note bodies.
    *   **Number style**—sets the character style applied to note references where they prefix note bodies. From this option, you can also create a new character style or edit the currently selected one.
    *   **Superscript**—sets whether note references are set above the text baseline and at a reduced size.
    *   **Note body style**—sets the paragraph style applied to note bodies.

*   **Generate hyperlinks**—when checked, the selected note type's references in story text and note bodies are hyperlinked to each other for easier cross-referencing in PDF publications.

*   **Note position**—sets where and how note bodies are presented. Available options depend on the selected note type: 
    *    For footnotes: 
        *   **Below Text**—anchored to the bottom of the referencing story text and spans the frame/column width.
        *   **Bottom of Column**—anchored to the bottom of the text frame, matching the column width, and positioned inside the frame.
        *   **Bottom of Frame**—anchored to the text frame's bottom edge, spans the text frame's width, and positioned inside the frame.
        *   **Below Frame**—anchored to the text frame's bottom edge, spans the text frame's width, and positioned outside the frame.

    *    For sidenotes: 
        *   **Left of Frame**—always to the left of the story text frame, regardless of being on a left or right page.
        *   **Right of Frame**—always to the right of the story text frame, regardless of being on a left or a right page.
        *   **Away From Spine**—in a facing-pages document, on the side of the story text frame that is furthest from the adjoining edge of the spread's pages. Otherwise, to the left of the frame.
        *   **Towards Spine**—in a facing-pages document, on the side of the story text frame nearest the adjoining edge of the spread's pages. Otherwise, to the right of the frame.
        *   **Alternate Sides**—on the opposite side of the story text frame from the previous sidenote in the same frame. The first sidenote body in each linked text frame is positioned: 
            *   away from the spine, if the document has facing pages.
            *   to the story text frame's left side, if the document does not have facing pages.

        *   **Closest Side**—to the side of the story text frame that is closest to the corresponding reference.

    *    For endnotes: 
        *   **End of Story**—after the story text in the last linked text frame.
        *   **Separate Frame**—in an unlinked text frame on the page after the story's last linked text frame.
        *   **Shared Section Frame**—in an unlinked text frame on the section's last page.
        *   **Shared Document Frame**—in an unlinked text frame on the document's last page.
        *   **End of Book**—bodies are displayed and edited in an unlinked text frame in a non-printing _#Booknotes_ section at the end of the document. All of a book's endnote bodies with this setting can be consolidated in a printing text frame of your choice by selecting **Endnotes > Insert Endnotes** from the **Books** panel's **Panel Preferences** menu.

*   **Width**—the width of the area in which sidenote bodies are presented.
*   **Distance from frame**—the distance between the nearest edges of the object that contains the story text and the area in which sidenote bodies are presented.
*   **Min gap before**—the minimum distance in points between story text and the start of footnote/endnote bodies.
*   **Gap between**—the distance between each note body.
*   **Min gap between**—the minimum distance in points between sidenote bodies.
*   **Initial advance**—sets the vertical spacing between the top of the note bodies and the first note body baseline. You can set the distance to the current **Leading**, a **Fixed** value, the font's **Point size**, or another typographic value.
*   **Min advance**—sets a minimum threshold value for initial advance. The value is global, i.e. not tied to the selected Initial Advance option.
*   **Allow split notes**—when selected, footnote/sidenote bodies can begin in one text frame and continue in another. When unselected, Affinity attempts to keep each body's lines together on the same page; story text may reflow, but unwanted whitespace may occur in some text frames.
*   **Pack short notes**—when selected, places short footnotes on the same line when they fit. When unselected, each note starts on a new line.
*   **Short note gap**—sets the horizontal distance between packed short notes.

*   **Rule before**—controls the type of rule affected by the section's other settings: a page's footnotes that start with a new note (**First Note**) or a split note (**Continued Note**), which begins in an earlier linked text frame.
*   **Draw rule**—controls whether a rule visually separates story text and a block of footnotes of the selected rule type.
*   **Stroke style**
    *   **Stroke Color**—sets the rule's color.
    *   **Stroke Style**—sets the rule's width and style.

*   **Left indent**—sets the distance at which the rule starts relative to the text frame's left edge.
*   **Length**—sets the rule's length.
*   **Vertical offset**—sets the rule's relative vertical position.

*   **Title text**—when endnotes are displayed in a different frame than the story text that references them, this setting's value is displayed in the first line of their text frame.
*   **Title style**—applies a paragraph style to the endnotes' title text.

![Image 4](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 The following options are available on the **Panel Preferences** menu:

*   **Update Document Settings from Selected <Note Type>**—makes the selected note's options the default for new notes of the same type in the current document.
*   **Revert Selected <Note Type> to Document Settings**—removes any custom settings from the selected notes.
*   **Revert All <Note Type> to Document Settings**—removes any custom settings from all notes of the type currently selected on the panel.
*   **Reset Document Settings to Factory Defaults**—restores Affinity's default note settings for new notes in the current document.
*   **Save Document Settings as New Defaults**—saves the current document's note settings so they're used as defaults for new documents.
*   **Convert Selection to <Note Type>**—changes the type of notes in your selection to the specified type.
*   **Convert Notes**—opens a dialog where you can choose to convert one type of note to another, across the whole document or within the current selection.
*   **Panels**—opens a dialog where you can quickly set the visibility of all panels in the current Studio.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

*   [About notes](https://www.affinity.studio/help/advanced-about-notes/)
*   [Inserting notes](https://www.affinity.studio/help/advanced-inserting-notes/)
*   [Styling notes](https://www.affinity.studio/help/advanced-styling-notes/)
*   [Hyperlinking notes](https://www.affinity.studio/help/advanced-hyperlinking-notes/)
*   [Customizing Studios](https://www.affinity.studio/help/workspace-customizing-studios/)

How would you rate the help you received from this article?
