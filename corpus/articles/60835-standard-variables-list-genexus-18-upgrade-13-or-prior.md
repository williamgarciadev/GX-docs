---
title: "Standard Variables List (GeneXus 18 Upgrade 13 or prior)"
source_id: 60835
source_url: https://wiki.genexus.com/commwiki/wiki?60835
genexus_version: "18"
---

# Standard Variables List (GeneXus 18 Upgrade 13 or prior)

In several [GeneXus objects](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1866,,), GeneXus offers pre-defined variables which are of common use. They are named **standard variables**.

Even though they are not shown by default in all types of objects, if you try to define a variable with the name of a **standard variable** it will automatically appear with the standard variable definition and you will not be able to define its data type or anything else. In other words, it's not possible to define user variables with those names in any type of object.

|  |  |  |  |
| --- | --- | --- | --- |
| **Standard variable name** | **Data Type** | **Objects in which it is shown by default** | **Observations** |
| [Err](https://wiki.genexus.com/commwiki/wiki?51028) | Numeric(3) |  |  |
| [ErrMsg](https://wiki.genexus.com/commwiki/wiki?51125) | Character(70) |  |  |
| [ErrMsgGxRemove](https://wiki.genexus.com/commwiki/wiki?8495) | Numeric(1.0) | [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) |  |
| [Line](https://wiki.genexus.com/commwiki/wiki?8099) | Numeric(6.0) | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |  |
| [Mode](https://wiki.genexus.com/commwiki/wiki?31225) | Character(3) | [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) |  |
| Mr | Character(3) |  | Deprecated.  It is no longer used. |
| Msg | Character(70) |  |  |
| Op | Character(1) |  | Deprecated.  It is no longer used. |
| Outdev | Character(1) |  | Deprecated.  It is no longer used. |
| [Output](https://wiki.genexus.com/commwiki/wiki?8101) | Character(3) | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |  |
| [Page](https://wiki.genexus.com/commwiki/wiki?8103) | Numeric(6.0) | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |  |
| [Pgmdesc](https://wiki.genexus.com/commwiki/wiki?7672) | Character(256) | Almost all |  |
| [Pgmname](https://wiki.genexus.com/commwiki/wiki?8870) | Character(128) | Almost all |  |
| RestCode | Numeric(3.0) | [API object](https://wiki.genexus.com/commwiki/wiki?46151) | It can only take the values of categories 2xx and 4xx.  For more information see [SAC #50865](https://www.genexus.com/developers/websac?en,,,50865) |
| RestMethod | [HttpMethod domain](https://wiki.genexus.com/commwiki/wiki?31498) | [API object](https://wiki.genexus.com/commwiki/wiki?46151) |  |
| [Time](https://wiki.genexus.com/commwiki/wiki?8102) | Character(8) | Almost all |  |
| [Today](https://wiki.genexus.com/commwiki/wiki?8873) | Date | Almost all |  |

## See Also

[GeneXus reserved words](https://wiki.genexus.com/commwiki/wiki?17531)
