---
title: "QueryViewer control properties"
source_id: 32920
source_url: https://wiki.genexus.com/commwiki/wiki?32920
genexus_version: "18"
---

# QueryViewer control properties

### [Control properties](#Control+properties)

[QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) properties are:

|  |  |
| --- | --- |
| [Auto Refresh Group property](https://wiki.genexus.com/commwiki/wiki?19793) | Allows the association of different QueryViewer controls that provide related information (or the same information, with a different output) to be automatically updated when one of them is changed. |
| [ControlName property](https://wiki.genexus.com/commwiki/wiki?8754) | ControlName, used to reference the control in the GeneXus object code. |

| Event Parameters Group |  |
| --- | --- |
| [Drag And Drop Data property](https://wiki.genexus.com/commwiki/wiki?19545) | Contains the name of the variable where DragAndDrop event parameters will be charged. |
| [Item Expand Data property](https://wiki.genexus.com/commwiki/wiki?19559) | Contains the name of the variable where ItemExpand event parameters will be charged. |
| [Item Collapse Data property](https://wiki.genexus.com/commwiki/wiki?19548) | Contains the name of the variable where ItemCollapse event parameters will be charged. |
| [Filter Changed Data property](https://wiki.genexus.com/commwiki/wiki?19571) | Contains the name of the variable where FilterChanged event parameters will be charged. |
| [Item Click Data property](https://wiki.genexus.com/commwiki/wiki?19564) | Contains the name of the variable where ItemClick event parameters will be charged. |
| [Item Double Click Data property](https://wiki.genexus.com/commwiki/wiki?19566) | Contains the name of the variable where ItemDoubleClick event parameters will be charged. |

|  |  |
| --- | --- |
| Data Bindings |  |
| [Object property](https://wiki.genexus.com/commwiki/wiki?19664) | Contains the name of the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) displayed in the QueryViewer Control. |
| [Elements Property](https://wiki.genexus.com/commwiki/wiki?19577) | Allows configuring Query elements properties on runtime |
| [Parameters](https://wiki.genexus.com/commwiki/wiki?19808) | Allows sending values to the Query Object or Data Provider Object at runtime. |

|  |  |
| --- | --- |
| Appearance |  |
| [Class property](https://wiki.genexus.com/commwiki/wiki?8741) | Personalize the control look & feel changing the QueryViewer class node within the associated Theme. (1) |
| [Shrink To Fit property](https://wiki.genexus.com/commwiki/wiki?21068) | Allows specifying if the used Column Width (Table and Pivot Table) is the minimum to display the contents of all cells.(2) |
| [Auto Resize property](https://wiki.genexus.com/commwiki/wiki?19597) | Allows reducing the size of the container in case the Query is displayed as Table or Pivot Table. However, if the Query is displayed as Chart, the Chart itself fulfill the Query container. |
| [Width property](https://wiki.genexus.com/commwiki/wiki?38374) | Determines the width of the control. |
| [Height property](https://wiki.genexus.com/commwiki/wiki?8792) | Determines the height of the control. |
| [Axes Selectors property](https://wiki.genexus.com/commwiki/wiki?19600,,) | Allows showing or hiding the lists of values (dialogs) that query elements have. |
| [Disable Expand Collapse property](https://wiki.genexus.com/commwiki/wiki?19602,,) | Inabilities the possibility of Expand/Collapse values of a determined Query element. |
| [Allow Change Axes Order property](https://wiki.genexus.com/commwiki/wiki?19603) | Allows changing the Query elements order. When the property value it's True, the order of the values of the Query elements is the same of the &Axes collection elements order. |
| [DisableColumnSort Property](https://wiki.genexus.com/commwiki/wiki?19606,,) | Allows disabling the possibility of sorting the values of the Query elements. |

| Export |  |
| --- | --- |
| [Export Properties group](https://wiki.genexus.com/commwiki/wiki?19609) | It allows exporting the Pivot Table or Table to XML, HTML, XLSX, XLS and PDF formats. |

| Output |  |
| --- | --- |
| [Type Property](https://wiki.genexus.com/commwiki/wiki?19612) | Allows developers to select the output type to be used. |
| [Chart Type property](https://wiki.genexus.com/commwiki/wiki?19613) | Allows developers to select the type of chart to be used. |
| [Title property](https://wiki.genexus.com/commwiki/wiki?7234) | Specifies the control title (valid for charts only) |
| [Plot series](https://wiki.genexus.com/commwiki/wiki?31056) | Allows determinating if the different Series of a Query are shown in the same chart or separate ones. |
| [XAxis Title property](https://wiki.genexus.com/commwiki/wiki?19680) | Allows writing the caption that will appear on the X axis. |
| [YAxis Title property](https://wiki.genexus.com/commwiki/wiki?42240) | Allows writing the caption that will appear on the Y axis. |
| [XAxis Labels property](https://wiki.genexus.com/commwiki/wiki?19617) | Set the position of the chart axis labels. |
| [X Axis intersection at Zero Property](https://wiki.genexus.com/commwiki/wiki?31025,,) | Allows determinating if the intersection between X axe and Y axe it's made static (at the Zero value), or it's calculated dynamically (depending on the nature of Data values). |
| [Show Values property](https://wiki.genexus.com/commwiki/wiki?19684,,) | Set if the chart values are shown in control. |
| [Paging property in QueryViewer Control](https://wiki.genexus.com/commwiki/wiki?19677) | Set if paging is required, if Type is set to Table or Pivot Table, By default set to true. |
| [Page size property](https://wiki.genexus.com/commwiki/wiki?19679) | Page size, applies when paging = true |
| [Show Data Labels In property](https://wiki.genexus.com/commwiki/wiki?24706,,) | Allows indicating how to display the labels of the elements' values in a Pivot Table: on the Data, Row or Column area. |
| [Total For Rows property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?49723) | Determines whether to show a total of all values in the pivot table rows. |
| [Total For Columns property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?49724) | Determines whether to show a total of all values in the pivot table columns. |

|  |  |
| --- | --- |
| State management |  |
| [Remember Layout property](https://wiki.genexus.com/commwiki/wiki?19619) | Allows keeping the latest Table/Pivot Table status (for the same user in the same browser). |

All these properties can be set at design time and runtime. To simplify the use of the properties at runtime, some Domains are automatically added to the Knowledge Base when a QueryViewer control is used for the first time.

### [Control properties (in run-time only)](#Control+properties+%28in+run-time+only%29)

|  |  |
| --- | --- |
| [IsExternalQuery](https://wiki.genexus.com/commwiki/wiki?23240,,) | Allows indicating that the query is defined in GXquery and not in the Knowledge Base itself. It is related to the ExternalQueryResult property. |
| [ExternalQueryResult](https://wiki.genexus.com/commwiki/wiki?23240,,) | Allows loading the result of the Execute method of the [GXquery API](https://wiki.genexus.com/commwiki/wiki?23003,,) before showing the query. It is related to the IsExternalQuery property. |

(1) - Available since [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,)

(1) - Deprecated since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,)


|  |
| --- |
| **Backlinks** |
| [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) | [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) |

---
