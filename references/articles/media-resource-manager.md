---
title: "Managing document resources - Affinity Help Center"
source: https://www.affinity.studio/help/media-resource-manager/
slug: media-resource-manager
fetched: 2026-08-06
---

# Managing document resources - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/media-resource-manager/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Page layout](https://www.affinity.studio/help/page-layout/)
3.   Managing document resources

The Resource Manager lists all image and text resources placed in your document.

![Image 1](https://images.ctfassets.net/3p2fxa94bzao/2LpwqYzD6p9nckbxokli3O/3e9181b333af73d21bf6ef9bd810a03f/resourcemanager.png)

Each entry in the resources list displays a file name, and additional details depending on the resource type:

*   **Page**—the number of the page the resource is on.
*   **Status**—whether the resource, if it's linked, has been modified.
*   **Changes** (text resources only)—shows whether the linked text file has been modified and in what way: 
    *   **None**—no modifications.
    *   **Text**—text content has been modified.
    *   **Format**—formatting has been modified.
    *   **All**—both text content and formatting have been modified.

*   **Placement** (image resources only)—placement type (linked, embedded, or remote).
*   **Size** (image resources only)—the amount of space the resource uses.
*   **Placed DPI**—the effective dots per inch of the resource on the page.
*   **Type**—the kind of file, e.g. _PNG_ or _Plain text_.

Select an entry to show a preview of the content along with metadata on the right.

1.   On the **Document** menu, select **Resource Manager**.
2.   On the window that appears: 
    1.   On the pop-up menu, select the resource type to manage: _Images_ or _Text_.
    2.   Select one or more resources you need to manage, then choose from the available options. Some options are available only when one resource is selected.

Selecting a resource's object in the document view automatically highlights its entry on the Resource Manager.

Double-clicking an entry in the resources list selects its object and shows the object in the document view.

When a file is placed in an Affinity document, its placement type is either **Linked** or **Embedded**. The key difference is whether data is stored in a separate file or within your Affinity document, respectively.

Images dragged and dropped from a web browser are embedded by default. On desktop, they can have a placement type of **Remote (Linked)**.

Each resource has one of the following statuses:

*   ![Image 2](https://images.ctfassets.net/3p2fxa94bzao/pYlpht9bNPwtYJpUtD3D3/365f3e7e03630938f9082d16a7dac43b/ChapterOK.svg) **OK**—the resource can be accessed and has not been modified. No action is required.
*   ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3Zk9Ph0WGSzl3lA45l39QO/9922e06373f1716a93f1c85ec8799942/ChapterMissing.svg) **Missing**—the linked file has either been moved from its original location, renamed, or deleted.
*   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/7rJJBxQ7QQfUHBQ0ZHhvcI/6c215ffb9e3e662788ea118a90b63e85/ChapterOutOfDate.svg) **Modified**—the linked file has been modified externally.
*   ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/33OCLzJe9idz8ryYmrGeyF/58651562f902ad1c57ef8bdee12687be/ChapterRestricted.svg) **Permission Denied/Access Denied**—the linked file cannot be displayed as there are insufficient folder permissions to access it.

On the **Resource Manager**:

*   Select the resource's entry in the list.
*   If the resource's status is: 
    *   **Modified**—click **Update**/**Refresh** to add the latest version of the file to your Affinity document.
    *   **Missing**—do one of the following: 
        *   To connect a file of the original's name, click **Relink**, navigate to the file's containing folder and select it, then click **Open**.
        *   To connect a file of any name, click **Replace**, navigate to the file and select it, then click **Open**.

    *   **Permission Denied** / **Access Denied**—use your operating system's features to ensure Affinity has access to the file's location.

To help find entries in the resources list, it can be sorted by any of its columns.

On the **Resource Manager**:

1.   Click a column's header to sort the list in ascending order of the column's values.
2.   (Optional) Repeat to sort in descending order.

When you **^(ctrl)**-click (Mac) / **right**-click (Windows) on any column header, you can choose which columns are shown or hidden.

The **Collect** feature gathers a document's resources, which may be in multiple folders, into a single folder to make management easier. For example, to archive a project when it is complete.

The collection process doesn't include fonts.

If you wish to share a project for collaboration purposes, Affinity's [Packaging](https://www.affinity.studio/help/sharing-about-packaging/) feature is a better option.

On the **Resource Manager**:

1.   On the pop-up menu, select the resource type to collect: _Images_ or _Text_.
2.   Select the resources to collect. (To select all, press **⌘****A** (Mac) / **Ctrl**+**A** (Windows).
3.   Click **Collect**.

Related behaviors can be adjusted from [the app's settings](https://www.affinity.studio/help/workspace-settings/):

*   **General > Automatically update linked resources when modified externally**

*   [Placing content](https://www.affinity.studio/help/media-place-images/)
*   [Embedding vs linking](https://www.affinity.studio/help/media-embedding-vs-linking/)
*   [Linked Services](https://www.affinity.studio/help/media-linked-services/)
*   [About packaging](https://www.affinity.studio/help/sharing-about-packaging/)

How would you rate the help you received from this article?
