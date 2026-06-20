---
title: "If command"
source_id: 8608
source_url: https://wiki.genexus.com/commwiki/wiki?8608
genexus_version: "18"
---

# If command

Executes a block of commands if the condition evaluates to true.

### [Syntax](#Syntax)

**If** *cond*  
       *block1*  
[Else  
       *block2*]  
**EndIf**

**Where:**  
  
*cond*  
   Condition evaluated in the If.

*block1*  
   Block that is executed if the *cond* condition evaluates to true.

*block2*  
   Block that is executed if the *cond* condition evaluates to false.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), 
[Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The If command allows you to condition the execution of command blocks.

Any command can be defined within block1 and block2 respectively.

### [Samples](#Samples)

```
If &del                    //&del is a boolean variable
  DelCustomer(CustomerId)  //DelClient is a Procedure and CustomerId is an attribute (with value in that context) sent by parameter
Else
  Return
EndIf
```

### [Restriction](#Restriction)

When using this command in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or a [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) there is a restriction for the *cond* syntax. It can only contain a variable, attribute or SDT element of [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) to be evaluated.

### 

####


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) |
| [HowTo: Using the ShowError method from Interop in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?51446) | [IIf function](https://wiki.genexus.com/commwiki/wiki?14280) |

---
