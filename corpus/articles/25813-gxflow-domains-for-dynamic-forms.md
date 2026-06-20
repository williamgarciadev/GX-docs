---
title: "GXflow Domains for Dynamic Forms"
source_id: 25813
source_url: https://wiki.genexus.com/commwiki/wiki?25813
genexus_version: "18"
---

# GXflow Domains for Dynamic Forms

The Domains component allows the user to view all the existing Domains and manage all their properties or create new ones. Domains are used by dynamic forms—the elements of a dynamic form can be based on one of the existing domains; these Domains give a general definition of a type as [GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221) do.

The following figure shows the Domains component interface, where you can create new ones or edit the existing ones:

`[imagen omitida: wiki id 52447]`

In the following sections, you will find the description of the different components.

### [Actions](#Actions)

The following buttons allow you to make changes to the Domains in the grid.

* **New**: the New button allows the user to create a new domain. Users will view the following dialog where they can set the domain properties:  
  `[imagen omitida: wiki id 52448]`
  + **Domain**: identifier of the domain—read-only.
  + **Description**: description of the domain—as it will be displayed when selecting it from an element.
  + **Type**: type of the domain; its possible values are:
    - Boolean
    - Character
    - Date
    - DateTime
    - Email
    - Enum
    - Group
    - Numeric
    - Password
    - Upload
  + **Length**: sets the length of a domain. Only available for string types.
  + **Display**: the way the domain must be displayed; in other words, its control. Possible values, depending on the type, are as follows:
    - None
    - Auto Complete
    - Combo
    - Date no picker
    - Default
    - In place edit
    - Label
    - Multi Select
    - Radio
    - Slider
    - Textarea
    - Grid
    - DSCombo
  + **Default Value**: sets the default value to be used for the domain.
  + **Validation Regex**: sets a regular expression to be queried when data is inserted in the field—the inserted data must match the pattern. Only available when using Character type.
* **Edit**: allows editing any property of an existing domain.
* **Display**: displays all the properties of the domain.
* **Remove**: removes/deletes the domain.

### [Domains Grid](#Domains+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns that should be visible.

`[imagen omitida: wiki id 52013]` It allows refreshing the grid.

It is possible to sort some columns by clicking on their title.

This grid consists of the following columns:

* **Id**: domain Id.
* **Description**: domain description.
* **Type**: domain type.

### [See Also](#See+Also)

* [GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809) | [GXflow Elements](https://wiki.genexus.com/commwiki/wiki?25812) |
| [HowTo: Using Global Events in Smart Device applications](https://wiki.genexus.com/commwiki/wiki?30201) |

---
