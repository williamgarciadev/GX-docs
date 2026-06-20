---
title: "Running tests on different browsers"
source_id: 41128
source_url: https://wiki.genexus.com/commwiki/wiki?41128
genexus_version: "18"
---

# Running tests on different browsers

Browser type needs to be defined before the &driver.Start() sentence, using the **Browsers** domain included in your KB when GXtest is installed.

Possible values to use are Chrome, Firefox, Edge Legacy, Edge (Chromium) and IE.

By default, each KB has a **Default Browser** property that will be used for all test executions. So, if you have no specific browser type defined by code, you can just change this value:

`[imagen omitida: wiki id 41129]`

This is the recommended way to do it.

On the other hand, if you want your test to use a specific browser type, you can change this value by code using the [SetBrowser](https://wiki.genexus.com/commwiki/wiki?41690) command, and Browsers domain to choose the value. Just remember to do it before "Start" sentence:

`[imagen omitida: wiki id 41130]`


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
|

---
