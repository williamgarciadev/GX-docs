---
title: "Standard Variables List"
source_id: 7386
source_url: https://wiki.genexus.com/commwiki/wiki?7386
genexus_version: "18"
---

# Standard Variables List

In several [GeneXus objects](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1866,,), predefined variables of common use—called **standard variables**—are available.

Even though they are not shown by default in all types of objects, if you try to define a variable using the name of a **standard variable**, it will automatically appear with the standard variable's definition. You will not be able to modify its data type or otherwise redefine it. In other words, it is not possible to define user variables with those names in any object type.

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
| [RestCode](https://wiki.genexus.com/commwiki/wiki?60841) | Numeric(3.0) | [API object](https://wiki.genexus.com/commwiki/wiki?46151) | It can only accept values of categories 2xx and 4xx.  For more information, see [SAC #50865](https://www.genexus.com/developers/websac?en,,,50865) |
| RestMethod | [HttpMethod domain](https://wiki.genexus.com/commwiki/wiki?31498) | [API object](https://wiki.genexus.com/commwiki/wiki?46151) |  |
| [Time](https://wiki.genexus.com/commwiki/wiki?8102) | Character(8) | Almost all |  |
| [Today](https://wiki.genexus.com/commwiki/wiki?8873) | Date | Almost all |  |
| [RestServiceName](https://wiki.genexus.com/commwiki/wiki?60844) | Character(256) | [API object](https://wiki.genexus.com/commwiki/wiki?46151) |  |

## [See Also](#See+Also)

[GeneXus reserved words](https://wiki.genexus.com/commwiki/wiki?17531)


|  |
| --- |
| **Backlinks** |
| [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) | [ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125) | [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853) |
| [Line variable](https://wiki.genexus.com/commwiki/wiki?8099) | [Mode variable](https://wiki.genexus.com/commwiki/wiki?31225) | [Output variable](https://wiki.genexus.com/commwiki/wiki?8101) | [Page variable](https://wiki.genexus.com/commwiki/wiki?8103) |
| [Program Description variable - Pgmdesc](https://wiki.genexus.com/commwiki/wiki?7672) | [Program Name variable](https://wiki.genexus.com/commwiki/wiki?8870) | [Standard Variables for API objects](https://wiki.genexus.com/commwiki/wiki?60834) | [Standard Variables for API Objects (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60839) |
| [Standard Variables List (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60835) | [Time variable](https://wiki.genexus.com/commwiki/wiki?8102) | [Today variable](https://wiki.genexus.com/commwiki/wiki?8873) | [Variable definition](https://wiki.genexus.com/commwiki/wiki?7375) |

---
