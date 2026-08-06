---
title: "Importing CAD documents - Affinity Help Center"
source: https://www.affinity.studio/help/get-started-import-cad/
slug: get-started-import-cad
fetched: 2026-08-06
---

# Importing CAD documents - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/get-started-import-cad/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Getting started](https://www.affinity.studio/help/getting-started/)
3.   Importing CAD documents

Affinity imports CAD documents from Autodesk® AutoCAD® apps and other CAD-based apps that output DWG or DXF files.

![Image 1: Imported CAD DWG/DXF](https://images.ctfassets.net/3p2fxa94bzao/55caFIFQCkzfO0ue65BRxZ/3bc65da378c45dff951c9c1e7b583a8d/cad_import.jpg)

The importing of CAD documents is a one-way process. Changes made after importing a document cannot be saved directly back to the original file. Instead, you can save as an Affinity document or export to a PDF file or to a new DWG or DXF file.

The DWG file format is the proprietary vector-based format for Autodesk® AutoCAD® apps. CAD apps can save to the DXF interchange file format, allowing easier importing of AutoCAD designs into a wider range of third-party apps.

Any drawing scale used in the CAD document is automatically applied to the new document (shown in **Document > Setup > Document Setup** and when using the **Measure Tool**).

For models, a drawing scale is applied to the imported CAD document in Affinity so it is presented at an acceptable size that fits your page. For paper space layouts, called pages in Affinity's CAD import dialog, the layouts are imported at a 1:1 ratio and have a drawing scale that represents each layout's viewports. For layouts with multiple viewports, each layout is imported as an artboard (Vector) or spread (Layout) that has a drawing scale that represents the viewport's zoom.

DWG or DXF files can be placed into an existing document instead of imported as a new document.

1.   On the **File** menu, click **Open**.
2.   Select the file you want and click **Open**.
3.    On the Import Options dialog, you can choose: 
    *   **Selection**—chooses the CAD layout(s) or the model to import. 
        *   _All Pages_—imports one or more Paper Space layouts if present, excluding the Model space. Each layout becomes a separate artboard.
        *   _Single Page_—imports an individual Paper Space layout if present; you can choose the specific layout from an additional **Selected Page** option.
        *   _Model_—imports just the Model space (with margins and offsets) without Paper Space layouts.

    *   **Insertion units**—sets the document units for the document when **Model** is chosen.
    *   **DPI**—sets the resolution for the document.
    *   **Background color**—adds a background color of your choice to the artboard or page (as a colored rectangle).
    *   **Color override**—this changes the color of all strokes in the document. Gradient fills use the color with adjusted luminosities for gradient colors.
    *   **Remove hidden items**—if checked, hidden or frozen layers are excluded on import.
    *   **Display entity handles**—when enabled, each imported named entity is given a handle suffix, e.g. HATCH - 0x19C2 instead of HATCH. Use for troubleshooting problems with individual entities.
    *   **Convert hatches to curves**—when enabled, hatch patterns and strokes are converted to curves, which can be edited. When disabled, hatches remain as fills and strokes.
    *   **Override line weights**—when **Selection** is set to Model, all line weights will be set to _0.1 pt_ with this option enabled.
    *   **Sanitize model**—when **Selection** is set to Model, this removes any objects in the model that appear physically distant from the main model; these objects can be introduced by CAD plug-ins. This would otherwise affect Affinity's ability to scale the model to fit the page.

Once open, you can display the CAD design as it would be seen in a CAD app by using the **Hairline** view mode (**View > Mode**).

Do one of the following:

*   For Mac: Open Finder and drag the DWG/DXF file to an off-page area of your workspace.
*   For Windows: Open File Explorer and drag the DWG/DXF file to an off-page area of your workspace.

*   [Opening documents and images](https://www.affinity.studio/help/get-started-open-document/)
*   [Importing PDF documents](https://www.affinity.studio/help/get-started-import-pdf/)
*   [Importing InDesign (IDML) documents](https://www.affinity.studio/help/get-started-import-in-design/)
*   [Importing other Adobe documents](https://www.affinity.studio/help/get-started-import-adobe/)
*   [Placing content](https://www.affinity.studio/help/media-place-images/)
*   [Color management](https://www.affinity.studio/help/clr-clr-profiles/)
*   [Navigator panel](https://www.affinity.studio/help/panels-navigator-panel/)
*   [Supported file formats](https://www.affinity.studio/help/appendix-fileformat/)

How would you rate the help you received from this article?
