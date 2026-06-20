---
title: "MetaEquiv Property"
source_id: 14623
source_url: https://wiki.genexus.com/commwiki/wiki?14623
genexus_version: "18"
---

# MetaEquiv Property

Allows to manage [meta elements](http://en.wikipedia.org/wiki/Meta_element) present in the generated HTML document header for the object, using the "**http-equiv**" attribute for them.

### [Description](#Description)

[Meta elements](http://en.wikipedia.org/wiki/Meta_element) are composed of a pair of texts name/value. This property manage this elements references are managed using a collection and in addition provide methods for getting the elements information.

In addition to the Count property (used to get the size of the collection), the following methods are available :

* *AddItem*. Given the name and value adds an item to the collection.
* *Clear*. Clears the collection
* *RemoveItem*. Given the name of an element, removes it from the collection.
* *Text*. Returns the name of an element given the index of the item in the collection.
* *Value*. Returns the value of an element given the index of the item in the collection.

### [Example](#Example)

This line in the GeneXus object

```
Form.MetaEquiv.Add('NewTag', 'NewValue')
```

will generate the following line in the generated HTML document header

```
<meta http-equiv="NewTag" content="NewValue">
```

### [Scope](#Scope)

**Objects:** [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Controls:** [Forms](https://wiki.genexus.com/commwiki/wiki?14619)  
**Interfaces:** Web

### [See Also](#See+Also)

[HeaderRawHTML Property](https://wiki.genexus.com/commwiki/wiki?14620)  
[JScriptSrc Property](https://wiki.genexus.com/commwiki/wiki?14621)  
[Meta Property](https://wiki.genexus.com/commwiki/wiki?14622)


|  |
| --- |
| **Backlinks** |
| [Form Control](https://wiki.genexus.com/commwiki/wiki?14619) | [HeaderRawHTML Property](https://wiki.genexus.com/commwiki/wiki?14620) | [JScriptSrc Property](https://wiki.genexus.com/commwiki/wiki?14621) |
| [Meta Property](https://wiki.genexus.com/commwiki/wiki?14622) |

---
