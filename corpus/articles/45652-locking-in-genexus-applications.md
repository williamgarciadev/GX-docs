---
title: "Locking in GeneXus Applications"
source_id: 45652
source_url: https://wiki.genexus.com/commwiki/wiki?45652
genexus_version: "18"
---

# Locking in GeneXus Applications

Below is explained how GeneXus handles locks when just reading data and when reading and writing data to [control the concurrency](https://wiki.genexus.com/commwiki/wiki?45563).

## [For reading](#For+reading)

If it is only for reading (when using [For Each commands](https://wiki.genexus.com/commwiki/wiki?24744), [Web Panel objects](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider objects](https://wiki.genexus.com/commwiki/wiki?5270), etc.), the generated SELECTs do NOT lock.

They are always affected by the exclusive locks. For example, in the reorganizations the tables are opened in an exclusive way; in this case, no other process will be able to open the table no matter if it is only for reading. On the other hand, if the information to be read is locked by another writing program, depending on the DBMS, the values that will be displayed. The DBMS is the one that will decide whether to display the old or new information (the [Isolation level property](https://wiki.genexus.com/commwiki/wiki?8991) available at the Data Store level in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) allows configuring this aspect).

## For reading and writing

A [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) that includes an update performs a SELECT with a lock when entering the For Each and then, the update (UPDATE / SET) is performed. Like any lock, it releases the records when executes the commit (or rollback).

**Note:** Certain For Each commands are optimized and then do not lock, but do UPDATE directly. They are only the optimizable ones (those that contain conditions that go to the server, and in their body only assignments).

### [See Also](#See+Also)

[For Each Optimizations](https://wiki.genexus.com/commwiki/wiki?26286)  
[Server Side Functions/Methods](https://wiki.genexus.com/commwiki/wiki?11572)


|  |
| --- |
| **Backlinks** |
| [Toc:Concurrency control](https://wiki.genexus.com/commwiki/wiki?45563) |

---
