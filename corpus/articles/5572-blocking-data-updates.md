---
title: "Blocking Data Updates"
source_id: 5572
source_url: https://wiki.genexus.com/commwiki/wiki?5572
genexus_version: "18"
---

# Blocking Data Updates

When throughput is an issue and you need to **update**, **insert** or **delete** a large number of records, reducing the number of roundtrips to the DBMS may be the answer.  
  
Blocking database update operations (generic for insert/update/delete) entails storing them in memory and sending them in groups to the DBMS. Instead of interacting with the DBMS on every database update operation, interaction takes place only every N update operations, where N is a number specified by you.

Say, for example, that you have to print all the invoices that have not yet been printed, and that the InvoicePrintedFlag is used to store printing status. The corresponding code should look something like the one shown below. This code reads matching records and updates them one at a time. Every time the EndFor is reached (one iteration) a record is sent to the DBMS to be updated.

```
For each
     where InvoicePrintedFlag = 'N'
       PrintInvoice.Call( InvoiceNumber )
       InvoicePrinterFlag = 'Y'
EndFor
```

Adding the **Blocking clause**, like in the code below, reduces the number of roundtrips to the server. In this case, a set of database updates are sent to the DBMS only every 100 times the EndFor is reached. This is usually faster than the previous code.

```
For each
     where InvoicePrintedFlag = 'N'
     Blocking 100
         PrintInvoice.Call(InvoiceNumber )
         InvoicePrinterFlag = 'Y'
EndFor
```

The same happens when inserting a large number of records in a repetitive code such as the following:

```
For &i = 1 to &j
       ...
       New Blocking 100
             Att1 = ...
             Att2 = ...
       EndNew
EndFor
```

### [Scope](#Scope)

This clause is not supported by the following platforms:

* Java - Db2 udb
* Net - MySql
* Net - Informix
* Net - Postgresql
* NetCore - Postgresql


|  |
| --- |
| **Pages** |
| [Block Insert Performance](https://wiki.genexus.com/commwiki/wiki?5573) | [Blocking Clause in 'New' Command](https://wiki.genexus.com/commwiki/wiki?4538) | [Blocking clause in a 'For each' command](https://wiki.genexus.com/commwiki/wiki?4837) |

---
