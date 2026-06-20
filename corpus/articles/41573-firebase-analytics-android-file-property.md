---
title: "Firebase Analytics Android File property"
source_id: 41573
source_url: https://wiki.genexus.com/commwiki/wiki?41573
genexus_version: "18"
---

# Firebase Analytics Android File property

Android configuration file downloaded from Firebase's backend

### [Scope](#Scope)

**Platforms:** Smart Devices(Android)

### [Description](#Description)

In order to use Firebase Analitytics in your application, you must add a configuration file. Such configuration file may be obtained from the Firebase console. You must add it to the KB as a File under the name "google-services\_json", and you must also make sure that the file is referenced from this property. GeneXus will do the rest automatically.

For further information on the creation of the project in Firebase go to [Add Firebase to Your Android Project](https://firebase.google.com/docs/android/setup)

### [Troubleshooting](#Troubleshooting)

#### [No matching client found for package name](#No+matching+client+found+for+package+name)

The following error occurs compiling the Android project.

```
Parsing json file: ...\google-services.json
> Task :MainObjectName:processDebugResources
error: 
error: FAILURE: Build failed with an exception.
error: 
error: * What went wrong:
error: Execution failed for task ':MainObjectName:processDebugGoogleServices'.
error: > No matching client found for package name 'com.artech.kbname.mainname'
```

Review the *google-services.json* configuration file uploaded to the KB and make sure it matches the configuration for the [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814) associated to the main object.

#### [FirebaseCrashlytics Failed to retrieve settings](#FirebaseCrashlytics+Failed+to+retrieve+settings)

The following error is detailed on the Android device logcat

```
com.artech.kbname.mainobject E/FirebaseCrashlytics: Failed to retrieve settings from https://firebase-settings.crashlytics.com/spi/v2/platforms/android/gmp/1:ID:android:Id/settings
```

You may need to wait up to 24 hours to get the [first analytics reports](https://stackoverflow.com/questions/37347991/how-much-time-does-it-take-for-firebase-analytics-first-report).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,).

### [See Also](#See+Also)

[Analytics Provider property](https://wiki.genexus.com/commwiki/wiki?41575)


|  |
| --- |
| **Backlinks** |
| [Analytics Provider property](https://wiki.genexus.com/commwiki/wiki?41575) | [Analytics Provider property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54454) | [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101) |

---
