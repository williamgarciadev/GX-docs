---
title: "Login Object for SD property"
source_id: 16589
source_url: https://wiki.genexus.com/commwiki/wiki?16589
genexus_version: "18"
---

# Login Object for SD property

Specifies a Login Panel to be used when GAM is enabled.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

When [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) is enabled, Native Mobile applications have security mechanisms automatically incorporated.

When the session token is expired or does not exist, and the application needs authentication, the Login Object specified in this property is displayed to let users enter their credentials.

You can set this property with the name of any [WW](https://wiki.genexus.com/commwiki/wiki?20840) Panel object that uses the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) to check the user credentials and keep the session active, taking into account the security policies specified for this user in the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568).

The security mechanism will behave as specified in the security policies in [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617), and according to what is explained in [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052).

**Note:**The default value for this property is "GAMSDLogin" which is a [WW](https://wiki.genexus.com/commwiki/wiki?20840) object imported into the KB when the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is set to True. In case this property is empty and you do not find the mentioned object in your KB, you can import it from <GeneXusInstallationPath>\Library\GAM\GAM\_Panels-for-SD.xpz   
Besides, this object can be taken as an example for implementing another login object.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214)  
[Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706)  
[Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590)  
[Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215)  
[Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216)  
[Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217)  
[Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) | [GAM - Activation Process](https://wiki.genexus.com/commwiki/wiki?21973) |
| [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) | [HowTo: Configure GXflow Client for Native Mobile from xpz](https://wiki.genexus.com/commwiki/wiki?50551) | [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) |
| [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) | [Integrated Security Level property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54226) | [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) | [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018) |
|

---
