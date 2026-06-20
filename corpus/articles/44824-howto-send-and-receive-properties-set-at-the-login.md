---
title: "HowTo: Send and receive properties set at the login"
source_id: 44824
source_url: https://wiki.genexus.com/commwiki/wiki?44824
genexus_version: "18"
---

# HowTo: Send and receive properties set at the login

At user login, it is possible to add user-related properties such as the company branch where the user works.

These properties are called "initial properties" and may be saved in the GAMSession to be retrieved and used later, regardless of the GAM Authentication Type used.

The use of these properties is recommended for the following cases:

* In [Local Authentication Type](https://wiki.genexus.com/commwiki/wiki?20703), [Remote Rest Authentication type (OAuth 2.0)](https://wiki.genexus.com/commwiki/wiki?44833) or any other authentication type, it is possible to save user-related data at the user's login (for example, the company branch the user tries to access). Upon a successful login, the Repository\_Login [event](https://wiki.genexus.com/commwiki/wiki?32698) is triggered, with the procedure subscribed to this event obtaining that information from the GAMSession, to verify the access for that company-branch. Otherwise, the login may be cancelled (see [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) - Example III).  
  In such case, apart from the benefits of cancelling the login, the information is persisted in the GAM database and cached. This is particularly useful for Mobile apps.
* In the case of a login with an Identity Provider ([GAMRemote Authentication](https://wiki.genexus.com/commwiki/wiki?25355)), the initial properties may be sent from the local login to the Identity Provider (IDP), and viceversa (the properties may be set at the Identity Provider's and sent to the client as well).  
  A case for using initial properties could be setting the language in which the user prefers the Identity Provider's login panel. When the user selects the language at the client's login, you can then use an initial property to save the language in the GAMSession. That information may be retrieved at the Identity Provider's, to show the panel in the language selected by the user.
* When GAMRemote Authentication Type is used at the client, and the Identity Provider uses any type of [External Authentication](https://wiki.genexus.com/commwiki/wiki?21755) ([Custom Authentication](https://wiki.genexus.com/commwiki/wiki?21751) or [External Web Services Authentication](https://wiki.genexus.com/commwiki/wiki?16512)), you can set additional parameters for the authentication Procedure (or web service) reading the initial properties set at the client login. The initial properties should then be retrieved at the IDP, and used to call the login. See [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752).

Note that the concept of initial properties is different from the [extended user attributes](https://wiki.genexus.com/commwiki/wiki?19634).  Initial properties relate to a user in the login and they are saved in the GAMSession and cached.  
It's also different from the SetApplication data and [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575) (1).

The initial properties may be retrieved from the GAM session using the method below:

```
GAMSession.InitialProperties
```

### [Samples](#Samples)

**For Web**

Notice the GAMExamplelogin object (of the [Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)) where the login is executed (Enter event).   
The initial properties are loaded into a variable of the GAMProperty data type and added to the properties collection of the GAMLoginAdditionalParameters -parameter of the login method.

```
&CustomProperty = new()  //&CustomProperty is GAMProperty data type
&CustomProperty.Id        = "branch"
&CustomProperty.Value    = "120"
&AdditionalParameter.Properties.Add(&CustomProperty) //&AdditionalParameter is GAMLoginAdditionalParameters data type
//These properties are saved in the session when the user authenticates
&AdditionalParameter.AuthenticationTypeName = &LogOnTo  //GAM Remote Rest
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
```

The code above must be added in the event that corresponds to the login, which will depend on the Authentication Type used. For example, in the case of the GAM Remote Authentication type, it must be added in the 'SelectAuthenticationType' event of the GAMexamplelogin panel.

**For Mobile**

In this case, the properties are assigned to a collection of LoginExternalAdditionalParameters data type.

```
Event 'LoginGAMLocal'
Composite
     &LoginExternalAdditionalParameters = new()
      &LoginExternalAdditionalParameters.AuthenticationTypeName = !"local"
      &LoginExternalAdditionalParameters.Repository = !"85a3006c-0606-41d2-980e-223f88463ec2"
      &LoginExternalAdditionalParametersProperty = new()
      &LoginExternalAdditionalParametersProperty.Id = !"branch"
      &LoginExternalAdditionalParametersProperty.Value = !"22-sd"
      &LoginExternalAdditionalParameters.Properties.Add(&LoginExternalAdditionalParametersProperty)
      &LoginExternalAdditionalParametersProperty = new()
      &LoginExternalAdditionalParametersProperty.Id = !"job"
      &LoginExternalAdditionalParametersProperty.Value = !"12-sd"
      &LoginExternalAdditionalParameters.Properties.Add(&LoginExternalAdditionalParametersProperty)
      GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.GAMLocal, &User, &Password, &LoginExternalAdditionalParameters)
      Return
EndComposite
Endevent
```

In all cases, initial properties may then be retrieved from the GAM session, using the following method:

```
GAMSession.InitialProperties
```

### [Where to retrieve the information](#Where+to+retrieve+the+information)

Initial properties may be retrieved using the Repository\_Login [subscription event](https://wiki.genexus.com/commwiki/wiki?32698). In the case of GAM Remote Authentication and Remote Rest Authentication type (OAuth 2.0), it can be the Repository\_Login event at the Identity Provider and at the client.  
In all cases, the initial properties are obtained using the GAMSession.InitialProperties method.

Note the following example code, which belongs to a procedure subscribed to the Repository\_Login event.

```
Parm(in:&EventName, in:&jsonIN, out:&jsonOUT);

do case
    case &EventName = GAMEvents.Repository_Login
        &GAMSession.FromJsonString(&jsonIN)
        for &GAMProperty in &GAMSession.InitialProperties
              /////
        endfor
........................
endcase
```

### [GAM Configuration in the case of GAM Remote Authentication type](#GAM+Configuration+in+the+case+of+GAM+Remote+Authentication+type)

In the case of GAMRemote Authentication Type, the properties may be retrieved in the GAMRemoteLogin object using the method below:

```
GAMRepository.GetGAMRemoteInitialProperties(&IDP_State)
```

For example, this may be the code in the Enter Event of the GAMRemoteLogin object:

```
&GAMProperties = GAMRepository.GetGAMRemoteInitialProperties(&IDP_State)
&AdditionalParameter.Properties = &GAMProperties
//Here you can add new properties if you want:
&GAMProperty = new()
&GAMProperty.Id = "section"
&GAMProperty.Value = "98"
&AdditionalParameter.Properties.Add(&GAMProperty)    
&AdditionalParameter.AuthenticationTypeName = &LogOnTo
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
```

In this example, note that the initial properties set at the client login were retrieved, and more initial properties were added as well.

**1.** At the client, you must configure that it will receive the initial properties from the server. Using the Web Backoffice in the Authentication Type's entry panel (GAMWCAuthenticationTypeEntryGeneral), you must check the "Add gam\_session\_initial\_prop scope?" option. See [Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039).

The corresponding code is as follows:

```
&AuthenticationTypeGAMRemote.GAMRemote.AddSessionInitialPropertiesScope = TRUE
```

**2.** In the Identity Provider's Application configuration, you must enable the Application for it to send the initial properties to clients. Using the Web Backoffice, you must check the  "Can get session initial properties?" option in the Application. See [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038).

The code is the following:

```
&GAMApplication.ClientAllowGetSessionInitialProperties = TRUE
```

### [GAM Configuration in the case of GAM Remote Rest Authentication type](#GAM+Configuration+in+the+case+of+GAM+Remote+Rest+Authentication+type)

In the case of Remote Rest Authentication type (OAuth 2.0), the properties may be received at the server, but no more properties may be added there (as it happens with GAM Remote Authentication).   
The following properties are for receiving, at the client, the same properties that were set at the client before the login (they are sent to the server and then sent to the client again, if the following properties are activated).

**1.** At the client, you must configure that it will receive the initial properties from the server. Using the Web Backoffice, you must check the "Add gam\_session\_initial\_prop scope?" option. See [Client side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44841).

The code is as follows:

```
&AuthenticationTypeGAMRemoteRest.GAMRemoteRest.AddSessionInitialPropertiesScope = TRUE
```

**2.** At the Identity Provider's Application configuration, you must enable the Application to send the initial properties to the clients. Using the Web Backoffice, you must check the  "Can get session initial properties?" option. See [Server side configuration for GAMRemoteREST Authentication type](https://wiki.genexus.com/commwiki/wiki?44840).

The code is as follows:

```
&GAMApplication.ClientAllowGetSessionInitialPropertiesRest    = TRUE
```

**Note**: Using Custom Authentication Type or External Web Services Authentication Type, you can also consider the following solution: [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752).

(1)There's a difference between the "initial properties" concept and SetApplication data and [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575). Both are used to save data associated with the user's session, but the initial properties may be recorded only at the time of login; and they may not be changed afterwards. These are also structure-predefined by ID-Token-Value (GAMProperty).  
The ApplicationData may be recorded n times during a user's session. The developer defines an SDT for his needs and sends, to the SetApplicationData, an &SDT.ToJSon() parameter, with a free style structure.

### [Availability](#Availability)

Since [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,)


|  |
| --- |
| **Backlinks** |
| [Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57067) | [Client side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57064) | [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603) |
| [GAM - OAuth User Scopes (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55820) | [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Server side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57068) |

---
