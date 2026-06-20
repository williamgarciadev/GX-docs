---
title: "GAM: \"User Missing Required Data\" Form"
source_id: 18920
source_url: https://wiki.genexus.com/commwiki/wiki?18920
genexus_version: "18"
---

# GAM: "User Missing Required Data" Form

When the registration of a new user fails because some required data is missing, some actions are triggered automatically in GAMExampleLogin object when the user logs in for the first time. In general, this happens with users registered with external [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) (not local).

The following code in GAMExampleLogin object is triggered in Refresh event, in order to call a registration form that asks the user to enter the missing data in order to finish the registration process.

```
(*) If &ErrorsLogin.Count > 0
  If &ErrorsLogin.Item(1).Code = GAMErrorMessages.UserMissingRequiredData
     //Webpanel to Complete User data
     GAMExampleUpdateRegisterUser.Link()
     &isRedirect = True
  Else
     &UserPassword = ""
     &Errors = &ErrorsLogin
     Do 'DisplayMessages'
  Endif
Endif
```

GAMExampleUpdateRegisterUser is a web panel that is distributed with the GAM Examples library and builds up a form in runtime where a field is shown in the form for each required data that is missing.

### [Sample](#Sample)

In case of [Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208), when the user logs in to the application for the first time, the email of the user is not part of the information sent by Twitter to the application.

Suppose that the repository configuration includes the following:

* User Identification = Name and email
* User Email is Unique = True
* Required Email = True

In this case, when the user logs in for the first time an error would be thrown because some of the required data is missing (the user email in this particular case).

By executing the code shown above (\*) the error is caught and the GAMExampleUpdateRegisterUser web panel is called, so the user can enter the missing data and finish the registration process.

See GAMExampleUpdateRegisterUser web panel code. It can be changed as desired in order to follow the user needs.

`[imagen omitida: wiki id 18921]`

##### [Figure 1. GAMExampleUpdateRegisterUser form at execution time](#Figure+1.+GAMExampleUpdateRegisterUser+form+at+execution+time)
