---
title: "Delete function in Transactions"
source_id: 8328
source_url: https://wiki.genexus.com/commwiki/wiki?8328
genexus_version: "18"
---

# Delete function in Transactions

Returns True when the Transaction is being executed in Delete mode. Otherwise, it returns False.

### [Syntax](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213) if **Delete**;

**Type Returned:**  
Boolean (True or False)

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)

### [Description](#Description)

The Delete function allows conditioning the triggering of a rule defined in a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) so that the rule is executed only if the end user performs a deletion.

### [Samples](#Samples)

A common use of this function is to include an error() rule denying access to a certain mode within Transactions.

For example, consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Order 
{ 
   OrderId*
   OrderDate
   OrderDescription     
}
```

```
Error('Orders may not be deleted') If Delete;
```

This rule prevents the user from accessing the delete mode, thus preventing the Orders from being deleted.

**Note**: In the iSeries environment, when an error rule for a certain mode is defined (as in this example, for Delete mode), the corresponding code to support this mode is not generated.

### [See Also](#See+Also)

[Update function](https://wiki.genexus.com/commwiki/wiki?8327)  
[Insert function](https://wiki.genexus.com/commwiki/wiki?8326)


|  |
| --- |
| **Backlinks** |
| [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Insert function in Transactions](https://wiki.genexus.com/commwiki/wiki?8326) |
| [Update function in Transactions](https://wiki.genexus.com/commwiki/wiki?8327) |

---
