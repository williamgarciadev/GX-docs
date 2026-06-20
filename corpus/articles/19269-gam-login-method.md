---
title: "GAM Login Method"
source_id: 19269
source_url: https://wiki.genexus.com/commwiki/wiki?19269
genexus_version: "18"
---

# GAM Login Method

* [GAM Login Method for web applications](#GAM+Login+Method+for+web+applications)
* [GAM Login Method for SD applications](#GAM+Login+Method+for+SD+applications)

+ [Login method](#Login+method)
+ [LoginExternal method](#LoginExternal+method)

* [Related information](#Related+information)
* [See Also](#See+Also)

### [GAM Login Method for web applications](#GAM+Login+Method+for+web+applications)

Take the [GAMExampleLogin object](https://wiki.genexus.com/commwiki/wiki?39427,,) as an example where the GAMRepository Login method is used.  
GAMRepository is an external object which is part of the [GAM](https://wiki.genexus.com/commwiki/wiki?14960) library (a folder where all the GAM External objects reside).

The Login method of the GAMRepository object receives the following parameters:

* UserName (GAMUserIdentificationType)
* Password (GAMDescriptionMedium Type)
* AdditionalParameters (GAMLoginAddittionalParameters type)
* Errors (GAMErrorType)

GAMLoginAdditionalParameters is an external object (which is part of the GAM library also), defined as follows:

`[imagen omitida: wiki id 39730]`

The property AuthenticationTypeName allows you to determine the name of the [Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508) to be used in the login (unless it is a[Local login](https://wiki.genexus.com/commwiki/wiki?20703) where this property can be empty).

```
Event 'login'
     &AdditionalParameter.AuthenticationTypeName = !"Facebook"
     &LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
EndEvent
```

Besides, the Properties collection can be used to send custom properties to the login. See [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752).

GAMLoginAdditionalParameters also has a property named "isBatch" which allows you to check the username and user password, without creating a session, that is, without logging in. See the code below:

```
&AdditionalParameter.AuthenticationTypeName = !"Custom"
&LoginAdditionalParameters.isBatch = TRUE
// Login User
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
If not &LoginOK
// Process Error
EndIf
```

### [GAM Login Method for SD applications](#GAM+Login+Method+for+SD+applications)

For Smart Devices applications, take as an example de GAMSDLogin object.

#### [Login method](#Login+method)

In this case, Local login is performed using the Actions external object, and the login method.

```
Event 'GXLogin'
    Composite
        GeneXus.Common.UI.Progress.ShowWithTitle("Connecting...")
        GeneXus.SD.Actions.Login(&User, &Password)
        GeneXus.Common.UI.Progress.Hide()
        Return
    EndComposite
EndEvent
```

The login method is overloaded, so it can include an extra parameter called &LoginExternalAdditionalParameters.

The LoginExternalAdditionalParameters object is as follows:

`[imagen omitida: wiki id 39418]`

Example:

```
Event 'GXLogin'
    Composite
        GeneXus.Common.UI.Progress.ShowWithTitle("Connecting...")
        &LoginExternalAdditionalParameters.Repository = !"1e89a9ca-bc52-482b-a344-c4cda4a9cc8f"
        GeneXus.SD.Actions.Login(&User, &Password,&LoginExternalAdditionalParameters)
        GeneXus.Common.UI.Progress.Hide()
        Return
    EndComposite
EndEvent
```

In the case of the SD login method, the LoginExternalAdditionalParameters allows to establish the Repository GUID to which to connect to. It's useful when there is more than one [Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) in the connection.gam file on the server. Given a value to the Repository property of the &LoginExternalAdditionalParameters parameter, you can establish the connection to use (any connection in the connection.gam which refers to this Repository GUID).

#### [LoginExternal method](#LoginExternal+method)

When using any Authentication type other than Local, the LoginExternal method should be used.

There you specify the Authentication Type using the GAMAuthenticationTypes domain. The method is overloaded so you can also specify the name of the Authentication Type in case you have more than one equal Authentication Type. You can specify the Repository Id as well.

Including the &LoginExternalAdditionalParameters is optional.

For example, in the case of [GAMRemote Authentication](https://wiki.genexus.com/commwiki/wiki?25355), consider that you have more than one in the Repository:

```
Event 'GAMRemote'
    Composite
        &LoginExternalAdditionalParameters = new()
        &LoginExternalAdditionalParameters.AuthenticationTypeName    = !"my_custom_gam_remote_auth" //Use only when more than one GAMRemote authentication type 
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.GAMRemote, &User, &Password, &LoginExternalAdditionalParameters)
        Return
    EndComposite
Endevent
```

### [Related information](#Related+information)

[GAM Repository: Default Authentication Type property](https://wiki.genexus.com/commwiki/wiki?17669,,)

### [See Also](#See+Also)

[HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824)


|  |
| --- |
| **Backlinks** |
| [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) | [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) |
| [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007) | [GAM - GAMRemoteREST Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) | [GAM - Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013) | [GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) |
| [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) | [Good practices for secure development using GAM](https://wiki.genexus.com/commwiki/wiki?47241) |

---
