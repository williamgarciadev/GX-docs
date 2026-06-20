---
title: "Confirmation property"
source_id: 7422
source_url: https://wiki.genexus.com/commwiki/wiki?7422
genexus_version: "18"
---

# Confirmation property

In Transactions, it indicates whether or not in runtime a user's confirmation must be requested when passing from one level to another.
In Procedures, it indicates whether or not in runtime a user's confirmation must be requested when the process starts executing.

### [Values](#Values)

|  |  |
| --- | --- |
| **Always prompt** | The user's confirmation will be requested to confirm the action. |
| **Do not prompt on first level** | In Transactions it will prompt the user for confirmation at each level of the Transaction, except for the first one (only .Net and Ruby generators). |
| **Never prompt** | No confirmation is asked. This is the default value. |
| **Use Environment property value** | The value set for the Confirmation property at the Environment level will be used. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Platforms:** iSeries(COBOL, RPG), Web(.Net, Java), iSeries(COBOL, RPG), Web(.Net, Java)

### [Description](#Description)

In a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), this property allows to indicate whether or not in runtime the user's confirmation must be requested when passing from one level to another.

If the value is different than “Never prompt”, when passing from one Level to the next, a message is displayed and the user is prompted to confirm data.

In a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), this property allows to indicates whether or not in runtime the user's confirmation must be requested when the process starts executing.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Given the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Country
{
   CountryId*
   CountryName
   City
   {
     CityId*
     CityName
   }
}
```

To disable the confirmation at both levels, you can use the **Confirmation property** with the Never prompt value. If you want to request confirmation only at the second level, you should use the **Confirmation property** with the Do not prompt on first level value.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.


|  |
| --- |
| **Backlinks** |
| [Confirm Transactions property](https://wiki.genexus.com/commwiki/wiki?7999) | [Pseudo Conversational Dialog Property](https://wiki.genexus.com/commwiki/wiki?13998) |

---
