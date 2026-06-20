---
title: "WWSD Pattern instance for Single-level Transactions"
source_id: 15996
source_url: https://wiki.genexus.com/commwiki/wiki?15996
genexus_version: "18"
---

# WWSD Pattern instance for Single-level Transactions

Supposing a Property [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) with the following attributes:   
`[imagen omitida: wiki id 37467]`

When the [Work With for Smart Devices pattern is applied](https://wiki.genexus.com/commwiki/wiki?15975), the following instance, associated with the Property Transaction, is generated:  
`[imagen omitida: wiki id 37468]`

The default instance of the Work With for Smart Devices associated with a transaction includes a tree showing the Level (Property) node, and within it:

* **[List Node](https://wiki.genexus.com/commwiki/wiki?15984)**  
  For displaying a list of Properties.
* **[Detail Node](https://wiki.genexus.com/commwiki/wiki?15985)**  
  For displaying the detail of each Property when selecting a record from the List.

The [List Node](https://wiki.genexus.com/commwiki/wiki?15984) allows designing how the item's list will be displayed on the Smart Device screen. By default, this node only includes a Grid control with a subset of Transaction's attributes, which includes an image-based attribute if it has one and the [description attribute](https://wiki.genexus.com/commwiki/wiki?2154) (marked with `[imagen omitida: wiki id 37469]` icon on the Transaction). Also, this Grid control has [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) with *<default>* value that will open the Detail node for the record tapped by the end-user. The developer can include another kind of content (e.g. TextBlocks, Images, etc.) if it desired.

`[imagen omitida: wiki id 37470]`

The [Detail Node](https://wiki.genexus.com/commwiki/wiki?15985) includes a *Section (General)*, a Section that shows all data relative to the record selected from the List Node.

`[imagen omitida: wiki id 37471]`

`[imagen omitida: wiki id 37472]`

The *Section(General)* node includes:

* **View mode**  
  Allows viewing detailed information on the record selected from the List.
* **Edit mode**  
  The screen that will be shown upon selecting the Insert action from List or Update from the View, of the record from the Smart Device.

## [Notes](#Notes)

* In this type of application, the Transaction is not used to edit data, and that is the reason for defining the additional Edit form, in order to perform the editing.
* It is also possible to configure different properties to change the appearance of the information shown on the Smart Device screen.

## [See also](#See+also)

* [Work With object](https://wiki.genexus.com/commwiki/wiki?15974)
* [Work With for Smart Devices Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004)
* [WWSD Pattern instance for Related Transactions](https://wiki.genexus.com/commwiki/wiki?16007)

## [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Container of sections in the Detail screen of the Work With](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/container-of-sections-in-the-detail-screen-of-the-work-with?p=3658)


|  |
| --- |
| **Backlinks** |
| [Work With for Smart Devices Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004) |
| [Category:Work With object](https://wiki.genexus.com/commwiki/wiki?15974) | [WWSD Pattern instance for Related Transactions](https://wiki.genexus.com/commwiki/wiki?16007) |

---
