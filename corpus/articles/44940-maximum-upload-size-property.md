---
title: "Maximum Upload Size property"
source_id: 44940
source_url: https://wiki.genexus.com/commwiki/wiki?44940
genexus_version: "18"
---

# Maximum Upload Size property

Size of the image transferred to the server

### [Values](#Values)

|  |  |
| --- | --- |
| **Actual Size** | Images are transferred in their original sizes. |
| **Large** | Image size is controlled by the value of property Large Image Upload Size. This is the default value. |
| **Medium** | Image size is controlled by the value of property Medium Image Upload Size. |
| **Small** | Image size is controlled by the value of property Small Image Upload Size. |

### [Description](#Description)

This property allows you to control the size of images transferred to the server.

If the upload is done by means of a Business Component, bear in mind the value of the attribute definition.

If the upload is done by means of a Procedure:

* As from [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,), it will take the lesser value between what was defined in the configuration of the Procedure parameters and what was defined in the variables of the SDPanel where it is used.
* In previous versions, it will only take the value of the Procedure parameters.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, Build a main object.

### [Scope](#Scope)

**Objects:** Image  
**Platforms:** Smart Devices(Android, IOS)

### [See Also](#See+Also)

[Image data type](https://wiki.genexus.com/commwiki/wiki?15204)  
[Image manipulation API](https://wiki.genexus.com/commwiki/wiki?39415)  
[Large Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24114)  
[Medium Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24115)  
[Small Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24116)


|  |
| --- |
| **Backlinks** |
| [Large Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24114) | [Medium Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24115) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Small Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24116) |

---
