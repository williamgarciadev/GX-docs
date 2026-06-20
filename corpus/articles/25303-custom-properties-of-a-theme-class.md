---
title: "Custom properties of a Theme Class"
source_id: 25303
source_url: https://wiki.genexus.com/commwiki/wiki?25303
genexus_version: "18"
---

# Custom properties of a Theme Class

This enables us to specify additional properties for a class in the GeneXus Theme. It applies to [Themes for Web applications](https://wiki.genexus.com/commwiki/wiki?6420).

Additional [CSS](http://en.wikipedia.org/wiki/Cascading_Style_Sheets) properties are added to the Class or HTML node where this property is specified.

#### [Description](#Description)

For the case of Themes for web, properties specified here will be included in the Class definition, in the CSS file generated for the Theme.

It also applies to Themes used by applications generated with the [Windows 8 Generator](https://wiki.genexus.com/commwiki/wiki?20825,,).

#### [Syntax](#Syntax)

String values with CSS properties separated by ";"

#### [Example](#Example)

```
background-color: white; background-image: url('imagens/fundo'); z-index: -1
```

#### [Scope](#Scope)

**Objects:** [Themes](https://wiki.genexus.com/commwiki/wiki?4447,,)  
**Classes:**All [Classes](https://wiki.genexus.com/commwiki/wiki?6246) and [HTML Nodes](https://wiki.genexus.com/commwiki/wiki?6262,,)  
**Interfaces:**Web

### [Note](#Note)

As of now, it accepts CSS format for Win8 and Web generators, and has no effect on others platforms.


|  |
| --- |
| **Backlinks** |
| [Custom Properties property](https://wiki.genexus.com/commwiki/wiki?50009) | [HowTo: Display a menu in a responsive application](https://wiki.genexus.com/commwiki/wiki?25778) |

---
