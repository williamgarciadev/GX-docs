---
title: "Test Target property"
source_id: 42595
source_url: https://wiki.genexus.com/commwiki/wiki?42595
genexus_version: "18"
---

# Test Target property

Defines the main object to use as a test target.

### [Scope](#Scope)

**Objects:** [UI Test](https://wiki.genexus.com/commwiki/wiki?38334)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Every [UI Test object](https://wiki.genexus.com/commwiki/wiki?46009) requires a [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) that indicates the application it is meant to test.

That Main object must be indicated in this property (**Test Target**), and it is required.

If not specified, the following error is shown:

error: Test '<test\_name>' has no main target set  
error: No main targets found to test

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?43446,,).

### [See Also](#See+Also)

[Unit Testing](https://wiki.genexus.com/commwiki/wiki?38334)


|  |
| --- |
| **Backlinks** |
| [Android UITest Log](https://wiki.genexus.com/commwiki/wiki?55471) | [UI Test for Native Mobile Automation](https://wiki.genexus.com/commwiki/wiki?44571) |

---
