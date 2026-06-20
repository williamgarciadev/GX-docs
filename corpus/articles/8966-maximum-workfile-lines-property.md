---
title: "Maximum workFile lines property"
source_id: 8966
source_url: https://wiki.genexus.com/commwiki/wiki?8966
genexus_version: "18"
---

# Maximum workFile lines property

Sets a maximum number of rows per page when this is indeterminate in server paging scenarios.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?49815,,)  
**Level:** Generator

### [Description](#Description)

This property sets a limit to the number of rows in [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) scenarios when the number of rows is unlimited(\*).

#### [Values:](#Values%3A)

Any positive integer  
  
**Default Value =** 10000

(\*) The number of rows is defined by the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) or the Count clause in a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) or a [Data Provider](https://wiki.genexus.com/commwiki/wiki?25410).

#### [Notes:](#Notes%3A)

* The maximum number in iSeries is 9,999 lines, in any case.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.
