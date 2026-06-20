---
title: "Apple Version Code property"
source_id: 39496
source_url: https://wiki.genexus.com/commwiki/wiki?39496
genexus_version: "18"
---

# Apple Version Code property

A value that represents the build version of the application code, which identifies an iteration (released or unreleased). The build version number should be a string comprised of three non-negative, period-separated integers with the first integer being greater than zero. If the value of the third number is 0, you can omit it and the second period.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

A complete definition and best practices for specifying version codes can be found under <https://developer.apple.com/library/archive/technotes/tn2420/_index.html>

The notation {Major}.{Minor}.{Build} is valid since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,). Previous versions only support the {Major}.{Minor} notation.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

* 1.0
* 1.0.1
* 13.5.2

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

* [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223)
