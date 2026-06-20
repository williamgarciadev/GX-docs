---
title: "ItemDoubleClick Event"
source_id: 19567
source_url: https://wiki.genexus.com/commwiki/wiki?19567
genexus_version: "18"
---

# ItemDoubleClick Event

This event is triggered upon double-clicking on a query element.

### [Syntax](#Syntax)

**&ItemDoubleClickData.**{ *Axis* | *Context* | *Filters* | *Name* | *Value* }

When the event is triggered, its parameters are queried in the "ItemDoubleClickData" property. It returns an SDT with the following data:

* **Axis** in which it was located.
* **Context** is a collection of elements that provide information on all the elements included in the query with the values related to the clicked-on value.
  + For a plain table, it's a list of all the elements included in the query with the values for the row corresponding to the clicked-on cell (including hidden elements).
  + For a pivot table, clicking on a cell selects several tuples of the query result (all those that contributed to the value of this cell). The related values are, for each element in the query, the different values included in said tuples.
* **Filters** is a collection of elements included in the pages with the list of values selected (only valid for Pivot tables).
* **Name** of the element that was clicked on.
* **Value**. The value contained in the clicked on cell.

### [Example](#Example)

In this example, code is added to the event so that double-clicking on the Client Nr element opens a popup window showing the element name, its value and context.

```
Event QueryClients.ItemDoubleClick
    &ContextDblClick = &ItemDoubleClickData.Context //ContextDblClick is a Context type variable
    &StrContext      = &ContextDblClick.ToJson() //StrContext is a VarChar/LongVarChar/Character type variable
    &window.Object   = PopupDialog.Create(&ItemDoubleClickData.Name,
                                          &ItemDoubleClickData.Value,
                                          &StrContext)
    &window.Width  = 400
    &window.Height = 300
    &window.Open()
EndEvent
```

`[imagen omitida: wiki id 19642]`

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Ouput type:** | Table, PivotTable |

### [See Also](#See+Also)

* [Item Click Data property](https://wiki.genexus.com/commwiki/wiki?19564)
* [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570)


|  |
| --- |
| **Backlinks** |
| [Allow Selection property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?42903) | [Item Double Click Data property](https://wiki.genexus.com/commwiki/wiki?19566) | [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570) |
| [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) |

---
