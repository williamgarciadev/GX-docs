---
title: "For To Step command"
source_id: 8595
source_url: https://wiki.genexus.com/commwiki/wiki?8595
genexus_version: "18"
---

# For To Step command

Iterates a value for a certain number of times.

### [Syntax](#Syntax)

**For** ***&****var* = *start* **to** *end*[*step leap*]  
       *code*  
**Endfor**

**Where:**  
  
***&****var* Is a variable based on the Numeric data type.

*start, end*  
    Are numeric expressions showing the start and the end of the loop.

*step*  
    Specifies the leap of the loop.

*leap*  
    Is a constant value.

*code*  
    Sequence of valid language commands.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This command allows iterating a value for a certain number of times. It is a loop from the start value of **&***var* and it increases a *leap*, as long as ***&**var* is <= than *end*. The *leap* default value is 1, but it can also be a negative number.

**Notes:**

* As it's usual in GeneXus, the scope of the loop variable is the whole object
* The value of the loop variable outside the loop is not defined/documented and may change through platforms and versions.

### [Samples](#Samples)

```
Event Refresh
    &Tabs = LoadPageTabs(&PageType, &PageFullName, &PageId, &PageLastVersionId1)
 
    // Select the subset of tabs that will be shown.
    &FirstTab = 1
    &LastTab  = &Tabs.Count

    &IsFirstTab = True
    For &Index = &FirstTab To &LastTab
        &Tab = &Tabs.Item(&Index)
        Do 'LoadItem'
        &IsFirstTab = False
    EndFor
    ...
EndEvent
```

###


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Do While command](https://wiki.genexus.com/commwiki/wiki?8582) |
| [Exit command](https://wiki.genexus.com/commwiki/wiki?8590) |

---
