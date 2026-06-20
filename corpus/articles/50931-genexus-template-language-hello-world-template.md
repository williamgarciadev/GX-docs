---
title: "GeneXus Template Language - Hello World Template"
source_id: 50931
source_url: https://wiki.genexus.com/commwiki/wiki?50931
genexus_version: "18"
---

# GeneXus Template Language - Hello World Template

This is the simplest template:

```
<%@ Template Language="C#" TargetLanguage="Text" Description="Default Menu." %>
<%-- Hello world template %>
<% for (int i = 0; i < 5; i++)
      { %>
Hello World <%= i %>
<%   } %>
```

When executed, this template will generate the following:

* Hello World 0
* Hello World 1
* Hello World 2
* Hello World 3
* Hello World 4

The two most common template tags are used. The <%-- %> tags are used to embed comments in the template; these comments are not generated in the template output.

The <% %> tags are used to embed code that will be executed during the template execution. It can be C# or Visual Basic .NET code, depending on the content of the ‘Template’ directive. The default code is C#.

The <%= %> tags are used to write the contents of an expression to the template output.

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
