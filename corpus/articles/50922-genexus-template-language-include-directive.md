---
title: "GeneXus Template Language - Include Directive"
source_id: 50922
source_url: https://wiki.genexus.com/commwiki/wiki?50922
genexus_version: "18"
---

# GeneXus Template Language - Include Directive

The Include directive includes the contents of a source code file in the template code. It is useful if you have a set of routines that you want to use in several templates.   
It must be in the same language as the one specified in the “Language” option of the Template directive.

For example:

```
<%@ Include Name="CommonScripts.cs" %>
```

The parameter is:

**Namespace:** The name of the file to include. It must be located in the same directory as the template.

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
