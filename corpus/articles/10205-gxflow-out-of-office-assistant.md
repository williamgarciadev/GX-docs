---
title: "GXflow Out of Office Assistant"
source_id: 10205
source_url: https://wiki.genexus.com/commwiki/wiki?10205
genexus_version: "18"
---

# GXflow Out of Office Assistant

This dialog allows you to set a user as out of the office and select a substitute user for him/her. You can access it by going to the [Account Settings](https://wiki.genexus.com/commwiki/wiki?10106) or [GXflow Users](https://wiki.genexus.com/commwiki/wiki?10193) menu and setting the Availability option to "User is currently out of the office".

When a user is set as out of the office, all the tasks in this user's inbox are redirected to the substitute user's inbox, and the same happens with new tasks associated with the user. In addition, when the original user returns, new tasks will no longer be redirected and those tasks not processed or taken by the substitute user will be removed from its inbox and kept in the original user's inbox. To remove those tasks, a [Rebuild Worklist](https://wiki.genexus.com/commwiki/wiki?53446,,) of the substitute user is necessary, so if the property Rebuild Worklist When Org. Struct. Changes is set to No, those tasks will not be removed automatically.

The return of the user who is out of the office isn't done automatically when the return date arrives. This can be done in two ways:

If the option Automatically undo the substitutions when entering the Inbox is activated, once the user enters the inbox it will be set as in the office, even if it is done before the return date, and new tasks will no longer be redirected to the substitute user. Remember that this will not execute a Rebuild Worklist, so tasks in the substitute user's inbox will not be removed.

If this option isn't activated, users must be set as in the office manually either from the [Account](https://wiki.genexus.com/commwiki/wiki?10106) or [GXflow Users](https://wiki.genexus.com/commwiki/wiki?10193) menus; in this case, the Rebuild Worklist will be executed.

### [Actions](#Actions)

`[imagen omitida: wiki id 53810]`

`[imagen omitida: wiki id 53811]`

General

* **Return Date**: Estimated date of return to the office.
* **Message**: Message associated.

Substitution

* **Define user/role substitute**: Defines the user or roles that will receive the tasks.
* **Automatically undo the substitutions when entering the Inbox**: If this option is activated, when the user enters the inbox, it will no longer be set as out of the office.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Users](https://wiki.genexus.com/commwiki/wiki?10193) |

---
