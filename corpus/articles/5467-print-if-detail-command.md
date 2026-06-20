---
title: "Print If Detail Command"
source_id: 5467
source_url: https://wiki.genexus.com/commwiki/wiki?5467
genexus_version: "18"
---

# Print If Detail Command

Avoids printing a record if no grid records exist.

### Syntax

Print If Detail

### Description

Sometimes you may want to print, for example, a report of certain customer data together with their invoices, leaving out the customers who have no invoices (i.e., a customer's name should not be printed if that customer has no documents). To achieve this you need to have two groups of nested For Each commands, where the external For Each command accesses the Customers table and the internal For Each command accesses the Invoices table, as shown below:

```
For each order CustomerId // Access Customer table
     Print Pb_CustomerInformation
     For each // Access Invoices table
          Print Pb_CustomerInvoices
     EndFor
EndFor
```

The objective of the "Print If Detail" command is to avoid printing a customer's data if there are no invoices related to that customer, as you will see in the following example. Look at the example below:

```
For each order CrewRank
     Print Pb_CrewData
     Print if detail
     For each
          Print Pb_FlightNumber
     EndFor
EndFor
```

The aim of this process is to list all the flight numbers of crew members assigned to a flight. If the "Print If Detail" command is omitted, all crew members will be listed, regardless of whether they have been assigned to a flight or not. In this case, the base table would be Crew through the CrewRank attribute and the attributes contained in the [printblock](https://wiki.genexus.com/commwiki/wiki?5468) Pb\_CrewData. So first it is necessary to run through the table containing the numbers of flights assigned to crew members. The objective of "Print If Detail" is to change the base table of the first For Each command, nesting the same base table (for every For Each command). However, the CrewRank attribute in the Order clause will continue to be the control break.

Although the examples given involve printing procedures, the "Print If Detail" command can also be used even if "printed outputs" are not specifically involved. For example, if you need to "mark" customers who have invoices instead of printing them.

### Scope

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Print command](https://wiki.genexus.com/commwiki/wiki?5479) |

---
