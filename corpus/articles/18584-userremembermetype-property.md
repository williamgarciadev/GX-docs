---
title: "UserRememberMeType property"
source_id: 18584
source_url: https://wiki.genexus.com/commwiki/wiki?18584
genexus_version: "18"
---

# UserRememberMeType property

"User Remember Me Type" is a [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) property whose purpose is to specify the way that the Login WEB object will be presented to the user.

Depending on this property, the login can be renewed automatically when the session expires or just the login information can be presented to the user to be confirmed.

If the login session is kept for a specific time or ever, the application will have more security risks.

### [Values](#Values)

|  |  |
| --- | --- |
| **None** | No possibility is given to the user in order to remember his login. |
| **Login** | The user is given the possibility to be shown the [Login](https://wiki.genexus.com/commwiki/wiki?15590) object with the last login information instantiated. |
| **Authentication** | The user is given the possibility to be logged in automatically when the session expires, without showing the [Login](https://wiki.genexus.com/commwiki/wiki?15590) object. |
| **Both** | The user is given the possibility to be shown the Login object with the last login information instantiated and to be logged in automatically when the session expires. |

### [Description](#Description)

Take as an example the "GAMExampleLogin" object provided in the GAM examples Library.

Note in the "GAMExampleLogin" object, the following code in the Refresh Event:

```
&Repository = GAMRepository.Get()
&RememberMe.Visible = False
&KeepMeLoggedIn.Visible = False
Do Case
   Case &Repository.UserRememberMeType = GAMRepositoryRememberUserTypes.Login
        &RememberMe.Visible = True
   Case &Repository.UserRememberMeType = GAMRepositoryRememberUserTypes.Authentication
        &KeepMeLoggedIn.Visible = True
   Case &Repository.UserRememberMeType = GAMRepositoryRememberUserTypes.Both
        &RememberMe.Visible     = True
        &KeepMeLoggedIn.Visible = True
EndCase
```

&RememberMe and &KeepMeLoggedIn are checkboxes. The purpose of these checkboxes is the following:

1. &RememberMe : If checked, when the session expires, the user is presented the GAMExampleLogin object, with the last login information instantiated.

2. &KeepMeLoggedIn: If checked, when the session expires the user is logged in automatically, the GAMExampleLogin object is not shown.

When "User Remember Me Type" = None, none of these checkboxes is shown in GAMExampleLogin object.

See the following figure which shows **both** options in runtime.

`[imagen omitida: wiki id 18585]`

Note that you can get the value selected by the user (if he checked &RememberMe or &KeepMeLoggedIn) by executing the following code:

```
GAMRepository.GetRememberLogin(&LogOnTo, &UserName, &UserRememberMe, &Errors) //&LogOntO is the Authentication Type and &Errors is of GAMError Collection data type. &UserRememberMe is returned.
```

If &UserRememberMe is "Login", the &UserName is loaded with the corresponding value, as well as &LogOnTo (with the [Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508) which was set in the last login).

In the login event (Enter Event) of GAMExampleLogin, the following code is executed. The values of &RememberMe and &KeepMeLoggedIn variables are used to perform the login (are used as parameters of the login). GAM checks that the login can be done using the values passed in the parameters (according to the value set to "User Remember Me Type" of the Repository).

```
If &KeepMeLoggedIn
   &AdditionalParameter.RememberUserType = iif(&KeepMeLoggedIn, GAMRememberUserTypes.Authentication, GAMRememberUserTypes.None)
Else
   If &RememberMe
      &AdditionalParameter.RememberUserType = iif(&RememberMe, GAMRememberUserTypes.Login, GAMRememberUserTypes.None)
   Else
      &AdditionalParameter.RememberUserType = GAMRememberUserTypes.None
   Endif
Endif

&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
```

#### [Note](#Note)

If the object has [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = None, the way to know if the user is logged in (in order to show some data afterwards for example), is by executing the GAM.Isvalid method.

```
&isSessionValid = GAMSession.IsValid(&GAMSession, &GAMErrors)
If not &GAMSession.IsAnonymous
//The user is logged
Else
//The user is not logged
EndIf
```

### [See Also](#See+Also)

[User Remember Me Timeout](https://wiki.genexus.com/commwiki/wiki?18586)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [User Remember Me Timeout](https://wiki.genexus.com/commwiki/wiki?18586) |

---
