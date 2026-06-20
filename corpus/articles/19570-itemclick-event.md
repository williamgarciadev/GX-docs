---
title: "ItemClick Event"
source_id: 19570
source_url: https://wiki.genexus.com/commwiki/wiki?19570
genexus_version: "18"
---

# ItemClick Event

Executes actions when this event is triggered after clicking on a query element.

### [Syntax](#Syntax)

**&ItemClickData.**{ *Axis* | *Context* | *Filters* | *Name* | *Value* }

When the event is triggered, its parameters are queried in the "ItemClickData" property. It returns an SDT with the following data:

* **Axis** in which it is located.
* **Context** is a collection of elements that provide information on all the elements included in the query with the values related to the clicked-on value.
  + For a plain table, it's a list of all the elements included in the query with the values for the row corresponding to the clicked-on cell (including hidden elements).
  + For a pivot table, clicking on a cell selects several tuples of the query result (all those that contributed to the value of this cell). The related values are, for each element in the query, the different values included in said tuples.
* **Filters** is a collection of elements included in the pages with the list of values selected (only valid for Pivot tables).
* **Name** of the element that was clicked on.
* **Value.** The value contained in the clicked-on cell.

### [Example](#Example)

In this example, code is added to the event so that clicking on the Client Nr element opens a pop-up window showing the element name, value, and context.

```
Event QueryClients.ItemClick
    &StrContext = &ItemClickData.Context.ToJson() //&StrContext is a VarChar/LongVarChar/Character type variable
    &window.Object = PopupDialog.Create(&ItemClickData.Name,
                                        &ItemClickData.Value,
                                        &StrContext)
    &window.Width  = 400
    &window.Height = 300
    &window.Open()
EndEvent
```

`[imagen omitida: wiki id 19642]`

### [Chart](#Chart)

You can execute the ItemClick event in:

* Data (columns in a Column Chart, points in a Line Chart, etc.)
* Labels

### [Maps](#Maps)

Since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,) you can execute the ItemClick Event in:

* Region: When the Choropleth type map is used.
* Bubble: When the Bubble type map is used with both data types (GeoPoint and ISO code 3166).

In both cases, the [Raise ItemClick](https://wiki.genexus.com/commwiki/wiki?42812) event property should be set to True. You can enable it only for an element whose attribute has the [Type property](https://wiki.genexus.com/commwiki/wiki?47137) set to Datum.

### [Scope](#Scope)

**Output type:** Table, PivotTable, Chart, [Map](https://wiki.genexus.com/commwiki/wiki?48199).

### See Also

[ItemDoubleClick Event](https://wiki.genexus.com/commwiki/wiki?19567)  
[Raise ItemClick event property](https://wiki.genexus.com/commwiki/wiki?42812)  
[Allow Selection property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?42903)


|  |
| --- |
| **Backlinks** |
| [Item Click Data property](https://wiki.genexus.com/commwiki/wiki?19564) |
| [ItemDoubleClick Event](https://wiki.genexus.com/commwiki/wiki?19567) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | [Raise ItemClick event property](https://wiki.genexus.com/commwiki/wiki?42812) |
| [Visible property in Query Element](https://wiki.genexus.com/commwiki/wiki?47140) |

---
