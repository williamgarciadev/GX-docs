---
title: "GAM - External Authentication Type"
source_id: 21755
source_url: https://wiki.genexus.com/commwiki/wiki?21755
genexus_version: "18"
---

# GAM - External Authentication Type

If you need to integrate your application with another in order to exchange information, solving the problem of authentication first is essential.

One solution is that the application you need to integrate exposes a web service SOAP that solves the authentication. In this case, the solution is to use [External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) from the side of the application integrated to [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

Another scenario is that of an external program of the application that solves the authentication issues, which is not necessarily a SOAP service. The solution for that scenario is to configure [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) in the GAM Repository.

In both cases, you need to configure GAM to accept the external program as an identity provider.

Using any of these types of authentication, GAM is not the owner of the user credentials, only the user name and other information, which depends on the external program output will be stored in GAM Repository. Information on roles can also be incorporated in GAM Repository if the external program returns this information in particular.

In case of authenticating to other external services, like LDAP, you can use an external program or web service in order to make a bridge between the GAM application and LDAP.  
See [LDAP authentication using GAM](https://wiki.genexus.com/commwiki/wiki?29473,,).

### [See Also](#See+Also)

[Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) |
| [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575) | [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) | [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) |
| [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) |

---
