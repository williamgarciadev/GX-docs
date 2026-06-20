---
title: "ClientStorage.Get method"
source_id: 24134
source_url: https://wiki.genexus.com/commwiki/wiki?24134
genexus_version: "18"
---

# ClientStorage.Get method

Gets the stored value for the given key.

### [Syntax](#Syntax)

**ClientStorage.Get(**<*Key*>**)**

Where:

<key> is the identifier of the value that we want to get, it has to be Strings.

### [Type returned](#Type+returned)

Character

### [Example](#Example)

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

This feature is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [Scope](#Scope)

|  |  |
| --- | --- |
| Objects: | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087), [Offline Procedures](https://wiki.genexus.com/commwiki/wiki?6293) |
| Platforms: | [Android platform](https://wiki.genexus.com/commwiki/wiki?14453), [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See also](#See+also)

* [ClientStorageAPI external object](https://wiki.genexus.com/commwiki/wiki?24132,,)
* [ClientStorage.Set method](https://wiki.genexus.com/commwiki/wiki?24133)
* [ClientStorage.Remove method](https://wiki.genexus.com/commwiki/wiki?24136)
* [ClientStorage.Clear method](https://wiki.genexus.com/commwiki/wiki?24135)


|  |
| --- |
| **Backlinks** |
| [ClientStorage.Clear method](https://wiki.genexus.com/commwiki/wiki?24135) | [ClientStorage.Remove method](https://wiki.genexus.com/commwiki/wiki?24136) | [ClientStorage.Set method](https://wiki.genexus.com/commwiki/wiki?24133) |

---
