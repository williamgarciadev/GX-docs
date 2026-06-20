---
title: "HowTo: Using ClearCache Method From Interop in Smart Devices Api"
source_id: 22580
source_url: https://wiki.genexus.com/commwiki/wiki?22580
genexus_version: "18"
---

# HowTo: Using ClearCache Method From Interop in Smart Devices Api

The Interop [external object](https://wiki.genexus.com/commwiki/wiki?17880) which can be found under the folder Smar Device API provides several methods to interact with the device where the app is executing.

The ClearCache method enables you to clear the cache on the device; the next interaction with the application server will retrieve all the information again.

To use it, you just need to add the following in any action associated to a Smart Devices object:

```
Event 'ClearAll'
    Interop.ClearCache()
EndEvent
```

Done! When the button ClearAll on the [SDPanel](https://wiki.genexus.com/commwiki/wiki?20880,,) is tapped all cached information on the device will be cleared, the next interaction with the server side will retrieve all information again, including the variables default values.


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
