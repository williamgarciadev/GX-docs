---
title: "Steps to build with GeneXus 18 a KB of GeneXus 17 or prior"
source_id: 52345
source_url: https://wiki.genexus.com/commwiki/wiki?52345
genexus_version: "18"
---

# Steps to build with GeneXus 18 a KB of GeneXus 17 or prior

This document describes the steps you need to follow to update a KB from GeneXus 17 to GeneXus 18.

If you're converting from previous versions, please refer first to: [Converting Knowledge Bases to GeneXus 16, 17 or higher](https://wiki.genexus.com/commwiki/wiki?10903,,).

## [Steps](#Steps)

To open a Knowledge Base ([KB](https://wiki.genexus.com/commwiki/wiki?2428)) that is already in [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,) with [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066), follow these steps:

**0)** First, take into account the [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080).

**1.A)** If your KB is not connected to a [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31337,,),

* [Back it up](https://wiki.genexus.com/commwiki/wiki?5735).
* Open it with GeneXus 18.

**1.B)** If your KB is connected to a GeneXus Server,

**1.B.1)** If you decide to install GeneXus Server on another instance,

* Follow the steps described in [Install new GeneXus Server Instance](https://wiki.genexus.com/commwiki/wiki?21510,,).
* Next, migrate the KB following this document: [Migrating a Knowledge Base between GeneXus Server instances](https://wiki.genexus.com/commwiki/wiki?18170,,).

   **1.B.2)** If you update your GeneXus Server 17 instance to GeneXus Server 18,

* Update the instance to GeneXus Server 18 following the steps described in [Update an existing GeneXus Server Instance](https://wiki.genexus.com/commwiki/wiki?21510,,).
* Open your KB with GeneXus 18.

**2)** Prepare for Build

* If you use GXtest, you may have a folder named GXtest with the objects Runner and TestReferences. You must delete them since they are not used anymore and won't compile. Follow the steps described in [New tests runner](https://wiki.genexus.com/commwiki/wiki?49806,,).

**3)** [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) (\*)

If your KB uses [GAM](https://wiki.genexus.com/commwiki/wiki?24746) or [GXflow](https://wiki.genexus.com/commwiki/wiki?43435), this process may update the associated database schemas.

If your KB uses GAM, and you still do not want to [migrate to Unanimo](https://wiki.genexus.com/commwiki/wiki?51821), [change GAM Settings](https://wiki.genexus.com/commwiki/wiki?21973) to not import the GAM frontend.

(\*) If you generate for Android, iOS, or Angular,

* Delete the <Environment Directory>\mobile folder before doing a Rebuild with GeneXus 18.

To compile iOS Native Apps, follow the steps below on your device with Mac OS:

* Delete the content (for each user of the Mac that is about to compile code)

```
/Library/Developer/Xcode/DerivedData
```

* Delete the “build” folder that is in the following location:

```
/Projects/<KB_NAME>/<ENVIRONMET_NAME>/<MAIN_NAME>
```

**4)** Check out Navigation changes using the [Navigation Comparer](https://wiki.genexus.com/commwiki/wiki?3217,,). Note that navigations may change due to several navigation improvements.

**5)** Test it.

**6)** If the KB is connected to GeneXus Server, commit the changes.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Keys for a successful migration to GeneXus 18](https://www.genexus.com/en/products/genexus/live-2022/legacy-modernization-digital-transformation/keys-for-a-successful-migration-to-genexus-18)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 adoption plan](https://wiki.genexus.com/commwiki/wiki?52499) |
| [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080) | [GeneXus 18 Compatibility Section (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53520) |

---
