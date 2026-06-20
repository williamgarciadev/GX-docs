---
title: "Dark Theme property"
source_id: 44354
source_url: https://wiki.genexus.com/commwiki/wiki?44354
genexus_version: "18"
---

# Dark Theme property

Theme variant to be used when dark is the user preferred color scheme on supported platforms.

### [Scope](#Scope)

**Objects:** [Theme for Smart Devices](https://wiki.genexus.com/commwiki/wiki?17876,,)  
**Platforms:** Smart Devices(IOS), Smart Devices(Android)

### [Description](#Description)

This property is available when you create a new [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) with a new [Color Palette](https://wiki.genexus.com/commwiki/wiki?31262) that defines which are the colors for the Dark Theme.

**Considerations:**

* The Dark Theme should be the son of the main Theme.
* Additionally, the [Enable Preferred Color Scheme property](https://wiki.genexus.com/commwiki/wiki?44353) must be set to True.
* It is required that the device has the dark mode set so that a Dark Theme can be shown.

Note: This property is available for Android as of [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,) and Android 10 is needed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

`[imagen omitida: wiki id 44448]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build All.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [Enable Preferred Color Scheme property](https://wiki.genexus.com/commwiki/wiki?44353) |

---
