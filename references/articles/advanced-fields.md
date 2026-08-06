---
title: "Fields - Affinity Help Center"
source: https://www.affinity.studio/help/advanced-fields/
slug: advanced-fields
fetched: 2026-08-06
---

# Fields - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/advanced-fields/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Fields

Fields let you insert information or metadata into your document's text. They automatically update as data—for example, a date—changes.

You can use fields to show section names and page numbers on pages. For example, a **Name** or **Page Number** field in a master page's footer automatically shows the correct info on all publication pages that use the master.

Items that can be inserted as fields can be found on the **Fields** panel.

On desktop, commonly used fields are also available via **Text > Insert > Fields**.

Available fields include:

*   **Document Information**—displays the **Author**, **Tags**, **Comments**, **Title**, **Subject**, **Revision**, **Publisher**, **Illustrator**, and **ISBN**.
*   **Document Statistics**—displays key statistics for the document: **Last edited by**, **Created**, **Saved**, **Printed/Exported**, **Save Count**, **Filename**, **Path**, and **Total Pages**.
*   **Document Sections**—displays the following for each section of the document: **Name**, **Running Header**, **Page Number**, **Last Page** and **Run Last Page**.
*   **Continuation**—displays the page number of the **Previous Frame** and **Next Frame** in a sequence of linked text frames, so you can add jump lines to publications.
*   **General Information**—displays the current **Date & Time**.
*   (Desktop only) **Data Merge (****_data source file name_****)**—dynamically displays fields from a currently connected external data source.
*   **Custom**—allows you to create your own fields that hold any text you want.

The **Author** field contains your user account's short name. If you do not want this name visible in documents you upload or share, click the text to edit it. Doing this without a document open makes what you type the new default.

The **Last edited by** field and the fields in the **Document Information** section are empty by default. You can edit each one's value, either by clicking the value or **Edit Format Defaults**

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/6x5gVVtCRh6FfMxDzWNZeH/8b7abc81ae1ef53b66fc755546852cbb/default_format.png)

 to its right.

You can convert a text selection to a field, or using the **Find and Replace** panel. The text must follow these rules:

*   It doesn't include any hard breaks (like paragraph or section breaks).
*   It doesn't contain filler text.
*   It's as a single, continuous selection.
*   It isn't an empty selection.

Use the **Find and Replace** panel to replace repeated text with a field.

Fields with editable formatting include **Date & Time**, **Created**, **Saved**, **Printed/Exported**, and **Running Header**.

Field formatting can be edited, via the **Fields** panel or the document view.

Date and time fields can show various pieces of information. Choose which info they show by editing their formatting: select **Custom** and enter the required details in the **Pattern** setting.

The table below lists supported items. Patterns can be combined as you wish, including with regular text to form longer phrases.

The **Language** setting changes how the values are shown. For example, _MMMM_ displays _July_ when an English language is selected, _julio_ for Spanish, and _Temmuz_ for Turkish.

| Symbol | Meaning | Pattern | Example value | Notes |
| --- | --- | --- | --- | --- |
| **G** | Era designator | **G****GGGG****GGGGG** | AD Anno Domini A |  |
| **y** | Year | **y****yy** | 2023 23 |  |
| **Q** | Quarter | **Q****QQ****QQQ****QQQQ** | 2 02 Q2 2nd quarter |  |
| **M** | Month in year | **M****MM****MMM****MMMM****MMMMM** | 9 09 Sep September S |  |
| **L** | Standalone month in year | **L****LL****LLL****LLLL****LLLLL** | 9 09 Sep September S | Some languages use a different spelling of the month in certain contexts, e.g. when a month is mentioned without a date and year. These spellings can be accessed using these patterns. For example, in Polish **MMMM** displays _lipca_ for July, whereas **LLLL** displays _lipiec_. |
| **w** | Week of year | **w** | 27 | Consecutive instances of the symbol add a leading zero to the resulting value. |
| **W** | Week of month | **W** | 2 | Consecutive instances of the symbol add a leading zero to the resulting value. |
| **d** | Day in month | **d****dd** | 2 02 |  |
| **D** | Day of year | **D****DD****DDD** | 1 01 001 | Example is 1st of January. |
| **F** | Day of week in month | **F** | 2 | Example is second Wednesday in July. Consecutive instances of the symbol add a leading zero to the resulting value. |
| **E** | Day of week | **E****EEEE****EEEEE****EEEEEE** | Tue Tuesday T Tu |  |
| **e** | Local day of week | **e****eee****eeee****eeeee****eeeeee** | 2 Tue Tuesday T Tu | When the field's language is set to US English, Monday is day 2 as the week starts on Sunday, whereas for UK English it is day 1 as the week starts on Monday. |

