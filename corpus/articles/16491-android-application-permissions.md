---
title: "Android Application Permissions"
source_id: 16491
source_url: https://wiki.genexus.com/commwiki/wiki?16491
genexus_version: "18"
---

# Android Application Permissions

An Android application generated with GeneXus by default requires all these permissions:

INTERNET, ACCESS\_NETWORK\_STATE, WRITE\_EXTERNAL\_STORAGE, ACCESS\_FINE\_LOCATION, ACCESS\_COARSE\_LOCATION, READ\_CONTACTS, WRITE\_CONTACTS, READ\_LOGS

Some of this may not be required in your application. So, if you want to not require them (avoid that customers not install the app because of security or privacy reasons), you can edit and <GeneXus Installation Directory\Android\Templates\AndroidManifest.xml> and comment them.

|  |  |
| --- | --- |
| INTERNET | Always required |
| ACCESS\_NETWORK\_STATE | Always required (to know from where to get the data, if from cache or from internet - for example) |
| WRITE\_EXTERNAL\_STORAGE | Always required (for caching purposes) |
| ACCESS\_FINE\_LOCATION | Required if Geolocation API or Geolocation Domain is used |
| ACCESS\_COARSE\_LOCATION | Required if Geolocation API or Geolocation Domain is used |
| READ\_CONTACTS | Required if Addressbook API is used to read contacts |
| WRITE\_CONTACTS | Required if Addressbook API is used to save contacts |
| READ\_LOGS | Optional, for debugging purposes. |

More info about this permissions can be read at

<http://developer.android.com/reference/android/Manifest.permission.html>

## [Notes](#Notes)

Permission scheme depends on the Android version. As from Android Marshmallow, permissions are solicited one-by-one at runtime, and in previous versions, all grants are requested together at installation time.

`[imagen omitida: wiki id 31237]`
