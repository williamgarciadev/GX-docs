---
title: "Update From GeneXus Server"
source_id: 10627
source_url: https://wiki.genexus.com/commwiki/wiki?10627
genexus_version: "18"
---

# Update From GeneXus Server

The *Update From Server* operation allows incorporating to the local Knowledge Base those changes made in the Server Knowledge Base since the last *Update From Server* operation.

### [Step by step](#Step+by+step)

To perform an Update operation, the Developer must follow the steps below:

1) Select the *Knowledge Manager*->*Team Development* menu option to open the [Knowledge Manager Team Development](https://wiki.genexus.com/commwiki/wiki?20864) dialog and choose the **Update** tab.

`[imagen omitida: wiki id 36760]`

**Note:** Remember that by double-clicking upon an object the comparer window will be open showing the differences between the object's local content and the server one.

2) Select the *Update* option to incorporate all the selected modifications into your local Knowledge Base (those objects which weren't selected in the *Pending for Update* tab will not be updated). Check the *Team Development output window* to make sure the operation was completed successfully.

**Note:** Also, the Developer will be able to pick the group of properties to import from GeneXus Server by checking the *KB Properties CheckBox.*

### [Update To a specific revision](#Update+To+a+specific+revision)

If the Developer wants to update to a specific revision, at the top-right of the tab, he could change the revision to update from. The Developer could select any revision and update from it. Suppose your local Knowledge Base is at revision 10, but you want it to reflect the state which it had in revision 2 - then simply update to revision 2.

**Note:** By default, the update is compared to the last revision at GeneXus Server. The revisions mentioned above can be find in the Activity of the Knowledge Base in GeneXus Server.

### [Update Options](#Update+Options)

If any object fails to Update, GeneXus provides two options:

`[imagen omitida: wiki id 31945]`

1) **Fail on errors:** The entire operation is reverted, and no object gets modified.

In these cases, GeneXus may automatically deselect the objects with errors, so that the Developer can easily retry a new update which doesn't include the failed objects. By default, GeneXus will ask for confirmation before automatically deselecting the objects with errors.

Using the ***Automatically deselect objects after failed Update,***located Tool->Options->Team Development, the Developer will be able to configure this behavior.

`[imagen omitida: wiki id 31946]`

The possible values are:

* **Always**: Automatically deselect all the objects (and referenced objects) that fail on an update operation (without asking for user confirmation)
* **Never**: Never deselect objects.
* **Ask**: Ask the user each time.

2) **Continue on errors:** Those objects which were successfully updated are kept while the failed objects' behavior is defined by the Developer.

For more information, please refer to [Update behavior](https://wiki.genexus.com/commwiki/wiki?31158).

### [See Also](#See+Also)

[Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626)


|  |
| --- |
| **Backlinks** |
| [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) |
| [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
|
|
| [History and Differences](https://wiki.genexus.com/commwiki/wiki?3178) | [Knowledge Manager Team Development](https://wiki.genexus.com/commwiki/wiki?20864) |
| [Preview Update](https://wiki.genexus.com/commwiki/wiki?17501) |
| [Send Knowledge Base to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10215) | [Show Differences](https://wiki.genexus.com/commwiki/wiki?17487) |
| [Category:Team Development with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9297) | [Update behavior property](https://wiki.genexus.com/commwiki/wiki?31158) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |
| [Versioning the application by Modules](https://wiki.genexus.com/commwiki/wiki?20937) | [Versioning the application to manage the different stages of Validation or Approval](https://wiki.genexus.com/commwiki/wiki?20938) | [Warn When Adding Or Removing Objects From Selection Property](https://wiki.genexus.com/commwiki/wiki?21078) |

---
