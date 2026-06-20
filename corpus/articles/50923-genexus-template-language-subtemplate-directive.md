---
title: "GeneXus Template Language - SubTemplate Directive"
source_id: 50923
source_url: https://wiki.genexus.com/commwiki/wiki?50923
genexus_version: "18"
---

# GeneXus Template Language - SubTemplate Directive

To apply the same code pattern in several places, you can create a sub template and invoke it. Using a sub template is a two-step process: first you need to declare it at the top of the main template. Then, you need to invoke it in the template using the CallSubTemplate directive. For example:

```
<%@ SubTemplate Name="MySubTemplate" File="TemplateUserDataGridCs_InitializeLevel.dkt" MergeProperties="True" %>
```

The parameters are:

**Name:** A logical name for the sub-template. It will be used when invoking it with the CallSubTemplate directive.

**File:** The name of the sub-template file. It must be located in the same folder as the calling template.

**MergeProperties:** Indicates whether you want to send the parent template properties to the sub-template. Its values can be “True” or “False”. 

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
