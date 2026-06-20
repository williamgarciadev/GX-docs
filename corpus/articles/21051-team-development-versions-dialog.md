---
title: "Team Development Versions Dialog"
source_id: 21051
source_url: https://wiki.genexus.com/commwiki/wiki?21051
genexus_version: "18"
---

# Team Development Versions Dialog

The purpose of the Team Development Version tab is to allow users to manage the [Knowledge Base Versions](https://wiki.genexus.com/commwiki/wiki?5680,,) of the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance from the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272).

Also, this section allows users to Bring Changes to the active local version from another [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) on the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911).

`[imagen omitida: wiki id 31962]`

The Versions Dialog allows users to:

* Create a new [Frozen Version](https://wiki.genexus.com/commwiki/wiki?5681) or [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) on the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance.
* Remove a  [Frozen Version](https://wiki.genexus.com/commwiki/wiki?5681) or [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) from the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance.
* Merge the local active version with the changes made on another [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) from the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) by using the [Bring All Changes](https://wiki.genexus.com/commwiki/wiki?21056,,) option.
* Create a local version from a remote version.

### Actions over a Development Version

Right-clicking on a [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) will display a menu:

`[imagen omitida: wiki id 31963]`

Where:

* [Bring All Changes](https://wiki.genexus.com/commwiki/wiki?21056,,) option will merge any changes made to that version with the local active version.
* Freeze option will create a [Frozen Version](https://wiki.genexus.com/commwiki/wiki?5681) from the selected [Development Version](https://wiki.genexus.com/commwiki/wiki?5684).
* Checkout Version will create a local version linked to this remote version
* Delete option (only available if it has not been frozen) will remove the [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) from the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance.

### [Actions over the Active Version](#Actions+over+the+Active+Version)

To show a menu only with the Freeze option, right-click on a [Development Version](https://wiki.genexus.com/commwiki/wiki?5684).

`[imagen omitida: wiki id 31964]`

### [Actions over a Frozen Version](#Actions+over+a+Frozen+Version)

If the user right-clicks on a [Frozen Version](https://wiki.genexus.com/commwiki/wiki?5681) a menu will be shown with the following options:

* New Version option. This action will create a [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) from the selected Frozen Version.
* Checkout Version option. This action creates a local version linked to this remote version.

`[imagen omitida: wiki id 31965]`

`[imagen omitida: wiki id 36792]`

* If the user wants to create a new version and bring the new version into a new local version he has to click on the checkbox Create a linked local version
* If the user wants to make the new version protected he has to click on the checkbox Create as Protected Version.


|  |
| --- |
| **Backlinks** |
| [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945) |
|

---
