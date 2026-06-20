---
title: "Pending Commit"
source_id: 24821
source_url: https://wiki.genexus.com/commwiki/wiki?24821
genexus_version: "18"
---

# Pending Commit

An object is said to be '*Pending for commit*' or in the list of 'Pending objects' when the object has been modified since it was [Synchronized with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?24822,,).  
This state has meaning only when the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is linked to a GeneXus Server.

When an object is *Pending for commit* it will be displayed in the "Pending Commits" List of the [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) dialog. This will allow you to [Revert](https://wiki.genexus.com/commwiki/wiki?17480,,) all changes made to it or to Commit its changes to the Knowledge Base hosted in the GeneXus Server instance to share those changes with the rest of your team.

### [Object Comparison](#Object+Comparison)

Take into account that not all the changes made to the object will be marked as *pending for commit*. In particular, the order of the elements in the Structure Comparison (such as Transaction structure, SDT, External Object, Theme) is not consciously considered significant order changes in the comparison. It means that changing a structure order from A, B, C to A, C, B) will not mark it as modified and so as *pending for commit*.

This is the default behavior, changing the order of elements in any Structure Editor does not leave the object modified for commit; if you need to mark the object to be committed later; it is necessary to make a specific modification, modify

* some property of the object
* add or remove any item
* modify any element property
* any other modification.

### [See Also](#See+Also)

[Pending Update](https://wiki.genexus.com/commwiki/wiki?24830,,)  
[Object Synchronized with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?24822,,)


|  |
| --- |
| **Backlinks** |
| [ChangeSets in GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31775) |
|

---
