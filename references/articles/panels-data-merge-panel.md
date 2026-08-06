---
title: "Data Merge panel - Affinity Help Center"
source: https://www.affinity.studio/help/panels-data-merge-panel/
slug: panels-data-merge-panel
fetched: 2026-08-06
---

# Data Merge panel - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/panels-data-merge-panel/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Data Merge panel

Use the Data Merge panel to link data sources to your Affinity document and generate a new document that combines data with your page layouts.

This feature is only available in Affinity for desktop.

For Mac/Windows: On the **Window** menu, select **Layout > Data Merge**.

The following options are available on the panel when no data sources are linked to your Affinity document:

*   **Add Data File**—opens a dialog where you can navigate to a compatible data file and open it. This links the file to your document.

The following options are available on the panel after you've linked one or more data sources to your Affinity document:

*   **Source** / **Sources**—shows the data source, or sources, that will be merged with the current document to generate a new one. If multiple data sources are added, you can choose which are enabled or disabled. Only enabled sources are used to generate the new document.For example, with a single data source enabled at a time, you can use Data Merge to generate separate versions of your document based on each source. If you enable multiple data sources, Data Merge uses records from all of them to generate a single document.
*   ![Image 1](https://images.ctfassets.net/3p2fxa94bzao/5Ycr9tH2LjBQAGrfkfVHEU/1be92e96b4b15a1203dcfa3afb28f9c9/add_data_merge_source.svg) **Add Data Source**—links an external data source to your Affinity document.
*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/3m8ciDtLqf07Yrma1i0j4x/202c1d508104bbb0a1290c5be7725eae/trash_can.svg) **Delete Data Source**—unlinks the selected data source from your Affinity document.
*   **File**—lets you perform the following operations on the selected data source: 
    *   **Reveal**—opens the folder containing the source's file.
    *   **Replace**—lets you relink the source, e.g. because its file has been moved or you want to use a different file.
    *   **Refresh**—fetches the latest records from the source.

*   **Delimiter**—specifies the character that separates the fields in the selected data source's file.
*   **Quote**—specifies the characters that surround field values that include the delimiter, such as commas.
*   **Data Source Summary**—shows the number of fields and records in the selected data source.
*   **Use**—lets you choose how much of the selected data source will be merged: 
    *   **All Records**—merges all records from the source. No records are omitted.
    *   **Range**—merges only records between the indexes you specify below.

*   **Advanced Data Tools**—opens the **Data Merge Data Viewer**, where you can view, filter, and edit your document's data sources. This is useful if editing isn't possible earlier in your workflow. See below for options.
*   **Repeat**—lets you choose which of your document's pages are repeated during the data merge process: 
    *   **All Pages**—repeatedly copies all document pages to the output document until all records in the data source are used.
    *   **Page Range**—repeatedly copies a range of pages to the output until all records in the data source are used. Use the **From** and **To** options to set the first and last pages of the range. Pages outside the range are copied to the generated document only once.

*   **Preview with record**—sets the index of the record whose data you want to see in the document view. Use the controls below to switch between records.
*   **Insert Field**—is shown when an insertion point exists in text. Click, then select the required field from the selected data source. When you generate a data-merged document, the field displays its literal value.
*   **Bind Field**—is shown when a picture frame is selected. Click, then select the required field from the selected data source. Field values might contain filenames stored locally or addresses (URLs) of online resources. When you generate a data-merged document, the picture frame displays content from locations specified in the field values.
*   **Generate**—creates a new Affinity document based on the current document, its enabled data sources and your specified settings.

The following options are available on the **Data Merge Data Viewer**:

*   **Source**—lets you choose which of your document's data sources is shown on the window and manipulated by its settings.
*   **Scope**—sets which data is shown in the records list: 
    *   **Source Data**—shows all records from the selected source.
    *   **Filtered Data**—shows only records that match your settings on the window.
    *   **Rows with Warnings**—shows only records that your settings on the Process section have marked with a warning. On the Process section, you can set different warning text for each criterion. In the records list, hover over an alert icon to see which warning was triggered by the corresponding record. 

*   **Data Source Summary**—shows the number of fields and records in the selected data source, and how many of them will be used for data merge as a consequence of your settings on this window.
*   **Refresh**—updates the records list. Column widths may change to fit data from records that match your settings on this window.
*   **Records list**—shows records from the selected data source that match your settings on this window.
*   **Range**—chooses whether all records or a specific range from the data source are used.
*   **Filter**—lets you specify criteria records must match to be shown in the records list. The filter can contain multiple rules, and you can specify whether records must match all or any of them.
*   **Sort**—lets you change the order in which records will be data merged. You can sort on multiple fields, and choose whether each is sorted in ascending or descending order.
*   **Process**—similar to the Filter tab, but performs your choice of actions on records that match your criteria. For example, you can add a prefix or postfix to a field's data, mark records with warnings, and skip records altogether.
*   **Script**—lets you use JavaScript to manipulate the selected data source. When you add a script, Affinity fills it with example code to use as a starting point.

Data comparisons performed on the Filter and Process sections are case-insensitive.

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/6UxpXBt5miovw347YaOPUz/6f8e3e8d9b379daa0bdc5a3ac6ff23e8/panel_preferences.svg)

 The following options are available on the **Panel Preferences** menu:

*   **Panels**—opens a dialog where you can quickly set the visibility of all panels in the current Studio.
*   **Close**—hides the current panel.
*   **Close Panel Group**—hides the current panel and any others grouped with it.

*   [Data merge](https://www.affinity.studio/help/advanced-data-merge/)

How would you rate the help you received from this article?
