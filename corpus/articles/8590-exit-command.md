---
title: "Exit command"
source_id: 8590
source_url: https://wiki.genexus.com/commwiki/wiki?8590
genexus_version: "18"
---

# Exit command

Leaves a For Each command, Xfor Each command, Do While command or For To Step command.

### [Syntax](#Syntax)

**Exit**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)

### [Description](#Description)

This command allows you to leave a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), [Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596), [Do While command](https://wiki.genexus.com/commwiki/wiki?8582) or [For To Step command](https://wiki.genexus.com/commwiki/wiki?8595). The next command to be executed after an Exit, is the command following the EndFor, Xendfor, EndDo or EndFor corresponding to the For each, Xfor each, Do While or For group containing it.​

**Notes:**

* The Exit command is not valid within a "For Each Line" group.
* The Exit does not work within a Do While when generated in Cobol for iSeries code.

### [Samples](#Samples)

In a system that handles Employee information, consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

**Employee  
{**   
   EmployeeId\*  
   EmployeeName  
   EmployeeDateOfBirth  
   EmployeeDateOfAdmission  
   EmployeeResignDate  
   ....  
**}**

Suppose you may want to know if an employee has quit within a specific period of time.

After verifying if there is at least one matching that condition, you want to exit the For each and stop the search.

The implementation would be:

```
&Found = 0
For each Employee order EmployeeResignDate
    Where EmployeeResignDate >= &StartDate
    Where EmployeeResignDate <= &EndDate
         &Found = 1
          Exit
EndFor

If &Found = 1
    Msg('Employee found that satisfies the condition')
Else
    Msg('NO Employee satisfies the condition')
EndIf
```

### [See Also](#See+Also)

[For Each command](https://wiki.genexus.com/commwiki/wiki?24744)  
[Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596)  
[Do While command](https://wiki.genexus.com/commwiki/wiki?8582)  
[For To Step command](https://wiki.genexus.com/commwiki/wiki?8595)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Do While command](https://wiki.genexus.com/commwiki/wiki?8582) |
| [For In Array/Collection command](https://wiki.genexus.com/commwiki/wiki?8585) |

---
