---
title: "CaptureOutput MSBuild Property"
source_id: 35863
source_url: https://wiki.genexus.com/commwiki/wiki?35863
genexus_version: "18"
---

# CaptureOutput MSBuild Property

The *CaptureOutput* property is a generic attribute available in any GeneXus MSBuild [task](https://wiki.genexus.com/commwiki/wiki?3908).

### [Syntax](#Syntax)

```
CaptureOutput="true|false"
```

### [Description](#Description)

When the property is enabled, you can get the complete MSBuild task output in a MSBuild variable to be processed programmatically.

Use the MSBuild [output parameter](https://msdn.microsoft.com/en-us/library/ms164287.aspx), reference the *TaskOutput* parameter value (TaskParameter) and declare a variable to store the result (PropertyName). For example, if you want to use it with the [OpenKnowledgeBase MSBuild Task](https://wiki.genexus.com/commwiki/wiki?35862) and retrieve the result in the OpenOutput variable, use the following:

```
<OpenKnowledgeBase
  Directory="$(KBDirectory)" 
  TargetModelId="$(ModelId)"
  DatabaseUser="UserId"
  DatabasePassword="Password"
  CaptureOutput="true">
<Output TaskParameter="TaskOutput" PropertyName="OpenOutput" />
</OpenKnowledgeBase>
```

The option is available since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,)


|  |
| --- |
| **Backlinks** |
| [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) |
| [OpenKnowledgeBase MSBuild Task](https://wiki.genexus.com/commwiki/wiki?35862) |

---
