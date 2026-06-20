---
title: "Login Object for Web property"
source_id: 15590
source_url: https://wiki.genexus.com/commwiki/wiki?15590
genexus_version: "18"
---

# Login Object for Web property

Specifies the Login Web Panel to be used when GAM is enabled.

### [Scope](#Scope)

**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

When [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) [is enabled](https://wiki.genexus.com/commwiki/wiki?19946) in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), security mechanisms are automatically imported.

The Login Object for Web property allows specifying a web object that will be called automatically when user authentication is needed (the security mechanism will behave as specified in the security policies in the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568)).

So, when the web session expires or does not exist, and the page needs authentication, the web object indicated in this property is displayed to let the user enter his/her credentials.

By default, the property is set with the GAMExampleLogin web object (imported into the KB when the Enable Integrated Security property is set to Yes).

The object referenced must have its [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) set to "None". In addition, it must use the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) to check the user credentials and keep the session active, taking into account the security policies specified for the user in the GAM repository.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [See Also](#See+Also)

[Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589)  
[Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706)


|  |
| --- |
| **Backlinks** |
| [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) | [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) |
| [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) | [GAM - Activation Process](https://wiki.genexus.com/commwiki/wiki?21973) | [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) |
| [GAM use Example: Private web application](https://wiki.genexus.com/commwiki/wiki?15923) | [GAM Use Example: Public Application With Some Private Components](https://wiki.genexus.com/commwiki/wiki?15772) | [GXflow Custom Client with GAM](https://wiki.genexus.com/commwiki/wiki?29533) | [HowTo: Have an SSO behavior by using SAML Authentication](https://wiki.genexus.com/commwiki/wiki?44887) |
| [HowTo: Setup Single Sign On between GeneXus and SAP Cloud Platform Fiori Application using SAML](https://wiki.genexus.com/commwiki/wiki?43404) | [HowTo: Use GAM and Windows Authentication](https://wiki.genexus.com/commwiki/wiki?24034) | [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) | [Integrated Security Level property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54226) |
| [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) | [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) | [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) | [User Remember Me Timeout](https://wiki.genexus.com/commwiki/wiki?18586) |
| [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) |

---
