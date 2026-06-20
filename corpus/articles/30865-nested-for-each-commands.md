---
title: "Nested For each commands"
source_id: 30865
source_url: https://wiki.genexus.com/commwiki/wiki?30865
genexus_version: "18"
---

# Nested For each commands

Nested For each commands are used to iterate over each record in a table to retrieve multiple records from another table (which may be the same table).

```
For each [BaseTrn] 
    ....                     
    For each [BaseTrn]       
    ...                      
    Endfor                   
    ...                      
endfor
```

When GeneXus detects nested [For each command](https://wiki.genexus.com/commwiki/wiki?24744)s, it first determines the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) of each one. Then, it interprets one of these cases:

1. **For each record** in a table, you want to retrieve **related** records from another table. Read more at [Nested For Each commands to implement a Join](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?30870,,).
2. **For each record** in a table, you want to retrieve **all** records from another table. Read more at [Nested For Each commands to implement a Cartesian Product](https://wiki.genexus.com/commwiki/wiki?30876).
3. You want to process information by groups; that is, **group the records from a table by the value of an attribute or group of attributes**, and, **for each group**, **retrieve the records corresponding to the group**. Read more at [Nested For each commands to implement a Control Break](https://wiki.genexus.com/commwiki/wiki?30878).


|  |
| --- |
| **Backlinks** |
| [For each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Nested For each commands to implement a Control Break](https://wiki.genexus.com/commwiki/wiki?30878) |

---
