---
title: "Native Mini App Cache Management and Update Policies"
source_id: 56775
source_url: https://wiki.genexus.com/commwiki/wiki?56775
genexus_version: "18"
---

# Native Mini App Cache Management and Update Policies

After the initial loading of a Native Mobile Mini App, its metadata is downloaded from the Mini App Center and stored in the Super App's cache. As a result, subsequent invocations of the Mini App will load almost instantly.

However, the cache may become invalid and need to be discarded under the following circumstances:

### [Automatic update due to version changes](#Automatic+update+due+to+version+changes)

When a new version of the Mini App becomes available in the Mini App Center, the metadata is downloaded again during the next load.

### [Automatically according to Super App Cache configuration](#Automatically+according+to+Super+App+Cache+configuration)

Within the [Super App object](https://wiki.genexus.com/commwiki/wiki?53457), specific properties can be configured to manage this behavior: [Maximum Mini apps count property](https://wiki.genexus.com/commwiki/wiki?50310) and [Number of days to keep property](https://wiki.genexus.com/commwiki/wiki?50311).

### [Programmatically using the Mini App Cache API](#Programmatically+using+the+Mini+App+Cache+API)

The functionality to manually manage the Mini Apps cache is provided in the [MiniApps External Object](https://wiki.genexus.com/commwiki/wiki?50959), which is included in the [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959). You can learn about the available methods in [GeneXus Super Apps Methods](https://wiki.genexus.com/commwiki/wiki?50959).

In any other case, the Mini App is kept in the cache indefinitely and the OS itself could remove it from the cache at its discretion because it is stored in a temporary directory.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |

---
