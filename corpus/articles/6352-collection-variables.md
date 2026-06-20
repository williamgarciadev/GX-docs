---
title: "Collection variables"
source_id: 6352
source_url: https://wiki.genexus.com/commwiki/wiki?6352
genexus_version: "18"
---

# Collection variables

When defining a variable, in any context, once the data type is established, you have the choice to declare it as a collection - not as a simple variable of that data type:

|  |  |
| --- | --- |
|  |  |

The default [Collection property (IsCollection checkbox)](https://wiki.genexus.com/commwiki/wiki?9761) value is 'False'. If you set it to 'True', you'll have a collection variable whose items are of the established data type.

To work with the individual items of the collection, you have to define a simple variable of the collection items data type, to run through the collection, using the '[For IN](https://wiki.genexus.com/commwiki/wiki?6359)' command.

```
For &var IN &collectionVar
   ...
EndFor
```

#### [What data type can items have?](#What+data+type+can+items+have%3F)

Any. Particularly, in addition to the basic (numeric, character, etc.) and extended ones (HttpRequest), it can be an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) type (simple as well as collection), or a [BC](https://wiki.genexus.com/commwiki/wiki?5846) one.

It's worth mentioning that once it has been established that the variable is a collection, the [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) automatically takes the 'Scalar' value. In other words, variables that are collections of arrays or matrices cannot be defined.

You can see the particular case of  [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296).

### [Considerations](#Considerations)

Collection variables associated with basic GeneXus data types (such as Numeric, Character, Date and so on) are not supported on the form; for those cases, you need to define a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021).

### [See also](#See+also)

[Collection Domains](https://wiki.genexus.com/commwiki/wiki?6393)  
[SDT on Form](https://wiki.genexus.com/commwiki/wiki?2090,,)


|  |
| --- |
| **Backlinks** |
| [Collection Domains](https://wiki.genexus.com/commwiki/wiki?6393) | [For in command](https://wiki.genexus.com/commwiki/wiki?6359) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [IN Operator](https://wiki.genexus.com/commwiki/wiki?11688) | [Input clause](https://wiki.genexus.com/commwiki/wiki?25406) | [Structured Data Type editor](https://wiki.genexus.com/commwiki/wiki?6365) | [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310) |
| [Variables Editor](https://wiki.genexus.com/commwiki/wiki?3173) |

---
