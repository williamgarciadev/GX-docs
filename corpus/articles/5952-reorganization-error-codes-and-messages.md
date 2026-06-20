---
title: "Reorganization Error Codes and Messages"
source_id: 5952
source_url: https://wiki.genexus.com/commwiki/wiki?5952
genexus_version: "18"
---

# Reorganization Error Codes and Messages

The list that follows shows all the messages that can appear in the Impact Analysis Report during the **specification of Reorganization Programs (rgznnnn)**.

| Code | Message |
| --- | --- |
|  | |
| **rgz0001** | **Table name %1 exceeds maximum name length allowed by language (%2 characters).** |
|  | The selected programming language cannot generate correctly with table names with more than %2 characters. The solution is to rename the table, change the programming language or change the method used to access data. |
|  | |
| **rgz0002** | ****Attribute name %1 exceeds maximum name length allowed by language (%2 characters).**** |
|  | The selected programming language cannot generate correctly with attribute names with more than %2 characters. The solution is to rename the attribute, change the programming language or change the method used to access data. |
|  | |
| **rgz0003** | ****Problems found on table %1 structure. It will not be created/reorganized.**** |
|  | This is a generic message that indicates that there were other problems preventing the table creation/reorganization. The other problems should appear in the impact analysis. |
|  | |
| **rgz0004** | ****For each value of %1 there could be several records of %2 in table %3. Data may be lost.**** |
|  | This warning message indicates that two tables (one subordinated to the other) are "merging" into a single table. E.g.: if we eliminate the detail in a typical Invoices transaction and we put the Product at Invoice level. In this example, the message indicates that only the Product in the first detail line will be kept in the reorganization; the remaining detail lines (and their Products) will be lost. |
|  | |
| **rgz0005** | ****For each value of %1 there may be several values of %2.**** |
|  | This warning message occurs when a table is created from another table's data. E.g.: the creation of a Clients table from the Invoices table. In this example, the message indicates that for each value of the ClientCode there may be many values of the ClientName. Only one value of the ClientName table values will be kept for each value of the ClientCode; the rest will be lost. |
|  | |
| **rgz0006** | ****AllowNulls=Yes for attribute %2 ignored. At least one attribute in foreign key %1 has the AllowNulls property set to No.**** |
|  | The %2 attribute is part of a foreign key made up of more attributes in the table that is being created/reorganized. The fact that some attributes of the foreign key can be null whereas others cannot be null is inconsistent. The solution is to give the same value (Yes or No) to the AllowNulls property of all foreign key attributes. |
|  | |
| **rgz0007** | ****Attribute %1 does not allow nulls and does not have an Initial value. An empty default value will be used.**** |
|  | It has been specified that the new %1 attribute does not allow nulls in the table that is being created/reorganized. Nevertheless, a value (or valid value) has not been specified in the Initial Value property.    The message indicates that when there is not a value defined by the user to be assigned, the "empty" value corresponding to the %1 attribute data type will be used. |
|  | |
| **rgz0008** | ****Attribute %1 changed from AllowNulls=Yes to AllowNulls=No and no initial value was specified. Null values will be treated as empty ones.**** |
|  | When changing the value of the AllowNulls property of the %1 attribute from Yes to No, the reorganization process can find records with the %1 null value.    The message indicates that, if during the reorganization process, null values are found for the %1 attribute, they will be replaced with the "empty" value corresponding to the %1 attribute data type. |
|  | |
| **rgz0009** | ****AutoNumber=True ignored. Attribute %1 is not table %2 primary key.**** |
|  | The Autonumber property applies only when the attribute is the primary key of a table. It does not apply when it is part of a primary key (made up of more attributes).    The message indicates that the primary key of the %2 table is made up of other attributes (in addition to the %1 attribute) or that the %1 attribute is not part of the 2 %table key. |
|  | |
| **rgz0010** | ****AutoNumber=True ignored for attribute %1. Autonumbering is not supported in this DBMS.**** |
|  | The %1 attribute should be defined as auto-numbered in the table that is being created/reorganized, but the DBMS for which it is being generated does not support the AutoNumber property. |
|  | |
| **rgz0011** | ****Secondary attribute %1 in more than one table.**** |
|  | This error indicates that the %1 secondary attribute is stored in more than one table. This situation usually occurs when there are transactions that have not been defined yet in Design, or when the defined transactions "contradict each other". |
|  | |
| **rgz0012** | ****%1 is associated to External file %2. It will not be reorganized.**** |
|  | In this model, the %1 table to be reorganized is associated to a Data view (%2) and this is the reason why it is not reorganized. |
|  | |
| **rgz0013** | ****%1 is a table on the server and the Model property ''Reorganize Server tables'' is No.**** |
|  | The %1 table to be reorganized is not a local table and it has been required that only local tables should be reorganized. |
|  | |
| **rgz0014** | ****Index name *%1* exceeds maximum name length allowed by language (%2 characters).**** |
|  | The selected programming language or DBMS cannot generate correctly with index names with more than %2 characters. The solution is to rename the index, change the programming language or DBMS, or change the method used to access data.    See [this](https://wiki.genexus.com/commwiki/wiki?7249,,) document for further information. |
|  | |
| **rgz0015** | ****Reorganization may fail if table %1 has records. Reference (%2) does not allow nulls and referenced table %3 is new (empty).**** |
|  | An integrity restriction, that cannot be null, has been created between table %1 and table %2, which is new (without records). If table %1 has records the reorganization will fail. |
|  | |
| **rgz0016** | ****Data lost may occur as duplicate key may arise when adding records to table %1 from multiple source tables (%2).**** |
|  | It occurs in reorganizations using several tables as data source to create a new table. It indicates that the records of the tables specified in %2 can have common key values and that, if this happens, duplicated secondary attributes data could be lost. |
|  | |
| **rgz0017** | ****At least one attribute in foreign key %2 does not have a (valid) "Initial value". Attribute %1 initial value ignored.**** |
|  | The message indicates that the value of the "Initial value" property must have been ignored since, otherwise, there is the possibility that the reorganization gets canceled if the table that is being reorganized has records. The reason for the cancellation would be that there are records in the table to be reorganized that make reference to a foreign key (non-null) that does not exist in the table referred to.    If you want all the records of the table to be reorganized to have a specific value (non-null) for the foreign key, you may take one of the following steps:    a. Process completely carried out with GeneXus  * Cancel the reorganization process. * Add a valid value for "Initial value" to all attributes indicated as %2. * Verify that there is a record in the table referred to whose key coincides with the initial values given to the foreign key. * Reorganize the database.  b. Process carried out by combining GeneXus with the DBMS tools  * Continue the reorganization * Using the tools of the DBMS you are working with:   + Verify that there is a record in the table referred to whose key coincides with the initial values desired for the foreign key.   + Replace the value of the attributes in the table that is being reorganized with the desired values. |
|  | |
| **rgz0018** | ****Foreign key to new (empty) table %2 cannot be initialized. Attribute %1 initial value ignored.**** |
|  | The message indicates that the value of the "Initial value" property must have been ignored since, otherwise, there is the possibility that the reorganization gets canceled if the table being reorganized has records. The reason for the cancellation would be that there are records in the table to be reorganized that make a reference to a foreign key (non-null) that does not exist in the table indicated as %2.    If you want all the records of the table to be reorganized to have a specific value (non-null) for the foreign key, you may take one of the following steps:    a. Process completely carried out with GeneXus  * Cancel the reorganization process. * Delete the objects that define the table indicated as %2. * Reorganize the database. * Add the objects that define the table indicated as %2. * Reorganize the database again.  b. Process carried out by combining GeneXus and the DBMS tools  * Continue with the reorganization. * Using the tools of the DBMS you are working with:   + Add a record with the desired key values in the table indicated in %2.   + Replace the value of the attributes in the table that is being reorganized with the desired values. |
|  | |
| **rgz0019** | ****Reorganization may fail if table has records. Unique indexes should not be created on new attributes only.**** |
|  | A unique index is being created, which is made up of new attributes only. If the table has records, the reorganization will fail as the new columns will be initialized as empty (all of them with the same value) for all records.    So, if you already know that the table has records, you can avoid this error by defining an "Initial Value" for new attributes. The initial value must initialize each record with a different value. This time the Impact Analysis will show rgz0030 instead. |
|  | |
| **rgz0020** | ****Reorganization may fail if there are duplicate values for %1.**** |
|  | A unique index is being created in the table. If the existing records have duplicated values, the reorganization may fail. |
|  | |
| **rgz0021** | ****Unique index %1 on table %2 is not supported in this environment. Ignored.**** |
|  | If the environment does not support candidate keys, the unique indexes %1 of table %2 are ignored. |
|  | |
| **rgz0022** | ****%1's data type (%2) is not supported on the selected environment (DBMS/Generator).**** |
|  | The attribute identified by %1 is %2 data type. The %2 data type is not supported by the DBMS and/or the combination DBMS/Generator. An alternative solution is to change the %1 attribute data type to one supported by the combination DBMS/Generator. Another alternative is to change the reorganization generator. |
|  | |
| **rgz0023** | ****Attribute '%1' cannot have the same name of a table when it has the Autonumber property set on and using Oracle.**** |
|  | This message indicates that there is a table with the same name of an attribute that has the Autonumber property in "Yes." In Oracle, this situation generates a names conflict that does not allow the reorganization to continue.    To support the Autonumber property, GeneXus creates a Sequence type object in Oracle. The name that GeneXus gives to this object is the name of the attribute that has the Autonumber property in "Yes." Oracle does not support a table and a Sequence object having the same name.    Solution: modify the name of the attribute or of the table to avoid the conflict. |
|  | |
| **rgz0024** | ****Column count of index %1 exceeds maximum allowed by DBMS (%2).**** |
|  | The number of columns of index %1 exceeds the maximum supported by the DBMS. This maximum value is indicated in %2.    It is necessary to reduce the amount of column for this index in order to solve the problem. |
|  | |
| **rgz0025** | ****Initial value %1 for attribute %2 does not have the correct Data Type or is out of range.**** |
|  | The value %1 of the Initial value property for attribute %2 does not match the attribute's data type or is out of range. The Initial value property value must be:  * A string delimited with single or double quotes for Character, Varchar or Long Varchar attributes. For example: "My initial value" or "My initial value." * A numeric value for numeric attributes. For example: 1234, 1.23, -10. * A date value in YYYY-MM-DD format for Date attributes. * A DateTime value in YYYY-MM-DD HH-MI-SS format for DateTime attributes. |
|  | |
| **rgz0028** | ****Data type, length or decimal places of %1 are not valid for an autonumbered attribute.**** |
|  | Attributes with the Autonumber property set must be Numeric without Decimal places and when Access is the DBMS the length should be between 5 and 9. |
|  | |
| **rgz0029** | ****Reorganization may fail if table %1 has records and the key value %2 does not exist in table %3.**** |
|  | A new not null referential integrity constraint has been created from table %1 to table %3. If table %1 has records and the value for the referenced key (%2) does not exist in table %3, the reorganization will fail.    Note: This kind of reorganization can be accomplished as from GeneXus X. See [rgo0002](https://wiki.genexus.com/commwiki/wiki?5965) for further details. |
|  | |
| **rgz0030** | ****Reorganization may fail if there are records with duplicate initial values for just new attributes (%1) in unique index %2**** |
|  | A unique index is being created, which is made up of new attributes only. If the table has records and the %1's Initial Value property does not guarantee a different value for each record, the reorganization will fail. |
|  | |
| **rgz0031** | **Formula %1 cannot be made redundant in table %2.** |
|  | Formula attributes cannot be defined as redundant in Transactions where they are inferred. Only in the Transaction(Table) where the formula is defined can be redundant. |
|  | |
| **rgz0032** | **Name conflict between attribute ''%2'' and ''%1''´s URI field.** |
|  | %1 is a multimedia attribute, such as an [image](https://wiki.genexus.com/commwiki/wiki?15204) attribute. Ande the name of this attribute URI Field, conflict with the name of attribute %2 and they are both in the same table. |
|  | |
| **rgz0033** | **Cannot convert to/from multitenant KB with pending impact.** |
|  | This message indicates that it is not able to convert a KB from no-multitenant to multitenant or vice versa if there is a pending impact. The conversion only is performed if there is no previous impact pending. |
|  | |
| **rgz0034** | **Invalid %1 index ''%2''. Attribute(s) %3 not found in table %4.** |
|  | In some cases, user-defined indices could reference an attribute that does not belong to the table anymore. This message warns you about this situation.   %1 refers to the index type (duplicate, unique), %2 is the index name. |
|  | |
| **rgz0035** | **Table %1 is associated to more than one Data View (%2).** |
|  | Two or more data views (%2) with the same associated table (%1) is not allowed. In this case, when impacting the database, the rgz0035 error is given (since X Evolution 2 Upgrade 3). |
|  | |
| **rgz0036** | **Cannot solve attributes %1%2.** |
|  | This message indicates for a Transaction which its property Used To = Retrieve data, that it was not able to solve the load of certain attributes. |
|  | |
| **rgz0037** | **View would be empty.** |
|  | This message indicates for a Transaction which its property Used To = Retrieve data, that it was not able to obtain a navigation for the associated view. |
|  | |
| **rgz0038** | **Cannot use variable %1%2.** |
|  | This message indicates for a Transaction which its property Used To = Retrieve data and whose associated Data Provider receives parameters, that variables can't be used either in the Parm rule nor the source. |
|  | |
| **rgz0040** | **Cannot use non-key attributes %1 in parm rule.** |
|  | This message indicates for a Transaction which its property Used To = Retrieve data and whose associated Data Provider receives parameters, that attributes that are not part of the dynamic transaction primary key can't be declared in the Parm rule. |
|  | |
| **rgz0041** | **The foreign key constraint to table %1(%2) cannot be enforced in this version of %3.** |
|  | This message would appear for a Transaction which its property Used To = Retrieve data. As for VIEWS, there is no referential integrity, GeneXus creates SQL triggers that check the referential integrity. For SAP HANA v1.0 it is not possible to create these triggers and this message informs that. |
|  | |
| **rgz0042** | **Attribute ''%1'' is a parameter, it should only be assigned to itself%2.** |
|  | This message indicates for a Transaction which its property Used To = Retrieve data and whose associated Data Provider receives parameters, that an attribute that is received in the Parm rule has been assigned a value that is different than itself. |
|  | |
| **rgz0043** | **Table %1 associated to dynamic transaction %2 cannot have parallel transactions (%3).** |
|  | This message indicates that a Transaction with the property Used To = Retrieve data has been defined, but its key is the same as the key of another transaction in the KB. A [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062) can't be defined as a parallel transaction, so this message is informing the wrong definition. |
|  | |
| **rgz0044** | **Table %1 definition exceeds maximum allowed size (%2).** |
|  | This error indicates that the sum of weights of the fields that make up a table exceeds the limit defined by the DBMS. It can occur in DB2 for iSeries, MySQL and Informix. To solve this, the length of Char / VarChar type fields must be reduced in such a way that the sum of the lengths of all the fields does not exceed the limit. |
|  | |
| **rgz0045** | **Invalid %1 index "%2". Attribute %3's type (%4) cannot be part of an index.** |
|  | This error indicates that there is an invalid index because the data type of an attribute that is part of it is not supported by the indexes for that DBMS. For example, an index whose composition contains a LongVarChar attribute is not accepted by any DBMS except Postgre. |
|  |  |
| **rgz0046** | **'%1' %2 is not supported in dynamic transaction %3 and cannot be applied %4.** |
|  | The following clauses of the [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) do not apply when it is used to load a [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062):   Default, Skip, Count, One, Input.  This error warns you about this situation. |
|  |  |
| **rgz0047** | **Unsupported DBMS (%1)%2** |
|  | Not all DBMSs have the support to create Dynamic Transactions. Some DBMSs even support the creation of VIEWS ([Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062)), but not FUNCTIONS ([Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732)).  This error indicates that certain DBMS does not have the support to create [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) or [Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732).  %1 indicates the DBMS (Informix, MySQL, SAP Hana).  %2 display additional information if it is necessary ("for parameterized dynamic transaction").     Example: rgz0047 Unsupported DBMS (MySQL) for parameterized dynamic transaction.  It occurs in the following cases:   * For any Dynamic Transaction (FUNCTIONS, VIEWS) - When using Informix or MySQL (version lower than 5.7.7). * For Dynamic Transactions (FUNCTIONS) - When using MySQL (5.7.7 or higher) or SAP Hana. |

## [See also](#See+also)

[Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965)


|  |
| --- |
| **Backlinks** |
| [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) |

---
