---
title: "Web Application Short Name property"
source_id: 42604
source_url: https://wiki.genexus.com/commwiki/wiki?42604
genexus_version: "18"
---

# Web Application Short Name property

Provides a short human-readable name for the application. This is intended for when there is insufficient space to display the full name of the web application, like device homescreens.

### [Description](#Description)

The property is available when [Web Application property](https://wiki.genexus.com/commwiki/wiki?42602) = Progressive.

It updates the [manifest](https://developers.google.com/web/fundamentals/web-app-manifest/) json file of the PWA application.

You must provide at least the short name or [name](https://wiki.genexus.com/commwiki/wiki?42603) property. If both are provided, short name is used on the user's home screen, launcher, or other places where space may be limited. Name is used in the [app install prompt](https://developers.google.com/web/fundamentals/app-install-banners/).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [Scope](#Scope)

**Objects:** Web Panel  
**Platforms:** Web(.Net, .Net Core, Java)

### [See Also](#See+Also)

* [Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600)


|  |
| --- |
| **Backlinks** |
| [How to create a PWA using GeneXus](https://wiki.genexus.com/commwiki/wiki?42601) | [Toc:Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600) | [Web Application Name property](https://wiki.genexus.com/commwiki/wiki?42603) |

---
