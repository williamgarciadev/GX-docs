---
title: "Web Object property"
source_id: 11884
source_url: https://wiki.genexus.com/commwiki/wiki?11884
genexus_version: "18"
---

# Web Object property

Indicates the GeneXus object associated with a Task.

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

This property allows setting the GeneXus object that will be invoked upon executing the [Task](https://wiki.genexus.com/commwiki/wiki?17495).

When associating a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to a Task, take into account that only one record can be modified during the Task execution.

If you navigate through the records with the Transaction object and try to update another Key value, the following error will appear:

```
Please 'Get' data before trying to update it
```

When the Task relevant data is mapped to the Transaction primary key and values are not null; the Transaction is executed using Update mode; otherwise, Insert mode is used.

When the Transaction uses the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) it is expected to use one parameter for each attribute of the Primary Key, with the same name, and an additional Mode parameter. In that way, GXflow client will execute the Transaction assigning those parameters with the relevant data mapped to the primary key.

[More information](https://www.genexus.com/en/developers/websac?data=39718)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).


|  |
| --- |
| **Backlinks** |
| [Model Automation](https://wiki.genexus.com/commwiki/wiki?25115) | [My first BPM Application](https://wiki.genexus.com/commwiki/wiki?11218) |

---
