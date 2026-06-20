---
title: "GAM - Events subscription (GeneXus 18 Upgrade 8 or prior)"
source_id: 57625
source_url: https://wiki.genexus.com/commwiki/wiki?57625
genexus_version: "18"
---

# GAM - Events subscription (GeneXus 18 Upgrade 8 or prior)

The purpose of the [GAM](https://wiki.genexus.com/commwiki/wiki?24746) Events subscription is to allow the automatic triggering of additional (external) code when a GAM event is executed. That is, being able to execute a custom event automatically after a GAM event is executed (i.e: the creation of a GAM user).

Consider a scenario where you have a Users table, and the user information is redundant with the GAM Users table. You need to   
keep the Users table up to date; that is, any time a GAM User is updated (created or removed) the Users table should be updated accordingly.

The following pseudo-code would be used in such a case:

```
&GAMUser.Save()
//Call a procedure to make the necessary changes in the Users table.
```

To avoid considering this piece of code everywhere you update a GAM User, the code may be automatically triggered immediately after the GAM user is updated.

So the GAM User *insert, update, and delete* are considered to be events that automatically trigger the piece of code declared to be executed.

In other words, you subscribe to some events, so that (external) code can be triggered as any of these events is executed.

### [Events you may subscribe to:](#Events+you+may+subscribe+to%3A)

* User\_Insert: Insert of a GAM User
* User\_Update: Update of a GAM User
* User\_Delete: Delete of a GAM User
* User\_UpdateRoles: Change of roles of a list of users
* User\_GetCustomInfo: This event allows to customize the information that the Identity Provider sends to the Client, and it’s executed when the User’s authenticate (SSO Web) or request a token (OAuth 2.0). For this purpose, the Output oh the procedure must return a JSON. It’s recommended to use an SDT that has the structure of the information to be shared.
* User\_SaveCustomInfo: This event is executed on the client when the [GAM Remote](https://wiki.genexus.com/commwiki/wiki?25355) or Remote Rest Authentication type (OAuth 2.0) login is successfully finished.
* Role\_Insert: Insert of a role
* Role\_Update: Update of a role
* Role\_Delete: Delete of a role
* Repository\_Login: GAM User login (any [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) is supported)
* Repository\_LoginFailed: User login fails (GAM Error 11 or GAM Error 18)
* Repository\_Logout: GAM log out
* Application\_CheckPermissionFail: Failure of a permission verification.
* [User\_OneTimePasswordValidUser](https://wiki.genexus.com/commwiki/wiki?48197). Check that the user that asked for an OTP code is allowed to do it.
* User\_OneTimePasswordGenerateCode. Developer event to generate the OTP code.
* [User\_OneTimePasswordSendCode](https://wiki.genexus.com/commwiki/wiki?48197). Developer event to send the OTP code.
* [User\_OneTimePasswordValidateCode](https://wiki.genexus.com/commwiki/wiki?48197). Developer event to validate the OTP code.

### [Requirements of a program that subscribes to an event](#Requirements+of+a+program+that+subscribes+to+an+event)

The way to subscribe to an event is to configure a program that will be triggered when the event is executed. The configuration may be done using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)(1) or the [Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)(2). We'll go over this topic in more detail below.

The program that considers the GAM events may be developed using GeneXus or not, and it has to fulfill some requirements.

First, the signature of the program has to be as follows:

(in Character **&EventName**, in Character **&jsonIn**, out Character **&jsonOut**)

**Where:**

* **&EventName**: belongs to the GAMEvents Domain.
* **&jsonIN**: JSON string whose format depends on the GAM event that the program is subscribed to (see the table below for more details).
* **&jsonOUT**: JSON string used to print information in the [GAM trace](https://wiki.genexus.com/commwiki/wiki?25395,,) (if it's enabled).

[Main program property](https://wiki.genexus.com/commwiki/wiki?7407) has to be on **True**.

Secondly, consider how the &jsonIN format should be:

|  |  |
| --- | --- |
| **Event** | **GAM object received parameters** |
| User\_Insert | GAMUser (i.e., the jsonIN format is derived from the GAMUser object) |
| User\_Update | GAMUser |
| User\_Delete | GAMUser |
| User\_UpdateRoles | GAMGUID collection representing the list of users whose roles were changed. |
| User\_GetCustomInfo | GAMSession |
| User\_SaveCustomInfo | *(free format)* |
| Role\_Insert | GAMRole (i.e., the jsonIN format is derived from the GAMRole object) |
| Role\_Update | GAMRole |
| Role\_Delete | GAMRole |
| Repository\_Login | GAMSession (i.e., the jsonIN format is derived from the GAMSession object) |
| Repository\_Logout | GAMSession |
| Repository\_LoginFailed | GAMSession |
| Application\_CheckPermissionFail | GAMSessionLogCheckPermissionFail |
| [User\_OneTimePasswordValidUser](https://wiki.genexus.com/commwiki/wiki?48197) | [GAMOTPEventSubscription](https://wiki.genexus.com/commwiki/wiki?48197) |
| [User\_OneTimePasswordGenerateCode](https://wiki.genexus.com/commwiki/wiki?48197) | GAMOTPEventSubscription |
| [User\_OneTimePasswordSendCode](https://wiki.genexus.com/commwiki/wiki?48197) | GAMOTPEventSubscription |
| [User\_OneTimePasswordValidateCode](https://wiki.genexus.com/commwiki/wiki?48197) | GAMOTPEventSubscription |

### [Example I](#Example+I)

In the following example, we have subscribed to the User\_Insert event.

In the [Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)(2), go through Settings > Event Subscriptions and define the Event as shown in the following figure.

#### [Net configuration](#Net+configuration)

`[imagen omitida: wiki id 54312]`

Java configuration (in this example the Java Package Name=com.gameventssubscription)

`[imagen omitida: wiki id 54313]`

|  |  |
| --- | --- |
| **Status** | It may be {subscribed,unsubscribed}. It has to be subscribed for the procedure to be triggered when the event is executed. |
| **Event** | It's a combo box where you can select any of the events available. |
| **File Name** | The name of the .dll or .class file which listens to the event execution. |
| **Class Name** | The name of the program including its package. |
| **Method Name** | The method of the program in GeneXus is always "execute". |

The code of the notifyuserinsert procedure is as follows:

```
Rules: Parm(in:&EventName, in:&jsonIN, out:&jsonOUT);
```

```
&GAMUser.FromJsonString(&jsonIN)

&MyUser.Load(&GAMUser.GUID)  //&Myuser is based on a BC.
If &MyUser.Fail()
    &MyUser = new()    
Endif
&MyUser.MyUserGUID    =&GAMUser.GUID
&MyUser.MyUserEmail    = &GAMUser.EMail
&MyUser.MyUserName    = &GAMUser.FirstName.Trim() +" "+ &GAMUser.LastName.Trim()
&MyUser.Save()
If &MyUser.Success()
    //Ok
Else
    //load &jsonOUT parameter with information about the error.
Endif
```

### [Example II](#Example+II)

See [HowTo: Get user's additional information from the GAM Identity Provider](https://wiki.genexus.com/commwiki/wiki?37703) for an example of User\_GetCustomInfo and User\_SaveCustomInfo events.

### [Example III](#Example+III)

In the case of the login event, the proc subscribed will be triggered at login (regardless of whether the login is local or not).  
In that procedure, you can make additional controls that allow you to cancel the login and prevent a session from being generated.

Consider the following example code that triggers at login:

```
&GAMSession.FromJsonString(&JsonIN)
For each
    Where  CustomerGUID = &GAMSession.User.GUID
    Where  CustomerActiveSubscription = True

         //OK
     When none
      &GAMError.Code        = GAMErrorMessages.UserInactive
      &GAMError.Message    = "The user's subscription is not valid."
      &JsonOUT = &GAMError.ToJsonString()
Endfor
```

The JsonOut format must be GAMError. Only if it is empty, it does not cancel the login.  
What happens internally is that the session is created and revoked immediately.

### [(1)How to subscribe to an event using the GAM API](#%281%29+How+to+subscribe+to+an+event+using+the+GAM+API)

You can define the event subscription as shown in the following example:

```
&GAMEventSubscription = new()    // &GAMEventSubscription is GAMEventSubscription data type
&GAMEventSubscription.Description =  "Inspecting the User Login"
&GAMEventSubscription.Event       =  GAMEvents.Repository_Login
&GAMEventSubscription.FileName    = "aNotifyUserLogin.dll"
&GAMEventSubscription.ClassName   = "GeneXus.Programs.anotifyuserlogin"
&GAMEventSubscription.MethodName  =  "execute"
&GAMEventSubscription.Save()
If &GAMEventSubscription.Success()
  Commit
  // Subscription activation:
  &isOK = GAMRepository.SubscribeEvent(&GAMEventSubscription.Id, &GAMErrors)
  If &isOK
     Commit
  Endif
Endif
```

You may define more than one program to be triggered when the event is executed.

Note that the subscription must be activated using the SubscribeEvent method of GAMRepository.

### [Considerations about the logic Transaction](#Considerations+about+the+logic+Transaction)

#### [Case 1. The program was developed using GeneXus](#Case+1.+The+program+was+developed+using+GeneXus+)

To include the program subscribed to the event in the same LUW (Logical Unit of Work) of the event, include the [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) after the code that triggers the event (i.e., &GAMUser.save() or &GAMRole.save()).

On the contrary, if you don't want to include the program in the same LUW, just configure [Execute in new LUW property](https://wiki.genexus.com/commwiki/wiki?8008) = True for the program.

The Repository\_Login and Repository\_Logout methods execute an implicit commit, so you don't need to execute it.

#### [Case 2. The program was not developed using GeneXus](#Case+2.+The+program+was+not+developed+using+GeneXus)

It will not be in the same LUW.
