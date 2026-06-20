---
title: "History and Differences"
source_id: 3178
source_url: https://wiki.genexus.com/commwiki/wiki?3178
genexus_version: "18"
---

# History and Differences

GeneXus keeps track of every change made to every object.

You can right-click on an object and select the **History** option (for example, from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210)) or on a specific attribute (for example, from the [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661)) to view a list of all the previous versions of that object/attribute:

`[imagen omitida: wiki id 59643]`

You can open any revision, which will be displayed as read-only.

Right-clicking on two different revisions and selecting **Compare Selected Revisions** will compare them and show their differences.  
  
`[imagen omitida: wiki id 59644]`

In this example, the difference is that the Transaction [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) was set to True.

`[imagen omitida: wiki id 59645]`

There are other ways to compare revisions.

When you are viewing a list of versions, and you right-click on a certain revision, the contextual menu offers these options:

`[imagen omitida: wiki id 59646]`

If you choose **Select Left Side To Compare**, then you have to right-click on another revision and choose **Compare With <object> Revision: <nbr>**.

When viewing the History of an object, the **Created in** column indicates the KB Version in which each Revision was created.

For example, if you have the following KB Versions:

`[imagen omitida: wiki id 59648]`

In the following History corresponding to the Product [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) you can see:

`[imagen omitida: wiki id 59649]`

Revision 8 was **Created in** the 'KBProducts' version. Then, 'Version1' was created (frozen version). So, the **Current in**column indicates that revision 8 is in the 'KBProducts' and 'Version1' versions.

After that, the 'Upgrades for Version 1' version was created and the Product [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) was modified. So, for Revision 9, the **Created in** column shows 'Upgrades for Version 1'.

**Modified Date**: Represents the date when a user saved an object. This date is updated with every Save(1) performed and distributed upon exporting an object and importing it in another KB. This date is not linear because upon importing the object in another KB, it may be assigned an earlier Modified Date than the latest one.

**Revision Date**: Is the date when a revision was saved, whether by a user or by any process that caused the generation of a new revision. This date is a monotonically increasing value.

(1) The Merge operation is considered to be a save made by the user. This is because, even though it is automatic, the user is changing the object. Therefore, the [Bring Changes](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20912,,) operation and [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) will update the "Modified Date" when merging changes.

### [Comparing objects before importing them](#Comparing+objects+before+importing+them)

Teamwork is facilitated by anticipating impacts. Before importing an object, you can open it and even compare it to the last Revision in the active Version of the KB into which you are importing objects.

`[imagen omitida: wiki id 59650]`

**Note**: Each object's History at the local KB level remains only in that KB. It is not possible to transfer or merge History between KBs without using [GeneXus Server](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?31337,,).


|  |
| --- |
| **Backlinks** |
| [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) |
|

---
