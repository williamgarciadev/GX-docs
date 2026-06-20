---
title: "Refresh command in Panels"
source_id: 25060
source_url: https://wiki.genexus.com/commwiki/wiki?25060
genexus_version: "18"
---

# Refresh command in Panels

Forces a refresh on the entire form.

### [Syntax](#Syntax)

**Refresh** *[keep]*

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974)

### [Description](#Description)

The Refresh command forces a refresh of the entire Panel. This means that the following events will be executed:

* [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) (general)
* [Load event](https://wiki.genexus.com/commwiki/wiki?8188) (for each grid of the panel)

By default, the refresh command will go to the top of the Grid after refreshing. However, if you want to keep the scroll where it is, you can do so by adding 'keep' to the refresh command.

If the Refresh command is executed on a client event of a [Work With for SD Detail](https://wiki.genexus.com/commwiki/wiki?15985) section, the system events (Refresh-Load) for the Detail node be executed as well as the sections that were previously activated, with the exception of those [Inline](https://wiki.genexus.com/commwiki/wiki?15847), which will be activated any time.

Schematically, that is:

**Refresh** (Detail)  
**Load** (Detail, if there is any non-SDT-based grid)  
    **Refresh** (Section 1, if it was previously activated or is Inline)  
    **Load** (Section 1, if it was previously activated -or is Inline- and there is any non-SDT-based grid)  
    …  
    **Refresh** (Section n, if it was previously activated or is Inline)  
    **Load** (Section n, if it was previously activated -or is Inline- and there is any non-SDT-based grid)

Each section is activated in an indeterminate (and possibly concurrent) order.

### [Samples](#Samples)

```
Event 'TapButton'
    &var = 4;
    Refresh keep
EndEvent
```

### [Availability](#Availability)

Refresh keep command is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) for
[Android](https://wiki.genexus.com/commwiki/wiki?14453).

### [See Also](#See+Also)

* [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069)
* [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234)
* [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069) |

---
