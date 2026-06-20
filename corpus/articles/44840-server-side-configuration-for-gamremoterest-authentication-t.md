---
title: "Server side configuration for GAMRemoteREST Authentication type"
source_id: 44840
source_url: https://wiki.genexus.com/commwiki/wiki?44840
genexus_version: "18"
---

# Server side configuration for GAMRemoteREST Authentication type

In [Remote REST Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833), you should consider following some configuration steps at both the GAM of clients and at the Identity Provider's.

Note, here, the server-side configuration.

First define a [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910).

`[imagen omitida: wiki id 57056]`

Note the Remote Authentication tab, set the Client Id and Client secret, which must match those configured at the [client](https://wiki.genexus.com/commwiki/wiki?44841).

The configuration of the Application that applies to GAMRemoteREST authentication type is under section **REST (GAMRemoteREST, SSO REST, MiniApp, API key)**.

* **Authentication request must include user scopes?.**This property forces the Client Application to request at least one user scope when authenticating.

* **Allow REST v2.0 authentication?.**This must be checked to allow authentication to this GAM. When it is not checked, the following error is shown in the client upon an attempt to authenticate with the server: *Remote authentication is not allowed in this application. Please contact the administrator. (GAM230)*
* **Allowed user scopes.** These scopes are the user data that the Client Application can access.The Client Application may request fewer scopes, but never more than those selected in this configuration. To know more details about them follow this [link](https://wiki.genexus.com/commwiki/wiki?55603).
* **Additional user scopes.** Here you can detail more specifically which user scopes to share with the Client Application. To know more details about them follow this [link](https://wiki.genexus.com/commwiki/wiki?55603)
* **Private encryption key.** The call among RESTservices may be encrypted; the same key must be used for the Identity Provider (IDP) and for the client.
* **RepositoryGUID.** Specifies the repository GUID in the IDP. Only required when the IDP GAM is multitenant.

### [See Also](#See+Also)

[Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841)


|  |
| --- |
| **Backlinks** |
| [Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841) | [Client side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57064) |
| [GAM - GAMRemoteREST Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [Server side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57068) |

---
