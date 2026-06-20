---
title: "MiniApp external object in GeneXusMiniApps module"
source_id: 58514
source_url: https://wiki.genexus.com/commwiki/wiki?58514
genexus_version: "18"
---

# MiniApp external object in GeneXusMiniApps module

The MiniApp external object (located in the [GeneXusMiniApps Module](https://wiki.genexus.com/commwiki/wiki?52076)) can be used within a Mini App to execute certain methods and allow the Mini App to interact with its environment (the Super App in which it is running).

`[imagen omitida: wiki id 58515]`

### [Properties](#Properties)

#### [**CurrentMiniAppId**](#CurrentMiniAppId)

Gets the Mini App identifier. It can be useful for Mini App development when a KB Object is shared among multiple Mini Apps or between a Mini App and a standalone App within the same Knowledge Base (KB).

### [Methods](#Methods)

#### [**Exit method**](#Exit+method)

Exits the Mini App and returns to the host application (the Super App). When returning to the Super App (GeneXus ones), it performs a GoHome().

### [Considerations](#Considerations)

The MiniApp External Object is available only when a Mini app is loaded inside a Super app. If called in another context, all methods will fail.

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)


|  |
| --- |
| **Backlinks** |
| [GeneXusMiniApps Module](https://wiki.genexus.com/commwiki/wiki?52076) |

---
