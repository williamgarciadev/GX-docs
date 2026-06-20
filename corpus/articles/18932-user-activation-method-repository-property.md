---
title: "User Activation Method Repository property"
source_id: 18932
source_url: https://wiki.genexus.com/commwiki/wiki?18932
genexus_version: "18"
---

# User Activation Method Repository property

This [repository](https://wiki.genexus.com/commwiki/wiki?17568) property determines whether users who register will have their accounts automatically activated, or if they will have to activate them in a second step after registering.

### [Values](#Values)

|  |  |
| --- | --- |
| **Automatic** | The user account is automatically activated after the registration. |
| **User** | The user will need to confirm the activation of the account. |
| **Administrator** | Only the administrator activates user accounts. |

The user activation is for all the repositories (for GAM and not for any particular repository). Once the account is activated, it cannot be set to inactive status.

To disable the user, it has to be blocked, deleted, or just disabled from accessing the Repository (see [Users enabled or disabled in the GAM Repository](https://wiki.genexus.com/commwiki/wiki?21042)).

The UserActivationMethod is a Repository property and should be configured using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935). The *GAMRepositoryConfiguration* web panel is an example where the property is used.

`[imagen omitida: wiki id 34648]`

The way to use it in GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)) is as follows:

```
&Repository.Load(&Id)
&Repository.UserActivationMethod            = &UserActivationMethod
&Repository.Save()
if &Repository.Success()
   Commit
else
   &Errors = &Repository.GetErrors()
   For &Error in &Errors
       Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
   EndFor
Endif
```

### [Different ways to activate a GAM user](#Different+ways+to+activate+a+GAM+user)

The *GAMExampleRegisterUser* Web Panel is a sample object included in the GAM Examples folder and may be used as an example of web registration form.  
  
Depending on the value set in this property, users who register in GAM will need to activate their account and wait for the administrator to activate it when it is not immediately activated.

### [Account activation confirmed by the user](#Account+activation+confirmed+by+the+user)

This is the case for the "User" value in this property.

When you set this property, a temporal key is created. This key has a timeout which is configured in the GAM.UserAutomaticActivationTimeout property in hours.

You can see a sample code in the GAMCheckUserActivationMethod object.

There are two ways to send the account activation key to the user:

#### [1. GAM sends the email with the URL and the account activation key:](#1.+GAM+sends+the+email+with+the+URL+and+the+account+activation+key%3A)

```
If &Repository.UserActivationMethod = GAMUserActivationMethod.User
    &User.Load(&UserGUID)
    &User.SendEmailToActivateAccount(&Application, &LinkURL, &Errors)
    If &Errors.Count = 0
        &Message = new()
        &Message.Type = MessageTypes.Warning
        &Message.Description = "The account was created successfully, an email was sent with instructions to activate your account!"
        &Messages.Add(&Message)
    Else
        GAMConvertErrorsToMessages(&Errors, &Messages)
    Endif
Endif
```

See [Account Activation Object property](https://wiki.genexus.com/commwiki/wiki?48421)

#### [2. The developer can program how the activation key is sent to the user:](#2.+The+developer+can+program+how+the+activation+key+is+sent+to+the+user%3A)

```
If &Repository.UserActivationMethod = GAMUserActivationMethod.User
   &ActivactionKey = &User.GetActivationKey(&Errors)
   // Send an email to the user (*)
Else
   Do 'DisplayMessages'
Endif
```

(\*) To activate the user account, send an email to the user including a URL like the following: http://server/app/webpanel\_ActivateAccount.aspx?&ActivactionKey.  
&ActivactionKey is the key used to activate the account, and it is received as a parameter.

In webpanel\_ActivateAccount, activate the user's account using the **GAMRepository.ActivateUser** method with the &ActivationKey received as a parameter. The sample code is as follows:

```
Event Start
    &isOK = GAMRepository.ActivateUser(&ActivactionKey, True, &Errors)
    If &isOK
       Msg("Your user account was successfully activated !!")
    Else
       Do 'DisplayMessages'
    Endif
EndEvent
```

### [Account activation confirmed by the Administrator](#Account+activation+confirmed+by+the+Administrator)

The GAM administrator user may activate the account by executing the [GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), editing the user properties, and selecting or clearing "Account is active".

`[imagen omitida: wiki id 34647]`

You can also do it via code, using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535):

```
&User.Load(&UserId)    
&User.Isactive= TRUE
&User.Save()
If &User.Success()
     Commit
Else
     &Errors = &User.GetErrors()
      For &Error in &Errors
           Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
      EndFor
 Endif
```

The IsActive property indicates if the user account is active; it can only be set to TRUE as explained above in this document.

### [See Also](#See+Also)

[User Automatic Activate TimeOut property](https://wiki.genexus.com/commwiki/wiki?18934)


|  |
| --- |
| **Backlinks** |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [User Automatic Activate TimeOut property](https://wiki.genexus.com/commwiki/wiki?18934) | [Users enabled or disabled in the GAM Repository](https://wiki.genexus.com/commwiki/wiki?21042) |

---
