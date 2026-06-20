---
title: "Reverse Engineering Process"
source_id: 2414
source_url: https://wiki.genexus.com/commwiki/wiki?2414
genexus_version: "18"
---

# Reverse Engineering Process

### [Overview](#Overview)

Reverse engineering is a broad term, but in this scenario it refers to the process of reading the structure of database tables and their relationships, and defining the necessary [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) Objects (data model) to represent the schema.

`[imagen omitida: wiki id 7601]`

### [Reverse Engineering](#Reverse+Engineering)

[GeneXus](https://wiki.genexus.com/commwiki/wiki?1756)' basic secret is the [URA](https://wiki.genexus.com/commwiki/wiki?1977,,) attribute naming convention. Most Databases do not use this attribute naming convention. The key objective of this process is to convert your Database schema to a [URA](https://wiki.genexus.com/commwiki/wiki?1977,,) based schema. Reverse engineering a non-URA major input affects the referential integrity constraints defined in the schema. Although you can use this tool even if you have not defined the database referential integrity, it is better to use it when the referential integrity is defined.  
  
The [DB Reverse Engineering](https://wiki.genexus.com/commwiki/wiki?6634) tool does not change your Database in any way. It just reads the table structures and their relationships. It does not even attempt to read table data.  
  
At the end of the DB Reverse engineering process you will have a [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) Knowledge Base pointing to your database and you will be able to access or update it.

### [What Does a Reverse Engineered Knowledge Base Have?](#What+Does+a+Reverse+Engineered+Knowledge+Base+Have%3F)

A [GeneXus Transaction](https://wiki.genexus.com/commwiki/wiki?1908) is created for each database table that has the same attributes. Based on the constraints defined in the tables, the actual "[GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) name" attribute may be different from the original. [DBRET](https://wiki.genexus.com/commwiki/wiki?6634) could change the internal attribute name to enforce the URA concept. Let us see some examples.  
  
**Example 1**  
Consider the following four tables and their referential integrity constraints. As you can see the same attribute name is used for all of the primary keys of the tables, and some of its secondary attributes. The following constraints were also defined in the database (shown with the arrows):

```
Invoice.Client  --> Customer.Code
InvoiceLine.Code --> Invoice.Code
InvoiceLine.Prod --> Product.Code
```

`[imagen omitida: wiki id 7602]`

After [DBRET](https://wiki.genexus.com/commwiki/wiki?6634) processes the schema, the following [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) Transaction and Tables are created:

`[imagen omitida: wiki id 7603]`

As you can see, some attribute names have changed. Now you don't only have a "Name" attribute, you have, for example, a "ProductName", which gives you context information and will enable you to program new objects without worrying about how to join tables.  
  
**Example 2**  
There are some cases in which [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) cannot use the same attribute name to represent the same thing, but still needs to maintain the relationship. For example, in specializations, self-relations, or when it has two or more foreign keys for the same table. In these cases, a [Subtype Group object](https://wiki.genexus.com/commwiki/wiki?20206) will be created.  
  
The following example shows a specialization diagram for an external Database, where all the primary keys were defined with the same name.

`[imagen omitida: wiki id 7604]`

[DBRET](https://wiki.genexus.com/commwiki/wiki?6634) will define the internal tables as follows:

`[imagen omitida: wiki id 7605]`

The following subtype groups will be also defined to maintain the relationship between tables:

```
SALES GROUP
SalesEmployee subtype of Employee

SUPPORT GROUP 
SupportEmployee subtype of Employee
```

The third [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) object created by the [DBRET](https://wiki.genexus.com/commwiki/wiki?6634) during this process is the [Data View](https://wiki.genexus.com/commwiki/wiki?1914) This object contains all the internal-table-to-external-table mapping information. As we saw above, some internal attribute names have changed. Data Views define, among other things, the mapping between Genexus and your database schema. The internal names are used in [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) objects, but the generated programs will use the external ones.

See also: [Database Reverse Engineering Wizard](https://wiki.genexus.com/commwiki/wiki?6627)


|  |
| --- |
| **Backlinks** |
| [Category:Database Reverse Engineering](https://wiki.genexus.com/commwiki/wiki?6634) | [Database Reverse Engineering Wizard](https://wiki.genexus.com/commwiki/wiki?6627) |

---
