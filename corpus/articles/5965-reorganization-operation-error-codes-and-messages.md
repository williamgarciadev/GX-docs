---
title: "Reorganization Operation Error Codes and messages"
source_id: 5965
source_url: https://wiki.genexus.com/commwiki/wiki?5965
genexus_version: "18"
---

# Reorganization Operation Error Codes and messages

The following list shows all the **rgo** messages that can appear in the [Impact Analysis](https://wiki.genexus.com/commwiki/wiki?31023).

The differences with [rgz messages](https://wiki.genexus.com/commwiki/wiki?5952) is that in this case, they warn you that some data needs to be added into the database in order to accomplish the reorganization successfully.

| Code | Message |
| --- | --- |
|  | |
| **rgo0001** | **This table is referenced by table %1 and at least one attribute in its foreign key ( %2) does not allow nulls. The table will be initialized with a default record if table (%1) has records.** |
|  | This reorganization allows you to add a new table and a foreign key (%2) to it, in an existing not empty one (%1).  As the new column (foreign key) does not accept nulls in the existing table, it must be initialized with some value. Besides, to avoid a referential integrity error during the reorganization that value must belong to the new table.  So, in this case, the reorganization will perform the following actions when the existing table has records:   * Create the new table. * Insert a new record in that table. The key's value is taken from the foreign key's Initial Value property. * Add the Foreign key to the existing table. The Initial Value property will be considered as the default value.   Look at an example [here](https://wiki.genexus.com/commwiki/wiki?5228) |
|  | | | |
| **rgo0002** | **Table %1 is referenced by table %2 and at least one attribute in its foreign key (%3) does not allow nulls. A default record will be added if table %2 has records and a record with default values does not exist in table %1.** |
|  | This reorganization allows adding a new not null foreign key that references an existing table.  Adding a not null foreign key that references an existing table could fail due to a referential integrity control if %2 already has records and the initial value of %3 does not exist in %1.  In order to accomplish this reorganization GeneXus will perform the following actions:   * Add the foreign key attribute to Table %2. The 'Initial Value' property will be considered as the default value. * If the initial value of %3 (empty value by default) does not exist in %1, a new record is inserted with that key. The rest of %1’s secondary attributes will be initialized with their default values. This means that the ‘Initial Value’ property is considered for each attribute, and for those attributes whose property is not set or the initial value cannot be evaluated by the DBMS, the empty value will be considered.   Look at an example [here](https://wiki.genexus.com/commwiki/wiki?6272) |
|  | | | |
| **rgo0003** | **Table %1 is referenced by table %2 and at least one attribute in its foreign key (%3) does not allow nulls. A default record will be added in table %1 if table %4 has records and a record with default values does not exist in table %1.** |
|  | This reorganization allows adding a new not null foreign key that references an existing table and in this table exists also a foreign to another table. This warning will never appear alone, it must appear with a rgo0001 or a rgo0002.  Scope note: Implemented in GXXU4  Look at an example [here](https://wiki.genexus.com/commwiki/wiki?10856) |
|  | | | |
| **rgo0004** | **Foreign key %1 from table %2 to table %3 does no longer support nulls. Null references on existing rows in table %2 will be replaced with default values and, if necessary, default records will be added to table %3.** |
|  | This reorganization allows changing the nullable property of a foreign key attribute from 'Yes' to 'No'. New records will be added in the FK table if after changing the nullable attribute property from yes to no. The value inserted in the table of the FK will be the initial value or the default value if no initial value is set  Scope note: Available since GX X Evolution 1 upgrade #3 |


|  |
| --- |
| **Backlinks** |
| [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Reorganization Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5952) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) |

---
