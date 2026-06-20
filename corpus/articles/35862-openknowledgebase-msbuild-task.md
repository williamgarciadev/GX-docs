---
title: "OpenKnowledgeBase MSBuild Task"
source_id: 35862
source_url: https://wiki.genexus.com/commwiki/wiki?35862
genexus_version: "18"
---

# OpenKnowledgeBase MSBuild Task

Opens the Knowledge Base in the specified directory.

Syntax

```
<OpenKnowledgeBase
  Directory="$(KBDirectory)" 
  TargetModelId="$(ModelId)"
  DatabaseUser="UserId"
  DatabasePassword="Password"
  CaptureOutput="true|false">
<Output TaskParameter="TaskOutput" PropertyName="OpenOutput" />
</OpenKnowledgeBase>
```

Options

*Directory*: $(KBDirectory) is the directory (absolute or relative) where the Knowledge Base is located. **REQUIRED (unless you use MDFPath; see below)**

*MDFPath:* Instead of using Directory, you can use this to choose an mdf to open (instead of the .gxw file).

*TargetModelId*: $(ModelId) is the ID of the Target model when working in a Version different than the Trunk Version. This parameter is optional, it is recommended to use the tasks SetActiveVersion and SetActiveEnvironment to position on the required version and environment.

*DatabaseUser*: user name to use when not using IntegratedSecurity .

*DatabasePassword*:password to use when not using IntegratedSecurity.

*[CaptureOutput](https://wiki.genexus.com/commwiki/wiki?35863) (1)*:captures the Task Output on the OpenOutput variable when enabled.

Samples

Open a Knowledge Base in directory C:\MyKnowledgeBases using Integrated Security.

```
<OpenKnowledgeBase Directory="C:\MyKnowledgeBases" />
```

Open a Knowledge Base in directory C:\MyKnowledgeBases using SQLServer Authentication

```
<OpenKnowledgeBase Directory="C:\MyKnowledgeBases" DatabaseUser="sa" DatabasePassword="saPassword" />
```

1 - Option supported since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,)


|  |
| --- |
| **Backlinks** |
| [CaptureOutput MSBuild Property](https://wiki.genexus.com/commwiki/wiki?35863) | [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) |
| [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) |

---
