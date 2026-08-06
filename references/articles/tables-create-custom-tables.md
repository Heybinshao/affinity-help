---
title: "Creating table formats - Affinity Help Center"
source: https://www.affinity.studio/help/tables-create-custom-tables/
slug: tables-create-custom-tables
fetched: 2026-08-06
---

# Creating table formats - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/tables-create-custom-tables/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Creating table formats

You can create and store table formatting, allowing it to be applied to multiple tables throughout your document.

A table format is a template. It stores the underlying structure and formatting for a table, but not its content. You can apply a table format to many tables. This ensures consistent design.

![Image 1: Custom table formatting](https://images.ctfassets.net/3p2fxa94bzao/3cOJHoNlxl2n5XSRc0lGgY/9adf93db2ef1ef6bfbfe29f8bca1fb72/customtable.png)

You can create a table format from an existing table. Or, start from scratch using a dialog.

A table's structure consists of rows and columns. In many tables, some of the outermost rows and columns serve as a header or footer. Headers and footers are of fixed position.

![Image 2: A table with header and footer rows and a header column](https://images.ctfassets.net/3p2fxa94bzao/7bANqBgM3ng48vSGhjdGj0/926474f0215088fd335a3f785046ae12/table_structure.png)

A table with header and footer rows and a header column.

If a table format is created from a table formatted like the example above, Affinity would infer the following, based on outer rows and columns having fill colors:

*   Rows 1 and 2 are header rows.
*   Row 6 is a footer row.
*   Column A is a header column.
*   Cells from B3 to E6 are the table body.

Formatting applied to the table body, such as the alternating row colors shown in rows 3 and 4 above, is repeated when you add rows or columns.

*   On the **Window** menu, select **Table > Table Formats**.

1.   Select the table.
2.   On the **Table Formats** panel's **Preferences** menu ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg) , select **Add Format from Selection**.

*   Select a table.
*   On the **Table Formats** panel, do one of the following: 
    *   To combine with any local formatting that's already applied, either: 
        *   Click on a table format's thumbnail.
        *   Click on a table format's options menu ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/2XLuXTwmEh714qaYONrPKP/6d26123960257b3233a3eb084188eda7/moremenuicon.svg)  and select **Apply "[Table format name]"**.

    *   To replace existing table formatting: click a table format's options menu ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg)  and select **Apply "[Table format name]" (Override Local)**.

1.   Select the table.
2.   On the **Table Formats** panel, click the table format's options menu ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg)  and select **Update From Selection**.

If multiple tables with different formatting are selected, the table format is updated using the one selected first.

This feature is only available in Affinity for desktop.

You can create and edit table formats using a dialog.

The dialog can also be used to edit table formats created from manually formatted tables.

The dialog contains the following sections:

*   **Structure**—for defining the header, footer and body areas of the table format and their formatting.
*   **Cell Formats**—a list of named cell formats which can be applied to cells in the structure.
*   **Cell Format Settings**—the selected cell format's fill, border, inset, vertical position, and paragraph style settings.

In the **Structure** diagram, row and column handles let you define the header and footer areas.

As the table grows, formatting applied to the header and footer does not repeat, but formatting for body rows and columns does.

The number of columns and rows in the Structure diagram is only for defining the header, body, and footer areas of tables. It does not limit how many rows or columns a table can have.

Selecting a cell in the **Structure** diagram also selects its cell format and displays the corresponding settings.

Each table format contains at least one cell format. You can create and apply additional cell formats, e.g. to color a table's header row differently than its body rows, or to alternate the background color of odd and even body rows.

Selecting a cell format applies it to the selected cells. Editing a cell format's settings automatically updates _all_ cells that use it.

*   On the **Table Formats** panel's **Preferences** menu ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg) , select **Create New Format**.

1.   On the **Table Formats** panel, click the table format's options menu ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg)  and do one of the following: 
    *   To edit the table format, select **Edit "<Table format name>"**.
    *   To create and edit a copy of the table format, select **Edit copy of "<Table format name>"**.

2.   On the dialog that appears: 
    1.   (Optional) Type a **Name** for the table format.
    2.   Edit the table format's **Structure** and cell formatting as required. You can select multiple cells on the Structure diagram by dragging through them. 
    3.   Click **OK**.

After editing a table format, the appearance of each table that uses it updates automatically.

To view table formats' names on the panel, click the panel's **Preferences** menu

![Image 9](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)

 and select **Show Names**.

When editing a table format:

1.   Below the list of **Cell Formats**, click the + button.
2.   Edit the cell format's name and other settings on the right.

When editing a table format:

1.   Select the unwanted cell format in the list.
2.   Click the – button below the list of cell formats.

The default cell format is applied to cells that used the deleted format.

When editing a table format:

*   On the **Structure** diagram, do one of the following: 
    *   To add a row, click the + button below the bottom-right corner.
    *   To add a column, click the + button to the right of the bottom-right corner.
    *   To remove a row, click the - button above the top-left corner.
    *   To remove a column, click the – button to the left of the top-left corner.

When editing a table format:

1.   On the **Structure** diagram, click the header column handle to move it right one column (for a header column) or the header row handle to move it down one row (for a header row).![Image 10: Row header area](https://images.ctfassets.net/3p2fxa94bzao/2Hfp9saq93MM4d3qIckgt0/6802f8f8e294b0abb3d9683553bfe01b/tableheader1.png)  If required, repeat to increase the number of rows/columns included in the header. 
2.   Drag across the cells in the header to select them.![Image 11: Row header selection](https://images.ctfassets.net/3p2fxa94bzao/4P5RKkutm7wJrYEYwE2v8W/18b16547945c4bd2162584aef8788717/tableheader2.png) 
3.   Create a new cell format for the header. It is automatically applied to the selected cells.
4.   Edit the cell format's settings as required to differentiate the header.![Image 12: Row header style](https://images.ctfassets.net/3p2fxa94bzao/3iHQd7CLOj7lBj4ZnWNKDI/7b3de758a8de61e26cd5449c1168c7f4/tableheader3.png) 

When editing a table format:

1.   On the **Structure** diagram, click the footer row handle to move it up one row (for a footer row) or the footer column handle to move it left one row (for a footer column).![Image 13: Table footer area](https://images.ctfassets.net/3p2fxa94bzao/2AiTpzT7l8IN4UUSZz0XML/4e7f9ba7a161012e2e1c70aff21b939c/tablefooter1.png)  If required, repeat to increase the number of rows/columns included in the footer. 
2.   Drag across the cells in the footer to select them.![Image 14: Table footer selection](https://images.ctfassets.net/3p2fxa94bzao/5tOz0lhoPF8E8xhUfQLKEj/8b3e8783702198c18256eee715bf83e8/tablefooter2.png) 
3.   Create a new cell format for your footer cells. It is automatically applied to the selected cells.
4.   Edit the cell format's settings as required to differentiate the footer.![Image 15: Table footer style](https://images.ctfassets.net/3p2fxa94bzao/5ShhL6jNEw5oDbpveg6HOe/93f11e8532f428e0941b04f507390bc9/tablefooter3.png) 

When editing a table format:

*   On the **Structure** diagram, select individual cells within the body area of the table, then apply different cell formats to alternating cells.![Image 16: Table pattern](https://images.ctfassets.net/3p2fxa94bzao/32ZLpXXBhlUuWV1aLOVp0G/bfa89d7eb2227eed083032120db7783e/tablepattern.png) 

This feature is only available in Affinity for desktop.

You can import table formats from another Affinity document, and save the current document's table formats as the default for reuse across multiple new documents.

1.   On the **Table Formats** panel, click the panel's **Preferences** menu ![Image 17](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg)  and select **Import Formats**.
2.   Navigate to and select the Affinity file from which to import table formats, then select **Open**.
3.   On the list of formats that appears, choose which to import, rename incoming formats, and resolve any conflicts.
4.   When you are ready to import, select **OK**.

*   On the **Table Formats** panel's **Preferences** menu ![Image 18](https://images.ctfassets.net/3p2fxa94bzao/6xHYQYa3ePyLnNbDC3c5Ey/56d26d75e40a2d195e578a41b2b16612/panel_preferences.svg) , select **Save Formats as Default**.

*   [Table Tool](https://www.affinity.studio/help/tools-tools-table/)
*   [Editing tables](https://www.affinity.studio/help/tables-edit-tables/)
*   [Sorting tables](https://www.affinity.studio/help/tables-sort-tables/)
*   [Table panel](https://www.affinity.studio/help/panels-table-panel/)
*   [Table Formats panel](https://www.affinity.studio/help/panels-table-formats-panel/)

How would you rate the help you received from this article?
