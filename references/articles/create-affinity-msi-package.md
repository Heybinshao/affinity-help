---
title: "Creating an Affinity MSI installation package - Affinity Help Center"
source: https://www.affinity.studio/help/create-affinity-msi-package/
slug: create-affinity-msi-package
fetched: 2026-08-06
---

# Creating an Affinity MSI installation package - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/create-affinity-msi-package/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Installation and setup](https://www.affinity.studio/help/installation-setup/)
3.   Creating an Affinity MSI installation package

An MSI (Microsoft Software Installer) package allows the installation of the Affinity app on Windows computers.

1.   Open an elevated Command Prompt and navigate to the location of the downloaded .exe file. You will need to append _/extract_ to the end of the file location, and press **Return**, e.g._C:\affinity.exe /extract_
2.   (Optional) On the **Create MSI** dialog, modify the install location using the **Install path** field if needed. By default, the install path is **C:\Program Files\Affinity\**.For a desktop shortcut to be created during the installation, check the **Create desktop** shortcut option.
3.   Click **Create**, and then **Save** in the **Save As** dialog.

The saved MSI file, in your Documents folder, is named _Affinity.msi_ by default.

On the Create MSI dialog there are several runtime options you can use:

*   **Disable Check for Updates**—decides if the user receives onscreen notifications for any new updates.
*   **Disable crash reports**—decides if crash reports are sent from the app to our developers.
*   **Disable Account Linking**—decides if the user can link their Affinity ID and Affinity Store Add-ons to their Canva account.
*   **Disable ML model config**—determines whether users are permitted to download and install machine learning models within Affinity. If enabled, you can specify the shared location of your stored Machine Learning models using the **Models path** field.

This MSI package can now be used for deployment via Group Policy, InTune etc. Once deployed, Affinity can be launched on the workstation and users will have to manually enter their Canva or Single Sign-on (SSO) login details to sign into Affinity.

**Machine learning**

When a user downloads Machine Learning models within Affinity they are stored in the following location:

_%APPDATA%\Affinity\Common\3.0\modelcaches_

Alternatively, Administrators may opt to download the Machine Learning models and store them on their local network. This allows all instances of Affinity within the domain to access these models from the shared location, rather than individual users downloading them. This method conserves bandwidth and bypasses potential firewall restrictions.

**Installing MSI Packages**

You can now deploy the MSI file using one of the following parameters:

For an unattended install with only a progress bar:

_msiexec /i <path to the affinity.msi file> /passive_

For an unattended install with no user interface:

_msiexec /i <path to the affinity.msifile> /qn_

**Can Affinity be pre-licensed for all workstations and users, eliminating the need for manual sign-in upon launch?**

Affinity cannot be pre-licensed before deployment. Each user must manually enter their Canva or Single Sign-on (SSO) details to access the app.

This method, utilising individual Canva accounts, ensures compliance with privacy regulations and delivers a secure, personalized experience for every user.

How would you rate the help you received from this article?
