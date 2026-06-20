---
title: "GAM Session expiration"
source_id: 39673
source_url: https://wiki.genexus.com/commwiki/wiki?39673
genexus_version: "18"
---

# GAM Session expiration

When the session has expired, or you are forced to change the password; the login is in a special state limited only to change the password.  
Use the GetUserToChangePassword method to get the current user and then UpdateUserToChangePassword to do the update.

For more details, check the GAMExampleChangePassword WebPanel where the following pattern is used:

```
Event Start
    &User = GAMRepository.GetUserToChangePassword() // get the logged User to change the password:
    ...    
Endevent

Event Enter
    If &UserPasswordNew = &UserPasswordNewConf
        &isOK = GAMRepository.UpdateUserToChangePassword(&UserPassword, &UserPasswordNew, &Errors)
        If &isOK
        ....
Endevent
```
