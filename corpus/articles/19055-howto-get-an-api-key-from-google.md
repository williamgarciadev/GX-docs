---
title: "HowTo: Get an API Key from Google"
source_id: 19055
source_url: https://wiki.genexus.com/commwiki/wiki?19055
genexus_version: "18"
---

# HowTo: Get an API Key from Google

This document explains how to get an API Key from Google and provides a brief overview about it.

To use Google Maps in any compiled Android application, you must have an API Key from Google. Otherwise, maps will not be shown when using the [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) or [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644).

**Note**: This is not required when prototyping the application through [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974), as it already has its own Maps API Key.

By default, the generated app uses a default Android debug-certificate to [sign the application](https://wiki.genexus.com/commwiki/wiki?23328) when compiling.  
That allows you to install the application on devices, directly with the *\*.**apk* file, but not through [Google Play](https://wiki.genexus.com/commwiki/wiki?15948) (since [GeneXus 15 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?32886,,)), unless a custom certificate is created.

However, to use Google Maps service you need a *special* certificate called **Map API Key**, different from the previous one. This particular key is linked to the specific [package name](https://wiki.genexus.com/commwiki/wiki?17814) and the certificate mentioned before, in order to restrict the access. 

### [How can this API key be obtained?](#How+can+this+API+key+be+obtained%3F)

This section explains how to obtain that key for your application.

#### [**Step 1. Retrieve the fingerprint**](#Step+1.+Retrieve+the+fingerprint)

The first thing to know is the fingerprint of the certificate that will sign the application (this is not required if while you are prototyping with the debug certificate provided by GeneXus).  
To see this fingerprint run the following command, using the keystore provided by Android.

```
keytool -list -v -keystore <your_release_key.keystore> -alias <your_alias_name> -storepass <your_store_pass> -keypass <your_key_pass>
```

**Where:**

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Value** | **Description** | **Default ([Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328))** |
|  | *<your\_release\_key.keystore>* | The filepath to the *\*.keystore* file, whose value is set on [Key Store File property](https://wiki.genexus.com/commwiki/wiki?19108). | *C:\Users\<user>\.android\debug.keystore* |
|  | *<your\_alias\_name>* | The alias of the *\*.keystore* file, whose value is set on [Key Alias property](https://wiki.genexus.com/commwiki/wiki?19112). | *androiddebugkey* |
|  | *<your\_store\_pass>* | The key store password to access the \*.keystore file, whose value is set on Store Password property. | *android* |
|  | *<your\_key\_pass>* | The key password to access a particular key pair's private key. | *android* |

This command tool will print an output like this:

```
Alias name: androiddebugkey
Creation date: Dec 01, 2016
Entry type: PrivateKeyEntry
Certificate chain length: 1
Certificate[1]:
Owner: CN=Android Debug, O=Android, C=US
Issuer: CN=Android Debug, O=Android, C=US
Serial number: ********
Valid from: Mon Jan 01 08:04:04 UTC 2013 until: Mon Jan 01 18:04:04 PST 2033
Certificate fingerprints:
     MD5:  AE:9F:95:D0:A6:86:89:BC:A8:70:BA:34:FF:6A:AC:F9
     SHA1: 5F:BD:E1:6B:93:D6:5A:01:D2:C2:43:04:DD:2D:3D:93:A9:AD:C8:E8
     Signature algorithm name: SHA1withRSA
     Version: 3
```

The SHA1 value corresponds to the fingerprints.

**Note**: The keytool program is installed in the */bin* directory of Java JDK

#### [**Step 2. Get the API Key**](#Step+2.+Get+the+API+Key)

Go to [Google API](https://console.developers.google.com/apis/) console and create a new API Key for your application.  
The process to obtain that key can be done accessing to:

*API Manager*> *Credentials* > *Create Credential* > *API Key.*

`[imagen omitida: wiki id 33140]`

#### [**Step 3. Adding access restrictions**](#Step+3.+Adding+access+restrictions+)

The fingerprint from Step 1 allows adding exclusive access for this application. The following steps explain how to do it.

**3.1 Select the API key**

Click on the API Key created in Step 2 from the list.  
`[imagen omitida: wiki id 33136]`

**3.2 Check Android apps**

On the *Key restriction* section, check for Android apps option.  
`[imagen omitida: wiki id 33137]`

**3.3 Add package/fingerprint**

Click on "*Add new package name and fingerprint*" button, and complete the fields with your [package name](https://wiki.genexus.com/commwiki/wiki?17814) and fingerprint (from Step 1)  
`[imagen omitida: wiki id 33138]`

**3.4. Save your changes**

#### [**Step 4. Enable the API**](#Step+4.+Enable+the+API)

Depending on the case, it is necessary to enable some API,  such as: Geolocation API and/or Directions API and/or Maps Static API, etc  into the Google Apikey.  
`[imagen omitida: wiki id 47742]`

#### [**Step 5. Set GeneXus's property**](#Step+5.+Set+GeneXus%27s+property)

Finally, set the [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) with the value of Google API console (notice that there is not longer a warning icon).  
`[imagen omitida: wiki id 33139]`

**Note:**

If you have applications in production with the previous default settings (i.e. the *\*.apk* file signed with Artech credentials), you must generate the fingerprint with the legacy values.

|  |  |
| --- | --- |
| **Value** | **Default** ([Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328), since  [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,)) |
| **<your\_release\_key.keystore>** | *C:\<GeneXus\_Dir>\Android\legacy.keystore* |
| **<your\_alias\_name>** | *alias\_name* |
| **<your\_store\_pass>** | *artech* |
| **<your\_key\_pass>** | *artech* |

### [See Also](#See+Also)

[Google Maps - First steps](https://developers.google.com/maps/documentation/android/start)  
[Google Maps - Get API Key](https://developers.google.com/maps/documentation/android-api/signup)


|  |
| --- |
| **Backlinks** |
| [Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328) | [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) |
| [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) | [HowTo: Configure Google Places API in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?30810) | [HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948) | [KB:Showcase - GeoCity](https://wiki.genexus.com/commwiki/wiki?49231) |

---
