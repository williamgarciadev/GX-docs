---
title: "Pseudo Conversational Dialog Property"
source_id: 13998
source_url: https://wiki.genexus.com/commwiki/wiki?13998
genexus_version: "18"
---

# Pseudo Conversational Dialog Property

**Note**: This property is not offered for Java, .NET nor .NET Core generators, but the behavior for them is the one corresponding to the **Check updated tables only** value.

Specifies what kind of Pseudo Conversational Dialog is used to implement the [Concurrency control](https://wiki.genexus.com/commwiki/wiki?45563).

### [Values](#Values)

**Check updated tables only:** Implements Pseudo Conversational Dialog, checking updated tables only. This is the default value.  
**Check all accessed tables:** Implements Pseudo Conversational Dialog, checking all accessed tables.

### [Description](#Description)

The aim of the Pseudo Conversational Dialog is to reduce the time the record remains locked, this is to say, reducing it exclusively to process’ time.

During the validation process the records are NOT blocked, and after the confirmation they are read again (this time with locks) to see if they have changed. The scheme would be:

* Accepting data
* Validating them
* Asking for confirmation
* Validating that the data have not been changed (with locks)
* If the information is the same one validated in the second tip then
* Update the DB
* Release locks
* If not, inform the user that the data have been modified

When using the **Check updated tables only** value, the control is performed at the table level. If the table is modified within the level, all attributes of that table that are involved in the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) are controlled. The problem of this implementation appears when there are users who base their decisions on tables not updated in the Transaction.

When using the **Check** **all accessed tables** value, the control is performed over all table attributes involved in the Transaction object. It seems to be the most adequate control level since uncontrolled situations will not exist.

### [Scope](#Scope)

**Languages:** Cobol, RPG  
**Interfaces:** Win

### [See Also](#See+Also)

[Confirmation property](https://wiki.genexus.com/commwiki/wiki?7422)  
[Optimistic concurrency control](https://wiki.genexus.com/commwiki/wiki?22885)
