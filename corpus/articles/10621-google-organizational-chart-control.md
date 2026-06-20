---
title: "Google Organizational Chart control"
source_id: 10621
source_url: https://wiki.genexus.com/commwiki/wiki?10621
genexus_version: "18"
---

# Google Organizational Chart control

This control shows an organizational chart that support selection.

### [Example](#Example)

The user control is really simple, you just need to set one property in order to get the control working: the VisualizationData property.

### [Show a simple chart to illustrate a hierarchical model of an organization](#Show+a+simple+chart+to+illustrate+a+hierarchical+model+of+an+organization)

* Drag and drop OrganizationalChart.
* Assign to VisualizationData property a variable based on OrganizationalChart data type (this SDT is automatically imported when dropping the control to the web form).
* Load the information that will be shown by the chart using the previous mentioned variable.

```
Sub 'LoadOrganizationalChart'
  &item.Text = "John"
  &item.Tooltip = "Tooltip for John"
  &list.Add(&item)

  &item = new()
  &item.Text = "Steve"
  &list.Item(1).Children.Add(&item)

  &item = new()
  &item.Text = "Paul"
  &list.Item(1).Children.Item(1).Children.Add(&item)

  &item = new()
  &item.Text = "Aaron"
  &list.Item(1).Children.Item(1).Children.Add(&item)
  organizationalChart1.Reload = true
EndSub
```

**Note:** *&item* is based on OrganizationalChartSDT.OrganizationalChartItem and *&list* is based on OrganizationalChartSDT (this SDT is also automatically imported when dropping the control to a web form).  
  
`[imagen omitida: wiki id 10619]`

### [Handling events](#Handling+events)

As we mentioned before, Organizational Chart Control is an interactive chart. That is, when clicking on an item, a GeneXus event wil be fired.

```
Event organizationalChart1.Selected
    msg(organizationalChart1.SelectedItem)
EndEvent
```

### [Implementation details](#Implementation+details)

Organizational Chart Control is based on [Google Organizational Chart](https://developers.google.com/chart/interactive/docs/gallery/orgchart).


|  |
| --- |
| **Backlinks** |
| [GXGoogle Visualization Library](https://wiki.genexus.com/commwiki/wiki?10447) |

---
