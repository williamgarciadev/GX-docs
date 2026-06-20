---
title: "Display property for PWA Web Panels"
source_id: 42608
source_url: https://wiki.genexus.com/commwiki/wiki?42608
genexus_version: "18"
---

# Display property for PWA Web Panels

Defines the developers' preferred display mode for the website.

### [Values](#Values)

|  |  |
| --- | --- |
| **Browser** | Standard browser experience. |
| **Fullscreen** | Opens the web application without any browser UI and takes up the entirety of the available display area. |
| **Minimal** | This mode is similar to full screen, but provides the user with some means to access a minimal set of UI elements for controlling navigation (i.e. back, forward, reload, etc.). Note: Only supported by Chrome on mobile. |
| **Standalone** | Opens the web app to look and feel like a standalone native app. The app runs in its own window, separate from the browser, and hides standard browser UI elements like the URL bar, etc. |

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

This property is available when the [Web Application property](https://wiki.genexus.com/commwiki/wiki?42602) = Progressive.

It updates the [manifest](https://developers.google.com/web/fundamentals/web-app-manifest/).json file of the PWA application.

The aim of this property is to customize the browser UI that is shown when your app is launched. For example, you can hide the address bar and Chrome browser.

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
