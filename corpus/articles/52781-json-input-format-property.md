---
title: "Json Input Format property"
source_id: 52781
source_url: https://wiki.genexus.com/commwiki/wiki?52781
genexus_version: "18"
---

# Json Input Format property

Specifies the Json Input Format for a Structured Data Type.

### [Values](#Values)

|  |  |
| --- | --- |
| **Unwrapped** | Does not include a label with the name of the SDT as part of the Json input. |
| **Wrapped** | Includes a label with the name of the SDT as part of the Json input. |

### [Scope](#Scope)

**Objects:** [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is only taken into account for a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) when it is the only out parameter of an [API object](https://wiki.genexus.com/commwiki/wiki?46151).

The Json Input Format property applies to the SDT Object. The accepted input format will change depending on the selected value.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

With the Wrapped (default) value, the accepted input is as follows:

```
{ "ClientSDT":
         { "id": 1,
            "Name" : "Juan",
           "LastName" : "Valdez",
            "Country" : "Colombia"
         }
}
```

With the Unwrapped value, the accepted input is as follows:

```
 { "id": 1,
    "Name" : "Juan",
    "LastName" : "Valdez",
    "Country" : "Colombia"
}
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).

### [See Also](#See+Also)

[Structured Data Type properties](https://wiki.genexus.com/commwiki/wiki?8081)
