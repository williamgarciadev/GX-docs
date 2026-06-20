---
title: "Nullable property - Attribute"
source_id: 7642
source_url: https://wiki.genexus.com/commwiki/wiki?7642
genexus_version: "18"
---

# Nullable property - Attribute

The null value for a given attribute should be considered as "not specified" or "not available" or "not assigned". It is different from the "empty" value that is a special value (i.e. zero for numeric data, empty string for character data, etc.). As from [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) 9.0, you can specify, in a Transaction's structure, whether or not an attribute can have a null value. This information is useful for several purposes:

* Protect data
* Improve referential integrity controls
* Enable better join performance

### [Null Definition](#Null+Definition)

Changes to attribute nullability can be done at the Transaction level by checking or unchecking the Nullable column. It can be set for any attribute that is stored in the underlying table except for the primary key attributes (that do **not** support the null value by definition).  
  
The Transaction's Nullable column can take the following values:

* **No**: means that the attribute in the underlying Table does not allow the null value.
* **Yes**: means that the attribute in the underlying table allows the null value.
* **[Compatible]**: This is a special compatibility value that is available only in Knowledge Bases that have been converted from GeneXus prior to 9.0. See Compatibility Section in [Null Property (GeneXus 9.0)](https://wiki.genexus.com/commwiki/wiki?1995,,) for more details.

The default value is No.

##### [Parallel Transactions](#Parallel+Transactions)

Parallel Transactions are Transactions having the same Primary Key composition in a given level. If there are Parallel Transactions in a Knowledge Base, they share null definitions. This means that the last Parallel Transaction saved from a set, overwrites previous null definitions for all the set.

### [Why should you care about Nulls?](#Why+should+you+care+about+Nulls%3F)

Nulls are very important in the relational model. Allowing the null value for a given attribute means that it may, under certain circumstances, be "ignored" as its value is "not set". On the other hand, if an attribute does not allow the null value, a valid value must always be assigned to it. Nulls information is used in [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) for defining Data Base tables and referential integrity controls, to determine the Join Type used to navigate de Data Base and check program's logic.  
  
**Data Base tables**  
Nulls definition is used by [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) when it creates KB tables. The IAR (Impact Analysis Report) shows Nulls capabilities of every attribute on each KB table. Changing Nulls definition forces a database reorganization.  
  
**Referential Integrity**  
Tables in a KB relate to each other. Cross references between them are made through foreign keys and primary keys. Null definitions for attributes comprising a foreign key let Genexus know how "strong" these references are. For example: if none of the attributes comprising a foreign key allow the null value. This is a strong reference (also known as a not null reference): it states that, no matter what happens, the foreign key must always point to an existing Primary Key value of the referenced table. On the other hand, a foreign key having at least one attribute supporting the null value is a weak reference (also known as null reference) and states that if this (or these) attribute(s) are null (any of them if many) the reference should not be checked.  
  
When a foreign key is a compound key (with more than one attribute) and nulls are allowed for any of its attributes, new references may be defined if the remaining attributes comprise a foreign key too, as in the following example.

|  |  |  |
| --- | --- | --- |
| **COUNTRY** | **CITY** | **CLIENT** |
| CountryId\* | CountryId\* | ClientId\* |
| CountryDsc | CityId\* | ClientName |
|  | CityDsc | CountryId |
|  |  | CityId |

In the CLIENT Transaction structure, the CountryId and CityId attributes make up a compound foreign key for the CITY table. If null values are **not** allowed for either CountryId or CityId, the reference's existence is unconditionally verified. On the other hand, if null values are allowed for CityId, reference to table CITY will be checked only if CityId is not null, and a reference to the table COUNTRY needs to be created. This last reference is needed to avoid entering an invalid (non-existing) CountryId when CityId is null.

**Determining Join Type**

Join refers to how tables are "linked" to retrieve data to fulfill a request ("For each"s, either explicit or implied). As this is written, Genexus supports two types of Joins: Natural and Outer. Natural means that if, for example, two tables are joined, records for not matching join conditions should not be retrieved. Outer means that records not matching join conditions must be retrieved.

Based on Null definitions for foreign keys, Genexus knows when to use Natural (not null reference) or Outer (nullable references).

**Checking program logic**

Null definitions can be used to check program logic. Basically, to avoid setting the null value for attributes that do not allow it.

### [Nulls in navigation reports](#Nulls+in+navigation+reports)

Navigation reports do not normally show information about null definitions. They do show, however, the effects of null definitions, for example:

* A '' symbol is prefixed to the table icon when nulls are allowed (Outer Join)
* The 'allowing nulls' suffix is added to 'READ <TABLE>' in the Detailed Navigation Report.
* An '=' symbol is prefixed to the table icon when nulls are not allowed (Natural Join).

### [Nulls and Foreign Keys Summary](#Nulls+and+Foreign+Keys+Summary)

* If a foreign key has the Null property set to 'No' for all its attributes:
  + Not null references will be allowed when inserting or updating.
  + Joins referencing these tables will be generated as Natural Joins.

* If a foreign key has some of its Compose attribute set to Yes:
  + Null values will be allowed when inserting or updating.
  + New referential integrity control is performed if other attributes of this FK match with another Primary Key.
  + Joins referencing these tables will be generated as Outer Joins.

### [Specification and Reorganization Controls](#Specification+and+Reorganization+Controls)

#### [Specification controls](#Specification+controls)

* If a program (Transaction or Procedure) inserts a record in a table with no referenced attributes with null value property in Yes, and the Initialize Not Referenced Attributes property is set to No, the following error message appears: *spc0081: Attributes %1 do not allow nulls in table %2 and are not referenced %3.*

> To fix the error:

* If the program is a Transaction, you may reference these attributes in the transaction structure or disable insertion in the appropriate level. Use the 'error() if insert' rule.
* If it is a Procedure, the 'New' group must reference them. Otherwise, you may change the nullability property of these attributes.
* Set the Initialize not referenced attributes property to Yes.

* If the Nullvalue() function is assigned to an attribute that doesn't support null values, and the Generate Nulls for Nullvalue() property is set to Yes, the following error occurs: *spc0082: Attribute %1 in table %2 does not allow nulls.*

> To fix the error:
>
> * Remove the assignment and change the Generate Null for Nullvalue() property value, or
> * Change the attribute nullability for this table.

* If a foreign key doesn't allow nulls and the Allownulls rule is specified for it, the following message appears: *spc0085: AllowNulls rule conflict with null definition for foreign key %1.*

> To fix the error:
>
> * Remove the Allownulls rule (it should not be necessary) and change the nullability of foreign key attributes as needed.

#### [Reorganization Controls](#Reorganization+Controls)

When changing an attribute Null=Yes to Null=No, or vice versa, a reorganization takes place. If the modified attribute belongs to a foreign key, this reorganization can change the foreign key constraint definition. If the attribute doesn't belong to a foreign key:

* Changing from Null=No to Null=Yes doesn't imply any problems because a new value is added (the null one) and the existent data cannot have it.
* Changing from Null=Yes to Null=No deletes a possible value of the existent data. To be able to reorganize the data without any errors in the process, you have to replace the null values with one of two possible values: the one specified in the Initial Value property or, in case this value has not been specified, the empty value corresponding to the attribute data type. In this case, the following warning will be given: *Rgz0008: Attribute %1 changed from AllowNulls=Yes to AllowNulls=No and no initial value was specified. Null values will be treated as empty ones.*

Besides, if the attribute belongs to a foreign key, changes in the foreign key constraint definition could cause the creation of Load Referential Integrity programs.  
  
If a new attribute is defined in an existing table that doesn't accept null, the following warning is displayed during reorganization: *Rgz0007: Attribute %1 does not allow nulls and doesn't have a default value. An empty default value will be used*. If this new attribute is a Foreign Key, a new referential integrity constraint is also created. Consequently, if the default value assigned to this attribute does not exist in the referenced table, the reorganization will fail. This is noted in the following message: *Reorganization may fail if table %1 has records and the key value %2 does not exist in table %3.*

### [Considerations](#Considerations+)

As mentioned above, when a foreign key is a compound key (with more than one attribute) and nulls are allowed for any of its attributes, new references may be defined if the remaining attributes comprise a foreign key too.


|  |
| --- |
| **Backlinks** |
| [Cosmos DB nulls handling](https://wiki.genexus.com/commwiki/wiki?53633) | [Database Reorganization cases where a temporary table is created](https://wiki.genexus.com/commwiki/wiki?19529) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) | [GeneXus for SAP Systems - Data Model changes](https://wiki.genexus.com/commwiki/wiki?34336) | [GeneXus for SAP Systems Data Model changes (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54688) | [Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946) |
| [Join Type and Join Location Specification](https://wiki.genexus.com/commwiki/wiki?19547) |

---
