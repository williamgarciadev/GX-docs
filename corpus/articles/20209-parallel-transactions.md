---
title: "Parallel Transactions"
source_id: 20209
source_url: https://wiki.genexus.com/commwiki/wiki?20209
genexus_version: "18"
---

# Parallel Transactions

Parallel Transactions is the name used for two or more [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s with the same identifier (primary key).

For instance, when you have the following two Transactions:

|  |  |
| --- | --- |
| **Supplier** | **Client** |
| **{** | **{** |
| CompanyId\* | CompanyId\* |
| CompanyName | CompanyName |
| CompanyAddress | CompanyAddress |
| CompanyPhone | CompanyPhone |
| SupplierPurchasesAmount | ClientDiscount |
| **}** | **}** |

they are Parallel Transactions because they share the identifier: CompanyId.

What effect does this have?

GeneXus designs the database upon standardization criteria, so, it will create an only physical table in the database whose attributes will be those resulting from the merged attributes of both Transactions:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| CompanyId\* | CompanyName | CompanyAddress | CompanyPhone | SupplierPurchasesAmount | ClientDiscount |

Then, GeneXus generates two different programs – each one with its own form, rules, events, properties, etc. – but they will have associated the same physical table where the data will be stored.

Thus, when executing the Supplier Transaction and entering a new company, with CompanyId=1, a record will be inserted in the COMPANY table with primary key value 1, and the values entered by the end-user in the CompanyName, CompanyAddress CompanyPhone, and SupplierPurchasesAmount attributes. What will happen with the ClientDiscount attribute – for this record? It will be empty because it is not present in the Supplier Transaction so the end-user can not enter a value for it.

Afterward, when executing the Client Transaction with the purpose of entering a new company, CompanyId=2, a record will be inserted in the COMPANY table with primary key value 2, and the values entered by the user in the CompanyName, CompanyAddress, CompanyPhone, and ClientDiscount. In this case, the SupplierPurchasesAmount attribute will be stored with an empty value.

Note that by executing any of the Transactions, the end-user will be able, for example, to query, update and delete any record present in the COMPANY physical table associated with both Transactions. Consider that because each Transaction is an independent object, it is possible to define different rules and events for each of the Parallel Transactions to define the desired controls and behavior.

Transactions may be parallel at several levels. The example above just mentioned one-level Transactions.

For example, you could have three transactions with the following structures:

|  |  |  |
| --- | --- | --- |
| **Transaction “T1”** | **Transaction “T2”** | **Transaction “T3”** |
| A\* | A\* | A\* |
| B | C | E |
| C | D | **{** M\* |
| **{** X\* | **{** X\* | N **}** |
| Z **}** | Y **}** |  |

In this case, there is double parallelism: between the first level of the three Transactions (they all have the same physical table associated), and between the second levels of the first two Transactions (they share the same physical table). GeneXus will create the three following physical tables in the database:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **T1** | A\* | B | C | D | E |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **T2** | A\* | X\* | Z | Y |

|  |  |  |  |
| --- | --- | --- | --- |
| **T3** | A\* | M\* | N |


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Module - Parallel Transactions and Object Visibility](https://wiki.genexus.com/commwiki/wiki?25344) | [Optimistic concurrency control](https://wiki.genexus.com/commwiki/wiki?22885) |

---
