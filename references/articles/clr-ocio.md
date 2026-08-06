---
title: "Using OpenColorIO - Affinity Help Center"
source: https://www.affinity.studio/help/clr-ocio/
slug: clr-ocio
fetched: 2026-08-06
---

# Using OpenColorIO - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/clr-ocio/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Design fundamentals](https://www.affinity.studio/help/design-fundamentals/)
3.   Using OpenColorIO

OpenColorIO color management systems offers a full color-managed workflow for motion picture production, but can be used for any situation where accurate end-to-end color management is required.

OCIO profile versions for v1 and v2.0.0 are currently supported. Profiles designed for newer versions (i.e., v2.1 and later) may not be backwards compatible.

Verify version numbers of the OCIO and ACES configurations to ensure appropriate Affinity support.

By default, OpenColorIO features are not immediately usable. An **.ocio** configuration file is required alongside a number of supporting files such as lookup tables.

The OpenColorIO website (http://www.opencolorio.org) contains some sample configurations that provide a number of suitable input and output profiles, including several Academy Color (ACES) configurations.

1.   Download and extract your chosen OpenColorIO configuration to a chosen location.
2.   Go to **Settings**.
3.   On the **Color** tab, under **OpenColorIO Configuration File**, choose **Select** and navigate to the **.ocio** file's folder. Choose the **.ocio** configuration file within this folder.
4.   For Mac: Under **OpenColorIO Search Folder**, click **Select** and choose the destination folder (it should already be the current highlighted folder from when the **.ocio** configuration file was selected).
5.   You will be prompted to restart the app, which is necessary for the OpenColorIO settings to take effect.

OpenColorIO is exposed through two methods:

*   The **32-bit Preview** panel contains a **Display Transform** option that only becomes available with a valid OpenColorIO configuration. This can be used to achieve a non-destructive, color managed workflow. See [32-bit Preview](https://www.affinity.studio/help/panels-32bit-panel/) for more information.

An **OCIO** adjustment layer (see [OCIO Adjustment](https://www.affinity.studio/help/adjustments-adjustment-ocio/)) can be added to losslessly convert between color spaces. You can have multiple **OCIO** adjustment layers within a document, which allows you to accommodate composite layers from different color spaces. An example layer stack might be (in hierarchical order):

*   **OCIO Adjustment**—from **_Utility - Linear - sRGB_** back to **_Role - scene\_linear_**
*   **sRGB Pixel Layer**—composite element
*   **OCIO Adjustment**—from **_Role - scene\_linear_** to **_Utility - Linear - sRGB_**
*   **Pixel Layer**—original layer

When loading OpenEXR documents, Affinity always converts from the source color space to **scene_linear**. With a valid OpenColorIO configuration, Affinity will also present a message to let you know which color profile it has converted from. This is usually determined by a filename affix, for example **"render_acescg.exr"**.

*   [32-bit Preview](https://www.affinity.studio/help/panels-32bit-panel/) (desktop only)
*   [OCIO adjustment](https://www.affinity.studio/help/adjustments-adjustment-ocio/)

How would you rate the help you received from this article?
