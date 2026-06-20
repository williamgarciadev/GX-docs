---
title: "App Transport Security property group"
source_id: 29368
source_url: https://wiki.genexus.com/commwiki/wiki?29368
genexus_version: "18"
---

# App Transport Security property group

This group of properties is available for Main Smart Device objects and is located under the App Transport Security properties group.

Allows insecure communication with particular servers.

## [**Introduction**](#Introduction)

As from iOS 9, all network connections must be secure unless stated otherwise. The feature is known as App Transport Security, and is described by Apple documentation:

> App Transport Security is a feature that improves the security of connections between an app and web services. The feature consists of default connection requirements that conform to best practices for secure connections. Apps can override this default behavior and turn off transport security.

In the case of Android, this is fulfilled from Android 9 version. [Official notes:](https://android-developers.googleblog.com/2018/04/protecting-users-with-tls-by-default-in.html?m=1)

> Android is committed to keeping users, their devices, and their data safe. One of the ways that we keep data safe is by protecting all data that enters or leaves an Android device with Transport Layer Security (TLS) in transit. As we announced in our Android P developer preview, we're further improving these protections by preventing apps that target Android P from allowing unencrypted connections by default.

These properties give the developer the ability to override the default OS settings.

## [**Properties**](#Properties)

### [Allows Arbitrary Loads property](#Allows+Arbitrary+Loads+property)

#### [Values](#Values)

|  |  |
| --- | --- |
| *False* | Each non-secure connection must be declared in the Exception Domains property |
| *True* | Turns off the SSL checks for the application, except for the exception domains (see property below) |

#### [The default value is *False*.](#The+default+value+is+False.)

Setting this property to *True* may be easier to configure, but disabling this security feature is not recommended.

**Note:** When working with the Android generator, this property allows the HTTP cleartext communication.

### [Allows Arbitrary Loads In Media property](#Allows+Arbitrary+Loads+In+Media+property)

It's analogous to *Allow Arbitrary Loads property* but restricted to media content.

### 

### [Allows Arbitrary Loads In Web Content property](#Allows+Arbitrary+Loads+In+Web+Content+property)

It's analogous to *Allow Arbitrary Loads property* but restricted to web content.

### [Allows Local Networking property](#Allows+Local+Networking+property)

It's analogous to *Allow Arbitrary Loads property* but restricted to load local resources.

### [Exception Domains property](#Exception+Domains+property)

It is a list of domains that do not conform to the requirements.

For each exception domain, a set of properties must be configured.

`[imagen omitida: wiki id 29370]`

#### 

#### [Domain Name](#Domain+Name)

The name of the domain.

Example: www.testdomain.com

#### 

#### [Include Subdomains](#Include+Subdomains)

Boolean value for applying the overrides to all subdomains of the top-level domain.

Example: if the Domain Name is "testdomain.com" then "www.testdomain.com" and "sample.testdomain.com" will both use these settings.

*False* is the default value.

#### 

#### [Third Party](#Third+Party)

If the domain is not controlled by the developer, it must be set to *True*. For example, for domains external to the application.

*False*is the default value.

#### 

#### [Minimum TLS Version](#Minimum+TLS+Version)

Specifies the minimum TLS version for the connections.

The default value is *1.2*.

#### 

#### [Requires Forward Secrecy](#Requires+Forward+Secrecy)

Set to *False* if the connection does not allow *forward secrecy*.

*True*is the default value

#### 

#### [Allow Insecure HTTP Loads](#Allow+Insecure+HTTP+Loads)

Boolean value for overriding the requirement that all connections use HTTPS. Use this key to access domains with no certificate, or with an error for a self-signed, expired, or hostname-mismatch certificate.

*False*is the default value.

### 

#### [Requires Certificate Transparency](#Requires+Certificate+Transparency)

A Boolean value to indicate if [Certificate Transparency](https://www.certificate-transparency.org/) is required.

*False*is the default value.

### [Note](#Note)

* In some cases, GeneXus automatically adds the corresponding exceptions to the app's configuration (i.e. Google Analytics, Facebook, etc).

## 

## [**Troubleshooting**](#Troubleshooting)

If these properties are not configured correctly, the application will not work as expected. To be more specific, some network connections may return(1) something similar to the following:

```
    "requestFail": {
        "url": "https://www.your.domain.com/some/url",
        "error": {
            "domain": "NSURLErrorDomain",
            "localizedDescription": "An SSL error has occurred and a secure connection to the server cannot be made.",
            "code": -1200
        }
    }
```

This means that the network domain *www.your.domain.com* does not support the configuration required by iOS 9.

You can use the *nscurl* utility in your OS X installation to check the domain. From a Terminal window:

```
/usr/bin/nscurl --ats-diagnostics https://www.your.domain.com
```

This tool runs a series of checks and will output the settings you need for the domain.

For example, if the output looks as shown below (only a part of it is shown here):

```

TLSv1.1 with PFS disabled and insecure HTTP allowed
2015-10-22 15:10:34.979 nscurl[50131:341576] CFNetwork SSLHandshake failed (-9801)
2015-10-22 15:10:35.038 nscurl[50131:341576] CFNetwork SSLHandshake failed (-9801)
2015-10-22 15:10:35.053 nscurl[50131:341576] CFNetwork SSLHandshake failed (-9801)
2015-10-22 15:10:35.054 nscurl[50131:341576] NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9801)
Result : FAIL
---
TLSv1.0 with PFS disabled and insecure HTTP allowed
Result : PASS
---
```

In GeneXus, you'll have to set *TLS* to *1.0* and *Requires Forward Secrecy* to *False*.

---

(1) When executed in Debug mode from Xcode, the text is shown in the Console.

**Note**: nscurl requires Mac OS 10.11 (El Capitan) (*Ref. <http://stackoverflow.com/questions/32723623/how-do-i-install-nscurl-on-mac-os-x-10-10-yosemite>*)

## [**Availability**](#Availability)

Available since [GeneXus X Evolution 3 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?29164,,) for iOS.

Available since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,) for Android.

---

|  |
| --- |
| **Backlinks** |
| [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) | [Dynamic Services URL property](https://wiki.genexus.com/commwiki/wiki?20366) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
