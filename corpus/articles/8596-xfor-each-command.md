---
title: "Xfor each command"
source_id: 8596
source_url: https://wiki.genexus.com/commwiki/wiki?8596
genexus_version: "18"
---

# Xfor each command

Scans records of an external file using a given index.

### [Syntax](#Syntax)

```
Xfor each <file_name> [Index <index_name>]
        [Where <condition1>]
          …
        [Where <conditionN>]
        [option distinct]
        [When none]
Xendfor
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*file\_name*  
     Is the name of the Data View defined to access the external file.

*Index*  
     Defines the name of the index to be used.

*index\_name*  
     Is the name of the Data View Index.

*[where](https://wiki.genexus.com/commwiki/wiki?8578)*  
     Clause that can be specified to establish a condition for data retrieval.

*condition*  
     Any valid logical expression.

*[option distinct](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23811,,)*  
     Only returns records where the set of values of the attributes referred to is unique.

*[when none](https://wiki.genexus.com/commwiki/wiki?8603)*  
     Specifies the code to be executed when the Xfor each does not filter any record.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)

### [Description](#Description)

This command defines an iterative loop for an external file, using the specified index (if any) and filters data according to the Conditions declared in the [Where](https://wiki.genexus.com/commwiki/wiki?8578) statements.

When a [Data View object](https://wiki.genexus.com/commwiki/wiki?1914) without an associated table is defined, this command will obtain the required information to perform updates over an external file. If the Data View has an associated table, the [For each command](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20195,,) may be used instead of the Xfor each command.

GeneXus will try to optimize the search in an intelligent way, taking into account the index specified in the Xfor each statement and the conditions defined in the Where of the Xfor each group. Xfor each groups can be combined by nesting them or by defining them as parallel groups.

The differences between the For each and the Xfor each commands are:

|  |  |
| --- | --- |
| **For each** | **Xfor each** |
| Several tables may be associated with the Group. | Only one table can be referenced. |
| The base table is inferred by GeneXus. | The base table must be declared by the user. |
| The index is inferred by GeneXus according to the specified order. | The index must be declared by the user. |
| Relationships between nested For each groups are done by GeneXus | No relationship is detected between nested Xfor each groups. |

### [See Also](#+See+Also)

[For each command](https://wiki.genexus.com/commwiki/wiki?24744)  
[Xfor First Command](https://wiki.genexus.com/commwiki/wiki?8601)  
[Data View object](https://wiki.genexus.com/commwiki/wiki?1914)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Exit command](https://wiki.genexus.com/commwiki/wiki?8590) | [When clause](https://wiki.genexus.com/commwiki/wiki?8629) |
| [When duplicate clause](https://wiki.genexus.com/commwiki/wiki?24843) | [When None Clause](https://wiki.genexus.com/commwiki/wiki?8603) | [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) | [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601) |
| [Xnew command](https://wiki.genexus.com/commwiki/wiki?8640) |

---
