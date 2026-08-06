---
title: "AI Automation with Claude - Affinity Help Center"
source: https://www.affinity.studio/help/ai-connector-setup/
slug: ai-connector-setup
fetched: 2026-08-06
---

# AI Automation with Claude - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/ai-connector-setup/

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Automation](https://www.affinity.studio/help/automation/)
3.   AI Automation with Claude

You can automate repetitive tasks in Affinity by giving natural language instructions to an AI assistant.

Affinity uses the Model Context Protocol (MCP)—an open standard that lets AI assistants communicate directly with apps—to receive instructions from your assistant and carry out tasks on documents.

Affinity’s MCP server runs locally on your device and connects to supported AI assistants.

Free during the beta period while we continue to develop and expand Affinity MCP capabilities.

![Image 1: The Claude chat window open alongside Affinity, showing Claude has renamed all 95 layers as asked. A colourful safari illustration is visible in Affinity, with named layers such as "Lion", "Elephant", and "Hyena" listed on the Layers panel.](https://images.ctfassets.net/3p2fxa94bzao/7qoEwRFwcRv3Hea58vyr6/1d0e003c8d28fd119f6319708d1298b5/B2_Affinity_PTK_Claude.png)

Using Claude to chat with Affinity via the Affinity MCP server

Describe a task in your own words and your AI assistant will use MCP to carry it out—no manual steps, scripting, or deep knowledge of Affinity’s interface required.

Typical uses include batch processing, file preparation, layer organization, localization, and making reusable custom tools.

If you give your AI assistant permission, it can save any completed workflow as a reusable script. This means you can repeat the process at any time, without needing to prompt again.

**Note:** Some tasks may not yet be possible during the beta.

Before you begin, confirm you have downloaded and installed the following:

*   Claude Desktop
*   Affinity April ’26 or later

Claude Desktop requires macOS Big Sur 11 or later. If you're on macOS Catalina 10.15, you won't be able to use Claude Desktop and the MCP server.

1.   In Claude’s settings, select **Connectors**, then **Browse connectors**.
2.   Search for the **Affinity**connector and install it.
3.   (Optional) Next to Affinity, click **Configure**, then choose approval settings for MCP capabilities. If you skip this step, the AI assistant may request permission when performing tasks.

1.   On the **Affinity** menu (Mac) / **Edit** menu (Windows), select **Settings**.
2.   On the dialog that appears:
    1.   Select **Model Context Protocol**.
    2.   Turn on **Enable MCP server**.

3.   Quit and reopen Affinity.

1.   Make sure both Affinity and Claude Desktop are running.
2.   In Claude, select **Chat**then give the following prompt: “Can you see the Affinity MCP server?”

Affinity and Claude Desktop must be running at the same time to communicate with each other.

*   **Access files on your Desktop**—Open, edit, and save files on your Desktop when required to complete tasks.
*   **Access networks**—Use internet and local network connections when required to complete tasks.
*   **Use saved scripts**—Existing scripts stored in your scripting panel can be read and used for new tasks.
*   **Save scripts to your scripting panel**—Save scripts from completed actions for use in Affinity.
*   **Use Canva AI Studio features**—Use Canva AI Studio features to complete tasks. Premium and Ultra Canva AI tools will use up your Canva plan’s monthly AI allowance.
*   **Save task hints to your device’s local memory**—Store task hints in local memory for similar tasks in the future.
*   **Share task hints with Affinity**—Share anonymized task hints to help improve the Affinity knowledge base.

With the MCP server enabled, here are a few powerful ways to get started.

**Example 1: Enhance all images in a document at once**

Quickly enhance all images in your document without manually editing each one. Ask your AI assistant to apply changes across all images for a consistent, eye-catching look. For example: “Add a purple to orange gradient map effect to all of the images in my document.”

**Example 2: Rename layers automatically**

Keep the Layers panel organized as your document grows—layer names can quickly become difficult to manage. Your AI assistant can recognize what each layer contains and rename them for you. For example: “Rename the layers in my Affinity document.”

**Example 3: Create a custom tool**

Build reusable tools tailored to your workflow. Describe the tool you want to create and include that it should have a UI. You can save what the AI assistant generates to the Scripts panel and reuse it later. For example: “Create a tool in Affinity that generates vector patterns and has a UI.”

*   **Work with existing documents**. Your AI assistant performs best when modifying, fixing, or automating tasks on an existing document. Asking it to design from scratch generally produces poor results.
*   **Retry failed tasks**. The AI assistant may not complete every task on the first attempt—this feature is still in active development. If it reports that something cannot be done, ask it to try again, as it often succeeds on a second attempt.
*   **Enable MCP local memory.**Turn on this setting in Affinity’s MCP settings to allow it to store task hints in local memory for similar tasks in the future.

Once you’ve used your AI assistant to complete a workflow, you can save it as a script so you don’t need to re-prompt each time.

If you gave the MCP permission to save completed workflows to the Scripts panel, they can be run again at any time by going to **Window > General > Scripts**. Click a script to run it on the current document immediately.

**Note:** Your AI assistant can save updated versions of a script under a new name, but will not overwrite existing scripts directly.

**Which AI assistants are supported?**

Claude is supported at this time.

**Why can't Claude connect to Affinity?**

Confirm Affinity April ’26 or later is open and running. Restart both Claude Desktop and Affinity.

**Why does Claude refuse my request or behave unexpectedly?**

Not all tasks will succeed on the first attempt. Rephrase your request or ask Claude to try again. We are continuing to develop and expand MCP support.

**Why does Claude think I'm using an older version of Affinity?**

Try prompting it directly, for example: “I’m using Affinity by Canva, April ’26 release.” This gives your assistant the context it needs to respond accurately.

**Can I use MCP on mobile?**

No. MCP requires the desktop versions of both Affinity and Claude.

**Does MCP use my monthly AI allowance?**

Using MCP with Affinity does not use your monthly AI allowance unless you have turned on Canva AI Studio in your MCP settings and are asking the assistant to use the premium or ultra model features. Claude usage is governed by your Claude plan.

**Can I use MCP in my region?**

It depends on whether Claude is supported in your region—see [Claude’s list of supported countries and regions](https://www.anthropic.com/supported-countries). However, MCP is not available in Affinity China.

**Why doesn't the Affinity connector appear in Claude after installing?**

Update Claude to the latest version. Then retry installing the connector from Claude's directory.

*   [Scripts panel](https://www.affinity.studio/help/panels-scripts-panel/)

How would you rate the help you received from this article?
