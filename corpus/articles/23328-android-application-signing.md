---
title: "Android Application Signing"
source_id: 23328
source_url: https://wiki.genexus.com/commwiki/wiki?23328
genexus_version: "18"
---

# Android Application Signing

This set of properties are used to sign the applications (the *\*.apk* binary file).

|  |  |  |
| --- | --- | --- |
| **Property** | **Description** | **Default value** |
| **[Key Store File](https://wiki.genexus.com/commwiki/wiki?19108)** | The filepath to the *\*.keystore* file, whose value is set on [Key Store File property](https://wiki.genexus.com/commwiki/wiki?19108). | *C:\<KB\_model>\<Environment>\mobile\Android\<Main\_object>\my-release-temp-key.keystore* |
| **[Key Alias](https://wiki.genexus.com/commwiki/wiki?19112)** | The alias of the *\*.keystore* file, whose value is set on [Key Alias property](https://wiki.genexus.com/commwiki/wiki?19112). | *alias\_name* |
| **Store Password** | The key store password to access the \*.keystore file, whose value is set on Store Password property. | *artech* |
| **Key Password** | The key password to access a particular key pair's private key. | *artech* |

The developer [must change](https://wiki.genexus.com/commwiki/wiki?19055) this values when the application is in Production (the default certificates are for prototyping purposes only). Once the application is signed with this configuration, every future update must require the same certificates (i.e. when is [published in Google Play](https://wiki.genexus.com/commwiki/wiki?15948) or distributed internally).

## [Compatibility](#Compatibility)

**Alert**: As of [GeneXus 15 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?32886,,) there is a new default setting. Google Play will refuse your application if the developer tries to upload it with this certificates.

|  |  |
| --- | --- |
| **Property** | **Default value** |
| **[Key Store File](https://wiki.genexus.com/commwiki/wiki?19108)** | *C:\<genexus\_dir>\Android\debug.keystore* |
| **[Key Alias](https://wiki.genexus.com/commwiki/wiki?19112)** | *androiddebugkey* |
| **Store Password** | *android* |
| **Key Password** | *android* |

Those developers who have applications already in Production without change the previous default certificates, as of [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,) they must set these properties with a **legacy** values (described in the below table).

|  |  |
| --- | --- |
| **Property** | **Legacy value** |
| **[Key Store File](https://wiki.genexus.com/commwiki/wiki?19108)** | *C:\<GeneXus\_Dir>\Android\legacy.keystore* |
| **[Key Alias](https://wiki.genexus.com/commwiki/wiki?19112)** | *alias\_name* |
| **Store Password** | *artech* |
| **Key Password** | *artech* |

## [Notes](#Notes)

* As of [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,) this set of properties are moved from [Smart Devices Generator properties](https://wiki.genexus.com/commwiki/wiki?14451) to [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817). If a Knowledge Base is migrated to newer versions, Main object properties will inherit Generator properties.
* As of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,) this set of properties are available only if the [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) has *Distribution* value.


|  |
| --- |
| **Backlinks** |
| [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) | [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) |
| [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