| Symbol | Meaning | Pattern | Example value | Notes |
| --- | --- | --- | --- | --- |
| **a** | AM or PM | **a****aaaaa** | PM p |  |
| **B** | Flexible time periods | **B** | at night | Possible values are _in the morning_, _noon_, _in the afternoon_, _in the evening_ and _at night_. |
| **h** | Hour in day (1–12) | **h****hh** | 7 07 |  |
| **H** | hour (0–23) | **H****HH** | 7 07 |  |
| **k** | Hour number in day (1–24) | **k****kk** | 4 04 |  |
| **K** | Hour in am/pm (0–11) | **K****KK** | 7 07 |  |
| **m** | Minute in hour (0–59) | **m****mm** | 8 08 |  |
| **s** | Second in minute (0–59) | **s****ss** | 3 03 |  |
| **z** | Short/Long Timezone | **z****zzzz** | BST British Summer Time |  |
| **O** | Time Zone: short localized GMT Time Zone: long localized GMT | **O****OOOO** | GMT-8 GMT-08:00 |  |
| **V** | Time Zone: short time zone ID Time Zone: long time zone ID Time Zone: time zone exemplar city Time Zone: generic location | **V****VV****VVV****VVVV** | gblon Europe/London London United Kingdom Time |  |
| **x** | Time Zone: ISO8601 basic hm Time Zone: ISO8601 basic hm Time Zone: ISO8601 extended hm | **x****xx****xxx** | +01, -0930 +0100, -0930 +01:00, -09:30 |  |

| Symbol | Meaning | Pattern | Example value | Notes |
| --- | --- | --- | --- | --- |
| **'** | Escape character to include literal text | **'Today is' EEEE** | Today is Tuesday | Surround literal text with apostrophes to display it alongside date and time values in a field. |
| **' '** | Two single quotes produce one | **'Today''s date is' MM/dd/yyyy** | Today’s date is 10/30/2025 |  |

The value of a **Date & Time** field (from the **General Information** fields category) is when the field was inserted into document text.

1.   In a text object, create an insertion point or select text that you want to replace.
2.   On the **Fields** panel, expand the section that contains the required field.
3.   Double-click the required field's name.

Fields can also be inserted using the **Text** menu, by selecting the required field from **Insert > Fields**.

1.    Do one of the following: 
    *    On the field in document text, **^(ctrl)**-click (Mac) / **right**-click (Windows) and select **Edit Field**. 
    *   In document text, select the field or create an insertion point immediately before or after it. On the corresponding entry on the **Fields** panel, select **Edit Format**![Image 2](https://images.ctfassets.net/3p2fxa94bzao/6x5gVVtCRh6FfMxDzWNZeH/8b7abc81ae1ef53b66fc755546852cbb/default_format.png)  (or **Edit Running Header Defaults** for that field).

2.   On the dialog that appears, select your preferred format.

This won't change other instances of the field.

1.    In the document view, ensure that: 
    *   an instance of the field is not selected.
    *   the insertion point is not immediately before or after an instance of the field.

2.   On the required field's entry on the **Fields** panel, select **Edit Format Defaults**![Image 3](https://images.ctfassets.net/3p2fxa94bzao/6x5gVVtCRh6FfMxDzWNZeH/8b7abc81ae1ef53b66fc755546852cbb/default_format.png) .
3.   On the dialog that appears, select your preferred format. New fields you insert later will use it.

*   On the field in document text, **^(ctrl)**-click (Mac) / **right**-click (Windows) and select **Expand Field**.

1.   Select the text range to convert.
2.   On the selection, **^(ctrl)**-click (Mac) / **right**-click (Windows) the selection and select **Convert Text to Field**.
3.   (Optional) Edit the proposed name and value for the field.
4.   Select **Close**.

*   On the **Text** menu, select **Highlight Fields**.

1.   On the **Fields** panel, expand the **Custom** section.
2.   Select **Create Custom Field**![Image 4](https://images.ctfassets.net/3p2fxa94bzao/7gaOXEE9Q1C4iEbXHvwuQW/3474ef102e15e65561ac168316e45610/add_field.svg) .
3.   Type a name and a value for the field in the corresponding boxes.
4.   Select **Close**.

1.   On the **Fields** panel, expand the **Custom** section.
2.   To the right of the custom field's name, click the existing value (or the blank space if there is no value).
3.   Type the new value.
4.    Press the **⏎** key (Mac) / **Return** key (Windows). 

The field updates to show the new value automatically. This can change how your text flows.

1.   On the **Fields** panel, expand the **Custom** section.
2.   On the field's entry, select **Edit Custom Field**![Image 5](https://images.ctfassets.net/3p2fxa94bzao/6x5gVVtCRh6FfMxDzWNZeH/8b7abc81ae1ef53b66fc755546852cbb/default_format.png) .
3.    Do one of the following: 
    *    To rename the custom field, click its current name, edit the text, and then press the **⏎** key (Mac) / **Return** key (Windows). 
    *   To delete the custom field, select **Delete**![Image 6](https://images.ctfassets.net/3p2fxa94bzao/3m8ciDtLqf07Yrma1i0j4x/202c1d508104bbb0a1290c5be7725eae/trash_can.svg) .

*   [Fields panel](https://www.affinity.studio/help/panels-fields-panel/)
*   [Data merge (Desktop only)](https://www.affinity.studio/help/advanced-data-merge/)
*   [Find and replace](https://www.affinity.studio/help/text-find-and-replace/)

How would you rate the help you received from this article?
