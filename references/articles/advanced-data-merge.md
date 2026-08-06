---
title: "Data merge - Affinity Help Center"
source: https://www.affinity.studio/help/advanced-data-merge/
slug: advanced-data-merge
fetched: 2026-08-06
---

# Data merge - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/advanced-data-merge/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Data merge

Data merge inserts text and image links from other programs into your publication pages.

This feature is only available in Affinity for desktop.

![Image 1: Data merge](https://images.ctfassets.net/3p2fxa94bzao/3SBFRw3KMKaSWTgBUjFb1n/e017f686c22309a008105864ec06a2c5/data_merge.png)

Awards and business cards (in an N-up grid layout) merged from an external data source.

Data merge means injecting data from a data source into documents such as personalized certificates, stationery, badges and passes to more complex multi-page business cards, catalogs, photo albums or any document where personalization is needed.

For example, you can publish ID passes that are personalized with pass-holders' names and profile pictures. You can also generate entry passes that contain unique QR codes from a field of a data source provided by your client. You might scan the passes with a device or an app to validate them.

Use the **Data Merge** panel to add the external data source, work with it, and generate a merged document.

Your data source can be a text file (plain, CSV, or TSV), a JSON file, or a spreadsheet (XLSX). These might come from apps like Microsoft Excel, Apple Numbers, and LibreOffice. Text files might include exported address books or contact lists.

Your data records could also include image links (resource path names) which can be associated with a picture frame in Affinity. On merging, the referenced images (e.g., profile or product photos) are merged into picture frames sequentially.

The key steps for successful data merging are:

*   Creating a data source
*   Designing on a single spread or grid layout
*   Adding the external data source
*   Filtering the data records
*   Inserting fields
*   Merging and publishing

The data source exists outside of Affinity, typically exported from another app or website. Contact lists can be exported from google.com, outlook.com and other services.

Make sure the source is available before merging, and that it has a consistent structure and contains data records.

You can add or change records in the data source at any time, even after merging. If a record doesn't contain data, it will be treated as a blank field.

*   For CSV and TSV files, the first line of your data source becomes the field names in Affinity; the row must contain explicit names to be fields. For example, a top row of "First name, Last name, email address" would offer the merge fields of _First name_, _Last name_ and _email address_ in Affinity. The CSV export format is more commonly used, but the TSV format avoids problems when processing data records containing punctuation.
*   For JSON files, obtained from web/mobile services or database export, only a single top-level array of objects (and values in those objects) are supported; lower level arrays and objects are not supported.
*    For image links, the resource path names can be absolute (like below), or relative to the data source's or saved document's file location. 
    *   Mac: /Users/_username_/Desktop/ProfilePics/magazine_staff_pics_andy.jpg
    *   Windows: C:\Users\_username_\Desktop\ProfilePics\magazine_staff_pics_andy.jpg

Several scenarios are possible:

*   For personalized certificates, letters, envelopes and greeting cards: Create a single design on one spread with fields inserted from your data source, e.g. for names and/or addresses. On merging, new pages will be generated until all the data records have been processed.
*   For business cards, mailing labels, badges and passes: Draw a grid layout using the Data Merge Layout Tool to create N-up tiled data records. For example, you could 'gang-up' business cards on a 5x2 row/column grid to minimize print costs. Merging is as for the previous scenario—Affinity generates new grid-based pages, with each page's grid 'cells' showing a different record.
*   For multi-page catalogs and photo albums: If your publication has multiple spreads, you can use either method above. On merging, Affinity will generate the multiple spreads for as many times as needed until the data records are processed and presented.

When you add an external data source to your document, it will be embedded in your file. You'll then be able to view and use its fields in Affinity.

After you add a source, it's remembered the next time you open your document. If the original data source file has been modified, you can update the embedded copy manually; it will not update automatically.

Data merge will generate preflight errors and warnings if the external data source has been modified.

Instead of merging all records, you can filter by a specific range (e.g., 100-200). This lets you control which records are output.

To filter from a specific record number to the end of your data source, enter a final number that's higher than your last record number (e.g., 100-20000).

The Data Merge panel also provides advanced data tools. You can use these to:

*   choose the records to use in data merge by specifying a range of records or criteria records must match.
*   sort records based on one or more fields.
*   process the data source to edit values, mark specific records with warnings, or stop the data merge process under certain conditions.
*   write JavaScript that manipulates the data.

This changes the data that goes into a generated document.

To merge information from a data source into your document, you can insert fields into document text and bind fields to picture frames. Text fields show exact values from your data source. A field bound to a picture frame uses values from your data source—a file path or a web address (URL)—to dynamically display images.

You can insert fields with metadata about the source and its records:

*   **Source**—displays the data source's filename.
*   **Merge Index**—displays a record's numerical order among only your choice of filtered records.
*   **Unfiltered Index**—displays a record's numerical order among all of its data source's records.

For example, if your data source's filename includes the file's creation date, you might include the filename and an index in a generated letter's footer.

When a field in a data source contains a web address (URL), an anchor, an email address, or a path to a file, a hyperlink added to text or an object in a data merge layout can use the field's value as its target.

![Image 2: Inserting a hyperlink in a data merge layout](https://images.ctfassets.net/3p2fxa94bzao/Q1jZLQ5tOy9aIjnbqNFNM/6ebc392fec4564c56fce3b72bbba5d23/dataMergeHyperlink.jpg)

Adding a hyperlink in a data merge layout. In each cell, the hyperlink's target comes from a field in the corresponding record of the data source.

After a data merge is performed, the resulting document will contain a hyperlink (on the Hyperlinks panel) for each of the data source's records.

Some records contain empty fields. For example, where an address is stored across multiple fields—e.g. Address1, Address2, City, and ZIP/postcode—many addresses do not use the Address2 field.

If empty fields are not handled, merged text may include unwanted blank lines or superfluous punctuation. For instance:

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/5xM6WVgjEHOvbR4nNFfJDD/e9f755494d6cb07abb87cd783f200395/emptyFieldWithoutBlankLine.png)

To avoid these issues, you can configure fields to automatically skip prefix or postfix text—such as a comma or line break—when the field is empty. This ensures clean, continuous output.

After inserting placeholder fields, you can merge your source data and your original publication to create _a new Affinity (.af) document_. Pages from your original document are repeated. This ensures all data records appear in the merged document.

On the **Data Merge** panel:

1.   Click **Add Data File** to add your first data source, or **Add Data Source** (the plus icon) to add another.
2.   Navigate to a data source file and select it.
3.   Click **Open**.
4.   If the data source is a text-based file (e.g. CSV), make sure **Delimiter** and **Quote** match the file's formatting.

1.   Select the **Data Merge Layout Tool**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/pz7RLgdWJSHEOjjBrAXkn/765542f5fd7caf6d45240bb98aef16df/data_merge_tool.svg) .
2.   In the document view, drag to create a grid-based layout. This displays a different record's data in each grid cell after merging.
3.   On the context toolbar: 
    1.   Set the number of **Rows** and **Columns**. This determines the number of cells your design repeats in.
    2.   Set **Cell Width** and **Cell Height** to the dimensions of your intended deliverable (e.g., business cards).
    3.   When you want to add something to the data merge layout:
        1.   Make sure the data merge layout is selected in the document view or on the **Layers** panel. If it isn't selected, the objects you draw will not be part of the data merge layout and won't repeat across its cells.
        2.   In the layout's top-left cell, create objects you want to be repeated in each cell but show data from different rows of your data merge source.

