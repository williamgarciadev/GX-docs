---
title: "Program Name variable"
source_id: 8870
source_url: https://wiki.genexus.com/commwiki/wiki?8870
genexus_version: "18"
---

# Program Name variable

Stores the name of the active program.

**Data Type:**  
Character   
    (Its length depends of the Significant Object Name Length property)

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This GeneXus variable stores the active program's name when evaluated. The name is the one specified in the object's property Name.

### [Samples](#Samples)

Suppose a procedure Process is called by many programs. This procedure processes the information it receives as parameters. Since it is called by many programs, the program's name is included in the parameter list in order to identify which one is the calling process.

```
Process.Call(&Pgmname,Parm1,....) ;
```

### [Compatibility](#Compatibility)

Up to GeneXus X Evolution 2, it returns its value as CamelCase.  
Since GeneXus X Evolution 3 and the inclusion of Modules, it returns its value as lowercase.

### [See Also](#See+Also)

[Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386)


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) | [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
