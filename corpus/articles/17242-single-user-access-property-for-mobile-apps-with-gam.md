---
title: "Single User Access property (for mobile apps with GAM)"
source_id: 17242
source_url: https://wiki.genexus.com/commwiki/wiki?17242
genexus_version: "18"
---

# Single User Access property (for mobile apps with GAM)

Single User Access is a Smart Devices [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) property that allows defining if a single user can access the application from different devices, without losing the session in all the devices he is logged in when he logs out from one of them.

`[imagen omitida: wiki id 17243]`

If set to False, the user can log in to two different devices, and if he logs out from one of them, he keeps logged in to the other.

This property is set through the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), in the Application properties dialog.

### [Example](#Example)

GAMExampleEntryApplication web panel (located in GAM Example folder) is an example where this property is used.

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is the following:

```
&Application.ClientAccessUniqueByUser = &AccessUniqueByUser // Boolean data type
```


|  |
| --- |
| **Backlinks** |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [Hardening of GeneXus Systems and Deployments with GAM](https://wiki.genexus.com/commwiki/wiki?47237) |

---
