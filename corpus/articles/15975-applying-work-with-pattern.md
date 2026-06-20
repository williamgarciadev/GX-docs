---
title: "Applying Work With Pattern"
source_id: 15975
source_url: https://wiki.genexus.com/commwiki/wiki?15975
genexus_version: "18"
---

# Applying Work With Pattern

Supposing a Property [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) with the following attributes:

```
Property
{
    PropertyId*
    PropertyAddress
    PropertyDefaultPhoto
}
```

Apply the Work With Pattern to the Transaction as follows:

* Open the Transaction
* Select the Patterns section
* Select the Work With tab
* Check “Apply this pattern on save”
* Save the Transaction

`[imagen omitida: wiki id 51730]`

Upon applying the Work With pattern, the following properties in the Transaction are set:

• [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True  
• [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) = True  
• Web Service Protocol property = REST Protocol

The UI pattern is applied for defining data lists, actions, etc.

Also, the Native Mobile generator is added as a secondary generator to the environment, having selected by default the following properties:

* [Main Platform property](https://wiki.genexus.com/commwiki/wiki?18657) = Android
* [Generate Android property](https://wiki.genexus.com/commwiki/wiki?18654) = True
* [Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656) = True

After pressing F5 and Building, a part that goes in the server (webapi) is generated, in addition to a part that is run on the client (taking data from the webapi for execution).

**Note**: When you Save As a Transaction, the action only creates a new Transaction object, but not the applied pattern instance. The Save As action creates a default pattern instance for the new Transaction (the layouts in list, detail and all property used in the original Transaction is not saved). If you want to keep all the information in the instance, you must do a Save As for the Work With instance.

### [See also](#See+also)

[Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984)  
[Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985)


|  |
| --- |
| **Backlinks** |
| [Calling objects from Menu Events](https://wiki.genexus.com/commwiki/wiki?17392) | [Composite examples](https://wiki.genexus.com/commwiki/wiki?15551) | [Designing the tables related to WWSD Layouts](https://wiki.genexus.com/commwiki/wiki?19487) |
| [Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433) | [How to use Unanimo](https://wiki.genexus.com/commwiki/wiki?52176) | [HowTo: Create a Three Step Wizard with Panels for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18718) | [HowTo: Embedding YouTube videos in an Android application](https://wiki.genexus.com/commwiki/wiki?21923) |
| [HowTo: Use AddContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15792) | [HowTo: Use Charts Control](https://wiki.genexus.com/commwiki/wiki?16106) | [HowTo: Use Check Box for Smart Devices](https://wiki.genexus.com/commwiki/wiki?18482) |
| [HowTo: Use Combo Box in Panels](https://wiki.genexus.com/commwiki/wiki?18408) | [HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180) | [HowTo: Use PlayVideo method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15986) | [HowTo: Use Radio Button in Panels](https://wiki.genexus.com/commwiki/wiki?18434) |
| [HowTo: Use RemoveContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15895) | [HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21661) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) | [HowTo: Use SendMessage method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15528) |
| [HowTo: Use Tab Control in Panels](https://wiki.genexus.com/commwiki/wiki?16800) | [HowTo: Use the Cancel Method from Actions in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18363) | [HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16778) | [HowTo: Use ViewContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15856) |
| [My first Android application](https://wiki.genexus.com/commwiki/wiki?14555) |
| [My first BPM Native Mobile application](https://wiki.genexus.com/commwiki/wiki?50516) | [My first iOS application](https://wiki.genexus.com/commwiki/wiki?14738) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) |
| [Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805) | [Pattern settings](https://wiki.genexus.com/commwiki/wiki?6546) | [Category:Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) | [Work With Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004) |
| [Work With Section Node](https://wiki.genexus.com/commwiki/wiki?20624) |

---
