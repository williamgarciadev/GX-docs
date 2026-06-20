---
title: "Required Xcode version property"
source_id: 50712
source_url: https://wiki.genexus.com/commwiki/wiki?50712
genexus_version: "18"
---

# Required Xcode version property

Xcode version to use when compiling applications and modules.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Generator

### [Description](#Description)

It allows defining which version of Xcode is necessary for compiling the application.

At the Apple Generator level, this has an impact at the time of module distribution, so it is recommended to target the oldest possible Xcode version to have the widest possible compatibility for the generated modules.

At the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) level, when the property is empty, GeneXus checks that the version selected in the Command Line Tools option (in the Xcode options of the Mac specified in the [Mac Host](https://wiki.genexus.com/commwiki/wiki?36371)) is compatible; if so, it is used. A version is compatible when GeneXus recognizes it as compatible. To this end, it must have the required SDK version.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).
