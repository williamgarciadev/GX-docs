---
title: "Visual Testing Repository URL property"
source_id: 49551
source_url: https://wiki.genexus.com/commwiki/wiki?49551
genexus_version: "18"
---

# Visual Testing Repository URL property

Specifies the URL of the Visual Testing Repository for Native Mobile UI Tests

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Front end

### [Description](#Description)

It is possible to perform automated screenshot comparisons in UI Tests by using the [verifyScreenshot method](https://wiki.genexus.com/commwiki/wiki?44873).

The verifyScreenshot method takes a screenshot of the running application and compares it to a reference image stored in a "visual testing repository server."

This property indicates the location of that server and is required to use the visual testing feature.

Refer to [Visual testing in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?49568,,) for more information.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).
