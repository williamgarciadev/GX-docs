---
title: "GAM - Time Based One Time Password for mobile"
source_id: 50708
source_url: https://wiki.genexus.com/commwiki/wiki?50708
genexus_version: "18"
---

# GAM - Time Based One Time Password for mobile

In this article, you will find the steps to use Time Based One Time Password (TOTP) authentication in a mobile application:

First, you must configure a [Time Based One Time Password](https://wiki.genexus.com/commwiki/wiki?49974).

After completing the configuration for TOTP authentication, you need to consider the following:

All the Events described below are in the same [Panel](https://wiki.genexus.com/commwiki/wiki?24829).

Just like [One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?50664), TOTP runs two core events. The first event validates the user's existence. The second event verifies the user code that is provided by authenticators like Google Authenticator, Microsoft Authenticator, iOS built-in authenticator, WinAuth, and so on.  
  
`[imagen omitida: wiki id 50709]`

### [Step 1: Verify user event](#Step+1%3A+Verify+user+event)

The logic inside this event will include a call to a method of the [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) named LoginExternal.

The first parameter is based on the GAMAuthenticationTypes domain, and its value should be OTP.

The &password parameter is ignored in this case.

The &LoginExternalAdditionalParameters has an AuthenticationTypeName property where you can set the name of the Authentication Type. This is due to the fact that more than one TOTP Authentication Type can be defined in the Repository.

Also, the &LoginExternalAdditionalParameters has the OTPStep which has the value "1" if it is validating the user, and "2" if it is validating the OTP code that the user inserted.

If the LoginExternal method returns True, the event GeneXusSecurity.GAMLoginEvents.OTPAuthenticationRequested is triggered.

This event calls the subroutine "DisplayOTPStep2" to change the inputs of the Panel, so it is prepared to read the TOTP code that the user will insert. Apart from that, this event also warns the user to check the authenticator code.

```
Event 'BtnNext'
    Composite
        GeneXus.Common.UI.Progress.ShowWithTitle("Connecting...")
        &LoginExternalAdditionalParameters = new()
        &LoginExternalAdditionalParameters.AuthenticationTypeName    = !"TOTP-FFA"
        &LoginExternalAdditionalParameters.OTPStep                    = 1
        &isLoginOK = GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.OTP, &UserName, &Password, &LoginExternalAdditionalParameters)
        GeneXus.Common.UI.Progress.Hide()
        If &isLoginOK
            //OK
        Else
            GAMSDGetLastErrors(&Messages)
        Endif
    EndComposite
Endevent

Event GeneXusSecurity.GAMLoginEvents.OTPAuthenticationRequested
    Msg("Verify your authenticator code")
    
    Do "DisplayOTPStep2"
    &LoginOTPStep = 2
    GeneXus.Client.ClientStorage.Set(!'LoginOTP-Step', &LoginOTPStep.ToString())
      GeneXus.Client.ClientStorage.Set(!'LoginOTP-UserName', &UserName.Trim())
EndEvent
```

### [Step 2: Validate code event](#Step+2%3A+Validate+code+event)

In this event, the external object method LoginExternal is used to validate the code given by the user. For this reason, the &LoginExternalAdditionalParameters.OTPStep property is defined as "2".

Besides, the &password parameter is changed to &TOTPCode in the LoginExternal method.

```
Event 'BtnValidCode'
    Composite
        GeneXus.Common.UI.Progress.ShowWithTitle("Connecting...")
        &LoginExternalAdditionalParameters = new()
        &LoginExternalAdditionalParameters.AuthenticationTypeName         = !"TOTP-FFA"
        &LoginExternalAdditionalParameters.OTPStep                        = 2
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.OTP, &UserName, &TOTPCode, &LoginExternalAdditionalParameters)
        GeneXus.Common.UI.Progress.Hide()
        Do "SetOTPStep1"
        Return
    EndComposite
Endevent
```

### [Event start](#Event+start)

In cases where the app is running in the background, it is important to keep the state of the login process. This means that when users have been verified in the first verification step and received a code, they must be able to open another app to read the code without losing the state of the OTP step that has already been done.

To solve this problem, the ["ClientStorage" external object](https://wiki.genexus.com/commwiki/wiki?31272) is used.

```
Event ClientStart
    &UserName.Enabled    = True
    BtnNext.Visible        = True
    TblCode.Visible        = False
    &LoginOTPStep.FromString(GeneXus.Client.ClientStorage.Get(!'LoginOTP-Step'))
    If &LoginOTPStep = 2
        Do "DisplayOTPStep2"
        &UserName = GeneXus.Client.ClientStorage.Get(!'LoginOTP-UserName')
    Endif
Endevent
```

### [Go Back event](#Go+Back+event)

This event calls the subroutine "SetOTPStep1" to cancel the TOTP login process.

```
Event 'BtnBack'
    Composite
        Do "SetOTPStep1"
        Return
    EndComposite
Endevent
```

### [Subroutines](#Subroutines)

The events described above call two different [subroutine](https://wiki.genexus.com/commwiki/wiki?24767)s.

The "DisplayOTPStep2" subroutine makes changes to the elements of the Panel so that the user can interact either with the username input or the TOTPcode input.

```
Sub "DisplayOTPStep2"
    &UserName.Enabled      = False
    BtnNext.Visible        = False
    TblCode.Visible        = True
EndSub
```

The "SetOTPStep1" subroutine reset the steps of the OTP login process, leaving the Panel by default.

```
Sub "SetOTPStep1"
    &LoginOTPStep = 1
    GeneXus.Client.ClientStorage.Set(!'LoginOTP-Step', &LoginOTPStep.ToString())
    GeneXus.Client.ClientStorage.Set(!'LoginOTP-UserName', "")
EndSub
```

### [Availability](#Availability)

This feature is available since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,).

### [See Also](#See+Also)

[GAM - Time Based One Time Password (TOTP)](https://wiki.genexus.com/commwiki/wiki?49974)


|  |
| --- |
| **Backlinks** |
| [GAM - One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50664) | [GAM - Time Based One Time Password (TOTP)](https://wiki.genexus.com/commwiki/wiki?49974) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
