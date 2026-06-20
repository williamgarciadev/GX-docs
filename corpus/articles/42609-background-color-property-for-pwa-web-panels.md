---
title: "Background Color property for PWA Web Panels"
source_id: 42609
source_url: https://wiki.genexus.com/commwiki/wiki?42609
genexus_version: "18"
---

# Background Color property for PWA Web Panels

Defines the expected background color for the website. This value repeats what is already available in the theme, but can be used by browsers to draw the background color of a shortcut when the manifest is available before the stylesheet has loaded. This creates a smooth transition between launching the web application and loading the site's content.

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is available when the [Web Application property](https://wiki.genexus.com/commwiki/wiki?42602) = Progressive.

It updates the [manifest](https://developers.google.com/web/fundamentals/web-app-manifest/).json file of the PWA application.

The background color property is used on the [splash screen](https://developers.google.com/web/fundamentals/web-app-manifest/#splash-screen) when the application is first launched.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,).

### [See Also](#See+Also)

* [Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600)


|  |
| --- |
| **Backlinks** |
| [How to create a PWA using GeneXus](https://wiki.genexus.com/commwiki/wiki?42601) | [Toc:Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600) |

---
