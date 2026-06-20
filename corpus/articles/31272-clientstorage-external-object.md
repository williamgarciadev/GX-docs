---
title: "ClientStorage external object"
source_id: 31272
source_url: https://wiki.genexus.com/commwiki/wiki?31272
genexus_version: "18"
---

# ClientStorage external object

Module to store information (pairs of key-values) locally that can be accessed from the client even without connectivity.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [Set method](#Set+method)

It saves the received value associated with the specified key. If it is applied consecutive times to the same key, its value is the latest assigned.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Key:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777), Value:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [SecureSet method](#SecureSet+method)

Analogous to the Set method, but it persists encrypted data.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Key:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777), Value::[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [Remove method](#Remove+method)

Deletes the stored value for the given key. If the key does not exist, the method has no effect.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Key:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [Get method](#Get+method)

Gets the stored value for the given key. If the key does not exist, it returns an empty string.

|  |  |
| --- | --- |
| **Return value** | [Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) |
| **Parameters** | Key:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [Clear method](#Clear+method)

Clears all pairs of key-values stored in the device.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

## [Events](#Events)

It does not have any.

## [Example](#Example)

This API is useful, for instance, when the application needs to save some user settings in the device.

```
Event 'ConfirmHomeGeolocation'
  Composite
     ClientStorage.Set('HomeGeolocation', &Geolocation)
     CustomerPanel()
  EndComposite
EndEvent

Event ClientStart
  Composite
     &Geolocation = ClientStorage.Get('HomeGeolocation')
     If not &Geolocation.IsEmpty()
          CustomerPanel()
     EndIf
  EndComposite
EndEvent
```

## [Notes](#Notes)

* ClientStorage API methods apply to both Online and Offline Smart Devices applications.
* The stored values persist even if the application is closed or the user logs off. (Note that [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) expires when the app is closed.)
* The application stores the information in the device, so you can only use this API in [offline procedures](https://wiki.genexus.com/commwiki/wiki?6293) and events executed on the device.
* When the developer uses Set and SecureSet methods for the same key, the persisted value it will be associated with the last method invoked.
* Get and Remove methods are shared with both Set methods.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), Angular |


|  |
| --- |
| **Backlinks** |
| [GAM - One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50664) | [GAM - Time Based One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50708) |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
