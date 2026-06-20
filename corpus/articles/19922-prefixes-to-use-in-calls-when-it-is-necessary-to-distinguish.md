---
title: "Prefixes to use in calls when it is necessary to distinguish concepts"
source_id: 19922
source_url: https://wiki.genexus.com/commwiki/wiki?19922
genexus_version: "18"
---

# Prefixes to use in calls when it is necessary to distinguish concepts

When defining calls, you may need to indicate explicitly whether you are referring to an attribute, domain, object, etc.

### [Supported prefixes in GeneXus](#Supported+prefixes+in+GeneXus)

|  |  |
| --- | --- |
| **att:** | Identifies an attribute. |
| **dom:** | Identifies a domain. |
| **obj:** | Identifies a callable object. |
| **image:** | Identifies an image object. |
| **type:** | Identifies a type for the case of using a static method. |

### [Description](#Description)

Prefixes are used to avoid conflicts, and you should use them only when necessary.

In general, prefixes aren't needed.

That is, you could have an attribute and a picture with the same name and never encounter a conflict. The grammar has rules to automatically identify the type of expression. For example, if you have an image object and an enumerated domain with the same name "xxx", and you write xxx.MethodName(), GeneXus verifies that the method applies only to domains and resolves the issue without requiring the explicit "dom:" prefix.

Conflicts are most common when the "Allow non-standard functions" property is set to True. In this case, many of the automatic grammar resolutions don't apply, because it isn't known whether xxx.yyy() refers to a standard expression or a non-standard expression. In these cases, you can use the prefixes to avoid conflicts.

### [Samples](#Samples)

Look at the following [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661) and the following event defined in an object section. There is a CustomerName attribute and a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) named CustomerName, too.

```
Customer
{
  CustomerId*
  CustomerName
  CustomerPhone
}
```

```
Event 'Gets Customer Name'
    &CustomerName=obj:CustomerName(CustomerId)
Endevent  
```

**Note**: This example illustrates the obj: prefix. However, you could also give the Procedure a clearer name (for example, ReturnsCustomerName).


|  |
| --- |
| **Backlinks** |
| [Call command](https://wiki.genexus.com/commwiki/wiki?8260) |

---
