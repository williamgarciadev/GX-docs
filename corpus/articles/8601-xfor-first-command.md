---
title: "Xfor First command"
source_id: 8601
source_url: https://wiki.genexus.com/commwiki/wiki?8601
genexus_version: "18"
---

# Xfor First command

Returns the first record of an external file using the specified index and filtering data according to the Conditions declared in the where statements.

### [Syntax](#Syntax)

```
Xfor first <file_name>  [Index <index_name>]
      [Where <condition1>]
       …
      [Where <conditionN>]
      [When None]
Xendfor
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*file\_name*  
    Is the name of the [Data View object](https://wiki.genexus.com/commwiki/wiki?1914) defined to access the external file.

*Index*  
    Defines the name of the index to be used.

*index\_name*  
    Is the name of the Data View Index.

[where](https://wiki.genexus.com/commwiki/wiki?8578)  
    Clause that can be specified to establish a condition for data retrieval.

condition1,...,conditionN  
    Any valid logical expression.

[when none](https://wiki.genexus.com/commwiki/wiki?8603)  
     Specify the code to be executed when the first Xfor each does not filter any record.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)

### [Description](#Description)

This command is similar to the [Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596), but it does not iterate (loop). It returns the first record (if there is one) of the external file using the specified index and filtering data according to the Conditions declared in the Where statements.

GeneXus will try to optimize the search in an intelligent way, taking into account the index specified in the Xfor Each group and the conditions established in the Where statement of the Xfor Eeach group.

### [See Also](#See+Also)

[Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [When clause](https://wiki.genexus.com/commwiki/wiki?8629) | [When None Clause](https://wiki.genexus.com/commwiki/wiki?8603) |
| [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) | [Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596) |

---
