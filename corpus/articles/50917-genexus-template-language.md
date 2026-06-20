---
title: "GeneXus Template Language"
source_id: 50917
source_url: https://wiki.genexus.com/commwiki/wiki?50917
genexus_version: "18"
---

# GeneXus Template Language

GeneXus includes a general-purpose Template Engine that is used to create patterns.

The template language is inspired by ASP.NET, and consists of a set of template directives and tags mixed with the template content. When working with templates, you will need to use the GeneXus object model so as to obtain information about the GeneXus [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

Some template directives must be located in the template header, before the template content, while others can be included in the content. The header directives are:

* [Template](https://wiki.genexus.com/commwiki/wiki?50918)
* [Import](https://wiki.genexus.com/commwiki/wiki?50919)
* [Assembly](https://wiki.genexus.com/commwiki/wiki?50920)
* [Property](https://wiki.genexus.com/commwiki/wiki?50921)
* [Include](https://wiki.genexus.com/commwiki/wiki?50922)
* [SubTemplate](https://wiki.genexus.com/commwiki/wiki?50923)

In the template body, you can use the following directives:

* [CallSubTemplate](https://wiki.genexus.com/commwiki/wiki?50924)

Also, a set of tags can be used in the template body:

* [GeneXus Template Language - Comment Tags](https://wiki.genexus.com/commwiki/wiki?50925)

```
         <%-- This is a comment --%>
```

* [GeneXus Template Language - Code Tags](https://wiki.genexus.com/commwiki/wiki?50926)

```
                 <%= %>
              <%  %>
                  <script runat=”template”>
                  </script>
```


* [Hello World Template](https://wiki.genexus.com/commwiki/wiki?50931)
* [Hello GeneXus Template](https://wiki.genexus.com/commwiki/wiki?50932)
* Directives
  + [Template](https://wiki.genexus.com/commwiki/wiki?50918)
  + [Import](https://wiki.genexus.com/commwiki/wiki?50919)
  + [Assembly](https://wiki.genexus.com/commwiki/wiki?50920)
  + [Property](https://wiki.genexus.com/commwiki/wiki?50921)
  + [Include](https://wiki.genexus.com/commwiki/wiki?50922)
  + [SubTemplate](https://wiki.genexus.com/commwiki/wiki?50923)
  + [CallSubTemplate](https://wiki.genexus.com/commwiki/wiki?50924)
  + [Comment Tags](https://wiki.genexus.com/commwiki/wiki?50925)
  + [Code Tags](https://wiki.genexus.com/commwiki/wiki?50926)

---
