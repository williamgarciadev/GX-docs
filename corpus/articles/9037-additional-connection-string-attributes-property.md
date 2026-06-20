---
title: "Additional connection string attributes property"
source_id: 9037
source_url: https://wiki.genexus.com/commwiki/wiki?9037
genexus_version: "18"
---

# Additional connection string attributes property

Adds to the connection string the parameters needed by the user.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)  
**Level:** [Data Store](https://wiki.genexus.com/commwiki/wiki?7117)

### [Description](#Description)

There is no default value for this property.

For more information on the attributes supported by the driver used, their meaning, and their values, please refer to the following specific links for each DBMS:

* For SQL Server, see the list of available values in [this link](https://learn.microsoft.com/en-us/dotnet/api/microsoft.data.sqlclient.sqlconnection.connectionstring?view=sqlclient-dotnet-standard-5.1).
* For Oracle, a list of values can be found in [this link](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4437990943.html#ADO.NET-Connection-Options).
* If you use DB2, you can see the available options in [this link](https://www.ibm.com/docs/en/db2/10.5?topic=properties-connectionstring).

In addition, SQL Server supports authentication with AD (Active Directory) in the Azure SQL database.

Authentication methods can be as follows:

1. Active Directory Password
2. Active Directory Integrated
3. Active Directory Interactive
4. Active Directory Service Principal
5. Active Directory Device Code Flow
6. Active Directory Managed Identity
7. Active Directory MSI
8. Active Directory Default

Note that you can add attributes found in the linked page table, as long as they do not conflict with the properties previously specified for the DBMS in GeneXus.

Avoid duplicates or values that may cause configuration problems.

Also, keep in mind that attributes must be separated by semicolons.

### [Samples](#Samples)

If you want to use the "Active Directory Password" authentication method in Azure SQL, the property value must be similar to the following:

Server=demo.database.windows.net; Authentication=Active Directory Password; Encrypt=True; Database=testdb; User Id=user@domain.com; Password=\*\*\*

With SQL Server, the Additional connection string attributes could be:  
  
Encrypt=true;Max Pool Size=40  
  
These attributes are separated by semicolons and allow you to customize the connection according to your specific needs.  
  
However, remember not to include "database=bd\_name" in the connection string. For example, this would be incorrect:  
  
Encrypt=true;Max Pool Size=40;database=bd\_name

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[HowTo: Configure the maximum pool size for ADO.NET](https://wiki.genexus.com/commwiki/wiki?28586,,)


|  |
| --- |
| **Backlinks** |
| [Additional connection string attributes property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55988) | [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330) | [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) |
|
|

---
