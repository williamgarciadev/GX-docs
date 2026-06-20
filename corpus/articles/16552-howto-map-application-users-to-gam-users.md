---
title: "HowTo: Map Application Users to GAM Users"
source_id: 16552
source_url: https://wiki.genexus.com/commwiki/wiki?16552
genexus_version: "18"
---

# HowTo: Map Application Users to GAM Users

For many applications, you may need to decide whether to keep a *User* table in the application's database, or on the other hand, to just have the GAM User table in a GAM database. This document explains how to solve this situation.

### [Situation 1](#Situation+1)

Suppose your application has already been implemented, the *Users*table already exists, and is related to many others. What are the alternatives for using [GAM](https://wiki.genexus.com/commwiki/wiki?14960)?

In general, changing the *Users*table to use other PKs (GAMGUID) is not feasible because there are relations to other tables which have the *UserCode* attribute as a Foreign Key.

For example, imagine you have the *AppUsers* Transaction, and a *TourReservations* Transaction, where *UserCod* is FK, as shown in the following pictures:

`[imagen omitida: wiki id 16553]`

`[imagen omitida: wiki id 16554]`

### [Situation 2](#Situation+2)

Another problem is what to do when you need to store the users' additional information, which is not in the GAM *User* table, and you do not want to use the [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634). That is, you want to store that information in an application's table.

### [Solution](#Solution)

If you keep a *Users* table in the application database, there are two possible alternatives to cope with the problem:

#### [Alternative A (recommended).](#Alternative+A+%28recommended%29.)

See [HowTo: Mapping Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643)

#### [Alternative B.](#Alternative+B.)

See [HowTo: Mapping Application Users to GAM Users - Using ExternalID](https://wiki.genexus.com/commwiki/wiki?16565)

In summary, the decision of keeping the User table in the application's database or having only the GAM User table in the GAM database will depend basically on the requirements of your application.

If you keep the user's information only in the GAM *User* table, each time you need to query the user's additional information (e.g: name), the GAM database has to be accessed using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

On the other hand, if the users are duplicated in the GAM database and the application's database, you need to keep both *User* tables updated.

Parallel with this, in case that you need to add new attributes to the GAM *User* table, the GAM *User* attributes can be extended dynamically in order to meet the needs of the reality you're modeling . See [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634) for more details.

### [See Also](#See+Also)

[GAM API: How to reference GAM users](https://wiki.genexus.com/commwiki/wiki?16534)  
[HowTo: Filtering Data by User Using the GAM API](https://wiki.genexus.com/commwiki/wiki?15387)  
[HowTo: Mapping Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565)  
[HowTo: Mapping Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643)  
[Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643) |
| [HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) |

---
