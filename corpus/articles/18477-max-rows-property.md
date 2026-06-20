---
title: "Max Rows property"
source_id: 18477
source_url: https://wiki.genexus.com/commwiki/wiki?18477
genexus_version: "18"
---

# Max Rows property

Limits the number of records shown in a query. It's very useful to obtain lists of rankings, scores, etc., with information in different orders.

### [Scope](#Scope)

**Objects:** Query

### [Description](#Description)

In this property, we can specify any numeric value.

There are two ways to set the property: either explicitly, with a numeric value, or otherwise, through a parameter.

### [Samples](#Samples)

With a numeric value, just include this in the property. The image below shows an example.

`[imagen omitida: wiki id 52505]`

With a parameter, define the parameter in the Parameters node of the Query object structure, and type this name in the property, as shown in the image below. Note that the parameter received, MaxRows, is explicitly set in the Max Rows property.

`[imagen omitida: wiki id 52506]`

Now, we need to pass the parameter from the Web Panel that contains the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) linked to the [Query object](https://wiki.genexus.com/commwiki/wiki?9026). To do this, we define the MaxRows variable with chatacter data type (you need not be concerned about its size), and write the following code in the Start event:

```
Event Start
    &MaxRows = "10"
    &Parameter = New()
    &Parameter.Name = "MaxRows"
    &Parameter.Value = &MaxRows
    &Parameters.Add(&Parameter)
Endevent
```

**Note:** You could also define another Web Panel to ask the number of rows to list.

### [See Also](#See+Also)

[Parameters QueryViewer property](https://wiki.genexus.com/commwiki/wiki?19808)


|  |
| --- |
| **Backlinks** |
| [Query Object Properties](https://wiki.genexus.com/commwiki/wiki?18471) |

---
