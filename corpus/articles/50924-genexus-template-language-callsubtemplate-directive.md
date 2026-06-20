---
title: "GeneXus Template Language - CallSubTemplate Directive"
source_id: 50924
source_url: https://wiki.genexus.com/commwiki/wiki?50924
genexus_version: "18"
---

# GeneXus Template Language - CallSubTemplate Directive

The CallSubTemplate directive is used to invoke a subtemplate.

The syntax is:

```
<%@ CallSubTemplate MySubTemplate UseComboBoxes=”true” Mode = “”Insert”” CurrentLevel = “level”%>
```

After the CallSubTemplate directive, you need to specify the subtemplate’s logical name as declared in the SubTemplate directive. You also need to specify the property values for the called subtemplate. In this case, there are three properties set.

Note that values should always be written in quotes, so to send a string parameter you need to use double quotes (that’s the case of the “Insert” parameter value). When you use single quotes, you are referring to variables, properties, constants, methods, etc.

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
