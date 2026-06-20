---
title: "Update function in Transactions"
source_id: 8327
source_url: https://wiki.genexus.com/commwiki/wiki?8327
genexus_version: "18"
---

# Update function in Transactions

Returns True when the Transaction is being executed in Update mode. Otherwise, it returns False.

### [Syntax](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213) if **Update**;

**Type Returned:**  
Boolean (True or False)

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)

### [Description](#Description)

The Update function allows conditioning the triggering of a rule defined in a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) so that the rule is executed only if the end user performs an update.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Document 
{ 
   DocumentId*
   DocumentDescription
   DocumentCreationDate     
}
```

Suppose you have an application that manages documents, where certain attributes must be filled in with information only at insert time, and must never be modified once entered (for example, the document's creation date). To meet this requirement, you can define the following rule in the Document Transaction Rules section:

```
NoAccept(DocumentCreationDate) If Update;
```

Thus, the DocumentCreationDate attribute will be read-only when the Document [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) is executed in Update mode.

**Note**: In the iSeries environment, when an error rule for a certain mode is defined, the corresponding code to support this mode is not generated.

### See Also

[Delete function](https://wiki.genexus.com/commwiki/wiki?8328)  
[Insert function](https://wiki.genexus.com/commwiki/wiki?8326)


|  |
| --- |
| **Backlinks** |
| [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [Delete function in Transactions](https://wiki.genexus.com/commwiki/wiki?8328) | [Insert function in Transactions](https://wiki.genexus.com/commwiki/wiki?8326) |

---
