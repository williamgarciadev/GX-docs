---
title: "Android Version Code property"
source_id: 58703
source_url: https://wiki.genexus.com/commwiki/wiki?58703
genexus_version: "18"
---

# Android Version Code property

A value that represents the version of the application code, relative to other versions.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Every time you make significant updates to your application, it is recommended to publish a new version and update this property.

When possible, follow the semantic versioning spec ({Major}.{Minor}.{Build}) described [here](https://semver.org/).

* *Major*: when you make an incompatible change.
* *Minor*: when you add functionality in a backwards-compatible manner.
* *Build*: when you make backwards-compatible bug fixes.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223)


|  |
| --- |
| **Backlinks** |
| [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) | [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
