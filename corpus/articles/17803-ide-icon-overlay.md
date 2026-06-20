---
title: "IDE Icon overlay"
source_id: 17803
source_url: https://wiki.genexus.com/commwiki/wiki?17803
genexus_version: "18"
---

# IDE Icon overlay

This article describes the icon overlays that the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) shows associated with objects in several dialogs. These icon overlays help you identify an object's status or other important characteristics.

## [Icon overlay for Team Development](#Icon+overlay+for+Team+Development)

When working with [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31337,,), the IDE allows adding object status indicators for the KB's server. For example, to identify in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) which of the objects were modified locally (they are *pending for commit*), as well as new objects and so on.

To identify these statuses, the standard object icon contains an icon overlay for those Knowledge Bases connected to a GeneXus Server instance.

### [Working without locks (Standard mode)](#Working+without+locks+%28Standard+mode%29)

|  |  |
| --- | --- |
|  | Objects that were modified locally (pending for commit) show a full blue circle in the bottom left corner of the object icon. |
|  | New objects show a full orange asterisk in the bottom left corner of the object icon. |
|  | Objects in Conflict show a red triangle in the bottom left corner of the object icon and change the font color to red. |

### [Working with locks](#Working+with+locks)

|  |  |
| --- | --- |
|  | In these cases, a further distinction is made. The [locked object](https://wiki.genexus.com/commwiki/wiki?17484) (with no edition) shows an empty blue circle on the object's icon. |
|  | After the object is modified, the new object state is locked and pending for commit (edited); the icon overlay changes from an empty blue circle to a full blue one. |
|  | When the object is [force edited](https://wiki.genexus.com/commwiki/wiki?17486) (with no edition), it shows an empty red circle on the object's icon. |
|  | For those cases when the object is force edited and pending for commit (edited), a full red circle is added to the object's icon. |

### [Considerations](#Considerations)

All icons are overlayed in the bottom left corner. Hints are displayed wherever the object icon type is displayed. In the sample below, the commit dialog is shown with new, deleted, and modified objects.

`[imagen omitida: wiki id 42638]`

## [Icon overlay for Modularization](#Icon+overlay+for+Modularization)

Showing [Object visibility](https://wiki.genexus.com/commwiki/wiki?22473) in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) or other tool windows helps you identify objects that are private, internal, or public.

More specifically, a heart is displayed when the object's visibility is internal, and a padlock when it's private.

In the sample below, the BL module is internal, Customer is private, and Core and GetCustomer are public:

`[imagen omitida: wiki id 50039]`
