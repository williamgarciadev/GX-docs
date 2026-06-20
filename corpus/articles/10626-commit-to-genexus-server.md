---
title: "Commit to GeneXus Server"
source_id: 10626
source_url: https://wiki.genexus.com/commwiki/wiki?10626
genexus_version: "18"
---

# Commit to GeneXus Server

The ***Commit to Server*** operation is executed to update a Knowledge Base hosted in a [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance.

Once a set of changes is completed, the Developer must publish them. Publishing changes is called ***Commit***and requires the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) to be active and accessible to the Developer.

### [Step by step](#Step+by+step)

To perform a Commit operation the Developer must follow the steps below:

1) Select the *Knowledge Manager*>*Team Development* menu option to open the [Knowledge Manager Team Development](https://wiki.genexus.com/commwiki/wiki?20864) dialog and choose the **Commit** tab.

`[imagen omitida: wiki id 31935]`

2) Press the ***Refresh*** button `[imagen omitida: wiki id 31936]` to load the set of objects that have been changed locally since the last C*ommit* operation.

3) The Developer can **select/deselect** the objects to C*ommit*.

4) The developer must type a *Comment* detailing what these changes mean (explaining the changes to another Developer). As a rule of thumb write a simple, one-line sentence that briefly explains the Commit and then write a few more sentences providing greater detail.

`[imagen omitida: wiki id 31937]`

5) Click the *Commit* button to finish. All the changes will be packaged and sent to the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) and the Knowledge Base will be updated. Use the *Team Development output* section (Output window) to verify that the *Commit* operation was successful.

**Note:**

* Knowledge Base Environment and Version properties can also be included in the Commit operation.
* Filters can be applied using the Filter option:

`[imagen omitida: wiki id 31940]`

### [Add to ignored objects option](#Add+to+ignored+objects+option)

Using the *Add to ignored objects* option from the contextual menu the Developer will be able to ignore objects so that they are not sent. These will be included in the list in the *Ignored Objects* tab and left there until they are (explicitly) recovered in a future Commit operation.

`[imagen omitida: wiki id 31938]`

`[imagen omitida: wiki id 31939]`

**Note:** Filters can be applied using the Filter option:

### [Pending Commits and Ignored Objects columns](#Pending+Commits+and+Ignored+Objects+columns)

| Column | Description |
| --- | --- |
| Selection Checkbox | Used to select whether the object is included in the Commit operation. |
| Action Icon | Displays an icon showing the action performed to the object. |
| Object Icon | Displays the icon of the object. |
| Name | Displays the [Name property](https://wiki.genexus.com/commwiki/wiki?6985) of the object. |
| Type | Displays the [object Type property](https://wiki.genexus.com/commwiki/wiki?10444). |
| Description | displays the [Description property](https://wiki.genexus.com/commwiki/wiki?7446) of the object. |
| Modified On | Last date when the object was modified—causing to be included in the pending commit list. This property column does not behave as the "Modified On" of the [History](https://wiki.genexus.com/commwiki/wiki?3178) dialog. |
| Module | Module to which the object belongs to. |
| Action | the action performed to the object, the possible values are: Inserted, Modified or Deleted. |
| Last Synchronized | Displays the date of the last synchronization, in other words, the time where the object was Updated or created by the [Create Knowledge Base from GeneXus Server](https://wiki.genexus.com/commwiki/wiki?22416) operation. |
| User | User who performed the last modification. |

### [Remind me to move changes to...](#Remind+me+to+move+changes+to...)

Please see [Bring Changes Reminder](https://wiki.genexus.com/commwiki/wiki?20145,,) to understand fully how to use this feature.

The Commit Number can be used to [Bring Changes](https://wiki.genexus.com/commwiki/wiki?20912,,)/[Bring All Changes](https://wiki.genexus.com/commwiki/wiki?21056,,) from another [Development Version](https://wiki.genexus.com/commwiki/wiki?5684)

### [See also](#See+also)

[ChangeSets in GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31775)  
[Partial Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31746,,)  
[Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627)  
[Revert Object Operation](https://wiki.genexus.com/commwiki/wiki?17480,,)  
[Warn When Adding Or Removing Objects From Selection Property](https://wiki.genexus.com/commwiki/wiki?21078)


|  |
| --- |
| **Backlinks** |
| [Blame in GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31190) |
| [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
|
|
| [Knowledge Manager Team Development](https://wiki.genexus.com/commwiki/wiki?20864) |
| [Pending Commit](https://wiki.genexus.com/commwiki/wiki?24821) |
| [Send Knowledge Base to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10215) | [Category:Team Development with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9297) |
| [Update behavior property](https://wiki.genexus.com/commwiki/wiki?31158) | [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |
| [Versioning the application by Modules](https://wiki.genexus.com/commwiki/wiki?20937) | [Versioning the application to manage the different stages of Validation or Approval](https://wiki.genexus.com/commwiki/wiki?20938) | [Warn When Adding Or Removing Objects From Selection Property](https://wiki.genexus.com/commwiki/wiki?21078) |

---
