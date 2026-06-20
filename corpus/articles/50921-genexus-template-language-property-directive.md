---
title: "GeneXus Template Language - Property Directive"
source_id: 50921
source_url: https://wiki.genexus.com/commwiki/wiki?50921
genexus_version: "18"
---

# GeneXus Template Language - Property Directive

The property directive declares properties that will be used as parameters by the template.  For example:

```
<%@ Property Name="TargetNamespace" Type="System.String" Category="Code" Description="Namespace of the generated class" %>
```

The parameters are:

**Name:** The property name must be a valid property name for the target language. For example, if the target language is VB.NET you cannot use ‘Namespace’ as a property name because it is a reserved word. On the other hand, you may use it in C# because ‘namespace’ is the C# keyword, and C# is case sensitive.

**Type:** The Type parameter provides a valid .NET data type. You need to use the .NET data type (i.e. ‘System.Int32’ instead of ‘int’ as in C# or ‘Integer’ as in VB.NET).  
GeneXus metadata has a number of predefined types that are usually used as parameters, such as FrameworkObject, Level, AttributeItem.

**Category:** The category of the property.

**Description:** The description of the property.

### [See Also](#See+Also)

[GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Template Language](https://wiki.genexus.com/commwiki/wiki?50917) |

---
