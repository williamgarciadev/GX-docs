---
title: "Significant attribute name length property"
source_id: 7248
source_url: https://wiki.genexus.com/commwiki/wiki?7248
genexus_version: "18"
---

# Significant attribute name length property

Defines the significant name length for attributes, domains, and structured data types.

### [Scope](#Scope)

**Objects:** [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Domain](https://wiki.genexus.com/commwiki/wiki?7221)

### [Description](#Description)

The property value does not limit the length of names. There may be objects whose names have more or less characters than those specified in this property. It just states how many characters of the name (at most) are considered for uniqueness checking.

If this property is set to 10, for example, you may define attributes like "CustNo" (less than 10) and "CustomerNumber" (more than 10) but you will not be able to define an attribute named CustomerStreetName and another named CustomerStreetNo as both share the same first 10 characters (CustomerSt).

#### [Values](#Values)

Any number from 4 to 128.  
  
Default Value: 30

#### [Notes](#Notes)

* If, for example, the value is replaced with a lower value but it is ignored and the previous value is reset, it means that the names of two attributes or objects are colliding.
* Domains are also validated against SDT.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |

### [See Also](#See+Also)

[Significant Table Name Length Property](https://wiki.genexus.com/commwiki/wiki?7249,,)  
[Significant object name length property](https://wiki.genexus.com/commwiki/wiki?7250)  
[Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719)


|  |
| --- |
| **Backlinks** |
| [BPD Name Property](https://wiki.genexus.com/commwiki/wiki?11444) | [Database Reorganization cases where a temporary table is created](https://wiki.genexus.com/commwiki/wiki?19529) | [Maximum numeric length property](https://wiki.genexus.com/commwiki/wiki?6801) |
| [Name property](https://wiki.genexus.com/commwiki/wiki?6985) | [Significant object name length property](https://wiki.genexus.com/commwiki/wiki?7250) | [Technical specifications of GeneXus](https://wiki.genexus.com/commwiki/wiki?55715) |

---
