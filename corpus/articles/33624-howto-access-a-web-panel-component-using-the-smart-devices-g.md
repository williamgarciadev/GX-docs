---
title: "HowTo: Access a Web Panel component using the Smart Devices GAM credentials"
source_id: 33624
source_url: https://wiki.genexus.com/commwiki/wiki?33624
genexus_version: "18"
---

# HowTo: Access a Web Panel component using the Smart Devices GAM credentials

This document explains how to access a
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) component using the Smart Devices GAM credentials and provides a brief overview about it.

Consider a scenario where you need to call a
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) inside an [SDPanel](https://wiki.genexus.com/commwiki/wiki?20880,,) using the [Component domain](https://wiki.genexus.com/commwiki/wiki?16186). The Web Panel, as well as the Smart Devices app, has [Integrated Security](https://wiki.genexus.com/commwiki/wiki?14706) enabled.

Once logged into the Smart Devices app, the end-user shouldn't be asked to log in again into the Web Panel and should be able to use the same credentials.

### [Implementation of the solution](#Implementation+of+the+solution)

The solution consists of sharing the GAMSession Token of the Web Panel. After having validated it, it can be used to go on with the execution.  
As any private object automatically validates security before the Start Event, you need to set the GAMSession [Token](https://wiki.genexus.com/commwiki/wiki?28820,,) before its execution. The only valid way to do that is to validate the GAMSession Token in a public Web Panel and then call the private Web Panel.

The *ValidAccessToken* method of the GAMRepository object is useful for validating the GAMSession Token and setting it in the environment.

### [Step 1](#Step+1)

Create a public Web Panel ([Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = None) which is called directly by the SDPanel using the [Component domain](https://wiki.genexus.com/commwiki/wiki?16186) and receives as parameter the GAMSession Token. The public Web Panel (let's call it "auxWBP") is used as a "bridge" and redirects to the private Web Panel ([Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authentication / Authorization).    
  
Note that for security reasons, the URL to be redirected can be hard-coded. In this example, its value has been loaded in the *&url* variable, and *&SessionSTR* is received as a parameter.

```
Event Start    

 &ValidAccessToken = GAMRepository.ValidAccessToken(&SessionSTR,&GAMSession,&Errors) //&Errors is a collection of GAMError
        
 if &ValidAccessToken //If the session token received as a parameter is valid 
    Link(&url)
 else //If the session token received as a parameter is not valid 
    //Error
 endif
Endevent
```

### [Step 2](#Step+2)

The SDPanel loads the GAMSession in a *&GAMSession* variable and calls the *auxWBP* Web Panel in the Start Event,passing the GAMSession Token as a parameter.  
  
**Where:**  
  
*&UrlToCall*  
      Is a variable based on the [Component domain](https://wiki.genexus.com/commwiki/wiki?16186):  
  
`[imagen omitida: wiki id 33626]`  
  
So, the Start Event code of the SDPanel is as follows:

```
Event Start
    &GAMSession = GAMSession.Get(&Errors) //&Errors is a collection of GAMError
    &UrlToCall = auxWBP.Link(&GAMSession.Token.ToString())
Endevent
```

Download the sample from [Sample: How to get the SD credentials in a web panel component](https://wiki.genexus.com/commwiki/wiki?33627,,).


|  |
| --- |
| **Backlinks** |
| [Share session to Webview property](https://wiki.genexus.com/commwiki/wiki?38266) |

---
