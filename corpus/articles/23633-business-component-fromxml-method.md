---
title: "Business Component FromXml method"
source_id: 23633
source_url: https://wiki.genexus.com/commwiki/wiki?23633
genexus_version: "18"
---

# Business Component FromXml method

Provides the opposite to the [ToXml method](https://wiki.genexus.com/commwiki/wiki?23483).

It can be applied to a character field whose content has a specific XML format (predefined by GeneXus), in order to extract from the XML format, the value of each attribute of a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), and charge a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846).

### [Syntax:](#Syntax%3A+)

**&***VarBasedOnBC*.**FromXml(**&String**)**

**Where:**

*&VarBasedOnBC*  
      Is a variable defined in a GeneXus object, based on a Business Component.

*&String*  
     Is a variable or attribute based on a character type and it must contain a specific XML format, with a Tag for each Transaction attribute.

### [See also](#See+also)

[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
