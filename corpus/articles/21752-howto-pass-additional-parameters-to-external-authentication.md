---
title: "HowTo: Pass additional parameters to external authentication programs using GAM"
source_id: 21752
source_url: https://wiki.genexus.com/commwiki/wiki?21752
genexus_version: "18"
---

# HowTo: Pass additional parameters to external authentication programs using GAM

The purpose of this article is to explain how additional parameters are passed to external authentication programs using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

With [GAM External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755) you can send custom information to the external authentication program, regardless of the external authentication version used, which can be [GAM External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) or [GAM External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555).

You need to load the additional information in a variable based on GAMProperty object collection, and assign it to the "Properties" property of a GAMLoginAdditionalParameters object variable (see figure below). The GAMLoginAdditionalParameters object variable is an input of GAMRepository object Login method, used to log in to web applications.

### [Sample](#Sample)

The following is a sample code of a web login object which uses GAM External Authentication: version 2.0.  
  
Before executing the login (which makes the GAM application call the external authentication program), load an SDT variable (called *&CustomProperty* in the example) with additional information that needs to be sent to the external program which makes the authentication.

The *&CustomProperty* variable is based on GAMProperty object.

The information has to be loaded in a collection of GAMLoginAdditionalParameters object (see the figures below in order to understand the structure of these data types).

```
&CustomProperty.Id  = "Company" //&CustomProperty is based on GAMProperty object
&CustomProperty.Token = "Local"
&CustomProperty.Value = "120"
&AdditionalParameter.Properties.Add(&CustomProperty) //&AdditionalParameter is based on GAMLoginAdditionalParameters
&CustomProperty = new()
&CustomProperty.Id  = "Operation"
&CustomProperty.Token = "Current"
&CustomProperty.Value = "345"
&AdditionalParameter.Properties.Add(&CustomProperty)
&AdditionalParameter.AuthenticationTypeName = &LogOnTo
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
```

`[imagen omitida: wiki id 55355]`

`[imagen omitida: wiki id 55356]`

This information is received (automatically) in the GAMWSLoginInSDT parameter of the web service when using [GAM External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) or in the input parameter of the external program when using [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751).

### [See Also](#See+Also)

[GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548)  
[GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555)


|  |
| --- |
| **Backlinks** |
| [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) | [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) |

---
