---
title: "HowTo: Use the same GAM Database by different applications"
source_id: 16151
source_url: https://wiki.genexus.com/commwiki/wiki?16151
genexus_version: "18"
---

# HowTo: Use the same GAM Database by different applications

This document explains how to use the same GAM database by different applications and provides a brief overview about it.

Consider a scenario, where one [GAM](https://wiki.genexus.com/commwiki/wiki?14960) database will be used by different applications.

In deployment time also, for example using GXserver, it will happen that the same GAM database will need to be referenced in each local copy of the knowledge base.

`[imagen omitida: wiki id 16177]`

### [Connecting to an existing external GAM repository from GeneXus](#Connecting+to+an+existing+external+GAM+repository+from+GeneXus)

If you want to connect to an existing repository, and not to create a new one, you need to do the following:

**1.**  Specify the corresponding [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802).

**2.**  In the GAM data store properties you need to specify the corresponding database name, user name and password in order to connect to the database.

**3.**  Specify [Administrator User Name](https://wiki.genexus.com/commwiki/wiki?15215), [Administrator User Password](https://wiki.genexus.com/commwiki/wiki?15216), of this GAM repository you want to connect to.

**4.**  You need to specify also [Connection User Name](https://wiki.genexus.com/commwiki/wiki?15217) and [Connection User Password Property](https://wiki.genexus.com/commwiki/wiki?15218). It´s recommended in case of multiple applications connecting to the same GAM, to create a new [GAM Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) for each application connecting to the same GAM, so each application will use its own GAM connection. So, after you create a new GAM connection, you can configure [Connection User Name Property](https://wiki.genexus.com/commwiki/wiki?15217) and [Connection User Password Property](https://wiki.genexus.com/commwiki/wiki?15218) with the corresponding values.

After following these steps when the "Build All" is done, GeneXus detects that this repository (with the connection properties associated to it) is a valid GAM repository (with a valid GAM repository connection) so there's no need to create a new GAM database, or reorganize this database.

### [See Also](#See+Also)

[GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150)  
[GeneXus Administration of GAM Repository](https://wiki.genexus.com/commwiki/wiki?15769)  
[GAM Repository structure](https://wiki.genexus.com/commwiki/wiki?17568)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [GAM repository management in GeneXus](https://wiki.genexus.com/commwiki/wiki?15769) |

---
