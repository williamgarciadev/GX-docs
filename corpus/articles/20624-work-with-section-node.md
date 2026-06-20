---
title: "Work With Section Node"
source_id: 20624
source_url: https://wiki.genexus.com/commwiki/wiki?20624
genexus_version: "18"
---

# Work With Section Node

A Section is just a group that allows separating certain operations related to the user interface.

In other words, in a certain Section there are data, Rules, actions (Events), Layouts, etc.

Below is an example, in which the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) is applied to the Property [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

Note that under the Detail node there are two Section nodes:

`[imagen omitida: wiki id 52225]`

**1)** The General Section:

`[imagen omitida: wiki id 52226]`

This Section includes:

* **View mode:**Allows viewing detailed information about the record selected from the List.
* **Edit mode:**Allows editing the record information upon selecting the Insert action from the List or Update action from the View.

**Note**: In this type of application, the Transaction is not used to edit data. This is the reason for having an additional Edit screen to perform the editing.

**2)** A second Section that is automatically created because there is an N-1 relation between the Property and PropertyAppointment Transactions:

`[imagen omitida: wiki id 52227]`

### [See Also](#See+Also)

[Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847)


|  |
| --- |
| **Backlinks** |
| [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) | [Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985) | [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984) |
| [Category:Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) | [Work With Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004) |

---
