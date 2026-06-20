---
title: "Import Type property"
source_id: 5612
source_url: https://wiki.genexus.com/commwiki/wiki?5612
genexus_version: "18"
---

# Import Type property

The Import Type property applies to objects in the Export file that already exist in the target Knowledge Base. It is intended to select what objects are going to be imported by comparing the modification date in the Export file and in the Knowledge Base.
Values:
Different objects ->Only objects in the Export file that have a different modification date than the corresponding objects in the Knowledge Base are imported.
Newer objects ->Only objects in the Export file that are newer (i.e. their modification date is more recent) than the corresponding objects in the Knowledge Base are imported.
All objects ->All the objects in the Export file are imported. The modification date is not taken into account.

### [Scope](#Scope)

**Level:** [Knowledge Manager -> Import](https://wiki.genexus.com/commwiki/wiki?3179)

### [Description](#Description)

Export files may include either objects that are in the target Knowledge Base or objects that are not in it. The Import Type property applies to objects in the Export file that already exist in the target Knowledge Base. It is intended to select what objects are going to be imported by comparing the [modification date](https://wiki.genexus.com/commwiki/wiki?5613,,) in the Export file and in the Knowledge Base.

Modification date comparisons may be used to improve Import process performance and/or avoid overwriting objects with older versions.

### [See Also](#See+Also)

[Import Dialog Options](https://wiki.genexus.com/commwiki/wiki?5571)


|  |
| --- |
| **Backlinks** |
| [Import Dialog Options](https://wiki.genexus.com/commwiki/wiki?5571) |

---
