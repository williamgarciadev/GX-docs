---
title: "Additional References property"
source_id: 47973
source_url: https://wiki.genexus.com/commwiki/wiki?47973
genexus_version: "18"
---

# Additional References property

Lists the objects to add to the reference tree of the main object being built.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))

### [Description](#Description)

In a typical scenario, objects referenced from the application's Main object are included automatically in the application.

However, if you are calling some objects dynamically(\*), those references are not resolved automatically and need to be explicitly added.

This property allows just that: to include, in the generated application, the objects that are not referenced explicitly.

(\*) Dynamic calls are those performed via a string literal or a variable. For example:

```
call('SomeObjectName')
```

or

```
call(&objectName)
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).
