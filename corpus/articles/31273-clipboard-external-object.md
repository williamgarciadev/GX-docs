---
title: "Clipboard external object"
source_id: 31273
source_url: https://wiki.genexus.com/commwiki/wiki?31273
genexus_version: "18"
---

# Clipboard external object

One of the most basic ways of interaction between applications is by using the Clipboard.  
One application puts something (text, image, blob) in the Clipboard and makes it available to the other applications.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [SetText](#SetText)

This method is used to copy text into the clipboard, replacing previously stored content.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Data:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [GetText](#GetText)

Use this method to get a copy of the string that the clipboard contains. It returns an empty string if no text is in the Clipboard.

|  |  |
| --- | --- |
| **Return value** | [Character(100)](https://wiki.genexus.com/commwiki/wiki?6777) |
| **Parameters** | None |

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

## [Availability](#Availability)

As of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

## [See also](#See+also)

* [Clipboard.setText method](https://wiki.genexus.com/commwiki/wiki?23957)
* [Clipboard.getText method](https://wiki.genexus.com/commwiki/wiki?23958)


|  |
| --- |
| **Backlinks** |
| [Clipboard.getText method](https://wiki.genexus.com/commwiki/wiki?23958) | [Clipboard.setText method](https://wiki.genexus.com/commwiki/wiki?23957) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
