---
title: "Validation Failed Message property"
source_id: 10483
source_url: https://wiki.genexus.com/commwiki/wiki?10483
genexus_version: "18"
---

# Validation Failed Message property

Specifies the error message that will be displayed to the end user of the generated application if the value range or regular expression validation fails.

### [Scope](#Scope)

**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Domain](https://wiki.genexus.com/commwiki/wiki?7221), [SDT member](https://wiki.genexus.com/commwiki/wiki?10021), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property depends either on the [Value Range](https://wiki.genexus.com/commwiki/wiki?6797) property or the [Regular Expression](https://wiki.genexus.com/commwiki/wiki?10484) property, and its default value is calculated as follows:

* If the **Value Range** has the value “Field %1 is out of range.” (the GXSPC\_OutOfRange translation key).
* If the **Regular Expression** has the value “Field %1 does not match the specified pattern.” (the GXM\_DoesNotMatchRegExp translation key).

Note that the attribute's **Description**property substitutes %*1*.

This property is not available when the attribute is a formula.

Note: The property is updatable, but the default value corresponds to the domain on which the variable / attribute / SDT member is based on.

### [Compatibility](#Compatibility)

Since GeneXus 17 Upgrade 4, this property also applies to SDT members.

### [See Also](#See+Also)

[Value range property](https://wiki.genexus.com/commwiki/wiki?6797)  
[Regular Expression property](https://wiki.genexus.com/commwiki/wiki?10484)  
[Name property](https://wiki.genexus.com/commwiki/wiki?6985)


|  |
| --- |
| **Backlinks** |
| [Conversational Flows Designer](https://wiki.genexus.com/commwiki/wiki?45145) | [Regular Expression property](https://wiki.genexus.com/commwiki/wiki?10484) | [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) |

---
