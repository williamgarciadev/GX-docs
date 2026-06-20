---
title: "Visible property in Query Element"
source_id: 47140
source_url: https://wiki.genexus.com/commwiki/wiki?47140
genexus_version: "18"
---

# Visible property in Query Element

Indicates whether the attribute will be visible or not at runtime in the QueryViewer control.

### [Values](#Values)

|  |  |
| --- | --- |
| **Never** | The element is not visible and cannot be changed, but is still accessible via code. |
| **No** | The element appears hidden from the start, but the user can unhide it with an action. |
| **Yes** | The element is visible from the start, but can be hidden from the UI. |

### [Scope](#Scope)

**Objects:** [Query](https://wiki.genexus.com/commwiki/wiki?9026)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

It allows you to indicate whether the attribute will be visible or not at runtime in the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).

The default value is Yes.

* *Yes*: the element is visible from the start, but can be hidden from the UI.
* *No*: the element appears hidden from the start, but the user can unhide it with an action.
* *Never*: the element is not visible and cannot be changed, but is still accessible via code; i.e., in the [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

`[imagen omitida: wiki id 47141]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build with this Only of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).

### [See Also](#See+Also)

[Type property in Query Element](https://wiki.genexus.com/commwiki/wiki?47137)  
[Axis and Visible property refactoring](https://wiki.genexus.com/commwiki/wiki?47094)


|  |
| --- |
| **Backlinks** |
| [Axis and Visible property refactoring](https://wiki.genexus.com/commwiki/wiki?47094) | [Axis property in Query Element](https://wiki.genexus.com/commwiki/wiki?47159) | [Type property in Query Element](https://wiki.genexus.com/commwiki/wiki?47137) |

---
