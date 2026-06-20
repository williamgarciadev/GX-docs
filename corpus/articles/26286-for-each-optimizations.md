---
title: "For each Optimizations"
source_id: 26286
source_url: https://wiki.genexus.com/commwiki/wiki?26286
genexus_version: "18"
---

# For each Optimizations

When the following patterns appear on a [For each command](https://wiki.genexus.com/commwiki/wiki?24744), a SQL optimized query will be generated.

### [Optimizations: First 1 record(s)](#Optimizations%3A+First+1+record%28s%29)

The following patterns optimize the SQL sentence to get the first record only.

```
For each [Order]
[Where ...]
[Defined by ...]
....
Exit
EndFor
```

or

```
For each [Order]
[Where ...]
[Defined by ...]
....
Exit
When None
...
EndFor
```

The Exit command must be set immediately before the EndFor or When None, no comments are allowed between the Exit and EndFor/When None keywords.

### [Optimizations: count(\*)](#Optimizations%3A+count%28*%29)

The following pattern optimizes the SQL sentence to generate a Count(\*) aggregation on the data.

```
&i = 0
For each
defined by AttName
  &i += 1
EndFor
```

### [Optimizations: Sum](#Optimizations%3A+Sum)

The following pattern optimizes the SQL sentence to generate an aggregate operation on the attribute referenced on the For each block section.

```
For each
defined by AttName
  &i = &i + AttId
Endfor
```

### [Optimizations: Update](#Optimizations%3A+Update)

The following pattern optimizes the SQL sentence to generate an Update SQL statement on the data.

```
For each
Where <Condition>
  Att1 = <Expression>
  Att2 = <Expression>
Endfor
```

### [Optimizations: Delete](#Optimizations%3A+Delete)

The following pattern optimizes the SQL sentence to generate a Delete SQL statement on the data.

```
For each
defined by AttName
  delete
Endfor
```

### [Considerations](#Considerations)

All conditions and filters must be evaluated on the DBMS.

An Expression can include attributes, variables or constants. All the assigned (updated) attributes must belong to the same table.


|  |
| --- |
| **Backlinks** |
| [Database performance from the GeneXus perspective](https://wiki.genexus.com/commwiki/wiki?26285) | [Lock time-out (seconds) property](https://wiki.genexus.com/commwiki/wiki?9116) | [Locking in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45652) |

---
