---
title: "Axis and Visible property refactoring"
source_id: 47094
source_url: https://wiki.genexus.com/commwiki/wiki?47094
genexus_version: "18"
---

# Axis and Visible property refactoring

The QueryElements [Axis](https://wiki.genexus.com/commwiki/wiki?19577) and [Visible](https://wiki.genexus.com/commwiki/wiki?43697,,) properties are refactored to ease the process of creating [Queries](https://wiki.genexus.com/commwiki/wiki?9026). The objective is to separate the structural representation of a query element from its visualization so they can evolve separately.

### [Changes](#Changes)

The [Axis](https://wiki.genexus.com/commwiki/wiki?19577) *Hidden* value is removed and moved to the [Visible](https://wiki.genexus.com/commwiki/wiki?43697,,) property; so, it changes from a [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) to an Enumerated three-valued value.

* *Yes*: the element is visible from the start, but can be hidden from the UI.
* *No*: the element appears hidden from the start, but the user can unhide it with an action.
* *Never*: the element is not visible and cannot be changed.

Besides, the [Axis](https://wiki.genexus.com/commwiki/wiki?19577) property is divided into two properties:

* *Type* (Datum|Axis): indicates the function of the attribute in the query
* *Axis* (Rows|Columns|Pages): only valid for *Type* = *Axis* and only if the query is displayed as a *PivotTable*.

### [Scope](#Scope)

**Objects:** [Dashboard](https://wiki.genexus.com/commwiki/wiki?36769), [Query](https://wiki.genexus.com/commwiki/wiki?9026)

### [Compatibility](#Compatibility)

The modifications impact the following components:

* Query structure; specifically, every [Query Element](https://wiki.genexus.com/commwiki/wiki?19788).
* The coding in a Web object using the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) (*&Axes* collection).
* [Dashboards](https://wiki.genexus.com/commwiki/wiki?36769) using a Query or DataProvider, every [Query Element](https://wiki.genexus.com/commwiki/wiki?19788).

#### [Query](#Query)

These properties are converted when opening a Query with version 17 Upgrade #1 or higher in the GeneXus IDE (there are no conversions in GeneXus Server). When saving the Query, they are saved with the new values and the version number of the Query is increased (internally, the version is updated from Version: 3 to 4) so that it cannot be opened with previous GeneXus versions (the version number is controlled in deserialization of the Query object). The version is also controlled in the Import, so it will not be possible to send a Query with a newer version to an IDE or to an older GeneXus Server through export / commit.

#### [Dashboard](#Dashboard)

The same properties are available within Query objects in a Dashboard. The Dashboard object is converted when opened in the IDE (as well as those that are configured directly in the Query). The new values will only be saved if the object is saved, at which point it can no longer be opened with previous versions of GeneXus.

#### [Code](#Code)

It is necessary to reprogram the WebPanels where the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) and properties are changed at runtime through programming. That is to say, if the *&Axes* collection is used; more specifically, the *Visible* or *Type* properties.

The necessary conversions are as follows:

* *QueryViewer.AllowChangeAxesOrder = <value>* must be changed to *QueryViewer.AllowElementsOrderChange = <value>*
* If you add an element *&Axis* to the *&Axes* collection and set the *Visible* or *Type* properties
* The property *QueryViewerAxes* changes to *QueryViewerElements*
* The property *Axes* changes to *Elements*
* The property *Axis* changes to *Element*

Use the following conversion table:

| Old Syntax | New Syntax |  |
| --- | --- | --- |
| ``` &Axis.Visible = true ``` | ``` &Axis.Visible = QueryViewerVisible.Yes ``` | (1) |
| ``` &Axis.Visible = true ``` | ``` &Axis.Visible = QueryViewerVisible.No ``` | (2) |
| ``` &Axis.Visible = false ``` | ``` &Axis.Visible = QueryViewerVisible.Never ``` |  |
| ``` &Axis.Type = QueryViewerAxisType.Row ``` | ``` &Axis.Type = QueryViewerElementType.Axis  &Axis.Axis = QueryViewerAxisType.Rows ``` | (3)(8) |
| ``` &Axis.Type = QueryViewerAxisType.Column ``` | ``` &Axis.Type = QueryViewerElementType.Axis  &Axis.Axis = QueryViewerAxisType.Columns ``` | (4)(8) |
| ``` &Axis.Type = QueryViewerAxisType.Page ``` | ``` &Axis.Type = QueryViewerElementType.Axis  &Axis.Axis = QueryViewerAxisType.Pages ``` | (5)(8) |
| ``` &Axis.Type = QueryViewerAxisType.Data ``` | ``` Axis.Type = QueryViewerElementType.Datum ``` | (6) |
| ``` &Axis.Type = QueryViewerAxisType.NotShow ``` | ``` &Axis.Visible = QueryViewerVisible.No ``` | (7) |

(1) - If &Axis.Type <> QueryViewerAxisType.NotShow  
(2) - If &Axis.Type = QueryViewerAxisType.NotShow  
(3) - Add an "s" to Row  
(4) - Add an "s" to Column  
(5) - Add an "s" to Page  
(6) - Axis property is ignored  
(7) - The values in the Type and Axis properties can be whatever you want  
(8) - The second line is only necessary if the output is Pivot Table.

##### [Conversion Example](#Conversion+Example)

The following code:

```
// Code valid up to GeneXus 17
&Axis.Name = !"CustomerName" // Some Attribute
&Axis.Visible = &Visible // Boolean
&Axis.Type = &Type // QueryViewerAxisType data type ('Row' 'Column' 'Page' 'Data' 'NotShow')
&Axes.Add(&Axis)
```

Has to be changed to:

```
// Code valid since GeneXus 17 Upgrade #1
&Axis.Name = !"CustomerName"
&Axis.Visible = &Visible // QueryViewerVisible data Type ('Yes' 'No' 'Never')
&Axis.Type = &Type // QueryViewerElementType ('Axis' 'Datum')
&Axis.Axis = &AxisItem // QueryViewerAxisType ('Rows' 'Columns' 'Pages')
&Axes.Add(&Axis)
```

Otherwise, the following error will appear:

```
// Change True|False to QueryViewerVisible.Yes|QueryViewerVisible.No|QueryViewerVisible.Never
spc0010 Type mismatch in assignment: &Axis.Visible = &Visible (QueryViewerVisible=Boolean).
// Change &Type from QueryViewerAxisType to QueryViewerElementType
spc0010 Type mismatch in assignment: &Axis.Type = &Type (QueryViewerElementType=QueryViewerAxisType).
// Change QueryViewerAxisType.Page to QueryViewerAxisType.Pages and review the conversion table to decide if a new assignment to &Axis.Type is needed
spc0010 Type mismatch in assignment: &Axis.Type = QueryViewerAxisType.Page (QueryViewerElementType=QueryViewerAxisType)
```

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).

**Warning**: When using GeneXus Server, updating to version 17 Upgrade #1 or higher is recommended; if Query Objects are used programmatically or saved with v17, it is mandatory.

### [See Also](#See+Also)

[Allow Change Axes Order property](https://wiki.genexus.com/commwiki/wiki?19603)  
[Axis property in Query Element](https://wiki.genexus.com/commwiki/wiki?47159)  
[Visible property](https://wiki.genexus.com/commwiki/wiki?47140)  
[Type property in Query Element](https://wiki.genexus.com/commwiki/wiki?47137)


|  |
| --- |
| **Backlinks** |
| [Query Object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?9105) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) |
| [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) | [Visible property in Dashboard widget element](https://wiki.genexus.com/commwiki/wiki?47161) | [Visible property in Query Element](https://wiki.genexus.com/commwiki/wiki?47140) |

---
