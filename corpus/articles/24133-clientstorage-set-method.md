---
title: "ClientStorage.Set method"
source_id: 24133
source_url: https://wiki.genexus.com/commwiki/wiki?24133
genexus_version: "18"
---

# ClientStorage.Set method

It saves the received value associated with the specified key. Note that this value persists in the device, and it is possible to get it back whenever by using the [ClientStorage.Get method](https://wiki.genexus.com/commwiki/wiki?24134)

### [Syntax](#Syntax)

**ClientStorage.Set(**<Key>**,** <Value>**)**

Where:

*<key>* is the identifier of the <Value>, it has to be Strings

<*Value*> is the value that we want to save, it has to be Strings

### [Type returned](#Type+returned)

None

### [Example](#Example)

This API is useful, for instance, when the application needs to persist some user settings in the device.

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

### [Availability](#Availability)

This feature is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)

### [Scope](#Scope)

|
|  |

|  |  |
| --- | --- |
| Objects: | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087), [Offline Procedures](https://wiki.genexus.com/commwiki/wiki?6293) |
| Platforms: | [Android platform](https://wiki.genexus.com/commwiki/wiki?14453), [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See also](#See+also)

* [ClientStorageAPI external object](https://wiki.genexus.com/commwiki/wiki?24132,,)
* [ClientStorage.Get method](https://wiki.genexus.com/commwiki/wiki?24134)
* [ClientStorage.Remove method](https://wiki.genexus.com/commwiki/wiki?24136)
* [ClientStorage.Clear method](https://wiki.genexus.com/commwiki/wiki?24135)


|  |
| --- |
| **Backlinks** |
| [ClientStorage.Clear method](https://wiki.genexus.com/commwiki/wiki?24135) | [ClientStorage.Get method](https://wiki.genexus.com/commwiki/wiki?24134) | [ClientStorage.Remove method](https://wiki.genexus.com/commwiki/wiki?24136) |

---
