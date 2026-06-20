---
title: "Infer Structure property"
source_id: 23628
source_url: https://wiki.genexus.com/commwiki/wiki?23628
genexus_version: "18"
---

# Infer Structure property

Indicates if GeneXus must infer the structure of the SDT (Structured Data Type) and create it by analyzing the structure declared in the Data Provider source.

### [Values](#Values)

|  |  |
| --- | --- |
| **Yes, if SDT is dynamic** | If the SDT set in the Output property –Dynamic Structure property– is set to True, the structure of the SDT is inferred from the Data Provider structure. |
| **No** | No SDT is inferred. This is the default value. |

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)

### [Description](#Description)

If you declare a structure manually in the source of a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) and set the Data Provider **Infer Structure property** to "Yes, if SDT is dynamic", you are indicating that GeneXus must automatically create a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) with the structure inferred from the Data Provider source.

Also, GeneXus will complete the Data Provider [Output property](https://wiki.genexus.com/commwiki/wiki?41037) with the name of the new SDT.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you define the following in the source of a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270):

```
  Customer
  {
      CustomerId = ...
      CustomerName = ...
      CustomerBirthDate = ...
  }
```

When you set the *Infer Structure* property to "Yes, if SDT is dynamic", the following [SDT](https://wiki.genexus.com/commwiki/wiki?2427) will be automatically created:

`[imagen omitida: wiki id 23630]`

Note that the Data Provider [Output property](https://wiki.genexus.com/commwiki/wiki?41037) is automatically set with the name of the created SDT. In addition, every time that the Data Provider is saved, the SDT structure will be inferred.

### [See Also](#See+Also)

[HowTo: Use the Infer Structure property of a Data Provider](https://wiki.genexus.com/commwiki/wiki?23651)  
[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)


|  |
| --- |
| **Backlinks** |
| [Dynamic structure property](https://wiki.genexus.com/commwiki/wiki?23632) | [HowTo: Use the Infer Structure property of a Data Provider](https://wiki.genexus.com/commwiki/wiki?23651) |

---
