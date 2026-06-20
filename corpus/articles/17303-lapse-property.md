---
title: "Lapse property"
source_id: 17303
source_url: https://wiki.genexus.com/commwiki/wiki?17303
genexus_version: "18"
---

# Lapse property

The seconds that must pass before the event 'Refresh' is triggered again.

### [Description](#Description)

For the Smart Devices, refreshes the Grid if the user does not perform any action during a certain period of time. For the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) (and [Work Panel object](https://wiki.genexus.com/commwiki/wiki?7387,,)), the refresh occurs at the entire object level.

For Web objets, the Lapse behavior depends on the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449). If [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Compatible, it is similar to the Browser Refresh (F5). It loads the whole page again every time.

If [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Smooth, only the web panel is refreshed, and the Master Page is not included.

This lapse must be specified in seconds.

#### [Values](#Values)

A value in seconds must be specified. By default (0) the object does not refresh.

### [Scope](#Scope)

**Objects:** Panel for Smart Devices, Web Panel, Work With for Smart Devices  
**Platforms:** Web(.Net, Java), Smart Devices(Android, IOS)

### [See Also](#See+Also)

[Triggers property](https://wiki.genexus.com/commwiki/wiki?7420)  
[Sleep function](https://wiki.genexus.com/commwiki/wiki?8075)


|  |
| --- |
| **Backlinks** |
| [Sleep function](https://wiki.genexus.com/commwiki/wiki?8075) | [Triggers property](https://wiki.genexus.com/commwiki/wiki?7420) |

---
