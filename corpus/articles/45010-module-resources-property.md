---
title: "Module Resources property"
source_id: 45010
source_url: https://wiki.genexus.com/commwiki/wiki?45010
genexus_version: "18"
---

# Module Resources property

List of File objects defined as resources for the module (e.g. External Object implementation); they are needed to integrate the packaged module in another Knowledge Base.

### [Scope](#Scope)

**Objects:** [Module](https://wiki.genexus.com/commwiki/wiki?22411)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The resources (list of [File objects](https://wiki.genexus.com/commwiki/wiki?5852)) set in these properties are packaged when [the module is packaged](https://wiki.genexus.com/commwiki/wiki?31376).

The File Object properties related to the extraction of the containing file have to be set accordingly in the different platforms

* [.NET](https://wiki.genexus.com/commwiki/wiki?38604) & [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892): TargetDirectory\bin,
* [Java](https://wiki.genexus.com/commwiki/wiki?12258) & [Android](https://wiki.genexus.com/commwiki/wiki?14453): TargetDirectory\modules

so that they can be packaged.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376)  
[Modules Server](https://wiki.genexus.com/commwiki/wiki?45933)


|  |
| --- |
| **Backlinks** |
| [Category:Module object](https://wiki.genexus.com/commwiki/wiki?22411) |

---
