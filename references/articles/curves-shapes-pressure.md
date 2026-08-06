---
title: "Pressure sensitivity - Affinity Help Center"
source: https://www.affinity.studio/help/curves-shapes-pressure/
slug: curves-shapes-pressure
fetched: 2026-08-06
---

# Pressure sensitivity - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/curves-shapes-pressure/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Graphic design](https://www.affinity.studio/help/graphic-design/)
3.   Pressure sensitivity

Affinity lets you draw or paint natural strokes using real or simulated pressure sensitivity.

![Image 1: Pressue sensitivity example](https://images.ctfassets.net/3p2fxa94bzao/3SzqPuIkotVp7P0CgHxk2Y/bb21a037e21078b579380f85cff9a226/pressure.jpg)

When you're using line or brush tools, several pressure-sensitive methods are possible:

*   _using a pressure-sensitive device_—this supports real pressure-sensitive drawing and painting. You can simply connect your device and you've automatically got pressure-sensitive input.
*   _without a pressure-sensitive device_—you can achieve simulated pressure sensitivity just using your mouse. The simulated pressure is based on the speed (velocity) of your mouse movement.
*   _pressure simulation manually_—create your own custom pressure profile from scratch, for a more custom look and to be fully in control of the stroke's look.

For brushes, this automatic response with a pressure-sensitive device is governed by the brush controller (input type)—it varies stroke width, brush size, flow, etc. Types of input are:

*   For editable path brushes: 'Automatic', 'Pressure', 'Velocity', 'Brush Defaults', or 'None'. Automatic will sense the type of input (Apple Pencil, finger) automatically for you.
*   For raster brushes: 'Pressure', 'Tilt', 'Velocity', 'Velocity Inverse', 'Random', 'Angle', 'Cyclic', 'Direction', Distance, 'None'.

If set to 'None', the stroke is always a fixed width, flow setting, etc. Otherwise, the stroke properties will vary from a minimum to maximum amount (e.g. the full stroke width).

While you get the response you need from either input, you'll still be able to fine-tune brush settings for pressure/velocity.

*    For editable path brush settings (Vector Studio![Image 2](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg) ): jitter options let you control how brush width and flow are affected by your type of input.
*   For raster brush settings (Pixel Studio![Image 3](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) ): as for editable path brush options, but additional jitter options are provided that affect brush hardness, shape, color, and the scatter and rotation of nozzles.

1.   Do one of the following: 
    *   ![Image 4](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg) ![Image 5](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg)  Navigate to the **Stroke** panel.
    *   ![Image 6](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg)  Click **Edit stroke settings**![Image 7: Edit stroke settings](https://images.ctfassets.net/3p2fxa94bzao/LAIAniI5tfK3bknzYOUQB/9af81e28e315cea94436ab657c986f85/stroke.svg) on the context toolbar.

2.   Click the **Pressure** option.
3.   Manipulate the graph to form the desired pressure profile. (See examples below.)
4.   Begin drawing your strokes.

![Image 8: Pressure profile](https://images.ctfassets.net/3p2fxa94bzao/2ke3TxFjvQD0BjGTwChzVR/26a58b2ee68dfc7a73fd98a959330f15/panel_stroke_pressureprofilequad.png)

Uniformly reducing stroke width using locked nodes (A), linear tapering of stroke (B; unlocked by ⌥-drag (Mac) / Alt-drag (Windows) or second click then drag), tapering of stroke at both ends (C; a combination of A and adding a new node by clicking) and modulating stroke width (D; a combination of A and adding multiple nodes).

| Node type | Description |
| --- | --- |
| ![Image 9](https://images.ctfassets.net/3p2fxa94bzao/6gXdQ0IJZoLj1tfn9PZTEr/3725560e075c20a4bc7de3e10f3d86b2/pressure_node_end_deselected.png) | End node (deselected)—drag to move _both_ end nodes up/down at the same time |
| ![Image 10](https://images.ctfassets.net/3p2fxa94bzao/45vqoHisj6V6KVe0076bZj/bd1e6766cdbeca07fa36ae4777e0c383/pressure_node_end_selected.png) | End node (selected)—drag to move _both_ end nodes up or down at the same time or click to move the end node independently of the other end node |
| ![Image 11](https://images.ctfassets.net/3p2fxa94bzao/4g1W7S047Hayh0zRlI8Dqj/c809f9469dad6a5ec6b2cb71e23f1451/pressure_node_added_deselected.png) | Added node (deselected)— drag to reposition the node which becomes selected |
| ![Image 12](https://images.ctfassets.net/3p2fxa94bzao/41R8VQkol465QCPhDx7xBh/e96780a83b58004fcc8a1caea7a63f20/pressure_node_added_selected.png) | Added node (selected)—drag to reposition the already selected node |

*   Under the chart, click **Save Profile**. The profile shows under the chart.

1.   Do one of the following:
    *   In Vector![Image 13](https://images.ctfassets.net/3p2fxa94bzao/2Mejuekyv1U5fQVTYLqGud/edc8c0247142081ce0079de3013e815d/persona_vector.svg)  or Layout Studio![Image 14](https://images.ctfassets.net/3p2fxa94bzao/4BbduuJ3zEK1FT2Ohg1aLs/98f305a0ad579187aa758ae37dc956e6/layout_studio.svg) , navigate to the **Stroke**panel.
    *   In Pixel Studio![Image 15](https://images.ctfassets.net/3p2fxa94bzao/x0qUKV0QmljBpXjlKaAyD/48b1503c7d6cc8f05d91c6af70f31b85/persona_photo.svg) , click **Edit stroke settings**![Image 16: Edit stroke settings](https://images.ctfassets.net/3p2fxa94bzao/LAIAniI5tfK3bknzYOUQB/9af81e28e315cea94436ab657c986f85/stroke.svg) on the context toolbar.

2.   Click the **Pressure**option.
3.   Select a custom profile from below the chart. The chart will update, showing the chosen profile.

*   Select **Reset** below the chart.

Click on any node to select it. Any added nodes can be deleted by pressing the **⌫** key (Mac) / **Delete** key (Windows).

*   On the **Stroke** panel's pressure profile chart (see above), select an end node on the profile's line and drag it vertically to a new position; nodes can be added by tapping on the line and then positioned freely to form a curve.
*   Repeat for other nodes as needed.

*   [Draw lines, curves and shapes](https://www.affinity.studio/help/curves-shapes-draw-lines-and-shapes/)
*   [Painting path brush strokes](https://www.affinity.studio/help/painting-path-painting/)
*   [Painting raster brush strokes](https://www.affinity.studio/help/painting-raster-painting/)
*   [Draw pencil lines](https://www.affinity.studio/help/curves-shapes-draw-pencil-lines/)
*   [Stroke panel](https://www.affinity.studio/help/panels-stroke-panel/)

How would you rate the help you received from this article?
