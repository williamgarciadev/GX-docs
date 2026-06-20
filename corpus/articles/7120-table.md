---
title: "Table"
source_id: 7120
source_url: https://wiki.genexus.com/commwiki/wiki?7120
genexus_version: "18"
---

# Table

GeneXus uses the [Transaction Structures](https://wiki.genexus.com/commwiki/wiki?7661) defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) to automatically define the data model that it will create.

In other words, considering your definitions, GeneXus determines whether to create a Database to store your Application’s Data, **Tables** (designed using the third normal form), access paths (called **Indexes**), Views, etc.

Each Database **Table** gets its default name from the name of the Transaction from which it originated. Therefore, if a Transaction has only one level, the Table name will be the same as the Transaction name. On the other hand, if the Transaction has several levels, the subordinated table names will be created by concatenating the Transaction name and the corresponding Level names.

### [Sample](#Sample)

Consider the following Transaction Structure:

```
Company
{
   CompanyId*
   CompanyName
   Branch
   {
       BranchId*
       BranchAddress
       BranchPhone    
   }
}
```

The Tables that GeneXus will create in the Database will be called Company and CompanyBranch.

* The Company Table will contain the attributes: CompanyId\*, CompanyName
* The CompanyBranch Table will contain the attributes: CompanyId\*, BranchId\*, BranchAddress, BranchPhone

### [Availability](#Availability)

Database Views are generated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,) by defining [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062).

### [See Also](#See+Also)

[Indexes](https://wiki.genexus.com/commwiki/wiki?7121)  
[Table Editor](https://wiki.genexus.com/commwiki/wiki?3928)


|  |
| --- |
| **Sub Categories** |
| [Category:Indexes](https://wiki.genexus.com/commwiki/wiki?7121) | [Category:Table and Index Properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7122,Category%3ATable+and+Index+Properties,) |

---

|  |
| --- |
| **Pages** |
| [Add User Index](https://wiki.genexus.com/commwiki/wiki?7157) | [Table Editor](https://wiki.genexus.com/commwiki/wiki?3928) |

---
