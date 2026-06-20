---
title: "CrashAnalytics external object"
source_id: 55161
source_url: https://wiki.genexus.com/commwiki/wiki?55161
genexus_version: "18"
---

# CrashAnalytics external object

Customizes and enhances crash reports in your mobile app by interacting with Firebase Crashlytics. Add additional information, such as log messages, user IDs, and custom key-value pairs to gain a more accurate understanding of crashes and take corrective actions effectively.

`[imagen omitida: wiki id 55172]`

You can find the CrashAnalytics external object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the Common module, which in turn is located within the GeneXus module. That is, it is part of the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288).

## [Properties](#Properties)

### [Enabled](#Enabled)

Returns True when you have enabled Crashlytics through the [Enable Firebase Crashlytics property](https://wiki.genexus.com/commwiki/wiki?48141) of the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

The methods of the CrashAnalytics external object will fail when this property returns False.

## [Methods](#Methods)

### [DidCrashOnPreviousExecution](#DidCrashOnPreviousExecution)

Returns True when the Crashlytics provider informs that the application crashed on the previous execution.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | None |

### [SetCustomKey](#SetCustomKey)

Assigns a custom value to a specific key in the Firebase Crashlytics bug reports. This additional information will be sent along with future bug reports to the Firebase Crashlytics backend, if and when available.

You can use this method to send a single additional key-value pair.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Key:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), Value:VarChar |

### [SetCustomKeys](#SetCustomKeys)

Allows you to send multiple custom key-value pairs in a single call. You can define a collection of key-value pairs and send them together in bug reports.

This is useful when you want to provide a larger amount of additional information related to bugs.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | CustomKeysAndValues:CrashAnalyticsKeyValue, GeneXus.Common |

### [RemoveCustomKey](#RemoveCustomKey)

Removes a specific key and its associated value from the Firebase Crashlytics bug reports.

This ensures that the corresponding information will no longer be sent in future crash reports to Crashlytics.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Key:VarChar |

**Note**: Android and iOS have different behaviors due to Firebase implementation details. The difference is that, when using the RemoveCustomKey method, in Android a line is shown indicating that the key value is empty while in iOS nothing is shown.

### [SetUserId](#SetUserId)

Assigns a custom user ID in the Firebase Crashlytics bug reports. This way, you can identify and track bugs related to individual users in your application.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | UserId:VarChar |

### [Log](#Log)

Sends log messages that will help you better understand bugs and problems in your application.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:VarChar |

## [Events](#Events)

It doesn't have any.

## [CrashAnalyticsKeyValue](#CrashAnalyticsKeyValue)

CrashAnalyticsKeyValue is a [SDT](https://wiki.genexus.com/commwiki/wiki?10021) used to represent key-value pairs in Firebase Crashlytics crash reports.   
  
The CrashAnalyticsKeyValue SDT consists of two attributes: "Key" and "Value".

* The "Key" attribute represents the key or identifier of the custom value you wish to send.
* The "Value" attribute stores the value associated with that key.

You can use this SDT CrashAnalyticsKeyValue to send multiple key-value pairs as a list, which allows you to include multiple custom values in a single crash report.

You can find the CrashAnalyticsKeyValue SDT in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the Common module, which in turn is located within the GeneXus module. That is, it is part of the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288).

## [Considerations](#Considerations)

Firebase Crashlytics -Android- SDK supports values of String, Boolean, Int, Long, Float, and Double type, but the GeneXus specifier doesn't support defining two methods with the same name and parameter amount. Therefore, this can be either resolved by the implementation (try parsing the value to the corresponding type before forwarding it to the provider) or by creating -at least- four methods, one for each type instead of just a generic "SetCustomKey" one. Those would be "SetCustomStringKey", "SetCustomBooleanKey", "SetCustomIntegerKey", and "SetCustomDecimalKey".

## [Scope](#Scope)

**Generators:**[Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).


|  |
| --- |
| **Backlinks** |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |

---
