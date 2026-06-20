---
title: "DeviceAuthentication external object"
source_id: 39252
source_url: https://wiki.genexus.com/commwiki/wiki?39252
genexus_version: "18"
---

# DeviceAuthentication external object

Nowadays most of the mobile devices provide biometric sensors that allow the end user to authenticate locally. This type of authentication can be done through fingerprint recognition, facial recognition, retinal scanning, etc. and its objective is to make sure that the end user is the owner of the device.

The DeviceAuthentication external object allows you to interact with these different types of authentication where available, without worrying about device-specific considerations.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [BiometricDescription property](#BiometricDescription+property)

Returns the name of the biometric authentication method available on the current device. For iOS, the possible values are "Touch ID", "Face ID", for Android are "Finger Print" or the empty value if the property IsAvailable returns False.

### [AllowableReuseDuration property](#AllowableReuseDuration+property)

Indicates the minimum time (in seconds) before asking the user to locally authenticate again after one successful authentication.

## [Methods](#Methods)

### [IsAvailable method](#IsAvailable+method)

Returns True if the API can be used in the current device, False otherwise.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameter** | method: DeviceAuthenticationPolicy |
|  |  |

### [Authenticate method](#Authenticate+method)

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | method: DeviceAuthenticationPolicy, title:VarChar(40), usageDescription:VarChar(40) |
|  |  |

This method performs the authentication step, using the method that corresponds to the current device.

If the method parameter is set to Biometrics, then only biometrics sensors will be used. If set to Any and biometrics is not available or is disabled, then the password will be used.

It returns True if the user could be authenticated, otherwise, it returns False. In particular, if the property IsAvailable has value False, the return value of this method is also False.

Calling the method without using the return value (assigning it to a variable, checking it in an if command, etc.) will make the Composite block containing the call to fail.

The title parameter is used to present the end user a title when they are prompted for the local authentication. It is used only in Android.

The UsageDescription parameter is used to present the end user with a message when they are prompted for the local authentication. It cannot be empty in iOS.

## [Domains](#Domains)

### [DeviceAuthenticationPolicy domain](#DeviceAuthenticationPolicy+domain)

Specifies the policy the developer wants to use.

|  |  |
| --- | --- |
| **Any** | Biometrics or Password. |
| **Biometrics** | Only Biometrics. |
|  |  |

## [Examples](#Examples)

The code shown below is a very simple example created for this document.

```
Composite
    &BioComfirmed = DeviceAuthentication.Authenticate(DeviceAuthenticationPolicy.Any, 'Authenticate', 'Please authenticate')
    If &BioComfirmed
        //Access granted
        return
    Else 
        Actions.Cancel()
    EndIf
EndComposite
```

Executing this code will display the following screens, depending on whether the device allows biometric authentication.

|  |  |
| --- | --- |
| **Authenticathion with Biometrics** | **Authentication when Biometrics is not accepted** |
|  |  |

## [Availability](#Availability)

Available from [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices(iOS, Android) |

## [See Also:](#See+Also%3A)

[DeviceAuthentication external object usage examples](https://wiki.genexus.com/commwiki/wiki?38412,,)


|  |
| --- |
| **Backlinks** |
| [Face ID Usage Description property](https://wiki.genexus.com/commwiki/wiki?38838) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
