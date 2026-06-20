---
title: "HowTo: Register an application to use OneSignal services"
source_id: 33671
source_url: https://wiki.genexus.com/commwiki/wiki?33671
genexus_version: "18"
---

# HowTo: Register an application to use OneSignal services

**Warning**: This guide shows how to integrate Push Notifications using OneSignal. GeneXus does not support or maintain the configuration of this external service. Screenshots, parameters, UI labels, and/or configuration steps in OneSignal may change over time.

This document describes how to obtain the **App ID** and **REST API Key** from the OneSignal console. These credentials identify your application in OneSignal and are required to send push notifications.

### [Step 1 - Generate Firebase Private Key](#Step+1+-+Generate+Firebase+Private+Key)

You must obtain the certificates required by each platform that will receive notifications.

For Android (FCM), OneSignal requires the Firebase **Admin SDK private key**.

To generate it:

* Go to Firebase Console > Project Settings > Service Accounts.
* Click on **Generate new private key**.

`[imagen omitida: wiki id 61123]`

This downloads a JSON file that you will upload later during the OneSignal platform configuration.

If your application also runs on Apple devices, follow the instructions in [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) (or try [OneSignal's Provisionator wizard](https://onesignal.com/provisionator)).

### [Step 2 - Log in](#Step+2+-+Log+in)

Go to the [OneSignal](https://onesignal.com) site, enter your user credentials, and log in.

### [Step 3 - Create a new app](#Step+3+-+Create+a+new+app)

In the OneSignal dashboard, select the **+ New App/Website** option.

Enter a name for your application in OneSignal and select (or create) an Organization.

`[imagen omitida: wiki id 61136]`

Choose the platform you want to configure.

GeneXus only supports [Android](https://wiki.genexus.com/commwiki/wiki?14453) and
[Apple](https://wiki.genexus.com/commwiki/wiki?14917).

For this example, select Google Android (FCM). Then, click on the **Next: Configure Your Platform**button.

`[imagen omitida: wiki id 61137]`

**Note**: First, you must indicate one. Then you can update your OneSignal app from its settings and add the other one.

Click on **Select file** and upload the **JSON file**obtained in step 1 depending on the platform you selected in the previous step.

`[imagen omitida: wiki id 61138]`

Click on Save & Continue button.

In the Select your Target SDK section, choose **Native Android** and click **Save & Continue**.

`[imagen omitida: wiki id 61139]`

OneSignal will show an overview page to verify all settings. Copy the value of **Your App ID.** You will need this value to configure the Notification Provider in GeneXus.

`[imagen omitida: wiki id 61140]`

Click on the **Done** button.

### [Step 4 - Obtain the App ID and the API Authentication Key](#Step+4+-+Obtain+the+App+ID+and+the+API+Authentication+Key)

Once the OneSignal application is created, go to **Settings > Key & IDs** of your application and copy the **OneSignal's App ID.**

Click on the **+ Add Key** button.

`[imagen omitida: wiki id 61143]`

Enter a name for the API Authentication Key and click on **Create**.

`[imagen omitida: wiki id 61144]`

**Copy to Clipboard** the API Authentication Key:

`[imagen omitida: wiki id 61146]`

**Note**: Copy the API Authentication Key and store it safely. **OneSignal shows this key only once**.

and click on the **Continue** button.

Keep these three values safe: **App ID, API Authentication Key**. You will need them later.

### [OneSignal error Codes](#OneSignal+error+Codes)

Below is a list of errors that can be obtained when using [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) with OneSignal.

* *1: Unknown error.* See Error Description for more details.
* *3: OneSignal Object ID is required*: Method parameter "OneSignal Object ID" (Provider DeviceId) was not set.
* *4: iOS invalid device token*: Device Token specified is not valid.
* *5: "GCMSenderId is required"*. GCMSenderId must be specified in OneSignalPush Config.
* *6: Device Token is required.*
* *7: No channels specified.* At least 1 channel must be set.
* *10: "Application ID parameter is Required"*: ApplicationId must be specified in OneSignalPush Config.
* *11: "REST API Key parameter is Required"*: RestAPIKey must be specified in OneSignalPush Config.
* *112: Invalid Channel Name*: Error code indicating an invalid channel name. A channel name is either an empty string (the broadcast channel) or contains only a-zA-Z0-9\_\* characters and starts with a letter.
* *114: Invalid Device Token.*
* *140: Exceeded\_Quota*: Error code indicating that an application quota was exceeded.


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) | [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) |
| [OneSignal - App ID property](https://wiki.genexus.com/commwiki/wiki?37492) | [REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493) |

---
