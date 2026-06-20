---
title: "GetApplicationData and SetApplicationData method of GAMSession object"
source_id: 21575
source_url: https://wiki.genexus.com/commwiki/wiki?21575
genexus_version: "18"
---

# GetApplicationData and SetApplicationData method of GAMSession object

Gets the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) session data which resides in database, and has been saved there using SetApplicationData method of GAMSession object.

### [Syntax](#Syntax)

GAMSession**.GetApplicationData()**: String

GAMSession.**SetApplicationData(**ApplicationData: LongVarchar, Errors: Collection<GAMError,GeneXusSecurity>**)**: Boolean

### [Description](#Description)

In some cases, there's the need to save additional information for the current user in the GAM session in addition to the default information that is saved when the user logs in. Specially in the case of applications which run under a load balancing architecture, when the web session cannot be shared among the nodes of the application server.

In these cases, it's useful to store the additional information you need to save for the user session in the GAM database, using SetApplicationData method of GAMSession object, and retrieve that information using GetApplicationData method of GAMSession.

Another use of GetApplicationData method is to retrieve information sent from an external authentication program, see [External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) (section 4) for more details.

The SetApplicationData method allows saving temporary information in the GAM Session, stores in the database and it’s related to the Token that the User has, can be used as a global variable of the application, and then can be read by other applications, allows sharing information about the session with other applications under the same session.

### [See Also](#See+Also)

[GAM - External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755)


|  |
| --- |
| **Backlinks** |
| [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603) | [HowTo: LDAP Authentication using GAM](https://wiki.genexus.com/commwiki/wiki?29474) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) |

---
