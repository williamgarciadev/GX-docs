---
title: "ShowAllValues property"
source_id: 12555
source_url: https://wiki.genexus.com/commwiki/wiki?12555
genexus_version: "18"
---

# ShowAllValues property

Sets whether the attributes values returned will be all the attribute values from the database or just the values from the joined tables.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Query](https://wiki.genexus.com/commwiki/wiki?9026)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

When the property is in False value (default value), the records from the associated table are shown.  
If you set the value to True, all the records from the master table are shown.

When creating queries using attributes with at least two tables, the values returned correspond to joined tables; this behavior is set using the *ShowAllValues* property.

### [Samples](#Samples)

For example, the following query collects information from *Customers* and related *Invoices*.

`[imagen omitida: wiki id 52796]`

The default result is the following:

`[imagen omitida: wiki id 52797]`

If you want *All values* from the *Customer Name* attribute, you will need to change the *ShowAllValues* property to true in the [query element definition](https://wiki.genexus.com/commwiki/wiki?9026).

`[imagen omitida: wiki id 52798]`

The new result is:

`[imagen omitida: wiki id 52799]`

Notice how in this case all the *Customers* are shown, those with and those without *Invoices*.

**Note:** It makes sense to use this property when selecting attributes from at least two tables.


|  |
| --- |
| **Backlinks** |
| [Category:Query object](https://wiki.genexus.com/commwiki/wiki?9026) |

---
