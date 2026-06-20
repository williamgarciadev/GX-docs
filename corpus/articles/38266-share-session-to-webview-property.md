---
title: "Share session to Webview property"
source_id: 38266
source_url: https://wiki.genexus.com/commwiki/wiki?38266
genexus_version: "18"
---

# Share session to Webview property

Sets whether to copy the session from a native app to a WebView component.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Allows sharing the session between the mobile application (Android and iOS) and the Web part, allowing for communication between them, by default, this property has 'false' value. It also makes it possible to share the session of a GAM user; this implementation is a valid alternative to the one already existing in this example: [HowTo: Access a web panel component using the Smart Devices](https://wiki.genexus.com/commwiki/wiki?33624)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

In your Main Panel for Smart Devices, place the variable on the screen and call your test Panel for Smart Devices by sending it via a parameter ("ShareWebSession" in the example).

```
Event 'RunTest'
    ShareWebSession(&SetSomeValue)
Endevent 
```

`[imagen omitida: wiki id 40328]`

In your test Panel for Smart Devices, place a variable based on the SD Component domain (variable &webview in the example). Also, add the value sent via a parameter to the web session:

```
Event Start
    &WebSession.Set('Test', &SetSomeValue)
    &WebView = WebPanel.Link()
Endevent
```

`[imagen omitida: wiki id 40329]`

Retrieve the value on your Web Panel and show it on the screen.

```
Event Start
    &WebVarchar = &WebSession.Get('Test')    
Endevent
```

`[imagen omitida: wiki id 40330]`

|  |  |
| --- | --- |
|  |  |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).
