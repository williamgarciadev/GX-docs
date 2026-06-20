---
title: "Connection Challenge Expire (minutes)"
source_id: 22023
source_url: https://wiki.genexus.com/commwiki/wiki?22023
genexus_version: "18"
---

# Connection Challenge Expire (minutes)

Connection Challenge Expire is a [GAM Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) property which allows to establish a period of time while the connection to the GAM database is managed in the server's memory. During this period, the database is not accessed for establishing a new connection.

It's a performance feature which favors applications with load balancing that use GAM.

The connection is associated with a "challenge" that is valid for the period indicated as Connection Challenge expire property.

The challenge is valid for each [GAM Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) and is used by all applications that use this connection.

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is as follows:

```
&Connection.ChallengeExpire = &ChallengeExpire //&Connection is GAMRepositoryConnection data type.
```

### [Values](#Values)

Time must be specified in minutes.

0 means that the connection challenge never expires.

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/wiki?18463,,)  
[SAC #34229](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,34229)