1.   Draw an object using the **QR Code Tool**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/7xgRYHv0scGgqZ9Bv27jaX/e427bae348160e5f81c5061609bfe260/qr_shape_tool.svg) .
2.   On the context toolbar, click the value next to **Data**.
3.   On the dialog that appears: 
    1.   Set **Type** to _Data Merge_.
    2.   Set **Field** to the field to use to generate QR codes.
    3.   Click **OK**.

1.   Select the text or object you wish to be hyperlinked.
2.   On the **Hyperlinks** panel, select **Add Hyperlink**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3v0tdiCwdl7bufnVuTysQB/1593f5e1939732c7866074a28242c777/add_item.svg) .
3.   On the dialog that appears: 
    1.   Set **Type** to _URL_, _Email_, or _File_, according to the field's values.
    2.   Check **From Data Merge**.
    3.   Set **Field** to the field that contains hyperlink targets.
    4.   Click **OK**.

On the **Data Merge** panel:

1.   Make sure your intended data source is selected.
2.   Set **Use** to **Range**.
3.   In the box below, type a range of records, then press the **⏎** key (Mac) / **Return** key (Windows).

For a range of records, type the starting index, a hyphen, then the finishing index, e.g. _1-100_. For non-consecutive records, separate their indexes with commas, e.g. _23, 65, 87, 92_. You can combine ranges and individual indexes, e.g. _1-44, 45-200_.

On the **Data Merge** panel:

1.   Click **Advanced Data Tools**.
2.   On the **Data Merge Data Viewer** that appears: 
    1.   Make sure your intended data source is selected.
    2.   Use the **Range**, **Filter**, **Sort**, **Process**, and **Script** options on the right as needed.

3.   Inspect that the list of records is as needed before generating a data-merged document.

This changes what data goes into a data-merged document.

1.   Insert fields that make up a larger piece of information (e.g. an address) into your text in order.
2.   On the Fields panel, for each data merge field that belongs to the information:
    1.   Select Edit Defaults on the field.
    2.   Set Prefix or Postfix to the text you want to appear before or after the field's data.To display a multi-field address as continuous text, add a prefix or postfix to fields. For example, set Postfix to a comma followed by a space on each field except the last. Alternatively, set Prefix to a comma followed by a space on each field except the first. To display the address across multiple lines, use a line break instead. 

3.   Enable Skip Prefix if field is empty or Skip Postfix if field is empty as needed. This prevents consecutive prefix or postfix text from appearing when optional fields are empty.

Alternatively, use the **Data Merge** panel's **Advanced Data Tools** to handle empty fields. In the **Process** section, you can create rules that add a prefix or postfix only when a field is not empty.

On the **Data Merge** panel:

1.   Add one or more data sources. (If you wish to exclude any you've added from data merge, uncheck them in the **Sources** list.)
2.   Set the options for which records will be merged and which pages of your document will be repeated.
3.   Click **Generate**.
4.   On the **File** menu, use either **Print** or **Export > Export** as usual.

*   [Data Merge panel (Desktop only)](https://www.affinity.studio/help/panels-data-merge-panel/)
*   [Data Merge Layout Tool (Desktop only)](https://www.affinity.studio/help/tools-tools-data-merge-node/)
*   [Fields panel](https://www.affinity.studio/help/panels-fields-panel/)
*   [Hyperlinks panel](https://www.affinity.studio/help/panels-hyperlinks-panel/)
*   [Preflight](https://www.affinity.studio/help/sharing-preflight/)

How would you rate the help you received from this article?
