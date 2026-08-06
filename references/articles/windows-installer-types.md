---
title: "Understand and choose between Windows installer types - Affinity Help Center"
source: https://www.affinity.studio/help/windows-installer-types/
slug: windows-installer-types
fetched: 2026-08-06
---

# Understand and choose between Windows installer types - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/windows-installer-types/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Installation and setup](https://www.affinity.studio/help/installation-setup/)
3.   Understand and choose between Windows installer types

Windows users can download Affinity apps using four installer variants:

*   **Windows (Intel/AMD)**: this is the recommended installer for Windows devices with Intel/AMD processors
*   **Windows (ARM)**: this is the recommended installer for Windows devices with ARM64 processors
*   **Enterprise (Intel/AMD)**
*   **Enterprise (ARM)**

These variants use either MSIX or MSI/EXE files for installation.

**MSIX vs. MSI/EXE installers**

"**Windows (Intel/AMD)**" and "**Windows (ARM)**" are the recommended option and are MSIX installers. They support in-app automatic updates, meaning you won’t need to manually download and run future installers.

"**Enterprise (Intel/AMD)**" and "**Enterprise (ARM)**" are MSI/EXE installers and may be preferable if:

*   You encounter issues with the MSIX version
*   You’re installing on an Education or Enterprise network that restricts MSIX
*   You want to change the installation location. This is easier with MSI/EXE rather than [MSIX](https://www.affinity.studio/help/change-installation-path-windows/) as you get to choose a custom installation directory during setup.
*   You need other applications to access Affinity directly. MSIX applications run in a sandboxed environment, whereas the MSI/EXE version is not sandboxed.

*   Windows (Intel/AMD) and Enterprise (Intel/AMD) installers are for **Intel/AMD-based PCs** (the most common systems)
*   Windows (ARM) and Enterprise (ARM) installers are intended for **ARM-based Windows devices** (e.g. those with a Qualcomm Snapdragon X Elite processor)

1.   Press the **Windows key** on your keyboard and type **“Settings”**
2.   Open the **Settings** app.
3.   Go to **System**>**About**
4.   Under **Device Specifications**, find **System Type**
    *   **x64-based processor**: Your computer uses a 64-bit Intel or AMD processor
    *   **ARM-based processor**: Your computer uses an ARM processor (ARM64) 

While you cannot run Windows (ARM) and Enterprise (ARM) installers on X64 versions of Windows, Windows (Intel/AMD) and Enterprise (Intel/AMD) installers are compatible with ARM versions of Windows. However, installing the Windows (Intel/AMD) version of Affinity on an ARM computer will force it to run in emulation, which will negatively affect performance.

*   [Affinity system requirements](https://www.affinity.studio/help/introduction-system-requirements/)

How would you rate the help you received from this article?
