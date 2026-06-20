---
title: "Collection Domains"
source_id: 6393
source_url: https://wiki.genexus.com/commwiki/wiki?6393
genexus_version: "18"
---

# Collection Domains

When defining a [Domain](https://wiki.genexus.com/commwiki/wiki?7221), once the Data Type is established, you have the choice to declare it as a collection of that Data Type:

`[imagen omitida: wiki id 6395]`

The default 'Collection' Property value is 'False'. If you set it to 'True', you'll have a collection Domain whose items are of the established Data Type.

Then, you can define a variable of the 'EMails' Data Type, which is a collection of items of Character(50) Data Type. Then, you can run through the collection using the '[For IN](https://wiki.genexus.com/commwiki/wiki?6359)' command.

Note that the attributes cannot be defined as collections (remember that talking about attributes is talking about columns of the database tables). What happens if an attribute is defined based on a collection domain (such as 'EMails' shown above)? In this case, the domain acts as a way to initialize all the similar attribute properties. That is, as the attribute doesn't have a Collection Property, its counterpart Domain Property is dismissed.

#### [What Data Type Can Items Have?](#What+Data+Type+Can+Items+Have%3F)

Any. Particularly, in addition to the basic (Numeric, Character, etc.) and extended ones (HttpRequest, etc.), it can be an SDT type (simple as well as collection) or a BC one.

It's worth mentioning that once it has been established that the Domain is a collection, the 'Dimensions' Property automatically takes the 'Scalar' value. In other words, variables that are collections of arrays or matrices cannot be defined.

#### [See Also](#See+Also)

[Collection variables](https://wiki.genexus.com/commwiki/wiki?6352)


|  |
| --- |
| **Backlinks** |
| [Collection variables](https://wiki.genexus.com/commwiki/wiki?6352) | [For in command](https://wiki.genexus.com/commwiki/wiki?6359) | [IN Operator](https://wiki.genexus.com/commwiki/wiki?11688) |
| [Structured Data Type editor](https://wiki.genexus.com/commwiki/wiki?6365) |

---
