---
title: "GAM - Main Role of a user"
source_id: 21643
source_url: https://wiki.genexus.com/commwiki/wiki?21643
genexus_version: "18"
---

# GAM - Main Role of a user

A [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) user can have many [Roles](https://wiki.genexus.com/commwiki/wiki?17569) associated and one Main Role.

The Main Role of a user is used to take the Security Policy of this role when the user has no security policy associated to him. See [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) for more details on this topic.

Programmatically, you can set the main role of a user, by the SetMainRoleById method of GAMUser object.

```
&GAMUser.Load(&UserId)
&isOK = &GAMUser.SetMainRoleById(&Id, &Errors) //&Errors is collection of GAMError, &Id is GAMKeyNumLong data type
```

The way to get the main role of a user is by the DefaultRoleId property of GAMUser object:

```
&Id = &GAMUser.DefaultRoleId //&Id is GAMKeyNumLong data type
```

In order to set a role as the main role of a user using [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) click "Set as Main" in the list of roles of the user (as shown in figure 1).

`[imagen omitida: wiki id 52500]`

##### [Figure 1.](#Figure+1.)

**Note:**

When defining a new permission in the Knowledge Base (editing the [Permission Prefix Property](https://wiki.genexus.com/commwiki/wiki?17571) of any object), this permission is assigned to the Main Role of administrator user (see [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215)). This is in order to facilitate prototyping, and it is another purpose of the main role.


|  |
| --- |
| **Backlinks** |
| [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569) | [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) |

---
