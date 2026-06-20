---
title: "Query Object - Troubleshooting"
source_id: 9105
source_url: https://wiki.genexus.com/commwiki/wiki?9105
genexus_version: "18"
---

# Query Object - Troubleshooting

## [Query Object](#Query+Object)

When executing a commit the following possible messages are detailed:

```
# Case 1
error: GeneXus Server: Part descriptor not found: 'Query Version 3' (provided by package 'Artech.GXplorer.BL').
...
error: GeneXus Server: Could not commit changes
# Case 2
error: GeneXus Server: Error reading from export file.
error: GeneXus Server: Unknown query version (4)
error: GeneXus Server: An error occurred in Query 'QueryObjectName' : Error reading from export file.
```

The GeneXus Server instance and IDE are not compatible, you need to update both to version 17 Upgrade #1 or higher, [more information](https://wiki.genexus.com/commwiki/wiki?47094).


When executing an Update operation; the following message is detailed:

```
Updating Web Panel 'SampleWebPanel'... Failed
error: Error reading from export file.
error: 'sdt:QueryViewerAxes.Axis' invalid value for property 'ATTCUSTOMTYPE' : Cannot convert value 'sdt:QueryViewerAxes.Axis'. (Variables, Axis)
error: An error occurred in WebPanel 'ViewQuery' : Error reading from export file.
'sdt:QueryViewerAxes.Axis' invalid value for property 'ATTCUSTOMTYPE' : Cannot convert value 'sdt:QueryViewerAxes.Axis'. (Variables, Axis)
```

The GeneXus Server instance and IDE are not compatible, you need to update both to version 17 Upgrade #1 or higher, [more information](https://wiki.genexus.com/commwiki/wiki?47094).

---

When opening a Knowledge Base with [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,) or lower, which has [Query object](https://wiki.genexus.com/commwiki/wiki?9026) saved with [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,) or higher, the following message is detailed:

```
Knowledge Base at 'PathToKB' contains items that GeneXus doesn't know how to handle and will therefore be inaccessible.
It is likely that the Knowledge Base has been previously opened with a GeneXus installation which had extensions that are not present in the current one.
These items are:
* 'QueryVersion3' - 'Query Version 3' (GUID 025b1afc-982f-4bdb-8fa0-4c1712cb94fc)
    Provided by 'Artech.GXplorer.BL' (GUID 6818d053-bcb6-46c3-beb9-41a2bd901d88).
Working on this Knowledge Base may lose information related to these unknown items.
Do you want to continue?
```

Upgrade the GeneXus version to [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,) or higher.

## [Query Viewer Control](#Query+Viewer+Control)

### [The Web Panel does not show the associated query](#The+Web+Panel+does+not+show+the+associated+query)

The [Query Viewer control](https://wiki.genexus.com/commwiki/wiki?9075) has assigned a [Query](https://wiki.genexus.com/commwiki/wiki?9026) in it's property definition. Make sure you have set it in design time

`[imagen omitida: wiki id 52810]`

or runtime:

```
QueryViewer.QueryName = &QueryName // must match a Query Object Name.
```

### [Error: null when executing a query in runtime](#Error%3A+null+when+executing+a+query+in+runtime)

Check the [DBMS properties](https://wiki.genexus.com/commwiki/wiki?9067) to make sure the connection with the database is set OK.

### [The Query viewer control is not shown](#The+Query+viewer+control+is+not+shown)

To view the [Query Viewer](https://wiki.genexus.com/commwiki/wiki?9075) content, JavaScript must be enabled in your browser, and you need the latest version of the *Adobe Flash Player*. Download the free player from [here](http://www.adobe.com/products/flashplayer/), otherwise you could get the following error:

```
Error: This content requires the Adobe Flash Player (version 9.0.28). Get Flash
```

### [The Query object does not exist](#The+Query+object+does+not+exist)

When assigning a [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) in runtime you could get the following error:

```
Error: The Query with name = myQueryObjectName does not exist
```

In this case the [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) no longer exists in the related knowledge base; make sure you set it's name correctly.

### [The Query object does not executes](#The+Query+object+does+not+executes)

If you are upgrading GeneXus, check the [compatibility section](https://wiki.genexus.com/commwiki/wiki?11032).

---

|  |
| --- |
| **Backlinks** |
| [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
