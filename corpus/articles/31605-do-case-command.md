---
title: "Do Case command"
source_id: 31605
source_url: https://wiki.genexus.com/commwiki/wiki?31605
genexus_version: "18"
---

# Do Case command

Performs a set of commands depending on the condition.

### [Syntax](#Syntax)

**Do Case**  
    **Case** condition*1*  
        CodeBlock*1*  
    **Case** condition*N*  
        CodeBlock*N*  
    **Otherwise**  
        OtherwiseCodeBlock  
**Endcase**  
  
**Where:**  
  
*condition1*  
   Condition*1* evaluated.  
  
*CodeBlock1*  
   Code block that is executed if *condition1* evaluates to true.  
  
*conditionN*  
   Condition*N* evaluated.  
  
*CodeBlockN*  
   Code block that is executed if *conditionN* evaluates to true.  
  
*Otherwise*  
    Clause that establishes a final alternative, in case all previous conditions are not matched.  
  
*OtherwiseCodeBlock*  
    Block that is executed if all previous conditions are not matched (evaluated false).

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550),  [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This command works in the same way as if/else. It performs a set of commands within cases depending on conditions, which can involve attributes and/or variables.  
  
When the first Case whose condition is satisfied is executed, it prevents the others from being executed.   
  
The statements specified under the Otherwise clause are executed only if all Case conditions are evaluated as false.

**Note**: In Native Mobile applications, it works on both [Client-side](https://wiki.genexus.com/commwiki/wiki?24332) and [Server-side](https://wiki.genexus.com/commwiki/wiki?24234) events.

### Samples

The following code can be defined, for example, inside a GeneXus object Event or Source:

```
Do Case
    Case &Today.Month()=1
          &Discount=15
          &Bonus=500
    Case &Today.Month()=2
          &Discount=10
          &Bonus=300
    Otherwise
          &Discount=5
          &Bonus=0
Endcase
```

### [See Also](#See+Also)

[Sub command](https://wiki.genexus.com/commwiki/wiki?8586)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) |

---
