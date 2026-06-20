---
title: "GAM - Reprocess Permissions Option"
source_id: 36013
source_url: https://wiki.genexus.com/commwiki/wiki?36013
genexus_version: "18"
---

# GAM - Reprocess Permissions Option

The menu option: Tools -> GAM -> Reprocess Permissions impacts the GAM permissions (which are already generated), without the need to Rebuild All of the objects in the Knowledge Base.

A use case of this Option is, for example, when there is a Knowledge Base(KB) with GAM that has certain Objects with Authorization (Objects with Integrated Security Level property: True).

If in that KB the GAM Database (DB) is changed to another existing DB, when executing the Reprocess Permissions option, the permissions that were already generated for the previous DB are impacted on the new DB.

These permissions keep the same GUID they had when generated.

## [See also](#See+also)

[GAM - Initialize Metadata option](https://wiki.genexus.com/commwiki/wiki?16287)

[GAM - Applications Registration option](https://wiki.genexus.com/commwiki/wiki?16288)

[GAM - Create tables option](https://wiki.genexus.com/commwiki/wiki?16588)


|  |
| --- |
| **Backlinks** |
| [GAM options in GeneXus toolbar](https://wiki.genexus.com/commwiki/wiki?19947) |

---
