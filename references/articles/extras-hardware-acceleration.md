---
title: "Hardware acceleration (Mac and Windows) - Affinity Help Center"
source: https://www.affinity.studio/help/extras-hardware-acceleration/
slug: extras-hardware-acceleration
fetched: 2026-08-06
---

# Hardware acceleration (Mac and Windows) - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/extras-hardware-acceleration/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Hardware acceleration (Mac and Windows)

To improve the performance of some operations, Affinity can use Metal technology (Mac) or OpenCL technology (Windows) to talk directly to your system's graphics hardware.

This feature is only available in Affinity for desktop.

Hardware acceleration is available for many graphics processors (GPUs), whether integrated into your computer's CPU (central processing unit), a discrete graphics card or onboard processor, or external and connected via Thunderbolt 3 or later. Affinity can make use of multiple GPUs in parallel.

It is recommended that hardware acceleration is enabled unless you experience unusual performance problems or our technical support team instructs you to disable it.

Hardware acceleration is enabled by default. If you experience poorer performance than expected, try disabling it to see if CPU-based processing works better on your system.

In practice, the performance boost depends on the task at hand.

Hardware acceleration is of great benefit to many raster-based tasks. Vector operations and specific features like blend options are performed on the CPU.

Tools, adjustments, canvas previewing and other operations will use GPU resources to achieve improved performance.

The benefits are especially noticeable when stacking several [Live filter layers](https://www.affinity.studio/help/layers-livefilters/) together—export times are significantly quicker and canvas previewing is snappier.

As a trade-off, memory requirements are increased and performance may be dependent on the amount of VRAM available to the GPU(s).

The VRAM requirement depends on the complexity of your workflow. Document resolution and bit depth, screen resolution, and layer complexity all contribute to it.

Using a 4K display as a baseline, 1–2GB of VRAM is sufficient for most light editing. For large amounts of compositing work, consider a GPU with 4GB—especially when working to 16-bit precision.

To perform 32-bit 3D rendering work with many layers, 4GB is the minimum amount, though we recommend 8GB.

Affinity support for OpenCL compute acceleration requires Windows 10.0.19042 (May 2020) or later.

It also requires GPU support for Direct3D 12 Feature Level 12.0 (https://en.wikipedia.org/wiki/Feature_levels_in_Direct3D#Direct3D_12), meaning the GPU must feature AMD's GCN (Graphics Core Next), NVIDIA's Maxwell, or Intel HD Graphics 510 (Skylake) or a later microarchitecture.

To assess the benefit of hardware acceleration to your system, use [the app's built-in benchmark](https://www.affinity.studio/help/extras-benchmark/) to measure and compare single- and multi-core CPU, single GPU and, where applicable, multi-GPU performance.

In Affinity's settings:

1.   Select **Performance**.
2.   Do one of the following: 
    *   For Mac: Set **Enable Metal compute acceleration** as required.
    *   For Windows: Set **Enable OpenCL compute acceleration** as required.

The setting is inaccessible if Affinity is unable to detect a compatible GPU on your system.

When enabled, compatible GPUs currently in use are listed under the setting.

*   [Performance settings](https://www.affinity.studio/help/workspace-settings/)
*   [Benchmark](https://www.affinity.studio/help/extras-benchmark/)

How would you rate the help you received from this article?
