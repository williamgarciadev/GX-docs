---
title: "HowTo: Create a language selector for the GXflow Client"
source_id: 53727
source_url: https://wiki.genexus.com/commwiki/wiki?53727
genexus_version: "18"
---

# HowTo: Create a language selector for the GXflow Client

This article explains how to create a language selector for the GXflow Client using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350). It can be especially useful if you are using GAM, or a custom login, because the only way a user can select a language for the GXflow Client is at login.

To do this, execute the following code:

```
&ExpirationDate = &Today.AddDays(180)
&OK = SetCookie(WorkflowWebSession.Language, &language, !'/', &ExpirationDate)    

Do Case        
Case &language = !'eng'
    &Ok = SetLanguage(!'English')
    
Case &language = !'spa'
    &Ok = SetLanguage(!'Spanish')
    
Case &language = !'por'
    &Ok = SetLanguage(!'Portuguese')
EndCase
```

Where the data type variables are:

```
&ExpirationDate – Date
&Today – Date
&OK – Numeric
&language – WFLanguage
```

For this code to work, you will need the WebSession domain, which you can obtain from the [Custom Client](https://wiki.genexus.com/commwiki/wiki?48897), and also the previously customized the [GXflow labels](https://wiki.genexus.com/commwiki/wiki?50114).
