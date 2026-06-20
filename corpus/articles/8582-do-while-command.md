---
title: "Do While command"
source_id: 8582
source_url: https://wiki.genexus.com/commwiki/wiki?8582
genexus_version: "18"
---

# Do While command

Executes a block of code repeatedly, until its condition becomes false.

### [Syntax](#Syntax)

**Do while** *Condition*  
       *Code*  
**Enddo**

**Where:**  
  
*Condition*  
    Any valid logical expression. The condition is evaluated prior to the execution of the commands.  
  
*Code*  
    Block that is executed while the condition evaluated is true.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)

### [Description](#Description)

This command executes every command within the Do while and the Enddo sentence, until the condition *cond* becomes false.

Any command can be specified within a Do while-EndDo group.

To force an exit from the Do while group you may use the [Exit command](https://wiki.genexus.com/commwiki/wiki?8590).

### [Samples](#Samples)

Suppose you need to print ten equal lines. To solve this need you can define the following code inside a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664):

```
&i = 1
Do while &i <= 10
   Print printblock1   /* The printblock contains fixed texts */
   &i = &i + 1
EndDo
```

### [See Also](#See+Also)

[Exit command](https://wiki.genexus.com/commwiki/wiki?8590)

[For To Step command](https://wiki.genexus.com/commwiki/wiki?8595)  
[For In Array Command](https://wiki.genexus.com/commwiki/wiki?8585)


|  |
| --- |
| **Backlinks** |
| [Code Snippets](https://wiki.genexus.com/commwiki/wiki?10662) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) |
| [Exit command](https://wiki.genexus.com/commwiki/wiki?8590) | [For In Array/Collection command](https://wiki.genexus.com/commwiki/wiki?8585) | [How to define Variables and Arrays](https://wiki.genexus.com/commwiki/wiki?7385) |

---
