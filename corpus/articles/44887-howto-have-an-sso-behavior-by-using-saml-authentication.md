---
title: "HowTo: Have an SSO behavior by using SAML Authentication"
source_id: 44887
source_url: https://wiki.genexus.com/commwiki/wiki?44887
genexus_version: "18"
---

# HowTo: Have an SSO behavior by using SAML Authentication

If you have more than one Service Provider (apps) and all of them are in a web SSO system, you can implement the SSO by introducing some changes to the GAMSSOLogin object of the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) by using [GAM SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212).

In the Start event, it will verify whether there is a valid session or not. If not, it should try to login automatically to the SAML Provider.

Take a look at this code (included at the Start Event):

```
&isRedirect = False
    //Gets last error in the GAM /////////////////////////////
    &Errors = GAMRepository.GetLastErrors()
    If &Errors.Count > 0  AND  &Errors.Item(1).Code <> GAMErrorMessages.UserMustBeAuthenticated
        Do 'DisplayMessages'
    Else
        &SessionValid = GAMSession.IsValid(&Session, &Errors)
        If &SessionValid and not &Session.IsAnonymous
            &URL = GAMRepository.GetLastErrorsURL()
            If &URL.IsEmpty()
                GAMApplication.GoHome()
            Else
                Link(&URL)
            Endif
        Else
            &AdditionalParameter.AuthenticationTypeName = !"SAML20"
            &LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
            &Errors = GAMRepository.GetLastErrors()
            If &Errors.Count > 0
                Do 'DisplayMessages'
            Endif
        Endif
    Endif
```

You can set the GAMSSOLogin object as the [Login Object for Web](https://wiki.genexus.com/commwiki/wiki?15590), which is called automatically when the web session fails.  
If there is a valid session in the IdP, the user will not need to login again, and the local GAM session will be renewed. Otherwise, the user will be redirected to the IdP for login, and a local session will be created in GAM.  
  
While the local GAM session is valid, the user will not be requested to login.

The session timeout is governed by GAM (see [Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338)).


|  |
| --- |
| **Backlinks** |
| [GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) |

---
