---
title: "File Extensions Whitelisting"
source_id: 45554
source_url: https://wiki.genexus.com/commwiki/wiki?45554
genexus_version: "18"
---

# File Extensions Whitelisting

## [ExtensionsWhiteList](#ExtensionsWhiteList)

This object is meant to be helpful for filtering files by their extensions. It is not a good enough measure for most cases; other security measures and use cases analysis are advised.

ExtensionsWhiteList object can be used in conjunction with [SFTP](https://wiki.genexus.com/commwiki/wiki?44965) and [FTPS](https://wiki.genexus.com/commwiki/wiki?45274) Modules throughout its connection options.

### [SetExtension](#SetExtension)

```
ExtensionsWhiteList.SetExtension(extension)
```

* Input extension: Character(20) available extension
* Returns void

## [Availability](#Availability)

[GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,)


|  |
| --- |
| **Backlinks** |
| [Connection Options FTPS](https://wiki.genexus.com/commwiki/wiki?45278) | [Connection Options SFTP](https://wiki.genexus.com/commwiki/wiki?44967) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
