---
title: "Reorganization message rgo0002"
source_id: 6272
source_url: https://wiki.genexus.com/commwiki/wiki?6272
genexus_version: "18"
---

# Reorganization message rgo0002

|  |  |
| --- | --- |
| rgo0002 | Table %1 is referenced by table %2 and at least one attribute in its foreign key (%3) does not allow nulls. A default record will be added if table %2 has records and a record with default values does not exist in table %1. |

This reorganization allows adding a new not null foreign key that references an existing table, and also adds the default record in it if necessary.

Example:

|  |  |
| --- | --- |
| Trn Cient  ClientCode\*  ClientName | Trn Country  CountryId\*  CountryName |
|  |  |

The reorganization consists in adding the CountryCode attribute to the Client Transaction:

Trn Cient  
ClientCode\*  
ClientName  
CountryCode –> not null and with initial value = 1

The Impact Analysis report is as follows:

`[imagen omitida: wiki id 6275]`

If the Country table didn't have a record with key = 1, this reorganization would add the record Key = 1 to the Country table, because the Client Table has some records. In this case, the resulting table status would be like this:

`[imagen omitida: wiki id 6277]`

`[imagen omitida: wiki id 6279]`

Note that a new Country (CountryCod = 1) was inserted in the Country Table. Also, CountryName was left empty as the attribute's Initial Value property had not been defined.

#### Compatibility Section

In GeneXus 9.0, if the Client table is not empty, and if the Country Table doesn’t have a record with code 1, the reorganization fails. In fact, the rgz0029 runtime control is given at specification time, like the following one:

`[imagen omitida: wiki id 6276]`


|  |
| --- |
| **Backlinks** |
| [Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965) |

---
