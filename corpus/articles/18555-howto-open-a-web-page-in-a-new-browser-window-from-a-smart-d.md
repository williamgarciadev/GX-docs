---
title: "HowTo: Open a Web Page in a New Browser Window from a Smart Devices Application"
source_id: 18555
source_url: https://wiki.genexus.com/commwiki/wiki?18555
genexus_version: "18"
---

# HowTo: Open a Web Page in a New Browser Window from a Smart Devices Application

There are two ways in which a web page can be opened from your Smat Devices Applications. The first, and recommended one, is the [Link Command](https://wiki.genexus.com/commwiki/wiki?8446) and the second is the "OpenInBrowser" method available from Interop's API.

Here we focus on a simple example on how to use the OpenInBrowser method, which follows the same aims as the [Link Command](https://wiki.genexus.com/commwiki/wiki?8446) as told before.

This tutorial is a simple and quick guide for developers that want to use this method in their smart devices applications.

In this tutorial we are going to open in a browser an URL inserted by the user.

1. First step is to create a new Work With for Smart Devices object, delete its List node and create a Detail node, it should be as follows:

`[imagen omitida: wiki id 18556]`

2. Define a variable of URL type and add it to the layout:

`[imagen omitida: wiki id 18557]`

`[imagen omitida: wiki id 18558]`

3. Define a new action 'OpenInBrowser' to the Action panel:

`[imagen omitida: wiki id 18559]`

```
Event 'OpenInBrowser'
	Interop.OpenInBrowser(&url)
EndEvent
```

All done! now hit f5 and see the results.

#### Examples

Android:

`[imagen omitida: wiki id 18563]`

`[imagen omitida: wiki id 18564]`

iOS:

`[imagen omitida: wiki id 18565]`

`[imagen omitida: wiki id 18566]`


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |
| [WebBrowser external object](https://wiki.genexus.com/commwiki/wiki?36384) |

---
