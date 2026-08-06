---
title: "Release notes - Affinity Help Center"
source: https://www.affinity.studio/help/release-notes/
slug: release-notes
fetched: 2026-08-06
---

# Release notes - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/release-notes/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Installation and setup](https://www.affinity.studio/help/installation-setup/)
3.   Release notes

**General**

*   [Brand Kit integration](https://www.affinity.studio/help/use-brandkits-affinity/)
    *   Leverage centralised Brand Kits in Affinity
    *   Build pro assets on-brand in Affinity
    *   Export directly to your Brand Kits

*   [AI Automation with Claude](https://www.affinity.studio/help/ai-connector-setup/)
    *   No coding knowledge required
    *   Describe repetitive production tasks in plain language to Claude Desktop
    *   Work with existing documents as well as new ones
    *   Save automations to the Scripts panel to reuse

*   [Import Affinity content into DaVinci Resolve](https://www.affinity.studio/help/extras-davinci-affinity/)
    *   For pro-level overlays and end cards
    *   Edited Affinity content updates automatically on timeline
    *   Split layers for more editing control
    *   Apply motion via keyframes

**Graphic Design**

*   [Vector Blob Brush Tool](https://www.affinity.studio/help/tools-tools-vector-blob-brush/)
    *   [Build new shapes](https://www.affinity.studio/help/object-control-join-vector-brushes/) from brush outlines
    *   Add to existing shape’s geometry
    *   Includes pressure support 

*   [Vector Blob Erase Tool](https://www.affinity.studio/help/tools-tools-vector-erase-brush/)
    *   The erase equivalent of the Vector Blob Brush Tool

**Photo Editing**

*   [Editing CaptureOne content in Affinity](https://www.affinity.studio/help/addons-capture-one/)
    *   Organize Affinity files easily with Capture One library's expansive filtering options
    *   Continue editing non-destructively without manually exporting files
    *   Retain masks and editing context without flattening the image
    *   Access more advanced layer-based retouching/composition workflows

*   [Texture filter](https://www.affinity.studio/help/filters-filter-texture-filter/)
    *   Enhance fine surface detail without harsh contrast
    *   Balance detail before sharpening
    *   Maintain realism while refining image quality

*   [Multi Band sharpen filter](https://www.affinity.studio/help/filters-filter-multi-band-sharpen/)
    *   A new Fine Detail sharpening option

*   Raw image processing:
    *   New [mask types](https://www.affinity.studio/help/raw-using-masks-develop-studio/): Object Selection, Luminosity, Hue Range and Compound. 
    *   Choice of tone curve methods on opening raw files 
    *   Sharpening and tone curve settings are remembered 
    *   Panorama, merge and stacking operations now use the currently set develop process
    *   Focus peaking visual aid for evaluating image focus and sharpness

*   Astrophotography improvements
    *   [Auto stretch](https://www.affinity.studio/help/filters-filter-auto-stretch/): options to preserve important highlights and detail
    *   Optional disabling of Tone Stretch when stacking FIT files
    *   [Automatic color mapping of layers](https://www.affinity.studio/help/filters-filter-color-map-mono-layers/)
    *   Assign color mapping in the Stacked Images panel

*   More choice in AI models with new AI quality options
    *   AI quality levels for [Generate Image](https://www.affinity.studio/help/canva-ai-canva-ai-generate-image/) and [Generative Edit](https://www.affinity.studio/help/tools-tools-generative-edit/), with support for Premium and Ultra models
    *   Model updates available between app updates

*   Pigment model for natural color blending ([Paint Mixer](https://www.affinity.studio/help/tools-tools-paint-mixer-brush/)/[Smudge](https://www.affinity.studio/help/tools-tools-smudge-brush/) brush tools)
*   Updated Affinity Raw Engine to 16th Apr 26 - [new cameras supported](https://www.affinity.studio/help/supported-raw-files/?query=release%20notes): 
    *   Ricoh GR IV Monochrome
    *   Sony A7V (ILCE-7M5): (updated colordata)

**Page Layout**

*   [Image bullets](https://www.affinity.studio/help/text-text-bullets-and-numbering/) – use an image file in place of a standard bullet glyph, with support for object defaults and text styles.
    *   Any placeable image file type supported
    *   Scale and offset controls relative to font size
    *   Vector images retained on export where possible
    *   SVGs can inherit font fill colour via currentColor

*   [Improved OpenType font support](https://www.affinity.studio/help/text-opentype-fonts/)
    *   Available via the Character panel and Text Style Editor
    *   Apply a font-supplied or custom palette to color fonts
    *   Recolor fonts by applying a blend: color, hue, or alpha

*   [Paste a URL](https://www.affinity.studio/help/object-control-copy-paste-options/) onto selected text to create a hyperlink

This section lists the key improvements and bug fixes included in this version.

**For all users**

Fixes for:

*   Black and white images no longer develop a color tint when adjusting Vibrance.
*   The app no longer crashes when editing an interpreted, password-protected PDF that wasn’t unlocked with its password.
*   Super Resolution no longer crashes when used on images that contain fully transparent pixels.
*   a crash that could occur when placing certain XLSX files.
*   a crash when opening a document containing an edited, password-protected embedded PDF.
*   an issue where a Table of Contents preflight error wouldn’t clear if the affected paragraph style was applied on a master page.
*   an issue where notes weren’t scaled correctly when changing a document’s DPI, which could also cause a crash when undoing and redoing the change.
*   Hatch fills now export to PDF correctly.
*   an issue where special characters in hyperlink URLs could be converted to their Unicode values.
*   an issue where pages of different widths in a multi-page spread exported at the same width when using raster file formats.
*   an issue where the Picture Frame tool’s context toolbar menu was missing some options.
*   an issue where exporting to PDF could fail silently if a dashed line’s phase was set to a large negative value.
*   an inconsistency in the character limit when naming or renaming custom document presets.
*   an issue where copying and pasting a placed image created a new entry in the Resource Manager instead of grouping it with the original.
*   an issue where saving text defaults didn’t work if attributes were changed while text was selected.
*   an issue where a horizontal guide on an ambidextrous master page only appeared on one page of a spread instead of stretching across both.
*   an issue where updating a preset with new settings would revert its name to a previous one.
*   an issue where SVG exports of duplicated objects could show incorrect or duplicated content when rasterizing unsupported properties.
*   an issue where the Memory Efficiency value in the Info panel could show an incorrect value after closing certain documents.

**For Mac users**

Fixes for:

*   a crash that occurred when pasting a clipboard image as an artboard name.
*   an issue where the Gradient Overlay icon was missing from the Quick FX panel.
*   an issue where the Edit in Canva icon in the Brand Kits panel appeared white and was hard to see in Light UI.
*   File type associations
    *   Book files (.afbook) can now be dropped onto the app icon in the dock.
    *   IDML files are now automatically associated with the app.
    *   Template files (.aftemplate) can now be opened from their icon or by dropping them on the dock icon.

*   Studio button tooltips now show the correct function key shortcut when Rich Tooltips are disabled.
*   an issue where the font type icon was missing from font lists.
*   a crash that could occur when opening the Document Setup, Spread Properties, Add Master, or Document Metadata dialogs on low-resolution screens.
*   an issue where changing PDF export settings for vector-heavy documents could cause the app to become unresponsive.
*   an issue where adding a hyperlink to text within a flow of linked text frames created duplicate entries in the Hyperlinks panel.
*   a performance issue where indexing entries in large, complex documents could cause the app to become unresponsive for an extended period.

**For Windows users**

Fixes for:

*   Hatch panel field values can now be adjusted using a mouse scroll.
*   Hairline view now retains color.
*   a crash in the Layers panel caused by quickly clicking away while a layer’s Opacity slider is still open.
*   The Color Picker tool’s Alt+Click shortcut now works correctly while painting.
*   an issue where the Path Brush Editor showed the wrong preview after drawing a brush stroke.
*   an issue where unchecking a Table of Contents text style also unchecked Include Page Numbers for that style.
*   an issue where buttons in the Export dialog appeared in the wrong place.
*   an issue where the Master Page context menu could appear in the wrong location the first time it was opened.
*   an issue where an empty group couldn’t be created using the Layers panel’s Group icon.
*   an issue where the app could hang when exporting a document with the Color Picker tool selected.
*   an issue where scrolling through the Stock panel could unexpectedly clear the results and show a ‘No results’ message.
*   Entering a decimal via the numeric keypad now respects the system locale (for example, using a comma instead of a period where appropriate).
*   a crash that could occur when using the arrow keys in the URL field of the Hyperlink Properties dialog.

This section lists the key improvements and bug fixes included in this version.

**For all users**

Fixes for:

*   Crashes when:
    *   exporting to EPUB (file specific)
    *   using Add Pages from File
    *   converting a text frame with a pinned object to art text
    *   opening a user file created before version 2.6 (Designer, Photo or Publisher)
    *   closing a document containing an image bullet
    *   switching between teams after viewing Canva export options

*   Captions:
    *   Picture frame caption font size is scaled incorrectly by the frame’s content scaling handle
    *   Caption positioning and scaling inside groups is incorrect
    *   A caption can’t be added when multiple objects are selected
    *   Marquee selecting multiple captioned objects only selects a single object or the captions

*   Export:
    *   Export to PDF fails silently if a dashed line phase is set to a large negative value
    *   Exporting a double page spread as All Pages to 'PDF Digital' loses items from a placed file on one of the pages
    *   A placed PDF appears blurry until zoomed in
    *   A placed PDF inherits the opacity of objects behind it in the layer stack
    *   EPUB Export: fixed issue where exported files produced DAISY validation warnings due to missing ARIA roles on navigation elements.

*   Preflight:
    *   The Preflight Table of Contents ‘Fix’ button results in a ‘Hyperlink to Invalid Anchor’ error
    *   A Table of Contents preflight error won’t clear after being resolved

*   Editing a Spare Channel does not display the channel
*   The Hatch Pattern editor is missing the left scroll button for Dash and Spaces
*   The Swatches panel shows misaligned icons when the Typography panel is open and docked
*   Inner and outer margins are reversed and linked when the link icon is toggled off
*   Text attribute defaults aren’t applied unless fill color is changed
*   Collectively adjusting the image bullet offset changes all bullets to the same image
*   Importing SVGs that render incorrectly or fail to import due to incorrect path syntax
*   Clicking Reset on the Tone Stretch adjustment layer dialog disables the Black Point slider
*   The Vectorscope does not show circular graph outlines in Light UI
*   The tooltip for the Layers panel cog says “Blend Ranges” but the panel is called “Blend Options”
*   Scripting SDK: dialog label text can't be updated dynamically

**For Mac users**

Fixes for:

*   Crashes when:
    *   toggling the lock colorspace option without an open document
    *   marquee selecting through a clipping mask inside another clipping mask group
    *   applying the Halftone filter with a very large cell size to a landscape image
    *   quitting after using the Paint Mixer Brush Tool in Pigment Blend mode

*   EPUB exports may fail DAISY accessibility validation due to missing role declarations and empty anchors
*   Hatch:
    *   The color well and color picker aren’t removed when using a non-English UI language
    *   Tooltips are incorrect for Add Dash, Add Space, and Delete
    *   The UI is inconsistent with the Windows version

*   Light UI:
    *   Save as Package shows low-contrast text
    *   Panel close buttons appear as gray circles
    *   The Macro panel has low-contrast text
    *   The Hatch dialog is unreadable
    *   Rulers are different sizes
    *   The Complementary colors lock icon disappears
    *   The Layer Effects curve profile is not visible
    *   The Grid and Snapping Axis settings have low-contrast text
    *   Several panel icons are invisible (Normals Adjustment, Table Formats, Lock Insets, Style Settings in TOC)
    *   Switching to the Light UI requires a restart
    *   The Typography ‘Hide Irrelevant Features’ option stays black
    *   The Develop Masks panel is invisible
    *   The K Only button has no highlight state
    *   The document tabs area doesn’t update when switching to Light UI
    *   The Develop and Tone Map sub-studio panel labels are invisible in Light UI

*   Caption width is not adjusted when cropped
*   Click and drag export is not working
*   The Background gray Level setting is not persistent
*   The Text Style Editor ‘Based On’ filter works incorrectly
*   The Booklet option is missing from the Books panel
*   The drawing scale can’t be changed for artboards
*   The Perlin Noise Blend Mode doesn’t apply

**For Windows users**

Fixes for:

*   Crashes when:
    *   scrolling in the font list for a Bitcount variable font 
    *   double-clicking on path brushes after importing other path brushes
    *   modifying a TOC after deleting a tab separator
    *   dragging items from the Stock panel
    *   committing a layer rename

*   Hatch:
    *   The spacer is inaccessible via Context Toolbar in certain languages
    *   Text labels are cropped in certain languages

*   Keyboard shortcuts:
    *   Keyboard shortcuts and cycling will select other studios
    *   Shortcuts stop working after a pop-up menu is dismissed

*   Light UI:
    *   The History Set Undo Brush is invisible
    *   The Send Feedback button has low-contrast text
    *   The Document Setup dialog has black on black text

*   The Chromatic Aberration and Remove Lens Vignette controls are missing source drop-down menus
*   The Sources panel height can’t be adjusted
*   Generate Image Variations is not working
*   Artboard thumbnails are not rendering correctly
*   The Isometric panel height can’t be adjusted
*   Split View labels are not displaying correctly
*   The Vector Flood Fill being activated in Layout studio when not hosted there
*   Export preset rename and delete options are grayed out
*   The Edit Caption shortcut is missing
*   The Chromatic Aberration progress bar is not displaying
*   Brand Kits cursor is not centering correctly
*   Alt+Drag layers is not working correctly
*   Flood Fill Source is not working at 150% display scaling
*   Macro parameters can’t be edited simultaneously
*   The OpenColorIO label is not displaying correctly
*   The Font List Character panel is not working
*   The Filter Brush Tool's Texture filter can't be selected
*   Brushes require a color to be applied before they can be used

This section lists the key improvements and bug fixes included in the above version.

**For all users**

Fixes for:

*   Brand Kit issues:
    *   The Affinity app crashes when exporting a Brand Kit swatches palette
    *   Default Brand Kit appears blank in the Quick Export Panel

*   Crash when Snap to Grid is enabled, if Grid and Snapping Axis is in Cube Mode
*   In the Pixel Studio, pressing the G key does not cycle between the expected tools
*   AI automation improvements, including better dialog support

**For Mac users**

Fixes for:

*   Export to Dropbox fails silently
*   Brand Kit issues:
    *   The Brand Kit selector collapses multiple brand kits with the same name into a single item
    *   The Export window shows unsupported formats
    *   Update Style is available on text tool's context toolbar for Brand Kit text styles
    *   Categories aren't showing in the Canva Brand Kits panel if all Categories are empty

*   Light UI Style issues:
    *   Multi Band Sharpen Tool and Texture Tool icons are solid black
    *   Settings for Model Context Protocol show text which is difficult to read

**For Windows users**

Fixes for:

*   Brand Kit issues:
    *   Default Canva swatch palette filenames include an illegal character
    *   Crash when loading assets during poor network connection
    *   Object is moved off the canvas when it is blocked from being dragged to a Brand Kit
    *   Double-click incorrectly lets you 'edit' read-only text styles from Canva

*   Paste image pastes an empty text frame
*   Inability to edit document color palettes

**For Affinity for China Mac users**

*   Affinity for China is not installing Quick Look extensions

This section lists the key improvements and bug fixes included in the above version.

**For all users**

Fixes for:

*   Customer feedback doesn't send when trying to send current document with no other attachments
*   App crashes when adding a caption to a picture frame based on a master page
*   Object captions shift vertically when the object is transformed if the caption text frame is scaled
*   Only the caption at the bottom of the layer stack is anchored when rotating an image with multiple captions
*   Master page captions aren't shown on publication pages unless the page is zoomed
*   Caption counter doesn't respect right facing master page
*   Unable to add a global swatch from text object using the right-click context menu
*   Selecting a logical condition in the Data Merge Data viewer process tab scrolls it back to the top of the panel
*   A new text style can be based on itself before being created

**For Mac users**

*   2-bit images inside PDF files import with incorrect colours
*   Linked vector stock panel resources are reported missing after a system restart
*   Color Picker is laggy when zooming/panning
*   Light UI mode fixes:
    *   Links panel contrast issues
    *   Many panel controls have too little contrast
    *   Index: blue highlight runs through some of the text in the fields
    *   Subscription upgrade and onboarding window is dark
    *   The Welcome screen user name drop-down arrow is hidden
    *   Switching between Light UI and Dark UI mode after launch fails to change the page number colour in the Pages panel

*   The Data Merge Data viewer button text overflows the buttons when the panel is at its narrowest width
*   Right-hand-side panels' widths behave oddly
*   Automatically named layers suffer from a contrast issue
*   Reference to Serif in submit feedback error message

**For Windows users**

*   App instability:
    *   When closing a file in the Tone Mapping Studio
    *   When auto-expanding groups with another layer
    *   When overwriting existing slices failing to show the overwrite warning dialog
    *   When Ctrl-clicking more than one file under the recent documents tab on the home screen
    *   On import IDML files (user specific)

*   The stroke in the context toolbar won't accept values >100
*   Layer visibility toggle in the Layers panel retains focus after clicking it
*   The Typography panel check boxes and radio buttons are not visible in Light UI mode
*   Subfolders fail to show their content when adding templates
*   Pixabay vector option is not working
*   Recent document has a white gradient appearing when it overflows
*   New from clipboard command only functions if there is already a document open
*   The Reset Content Migration prompt is still found under Clear User Data

*   [How do I update Affinity?](https://www.affinity.studio/help/update-affinity/)
*   [Previous release notes](https://www.affinity.studio/help/mar-26-release-notes/)

How would you rate the help you received from this article?
