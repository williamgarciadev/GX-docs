---
title: "Parameters QueryViewer property"
source_id: 19808
source_url: https://wiki.genexus.com/commwiki/wiki?19808
genexus_version: "18"
---

# Parameters QueryViewer property

Parameters property is a QueryViewer property which allows sending values to the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) at runtime.

### [Values](#Values)

|  |  |
| --- | --- |
| **&Parameters** | Name of the variable which will contain the collection of parameters. This is the default value. |

The &Parameters variable mentioned before is based on QueryViewerParameters Structured Data Type:

`[imagen omitida: wiki id 21062]`

Where

* **Name:** is the name of the parameter.
* **Value:** is the value of the parameter.

**Note:** Collections type parameters can also be defined as a Query Object parameter. The following code example shows how to do it:

```
&Parameter = New()
&Parameter.Name = "ParamCollection"
&Parameter.Value = &CollectionVariable.ToJson()
&Parameters.Add(&Parameter)
```

### [Usage example](#Usage+example)

Imagine having the following [Query object](https://wiki.genexus.com/commwiki/wiki?9026):

`[imagen omitida: wiki id 21063]`

Where the parameter &MakeId was defined to be used as a filter (MakeId = &MakeId).

The defined Query Object will be shown in a corresponding [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) embedded intro a Web Panel. Where also the &MakeId variable is added and defined as Dynamic ComboBox type to load the car brands.

The Click event of this variable is programmed so that when the user selects a brand from the ComboBox, the Query Object associated with the control for filtering by that brand is executed again. The code would be as follows:

```
Event &MakeId.Click
    &Parameters = New()
    &Parameter.Name = "MakeId"
    &Parameter.Value = &MakeId.ToString().Trim() // ‘ToString’ because Value is character and MakeId is numeric.
    &Parameters.Add(&Parameter)
EndEvent
```

### [Compatibility](#Compatibility)

**Warning**: It is recommended to use the new property [Object property in QueryViewer control](https://wiki.genexus.com/commwiki/wiki?19664) insted to change query elements parameters.

### [See also](#See+also)

[Click event](https://wiki.genexus.com/commwiki/wiki?8177)  
[Refresh command](https://wiki.genexus.com/commwiki/wiki?8621,,)


|  |
| --- |
| **Backlinks** |
| [Max Rows property](https://wiki.genexus.com/commwiki/wiki?18477) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |

---
