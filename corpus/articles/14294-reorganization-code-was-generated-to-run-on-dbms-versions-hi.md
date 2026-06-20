---
title: "Reorganization code was generated to run on DBMS versions higher than the current one"
source_id: 14294
source_url: https://wiki.genexus.com/commwiki/wiki?14294
genexus_version: "18"
---

# Reorganization code was generated to run on DBMS versions higher than the current one

Executing a [reorganization](https://wiki.genexus.com/commwiki/wiki?5288) the following error is displayed:

```
Reorganization code was generated to run on DBMS versions higher than the current one
```

An error was found in the database schema verification process. Reorganization code was generated to run on DBMS versions higher than the current one. DBMS should be at least in version 2005 or you may regenerate and rerun the reorganization after changing the corresponding DBMS version property.

The reorganization process was not successfully completed.

**Scope:** SQL Server

**Cause:** generated for SQL Server 2005 is being executed against SQL Server 2000.

**Solution:** Change the value of the ‘SQL Server Version’ data store property from 2005 to 2000 and rerun the reorg.
