---
title: "Synchronization.ResetOfflineDatabase method"
source_id: 29785
source_url: https://wiki.genexus.com/commwiki/wiki?29785
genexus_version: "18"
---

# Synchronization.ResetOfflineDatabase method

### [Syntax](#Syntax)

Synchronization**.ResetOfflineDatabase**()

### [Description](#Description)

It returns the local database content of the offline App to its initial state. That means:

* restoring the [preloaded database](https://wiki.genexus.com/commwiki/wiki?22298) if it exists, or
* executing a Create Database in order to empty database tables.

This behavior is the same that happens when the [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) returns the message *Metadata error code received. Code: 2*. In this case the database is automatically restored and a new Receive operation is performed.

**Note:** The method can only be used inside a [Client-side Event](https://wiki.genexus.com/commwiki/wiki?24332)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) |
| **Platforms** | Android, Apple iOS |

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?29770,,)

### [See also](#See+also)

* [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |
| [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) |

---
