---
title: "GeneXus Template Language - Assembly Directive"
source_id: 50920
source_url: https://wiki.genexus.com/commwiki/wiki?50920
genexus_version: "18"
---

# GeneXus Template Language - Assembly Directive

The Assembly directive tells the Template Engine which external assemblies should be referenced for the template. For example, if you want to use the .NET XML classes in the template, you need to reference the “System.Xml” assembly.

GeneXus automatically includes all the references to the GeneXus Sdk assemblies.

For example:

```
<%@ Assembly Name="Artech.Architecture.Common" %>
```

**Name:** This is the fully qualified name of the assembly. The assembly must exist in the Global Assembly Cache, in the GeneXus Packages directory (<GeneXus Installation Folder>\Packages or in the Patterns folder.

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
