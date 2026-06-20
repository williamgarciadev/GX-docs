---
title: "Enable Preferred Color Scheme property"
source_id: 44353
source_url: https://wiki.genexus.com/commwiki/wiki?44353
genexus_version: "18"
---

# Enable Preferred Color Scheme property

Enables light and dark colors schemes on supported platforms.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

When this property is set to False (default value) means that the application only supports one color scheme, defined by the value set for the [Base Color Scheme property](https://wiki.genexus.com/commwiki/wiki?18402).

On the other hand, when this property is set to True, the application supports Light and Dark color schemes. The application theme or the one referenced in the [Dark Theme property](https://wiki.genexus.com/commwiki/wiki?44354) is used considering the OS setting. On OS versions or platforms where it's not supported, it will fall back to the behavior specified by the [Base Color Scheme property](https://wiki.genexus.com/commwiki/wiki?18402).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build All.

### [Scope](#Scope)

**Objects:** [Menu for Smart Devices](https://wiki.genexus.com/commwiki/wiki?16321), [Panel for Smart Devices](https://wiki.genexus.com/commwiki/wiki?24829)  
**Platforms:** Smart Devices(IOS)


|  |
| --- |
| **Backlinks** |
| [Dark Theme property](https://wiki.genexus.com/commwiki/wiki?44354) |

---
