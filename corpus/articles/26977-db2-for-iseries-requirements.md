---
title: "DB2 for iSeries requirements"
source_id: 26977
source_url: https://wiki.genexus.com/commwiki/wiki?26977
genexus_version: "18"
---

# DB2 for iSeries requirements

In order to use an [iSeries](https://wiki.genexus.com/commwiki/wiki?9296) [environment](https://wiki.genexus.com/commwiki/wiki?7115), check the following prerequisites:

* Make sure the iSeries user has rights to check iSeries catalog tables.
* Make sure the user has access to the following system libraries and that they are part of the System Library List:
  + QSYS
  + QSYS2

These libraries are used during reorganizations when system tables are checked. You can execute the command DSPSYSVAL QSYSLIBL.

### [See Also](#See+Also)

[SAC # 29959](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,29959)  
[Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154)
