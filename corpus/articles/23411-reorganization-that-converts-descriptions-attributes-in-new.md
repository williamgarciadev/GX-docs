---
title: "Reorganization that converts descriptions attributes in new tables"
source_id: 23411
source_url: https://wiki.genexus.com/commwiki/wiki?23411
genexus_version: "18"
---

# Reorganization that converts descriptions attributes in new tables

Sample

Suppose you have the following transaction

```
Client
{
   ClientId*
   ClientName
   CountryName
}
```

And the corresponing table has these records

`[imagen omitida: wiki id 23412]`

The reorganization consists in creating a new transaction Country, and adding the Foreign Key CountryId to the Client Transaction:

```
Client
{
   ClientId*
   ClientName
   CountryId
   CountryName
}

Country
{
   CountryId*
   CountryName
}
```

After running this reorganization,  the table Country is loaded with the country names referenced in table Client, and in the Client Table, the corresponding CountryId is added:

|  |  |
| --- | --- |
| Client | Country |
|  |  |

### [Availability](#Availability)

This feature is available as of GeneXus Tilo Beta 1.
