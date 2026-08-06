---
title: "Warping using the Liquify Studio - Affinity Help Center"
source: https://www.affinity.studio/help/liquify-persona-liquify/
slug: liquify-persona-liquify
fetched: 2026-08-06
---

# Warping using the Liquify Studio - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/liquify-persona-liquify/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Photo editing](https://www.affinity.studio/help/photo-editing/)
3.   Warping using the Liquify Studio

The Liquify Studio provides the perfect environment for highly accurate warping of images.

![Image 1: After](https://images.ctfassets.net/3p2fxa94bzao/6Z9JLdD6ag29sh4SH1GiwK/d715d351aaa1909a043ac61c5dcde8c1/liquify_after.png)

After using the Liquify Pinch Tool.

![Image 2: Before](https://images.ctfassets.net/3p2fxa94bzao/1lDpFuYKcPFkeY8sdDhtUH/e953e9a0b6b70b1848da00face937176/liquify_before.png)

Before using the Liquify Pinch Tool.

When a warp is applied to an image, the overlaid mesh will update to describe the warp on a grid. Furthermore, modifying the grid will update the warped image below.

Prior to entering the Liquify Studio, ensure you have selected the correct image or RAW layer in the panel.

Image warping is controlled using a combination of the Liquify tools. These can be divided into three types:

*   Direct—these affect the image by painting over image pixels. These include the **Liquify Push Forward**, **Liquify Push Left**, **Liquify Twirl**, **Liquify Pinch**, **Liquify Punch**, **Liquify Turbulence** and **Liquify Reconstruct** tools.
*   Indirect—these affect the mesh. These include the **Mesh Clone** Liquify tool.
*   [Masking](https://www.affinity.studio/help/liquify-persona-liquify-masking/)—these apply or remove masked areas. These include the **Freeze** and **Thaw** Liquify tools.

The mesh is an overlay which is used as a visual aid to help identify any previous warp operations. The mesh can also be reconstructed to uniformly strengthen or weaken the overall warping effect.

These Liquify tools are supported by a dedicated [Brushes panel](https://www.affinity.studio/help/panels-liquify-panel-brush/).

Warping can be further modified and controlled using the [Mesh](https://www.affinity.studio/help/panels-liquify-panel-mesh/) and [Mask](https://www.affinity.studio/help/panels-liquify-panel-mask/) panels.

1.   Select a pixel layer.
2.    Do one of the following: 
    *   To apply the effect _non-destructively_: Apply the effect as a live filter layer from the **Layers** panel or **Pixel > New Live Filter Layer > Distort > Liquify**.
    *   To apply the effect _directly to the image_: **^(ctrl)**-click (Mac) / **right**-click (Windows) on the image and select **Liquify**. 
    *   With the **Move Tool** active, on the context toolbar click **Liquify**.

3.   Use the Liquify tools, as described above.
4.   Select **Apply** or **Done**.

1.   Select a Liquify tool ![Image 3](https://images.ctfassets.net/3p2fxa94bzao/2C593PuuUuzJnS8Zk6Uysk/15798476ec5635bb898f118514ebe8ff/liquify_push_forward_tool.svg) ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/7coh6pqNG77HluxAble7XF/e32007fb9041a5209c3850f8c5ed09a1/liquify_push_left_tool.svg) ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/6HgtWuDfcB8uXtKpVLYvNx/d2d25a9eb3896dad0e4a1e8666caaf3e/liquify_twirl_tool.svg) ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/40SzCWTsK6kIkQ9dpBZc6J/5d37dd018b2817b4660818b4766883b8/liquify_pinch_tool.svg) ![Image 7](https://images.ctfassets.net/3p2fxa94bzao/4t5mNltjNwJVDXftYyA3dR/0d5398fe64f4c16bc3f038f1c0cef5d2/liquify_punch_tool.svg) ![Image 8](https://images.ctfassets.net/3p2fxa94bzao/011Kb7jOLyxRvL1mBgzpsX/0571f0bd3602a7f443a78da07a34e21c/liquify_turbulence_tool.svg) .
2.   Adjust settings on the **Brush** panel.
3.    Do one of the following: 
    *   Click or drag on the image to apply the default warp effect.
    *   **⌥**-click (Mac) / **Alt**-click (Windows) or **⌥**-drag (Mac) / **Alt**-drag (Windows) on the image to apply the opposite warp effect. (Not available on all tools.) 

4.   The effect of the tool is cumulative. If the result is not strong enough, repeat the step above.

The following can be used:

*   Hold the **⌃(ctrl)⌥** keys (Mac) / **Ctrl**+**Alt** keys (Windows) and drag on the page. Dragging left or right will decrease or increase the brush size, respectively. Alternatively, use the **[** or **]** keys, respectively. Dragging up or down will decrease or increase the brush hardness, respectively. 
*   With many Brush tools in the Pixel and Liquify Studios, you can quickly change the opacity of your brush using numerical keys.

1.   Click the **Liquify Clone Mesh Tool**![Image 9](https://images.ctfassets.net/3p2fxa94bzao/6RF1xhioHoU79Y72PKUdPY/2945f19a0c926ea29f95351a4e2e8128/liquify_clone_mesh_tool.svg) .
2.   Adjust settings on the **Brush** panel.
3.   **⌥**-click (Mac) / **Alt**-click (Windows) on the area of the mesh you wish to copy. 
4.   Click on the area of the mesh to 'paste' the copied effect.
5.   Repeat the step above to apply the copied effect elsewhere on the image.

For individual pixels:

1.   Click the **Liquify Reconstruct Tool**![Image 10](https://images.ctfassets.net/3p2fxa94bzao/1FscGrp8mqervTOQyWdHdG/535181f739642919ff8fad6cc8ef9fc0/liquify_reconstruct_mesh_tool.svg) .
2.   Click or drag on the image to remove the warp effect.

For the entire image:

*   On the **Mesh** panel, click **Reset Mesh**.

1.    On the **Mesh** panel, set the **Reconstruct Mesh** value: 
    *   **Above 100%** to strengthen the effect.
    *   **Below 100%** to subdue the effect.

2.   (Optional) Click **Apply** and then repeat the above step to further strengthen or subdue the effect.

*   On the context toolbar, click **Apply**.The warp is permanently applied to the image and the Pixel Studio will display.

To discard applied warp effects and exit the Liquify Studio, click **Cancel** on the context toolbar.

The Toolbar provides quick access to mesh controls which allow you to reset, save and load a mesh.

*   ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/6lAkdpnoMyo82fMMTzbzMq/8b5880cb4055d0d63c6f17160fcbfe77/save_mesh.svg) **Reset Mesh**—applies a new mesh and removes all currently applied effects from the underlying image.
*   ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/6lAkdpnoMyo82fMMTzbzMq/8b5880cb4055d0d63c6f17160fcbfe77/save_mesh.svg) **Save Mesh**—saves the current mesh for future application.
*   ![Image 13](https://images.ctfassets.net/3p2fxa94bzao/2hVL5h2pnctQnvrqBk1dE4/80a4880486470b7874b611730efa5f73/load_mesh.svg) **Load Mesh**—applies a previously saved mesh.

For more information on mesh controls, see the [Mesh panel](https://www.affinity.studio/help/panels-liquify-panel-mesh/) topic.

There are a variety of view modes available in the Liquify Studio which give you the opportunity of seeing how your warped image compares to the original.

On the Toolbar, do one of the following:

*   Click **None**![Image 14](https://images.ctfassets.net/3p2fxa94bzao/64YJgmKSUbLdSuf5GsGqvK/db4f634044988a695cc7da9cde6a964b/standard_view.svg)  to display the warped image in isolation.
*   Click **Split**![Image 15](https://images.ctfassets.net/3p2fxa94bzao/SWhhcyi7P9xZaJXlyOFDE/56a0c275bb369631b3c5564fb9f24c83/split_view.svg)  to display both warped and original image on the same page. A sliding divider can be repositioned to view the image 'Before' and 'After' warping
*   Click **Mirror**![Image 16](https://images.ctfassets.net/3p2fxa94bzao/3oYRYc43vhHLh1fSgVmMxu/7a99e5a811f9fe9ef886c16980d7b95b/mirror_view.svg)  to display warped and original image side-by-side on separate pages. Panning and zooming affects both pages simultaneously so the same area is always displayed in both pages

*   [Liquify Push Forward Tool](https://www.affinity.studio/help/tools-tools-liquify-push-forward/)
*   [Liquify Push Left Tool](https://www.affinity.studio/help/tools-tools-liquify-push-left/)
*   [Liquify Twirl Tool](https://www.affinity.studio/help/tools-tools-liquify-twirl/)
*   [Liquify Pinch Tool](https://www.affinity.studio/help/tools-tools-liquify-pinch/)
*   [Liquify Punch Tool](https://www.affinity.studio/help/tools-tools-liquify-punch/)
*   [Liquify Turbulence Tool](https://www.affinity.studio/help/tools-tools-liquify-turbulence/)
*   [Liquify Mesh Clone Tool](https://www.affinity.studio/help/tools-tools-liquify-mesh-clone/)
*   [Liquify Reconstruct Tool](https://www.affinity.studio/help/tools-tools-liquify-reconstruct/)
*   [Liquify Freeze Tool](https://www.affinity.studio/help/tools-tools-liquify-freeze/)
*   [Liquify Thaw Tool](https://www.affinity.studio/help/tools-tools-liquify-thaw/)
*   [Brushes panel](https://www.affinity.studio/help/panels-liquify-panel-brush/)
*   [Mesh panel](https://www.affinity.studio/help/panels-liquify-panel-mesh/)
*   [Mesh Warp Tool](https://www.affinity.studio/help/tools-tools-mesh-warp/)
*   [Liquify filter](https://www.affinity.studio/help/filters-filter-liquify/)

How would you rate the help you received from this article?
