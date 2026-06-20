---
title: "Blocking clause in a 'For each' command"
source_id: 4837
source_url: https://wiki.genexus.com/commwiki/wiki?4837
genexus_version: "18"
---

# Blocking clause in a 'For each' command

When throughput is an issue and you need to **update** or **delete** a large number of records, reducing the number of roundtrips to the DBMS may be the answer. See an overview at [Blocking Data Updates](https://wiki.genexus.com/commwiki/wiki?5572).

The differences in performance between optimized update/delete, single-record update/delete and block update/delete are quite important. Optimized update/delete usually delivers the best performance, as it only requires one trip to the server. The worst case is usually single-record update/delete, as it requires as many as two roundtrips to the server for every record involved. Block update/delete is usually a good alternative to single-record update/delete if optimization is not possible.

### [Syntax](#Syntax)

The Blocking clause in a For each group, as described below, activates update and/or delete blocking in a For each command. The NumericExpression specifies the number of records in each block

```
For each
   [Order ... ] [Where ... ] [defined by ... ]
   [Blocking NumericExpression]
    ...
   /* Delete Code */ 
   /* Update Code */ 
When None
   /* When none code */
EndFor
```

### [Example](#Example)

```
For each
    Where Att1 < Value1
          Blocking 100
          Att2 = Value2 
    When none 
         msg("...")
EndFor
```

### [Implementation](#Implementation)

When the Blocking clause is specified, the code generator will be similar to the following:

```
For each
     Add record to block (Update or delete code)
     NumberOfRecordsUpd += 1 or NumberOfRecordsDel += 1 (dependant of Update or Delete code)
     If NumberOfRecordsUpd = NumericExpression
        Update Record Block 
        NumberOfRecordsUpd = 0
     EndIf
     If NumberOfRecordsDel >= NumericExpression
        Delete Record Block 
        NumberOfRecordsDel = 0
     EndIf
  When none      
     /* Here goes When none */
EndFor
```

* If Blocking is specified and no updates and/or deletes are performed, it will be ignored.
* Block size applies to deletes and updates. You cannot specify a different number for each.
* Implementation uses different blocks for updates and deletes. One may be filled before the other. For example, there may be 5 updates and only 1 delete executed. If the Block size is, say, 5, then the update block is sent to the server but the delete block is not.
* Executing a Commit within the scope of the group causes all pending updates/deletes to be sent to the server. That is, do **not** issue a Commit command for every record processed, as Blocking will not make any difference in performance.
* Executing a Rollback within the scope of the group causes all pending to be **cleared**, so they will never be sent to the server.

### [Scope](#Scope)

This clause is not supported by the following platforms:

* Java - Db2 udb
* Net - MySql
* Net - Informix
* Net - Postgresql
* NetCore - Postgresql


|  |
| --- |
| **Backlinks** |
| [Database performance from the GeneXus perspective](https://wiki.genexus.com/commwiki/wiki?26285) | [Delete command](https://wiki.genexus.com/commwiki/wiki?6828) | [For each command](https://wiki.genexus.com/commwiki/wiki?24744) |

---
