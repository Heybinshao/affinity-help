---
title: "Refining pixel selection edges - Affinity Help Center"
source: https://www.affinity.studio/help/selections-selections-refine/
slug: selections-selections-refine
fetched: 2026-08-06
---

# Refining pixel selection edges - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/selections-selections-refine/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Refining pixel selection edges

Once a pixel selection has been made, you can refine its edges to ensure it is as accurate as needed.

For very fine selection (e.g., of hair against a colored background) use an adjustment brush as part of the refinement to 'brush-in' fine detail.

![Image 1: Refine selection after](https://images.ctfassets.net/3p2fxa94bzao/6jQXDJdEHPB3M9ycZFL4em/656c806c867db1c048148ddc79dc62c1/raster_selections_refine_before.jpg)

A Quick Mask preview prior to refining pixel selection.

![Image 2: Refine selection before](https://images.ctfassets.net/3p2fxa94bzao/2N8DJE7lCxng5miBt9bRyl/a2ae6002f31c8fbc388c67ba631c149a/raster_selections_refine_after.jpg)

Base image before making a pixel selection.

The following settings can be adjusted from the dialog:

*   **Preview**—sets the way your selection and page display. Select from the pop-up menu. 
    *   **Overlay**—presents the selection overlaid against red, translucent area indicating that area as not part of the selection.
    *   **Black Matte**—presents the selection against non-selected areas being blacked out.
    *   **White Matte**—presents the selection against non-selected areas in white.
    *   **Black & White**—presents the selection as white while non-selected areas as black.
    *   **Transparent**—presents the selection against a checked pattern indicated as non-selected.

*   **Matte Edges**—when selected (default), the selection area closely follows image edges. If this option is off, selection doesn't follow image edges which is useful for more accurately refining straight selection edges.
*   **Border width**—expands the selection by adjusting the width of its border. Drag the slider to set the value.
*   **Smooth**—determines the curvature of the selection's edge. Drag the slider to set the value.
*   **Feather**—determines the softness (opacity) of the transition at the edge of the selection. Drag the slider to set the value.
*   **Ramp**—In areas where there is a gradual transition from opaque to transparent pixels it makes the transition sharper and moves the selection in or out, depending on which direction you drag the slider. Fully opaque and fully transparent pixels are unaffected.
*   **Adjustment brush**—determines the adjustment brush's refinement mode. 
    *   **Matte**—re-analyses the selection and attempts to separate foreground detail from the background. Perfect for fine detail refinements such as stray hairs or similar thin elements of a subject.
    *   **Foreground**—adds to the selection (revealing more of the foreground).
    *   **Background**—deletes from the selection (revealing more of the background).
    *   **Feather**—softens the alpha edge of the selection.

*   **Size**—sets the size of the brush tip. Type directly in the text box or drag the pop-up slider to set the value.
*   **Output**—determines how the selection is applied upon exiting the dialog. Select from the pop-up menu. 
    *   **Selection**—applies the refinement directly to the selection.
    *   **Mask**—applies the refinement to the selection as a mask.

*   **Color decontamination**—when checked, protects the edges of the selected areas from undesired color spills.

The size of a brush (when using the Matte option) determines what is taken into consideration when Affinity evaluates the appointed areas. Use a brush size that allows the app to recognize the differences between pixels and don't be afraid to paint your strokes to cover both the areas you'd like to select and those you'd like to exclude as this aids calculations.

![Image 3: Refining selection along an edge containing finely detailed fur](https://images.ctfassets.net/3p2fxa94bzao/6lmLUoQDDs78tmamGfLFJU/50753d0cadf65c53fa4904393572e1da/selections_refine.jpg)

Use the Foreground adjustment brush to select the interior (top left, brush strokes; top right, resulting selection), then the Matte adjustment brush to paint along the edge and individual hairs (bottom left). Use the Preview options to inspect the refined selection (bottom right).

In Affinity, smoothing the edges of your selection can be performed with the dedicated in-dialog slider.

![Image 4: Smooth setting in refining selections](https://images.ctfassets.net/3p2fxa94bzao/3IqP8NHrywGegZjwhWn1ed/1ca256239049156dbd07ddf9b3029ea4/smooth_low_high.jpg)

Left: Smooth setting effect with a low value of 0.3px. Right: Smooth setting effect on the edges with a high value of 48px.

As you increase the slider value, you’ll notice the amount of details included (left) and excluded (right) from the selection. The setting takes effect by evaluating edge pixel data and delivering a softer result as you increase the pixel value, which is great for at least a couple of scenarios: one, where you need the selected object to fade into the underlying image; or two, whereby you’d like for it to stand out with solid, more defined edges.

Feathering the edges of your selection can be performed by either adjusting the dedicated in-dialog slider, or setting the brush mode to **Smooth**.

![Image 5: Feather setting in refining selections](https://images.ctfassets.net/3p2fxa94bzao/4gKAxl9wrKJqFLYUwgYkih/69f6857aeac276b4c27e32478fd19dab/feather_low_high.jpg)

Left: Smooth setting effect with a low value of 0.2px. Right: Smooth setting effect on the edges with a high value of 49px.

The **Feather** brush mode allows for the borders of your selection to be smoother, even more refined with edge pixels progressively blurred as you increase the brush size. In addition, you can modify these edges further by experimenting with the Feather slider in the dialog – the brush mode works in tandem with the slider to deliver the desired effect.

Brush size can be adjusted mid-stroke with the **[** and **]** keys.

To better visualize the effects of feathering refinements, change the Preview mode to **Black and white**.

This feature is only available in Affinity for desktop.

If you selected the **Mask** output option the first time you refined the selection, simply right-click on the mask in the layers panel and select **Refine Mask**. If your output was set to Selection, with the selection still in place, use the same **Refine** button on the context toolbar, as before.

The following modifier key(s) can be used:

*    Press the **⌃(ctrl)⌥** keys (Mac) / **Ctrl**+**Alt** keys (Windows) together and drag on the page to set brush sizes. Dragging left/right will decrease/increase the brush size, respectively. Alternatively, use the **[** or **]** keys to achieve the same. 

1.    Do one of the following: 
    *   From any selection tool's context toolbar, click **Refine**.
    *   On the **Pixel** menu, select **Pixel Selection > Refine Edges**.

2.   Adjust the settings in the dialog and/or select the brush mode, as required.
3.   If you wish to adjust the selection edges by painting, drag on the preview.
4.   Click **Apply**.

*   [Creating pixel selections](https://www.affinity.studio/help/selections-selections-create/)
*   [Modifying pixel selections](https://www.affinity.studio/help/selections-selections-modify/)

How would you rate the help you received from this article?
