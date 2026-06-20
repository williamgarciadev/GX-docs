---
title: "Live Editing in Web Applications"
source_id: 27771
source_url: https://wiki.genexus.com/commwiki/wiki?27771
genexus_version: "18"
---

# Live Editing in Web Applications

GeneXus allows you to change the design style settings of your applications within the GeneXus IDE, and view changes at runtime without pressing F5. All the style changes are reflected directly in the application running on the device or the web browser.

### [Agile prototyping!](#Agile+prototyping%21)

Live Editing allows you to change the [Design System](https://wiki.genexus.com/commwiki/wiki?47375) or [Theme](https://wiki.genexus.com/commwiki/wiki?4375) settings and immediately see those changes without building the application.

If you are satisfied with the changes, you can save them. Otherwise, change the settings until they are good enough without doing any build operation.

Remember that the best preview for design time is running the application on the device itself because you are seeing exactly what the end user will see: the data is available, and all the specific features of the device screen are present.

## [How to activate Live Editing](#How+to+activate+Live+Editing)

To enable it, set [Live Editing mode](https://wiki.genexus.com/commwiki/wiki?27805) from the GeneXus Toolbar and press F5 to run your application.

### [Example in a web application](#Example+in+a+web+application)

In this example, you are going to change the background and fore colors of the Delete button of a web transaction. The corresponding Theme class is BtnDelete.

So, you just open the Theme and change the background color for this class:

`[imagen omitida: wiki id 32608]`

After that, without saving or building, the changes are reflected in the browser:

`[imagen omitida: wiki id 32609]`

#### [Implementation details for the web:](#Implementation+details+for+the+web%3A)

* For web applications, when F5 or Run with this only is executed, a new entry is registered in the gxcfg.js; for example: gx.livePreviewUri="http://172.16.2.220:30100/gxlivepreviewservice/?2c413e52-b6a2-4ed9-83de-cdea7df23658:TestLiveEdi";
* The browser makes a request using WebSockets to the web server that runs in this port and responds with a JSON format message containing the new CSS settings for the browser to be interpreted. The request looks as follows, and can be seen in the network tab of the browser console in "WebSocket frames".

### [Availability](#Availability)

This functionality is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).


|  |
| --- |
| **Backlinks** |
| [Debugging in GeneXus](https://wiki.genexus.com/commwiki/wiki?9307) |
| [Toc:Live Editing](https://wiki.genexus.com/commwiki/wiki?27805) |

---
