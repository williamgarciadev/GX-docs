---
title: "Suggest property"
source_id: 8800
source_url: https://wiki.genexus.com/commwiki/wiki?8800
genexus_version: "18"
---

# Suggest property

Defines whether to suggest possible values when entering data and how.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | No suggestion list is shown. |
| **OnRequest** | The user manually makes a request to calculate suggestions. |
| **Incremental** | The list is updated as the end user enters data. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: Edit)

### [Description](#Description)

The Suggest property applies to Edit controls.

It can be set for attributes in [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, as well as for variables in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s, respectively.

It can only be used over attributes or variables based on the Character or VarChar data types. Otherwise, the following specification error will be shown:

```
spc0112 ("Item value %1 for control %2 must be Character data type or VarChar data type")
```

Enabling the Suggest property will cause a list of possible values for that control to be displayed when entering data.

The suggestions list can be calculated:

* In an incremental way: The list is updated as the user enters data.
* By making requests: The end user manually makes a request to calculate suggestions.

List updates are asynchronous and calculation times depend on the quality of the connection.

The **Suggest property** can be set specifically for a certain Attribute/Variable control (with its Control Type property set to "Edit") or at the attribute level. If it is applied to an attribute, the Suggest property will be enabled by default everywhere the attribute is used. This property is independent of the [InputType property](https://wiki.genexus.com/commwiki/wiki?8799). However, it is advisable to read the InputType property documentation first because using both properties will make it easier to create user-friendly interfaces. Read more about how these features can work together.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) |
| [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |
| [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) |

---
