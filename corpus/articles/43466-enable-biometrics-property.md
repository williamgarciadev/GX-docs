---
title: "Enable Biometrics property"
source_id: 43466
source_url: https://wiki.genexus.com/commwiki/wiki?43466
genexus_version: "18"
---

# Enable Biometrics property

Establishes whether the application will use biometrics for user authentication; it requires logging in only once.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Enables [GAM](https://wiki.genexus.com/commwiki/wiki?24746) users to access an app through the biometric authentication of the device.

When the user first logs into the application by using his/her username and password—if the device has biometric sensors and they are turned on—the application will ask if it should use biometric security the next time. If the user wants to use biometrics (fingerprint or face recognition), the next time he/she enters the application it will ask for biometric authentication instead of asking for a username and password.

To use this feature in a Native Mobile application with [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) activated, set the **Enable Biometrics** property to True for the desired [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). For more information, read about the [Biometrics Reuse Duration](https://wiki.genexus.com/commwiki/wiki?43467) property.

Take into account that when the user provides biometric credentials, the application locally stores a GAM token associated with that biometric information. This token will be later used to log in the next time the user accesses the application. No further information is required from the user.

The next time the user enters the application, if the session expired, the application prompts for the biometric credentials, and if provided it uses the stored token to perform the login operation. If the biometric information is not provided or if it fails to authenticate, then the login panel is shown and the end user needs to enter the credentials (username and password).

The way to indicate for how long the GAM token is valid, for example when the authentication process is done using OAuth, is   
by configuring the [OAuth token expire (minutes) property](https://wiki.genexus.com/commwiki/wiki?18577) of the GAMSecurityPolicy external object (when setting it to 0, it never expires).

**Notes:**

* For Android devices, face recognition is not available in versions lower than Android 9 (API 28).
* For Apple devices, the [Face ID Usage Description property](https://wiki.genexus.com/commwiki/wiki?38838) must be set in order to use this feature.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

**Android device Sample**

After entering the app's login data for the first time, the screen will show the following message:

|  |
| --- |
|  |

If the user answers affirmatively, verification of credentials will be required and the following screen will be shown:

|  |
| --- |
|  |

For Apple devices, the verification of biometric data will not be required upon login, but rather the next time that the application is started or upon the expiry of the time indicated in the [Biometrics Reuse Duration property](https://wiki.genexus.com/commwiki/wiki?43467).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,).

### [See Also](#See+Also)

[Biometrics Reuse Duration property](https://wiki.genexus.com/commwiki/wiki?43467)  
[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214)  
[Secure Application Content](https://wiki.genexus.com/commwiki/wiki?43468)  
[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746)


|  |
| --- |
| **Backlinks** |
| [Biometrics Reuse Duration property](https://wiki.genexus.com/commwiki/wiki?43467) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |
| [Secure Application Content](https://wiki.genexus.com/commwiki/wiki?43468) |

---
