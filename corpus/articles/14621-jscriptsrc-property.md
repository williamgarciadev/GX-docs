---
title: "JScriptSrc Property"
source_id: 14621
source_url: https://wiki.genexus.com/commwiki/wiki?14621
genexus_version: "18"
---

# JScriptSrc Property

Manages the Javascript references present in the generated HTML document header for the object.

### [**Description**](#Description)

The Javascript references are managed using a collection of Javascript files. Clear, Add and Item methods are available in addition to the Count property.

### [Example](#Example)

This line in the GeneXus object

```
Form.JScriptSrc.Add('example.js')
```

will generate the following line in the generated HTML document header

```
<script type="text/javascript" src="example.js"></script>
```

When smooth is enabled the generation is as follows, the *data-gx-external-script* attribute force the script to be included in every refresh.:

```
<script type="text/javascript" src="example.js" data-gx-external-script></script>
```

### [Scope](#Scope)

**Objects:** [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Controls:** [Forms](https://wiki.genexus.com/commwiki/wiki?14619)  
**Generators:** :NET Core, .NET, Java

### [**See Also**](#See+Also)

[HeaderRawHTML Property](https://wiki.genexus.com/commwiki/wiki?14620)  
[Meta Property](https://wiki.genexus.com/commwiki/wiki?14622)  
[MetaEquiv Property](https://wiki.genexus.com/commwiki/wiki?14623)


|  |
| --- |
| **Backlinks** |
| [Form Control](https://wiki.genexus.com/commwiki/wiki?14619) | [HeaderRawHTML Property](https://wiki.genexus.com/commwiki/wiki?14620) | [Meta Property](https://wiki.genexus.com/commwiki/wiki?14622) |
| [MetaEquiv Property](https://wiki.genexus.com/commwiki/wiki?14623) |

---
