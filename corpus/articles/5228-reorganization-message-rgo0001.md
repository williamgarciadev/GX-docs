---
title: "Reorganization Message rgo0001"
source_id: 5228
source_url: https://wiki.genexus.com/commwiki/wiki?5228
genexus_version: "18"
---

# Reorganization Message rgo0001

|  |  |
| --- | --- |
| **rgo0001** | This table is referenced by table (%1) and at least one attribute in its foreign key ( %2) does not allow nulls. The table will be initialized with a default record if table (%1) has records. |

This reorganization allows you to add a new table, with a foreign key in it, into an existing table that is not empty. Let's see an example:

Trn Cient  
ClientCode\*  
ClientName

And the reorganization consists of:

1. New Trn Country  
CountryId\*  
CountryName

2. New FK to Country in Table Cient  
ClientCode\*  
ClientName  
CountryId

The Impact Analysis shows:

`[imagen omitida: wiki id 5226]`

`[imagen omitida: wiki id 5225]`

This type of reorganization was not supported in Genexus 9.0 and prior versions, and in fact a rgz0015 runtime control (like the one shown below) was given:

`[imagen omitida: wiki id 5227]`


|  |
| --- |
| **Backlinks** |
| [Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965) |

---
