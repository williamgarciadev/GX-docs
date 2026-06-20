---
title: "Autonumber for replication property"
source_id: 7225
source_url: https://wiki.genexus.com/commwiki/wiki?7225
genexus_version: "18"
---

# Autonumber for replication property

Allows specifying what can be done when the table has DBMS replication.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240)

### [Description](#Description)

This property is offered for a key numeric attribute if its [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) is set to True.

#### [Values](#Values)

True: It indicates to the DBMS that it should not apply the property if the table receives replication - it must keep the numbers coming through replication. This is the default value.

False: It does not keep the numbers coming through replication.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798)  
[Autonumber start property](https://wiki.genexus.com/commwiki/wiki?7223)  
[Autonumber step property](https://wiki.genexus.com/commwiki/wiki?7224)


|  |
| --- |
| **Backlinks** |
| [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) | [Autonumber start property](https://wiki.genexus.com/commwiki/wiki?7223) | [Autonumber step property](https://wiki.genexus.com/commwiki/wiki?7224) |

---
