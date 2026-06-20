---
title: "How to specify an object list in a MSBuild task"
source_id: 44328
source_url: https://wiki.genexus.com/commwiki/wiki?44328
genexus_version: "18"
---

# How to specify an object list in a MSBuild task

This article shows how to write an object list in a MSBuild task.

Syntax:  /p:ObjectNames="[ObjectType:]ObjectName 1,...,ObjectName N[;...;[<ObjectType:]ObjectName M,...,ObjectName R>]"

where

* Object names should be fully qualified
* Possible values for object types:  Procedure, Transaction, WebPanel, ExternalObject, DeploymentUnit, DataProvider, API

### [Sample](#Sample)

```
/p:ObjectNames="Object1;Module1.Object2;Transaction:Module3.Object1,Module3.Object2;DeploymentUnit:Object4"
```

## [See Also](#See+Also)

* [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908)
* [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073)


|  |
| --- |
| **Backlinks** |
| [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073) | [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877) |

---
