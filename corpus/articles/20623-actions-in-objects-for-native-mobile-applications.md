---
title: "Actions in objects for Native Mobile applications"
source_id: 20623
source_url: https://wiki.genexus.com/commwiki/wiki?20623
genexus_version: "18"
---

# Actions in objects for Native Mobile applications

Actions in objects for Native Mobile applications provide interaction between the application and the end user in several ways:

* With a server-side process (web service).

For instance, in the case of an action that calls a procedure, that procedure is executed on the server side and invoked via a REST web service.

* With a local process.

For instance, when the app is generated offline, the procedure will be executed locally on the device.

* With a call to a native device app.

For instance, to use the camera or add a new Contact to the contact list (for example, using an external object method).

### [Actions, Events, and Controls](#Actions%2C+Events%2C+and+Controls)

|  |  |
| --- | --- |
| **Action** | The concept of the action the end user wants to perform (Authorize, Add to favorites, etc.). |
| **Event** | Every **Action** has an associated **Event**. So, when the end user takes an **Action**, the associated **Event** is triggered and the code defined inside that event is executed.  See [Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042). |
| **Control** | A visual aspect associated with an Action. When the end user selects it, the Action is performed and the associated Event is executed. |

### [Objects for Native Mobile Applications where Actions can be defined](#Objects+for+Native+Mobile+Applications+where+Actions+can+be+defined)

Actions can be defined for:

* [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s
* [Work With objects](https://wiki.genexus.com/commwiki/wiki?15974)
* [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)s

### [iOS Destructive Actions](#iOS+Destructive+Actions)

On iOS you can have a [destructive action](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/destructiveaction) that will be shown in red, as follows:

`[imagen omitida: wiki id 28776]`

To have an action like this in GeneXus, you only need to name the event 'Delete'.


|  |
| --- |
| **Backlinks** |
| [Application Bar control in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19486) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) |
| [HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194) | [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) | [Remote Notifications External Object](https://wiki.genexus.com/commwiki/wiki?39316) |
| [Category:Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |

---
