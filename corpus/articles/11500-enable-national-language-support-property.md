---
title: "Enable national language support property"
source_id: 11500
source_url: https://wiki.genexus.com/commwiki/wiki?11500
genexus_version: "18"
---

# Enable national language support property

Allows you to insert multi-byte characters in character fields created in the database, in order to represent a greater range of characters. For example, it allows you to insert data in Chinese language.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Does not allow you to insert multi-byte characters in the database. |
| **Yes** | Allows you to insert multi-byte characters in character type fields. This is the default value. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** Iseries, DB2 UDB, MYSQL, ORACLE, SQLSERVER  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Version

### [Description](#Description)

The property must be set at [Version preferences](https://wiki.genexus.com/commwiki/wiki?7860) level and its granularity can be changed at [Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) or [GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221) level.

#### [**Notes**](#Notes)

After settingthe [version level](https://wiki.genexus.com/commwiki/wiki?7860) property, you have to execute **Build > Create Database Tables** and **Build > RebuildAll***.* The Impact Analysis does not take into account the change of this property. It is always necessary to recreate tables and objects.

When changing this property at the attribute level, an Impact Analysis is made.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) and after that execute [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |


|  |
| --- |
| **Backlinks** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) |
| [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297) | [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [GeneXus and Diacritics](https://wiki.genexus.com/commwiki/wiki?24615) | [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371) |
| [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

---
