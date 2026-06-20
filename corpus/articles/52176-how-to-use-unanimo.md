---
title: "How to use Unanimo"
source_id: 52176
source_url: https://wiki.genexus.com/commwiki/wiki?52176
genexus_version: "18"
---

# How to use Unanimo

This article is a guide on how to use Unanimo [Design System](https://wiki.genexus.com/commwiki/wiki?40108) in a [new Knowledge Base](https://wiki.genexus.com/commwiki/wiki?9596) and in an existing one.

### [In a new Knowledge Base](#In+a+new+Knowledge+Base)

Since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066), when you create a new Knowledge Base, the GeneXusUnanimo module is installed inside it.

`[imagen omitida: wiki id 52188]`

Also, a Design System will be automatically created with the name of the [KB](https://wiki.genexus.com/commwiki/wiki?2428); that is, <KB Name>, which is configured as the [Default Style](https://wiki.genexus.com/commwiki/wiki?8145) at the KB [version level](https://wiki.genexus.com/commwiki/wiki?7860) and includes an import to the GeneXusUnanimo.UnanimoWeb Design System as shown below:

```
styles KBName {

@import GeneXusUnanimo.UnanimoWeb;

}
```

This is all you need to start using Unanimo as the Design System in your new KB.

Then, when you start applying the patterns [Work With](https://wiki.genexus.com/commwiki/wiki?15975) and [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) automatically, all the GeneXus objects created by the patterns will use all the classes defined by Unanimo. See [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) to learn how to use these patterns. The same applies to the default forms in Transactions.

### [In an existing Knowledge Base](#In+an+existing+Knowledge+Base)

See [Migrate to Unanimo](https://wiki.genexus.com/commwiki/wiki?52177) to learn how to apply Unanimo to your existing Knowledge Base.

### [See Also](#See+Also)

[Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636)


|  |
| --- |
| **Backlinks** |
| [Customize Unanimo](https://wiki.genexus.com/commwiki/wiki?52178) | [Toc:Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) |

---
