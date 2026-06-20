---
title: "Allow Selection property in QueryViewer"
source_id: 42903
source_url: https://wiki.genexus.com/commwiki/wiki?42903
genexus_version: "18"
---

# Allow Selection property in QueryViewer

Keeps an item (and related items) selected when the user clicks on it.

### [Syntax](#Syntax)

**control.** AllowSelection

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** QueryViewer

### [Description](#Description)

This property allows keeping an item selected once the ItemClick event has been raised. It can be useful when visual feedback is required after a mouse click.

It's valid for all the output types in the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075), except for Card and Gauge Charts.

The first click on an item selects it, and all the items related to the clicked item will be selected too. An additional click on it deselects it.

There is a default color for the selection but you can change it through the [Selection Color](https://wiki.genexus.com/commwiki/wiki?42904) property in the associated Theme.

You can inspect the &ItemClickData variable when processing the ItemClick event to check if the value you've just clicked on has remained selected or not.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

**Chart**

`[imagen omitida: wiki id 42933]`

**Table**

`[imagen omitida: wiki id 42935]`

**Pivot Table**

`[imagen omitida: wiki id 42936]`

**Maps**

You can use this since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,).

It's valid for all the output map types in the Query Viewer.

For example, the image below represents the total vaccination per million people in each country.

`[imagen omitida: wiki id 49737]`

In this case, a Choropleth type map is used and Brazil is selected.

Now, look at this other map below. It represents the total population by state in the United States of America.

`[imagen omitida: wiki id 49738]`

In this case, a Bubble type map is used and the state of California is selected.

Finally, look at this other map below. It represents the total population by city in the United States of America.

`[imagen omitida: wiki id 49739]`

In this case, a Bubble type map with GeoPoint dataType is used and a city is selected.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [See Also](#See+Also)

[QueryViewer SelectionColor property](https://wiki.genexus.com/commwiki/wiki?42904)  
[ItemDoubleClick Event](https://wiki.genexus.com/commwiki/wiki?19567)  
[Raise ItemClick event property](https://wiki.genexus.com/commwiki/wiki?42812)


|  |
| --- |
| **Backlinks** |
| [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570) | [QueryViewer SelectionColor property](https://wiki.genexus.com/commwiki/wiki?42904) |

---
