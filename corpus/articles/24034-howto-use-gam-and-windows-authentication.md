---
title: "HowTo: Use GAM and Windows Authentication"
source_id: 24034
source_url: https://wiki.genexus.com/commwiki/wiki?24034
genexus_version: "18"
---

# HowTo: Use GAM and Windows Authentication

**Warning**: This sample shows how to configure GAM to work with Windows Authentication. GeneXus does not support the configuration of these external systems. Samples, screenshots, parameters, and/or locations may change over time.

Consider a scenario where a
[.NET](https://wiki.genexus.com/commwiki/wiki?38604) Web application authenticates using IIS [Windows Authentication](http://en.wikipedia.org/wiki/Integrated_Windows_Authentication), but [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) has to be used to manage the entire security of the application.  
  
In this scenario, since GAM does not support Windows Authentication, it can delegate the authentication to IIS and solve the security concerns of the application after the user has logged in successfully (which means that IIS recognizes the user logged into Windows).  
  
The main goal of this feature is to allow the user to access the web application using his or her Windows credentials without the need to enter the credentials in a dialog box.  
  
These are the steps to follow:

### [Step 1](#Step+1)

The condition is that the virtual directory in IIS web server allows Windows Authentication (it is enabled). Besides, consider [SAC #11464](https://www.genexus.com/en/developers/websac?data=11464;;).

### [Step 2](#Step+2)

In GeneXus, the solution consists of implementing [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751), where in this case the Procedure will get the information of the user who is logged into the application and return this information to GAM. This is a GeneXus Procedure that implements the authentication.

In this example, a custom authentication external service version 1.0 is implemented using the guide in [GAM External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) link.

The Procedure which implements the authentication looks as follows (named "gamwslogin" in this example):

```
Parm( in:&GAMWSLoginInStr ,out:&GAMWSLoginOutStr ); //&GAMWSLoginInStr and &GAMWSLoginOutStr are varchar(256)

&GAMWSLoginIn.FromJson(&GAMWSLoginInStr) //&GAMWSLogin is GAMWSLogin SDT data type
&UserLogin = &GAMWSLoginIn.GAMUsrLogin
if not &UserLogin.IsEmpty() //If there is no error, load the out parameters of the authentication Procedure.
   &GAMWSLoginOut             = New GAMWSLoginOutSDT()
   &GAMWSLoginOut.WSVersion   = !"1."
   &GAMWSLoginOut.User        = New GAMWSLoginOutUserSDT()

   &GAMWSLoginOut.WSStatus          = 1 //Success
   &GAMWSLoginOut.User.Code         = &UserLogin

else
   &GAMWSLoginOut.WSStatus = 2 //User unknown
endif

&GAMWSLoginOutStr = &GAMWSLoginOut.ToJson()
```

**Note**: The data type of &GAMWSLoginOut is GAMWSLoginOut SDT, which is available [here](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16927,,).

### [Step 3](#Step+3)

Suppose the name of the GAM custom authentication type is "Windows Authentication".

##### Figure 1. Definition of the Custom Authentication type, which is implemented by "gamwslogin" GeneXus Procedure.

Using [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) configure the following:

* [GAM Repository: Default Authentication Type property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17669,,) = "Windows Authentication"
* [User Identification](https://wiki.genexus.com/commwiki/wiki?21030) = name
* Required Email = No
* Required Password = No
* User Email is unique = No

##### Figure 2. Repository settings. General Tab

##### Figure 3. Repository settings. Users Tab

### [Step 4](#Step+4)

The behavior of the [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) and Web Transactions which have [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authentication / Authorization, is that when they execute and there is no valid user session, the object specified in [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590) (GAMExampleLogin Web Panel) is launched.

Then you need to program the Start Event of this object so that the GAMRepository.Login method is executed before showing any screens.

In this case, the login method calls the external authentication Procedure, which returns the user given by [UserId function](https://wiki.genexus.com/commwiki/wiki?8518), and GAM creates a session for that user.

Below is the code of the Login object. Note that you execute the GAMRepository.Login method, and when the operation is successful, there is a redirect to the web object which had thrown the user session invalid exception.

```
Start Event
    ........................
    &UserName = userid() //Get the user login using the [[UserId Function]].
    &LoginOK = GAMRepository.Login(&UserName, "", &AdditionalParameter, &Errors ) //Login using external Procedure which is called automatically.
    If &LoginOK
       &URL = GAMRepository.GetLastErrorsURL()
       If &URL.IsEmpty()
          Home()
       Else
          Link(&URL) //return and continue with the flow of the application.
       Endif
    Else
       If &Errors.Count > 0
          ........................
       Endif
    EndIf
  
EndEvent
```

The first time the user executes the application, GAM registers it in the GAM User table. This registration is done automatically (see [GAM - Registration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?19913,,) for more information).

Since then, each time the web session expires, the login is performed again, but a different session is given to the user.

Download the sample [here](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24041,,). The xpz file contains the Procedure which implements the authentication (gamwslogin) and all the SDTs needed. Besides, it contains a SampleLogin Web Panel which should be configured as [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590).

### [See Also](#See+Also)

[UserId function](https://wiki.genexus.com/commwiki/wiki?8518)  
[GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
