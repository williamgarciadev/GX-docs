---
title: "API object - Troubleshooting"
source_id: 55436
source_url: https://wiki.genexus.com/commwiki/wiki?55436
genexus_version: "18"
---

# API object - Troubleshooting

### [Troubleshooting permissions in API Object when using Authentication](#Troubleshooting+permissions+in+API+Object+when+using+Authentication)

[Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) present a problem when setting the Authentication value in the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214). If the [[SecurityLevel](https://wiki.genexus.com/commwiki/wiki?55437)(Authorization)] annotation is added to one of the methods to use authentication, the system does not automatically generate the base permissions for the object in the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Database.

### [Solution](#Solution)

There are two solutions to address the problem:

#### [Create the Permission Manually in the GAM](#Create+the+Permission+Manually+in+the+GAM)

One option is to [manually create the required permission](https://wiki.genexus.com/commwiki/wiki?29723) in the GAM Database and then add the [[SecurityPermission](https://wiki.genexus.com/commwiki/wiki?55422)()] and [SecurityLevel(Authorization)] annotations to the corresponding method. This ensures that the user has access to the appropriate authorization to consume the method without problems.

#### [Change the Object to Authorization](#Change+the+Object+to+Authorization)

Another effective alternative is to change the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) to Authorization. Subsequently, the annotations [SecurityLevel(None)] can be added to methods that do not require authorization and [SecurityLevel(Authorization)] to the method that does. When this change is made, the base permissions for the object in the GAM Database are automatically generated. This will allow the appropriate permissions to be assigned to the user attempting to consume the method more easily and avoids potential unauthorized access conflicts.


|  |
| --- |
| **Backlinks** |
| [Toc:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |

---
