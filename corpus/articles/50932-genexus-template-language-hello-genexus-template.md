---
title: "GeneXus Template Language - Hello GeneXus Template"
source_id: 50932
source_url: https://wiki.genexus.com/commwiki/wiki?50932
genexus_version: "18"
---

# GeneXus Template Language - Hello GeneXus Template

The following example will create an HTML page with the structure of a given [Business Component](https://wiki.genexus.com/commwiki/wiki?5846). It will receive a GeneXus ‘FrameworkObject’ parameter, traverse its attributes, and print them:

```
<%@ Template Language="C#" TargetLanguage="GX" Description="List Business Component" %>
<%@ Property Name="Object" Type="Artech.Architecture.Common.Objects.KBObject"%>
 
<TABLE>
<TR><%= Object.Name %></TR>
</TABLE>
```

This will output a text with a table with the object name for the given object.

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
