---
title: "Blocking Clause in 'New' Command"
source_id: 4538
source_url: https://wiki.genexus.com/commwiki/wiki?4538
genexus_version: "18"
---

# Blocking Clause in 'New' Command

When throughput is an issue and you need to **insert** a large number of records, reducing the number of roundtrips to the DBMS may be the answer. See an overview in [Blocking Data Updates](https://wiki.genexus.com/commwiki/wiki?5572).

When large numbers of records have to be inserted, performance differs significantly if you insert records in blocks instead of inserting them one by one (read [block insert performance](https://wiki.genexus.com/commwiki/wiki?5573)). These significant differences in performance depend on the number of rows and the block size.

The New syntax supports the '**Blocking** *NumericExpression*' optional clause as shown below. Its presence activates the Block (Batch) insertion mechanism and controls the number of records per block. See also the complete syntax of the [New command](https://wiki.genexus.com/commwiki/wiki?6714).

### [Syntax](#Syntax)

New **[Blocking** *NumericExpression*] ....

[When Duplicate] .... EndNew

where *NumericExpression* is an expression that returns a number between 1 and 2,147,483,647*.*

### [Example](#Example)

```
for each 
   ...
   new blocking 100
      Att1 = ...
      Att2 = ...
   when duplicate
      Att2 = ...
  endnew
endfor
```

#### [When is the insertion performed?](#When+is+the+insertion+performed%3F)

The real insertion will be performed at the end of each block. Suppose the New command has a blocking factor N and is inside a repetitive structure (a For Each command, for example). Every time an execution of the body of the For Each command (and of the New command inside it) is performed, the New record is not actually inserted but is added into a size N memory block (a buffer). After that, if the buffer is filled, a special insert (of many rows) is sent to the database, in order to insert the whole block. Then, if some of the N records to be added are found to be duplicated, the special insertion will fail, and a one-by-one insertion will be performed, running through the N block, using the simple insert command, as you can see below.

**Note:**The last block (containing less than N records), will be inserted:

* Until [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  When the next commit is executed.
* Since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,): When the next commit is executed or when the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) finishes (the first that occurs).

### [Implementation](#Implementation)

When block saving is activated, the code generated for the group would be similar to the following:

```
Add record to block
NumberOfRecords += 1
if NumberOfRecords >= NumericExpression
    Insert Record Block	//masive insertion command
    When Duplicate  //some record insertion has failed
    /* Scan every record in block for duplicates */
         For each record in block
             Insert Record	//simple insertion command
             When Duplicate
                 /* Here goes When duplicate user code */
             endwhenduplicate
         endfor
    endwhenduplicate
    NumberOfRecords = 0
endif
```

Note that in the event of a duplicate key error, the code sweeps the block's records attempting to insert them one by one and executing the When Duplicate code for the records that generate duplicate keys. When a Rollback command is executed, the transaction's Rollback is executed, deleting all the records in the block (buffer) that are ready to be inserted.

### [Scope](#Scope)

This clause is not supported by the following platforms:

* Java - Db2 udb
* Net - MySql
* Net - Informix
* Net - Postgresql
* NetCore - Postgresql

Notes:

As of Genexus 17, when the blocking clause is not supported by the platform, the following spec message is thrown: **spc0222**Blocking clause for %1% is currently not supported in group starting at line %2%.

### [FAQ (Frequently Asked Questions)](#FAQ+%28Frequently+Asked+Questions%29)

#### [Is it better to insert records in blocks or individually?](#Is+it+better+to+insert+records+in+blocks+or+individually%3F)

It depends on the logic, the frequency of When Duplicate codes, etc. If you need to access the record immediately after inserting it, you cannot use Block Insert. If there are many duplicate records it is usually best not to use it.

#### [How many records per block should you use?](#How+many+records+per+block+should+you+use%3F)

Different numbers of records per block need to be tried for each case. There is no set recipe.

#### [When is the last block inserted (number of records is not a multiple of the number of records per block)?](#When+is+the+last+block+inserted+%28number+of+records+is+not+a+multiple+of+the+number+of+records+per+block%29%3F)

* Until [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  When the next Commit command is performed, whether it is implicit or explicit.
* Since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,): When the next Commit command is performed or when the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) finishes (the first that occurs).

#### What happens if you change the number of records per block at runtime?

If *NumericExpression* is a variable expression, its value will be considered only at the first insert of each block.

#### [What happens if there is a "return" within the When Duplicate code?](#What+happens+if+there+is+a+%22return%22+within+the+When+Duplicate+code%3F)

The When Duplicate code is executed up to the Return. It does not go on with the rest of the program (the When Duplicate code is generated in a new routine that is called when the buffer of a cursor batch is completed or when a Commit command is performed).

#### [What happens if there is a "do" or "call" within the When Duplicate code?](#What+happens+if+there+is+a+%22do%22+or+%22call%22+within+the+When+Duplicate+code%3F)

The corresponding call is made in both cases.

#### [What happens if a Commit command is executed?](#What+happens+if+a+Commit+command+is+executed%3F)

Executing a Commit command within the scope of the group causes all pending updates/deletes to be sent to the server. That is: do **not** issue a Commit command for every record processed as Blocking will not make any performance difference.

#### [What happens if a Rollback is executed?](#What+happens+if+a+Rollback+is+executed%3F)

When a Rollback command is executed, the transaction's Rollback is performed, deleting all the records that were inserted after the last commit. All records that correspond either to blocks completed and inserted or to a block incomplete, will be deleted.


|  |
| --- |
| **Backlinks** |
| [Example: New Command](https://wiki.genexus.com/commwiki/wiki?6742) | [New command](https://wiki.genexus.com/commwiki/wiki?6714) |

---
