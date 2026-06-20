---
title: "Qualified Name property"
source_id: 22477
source_url: https://wiki.genexus.com/commwiki/wiki?22477
genexus_version: "18"
---

# Qualified Name property

Read-only property showing the actual object name. It is composed of the [Module path](https://wiki.genexus.com/commwiki/wiki?22437) and the Object name.

## [Syntax](#Syntax)

[ModuleName1.ModuleName2.ModuleNameN.]ObjectName

**Where:**  
  
*[ModuleName1.ModuleName2.ModuleNameN.]*  
   Is the [Module path](https://wiki.genexus.com/commwiki/wiki?22437).

**Note:** The [Root module](https://wiki.genexus.com/commwiki/wiki?22439) is always omitted in the Module path.

*ObjectName*  
   Is the name of the Object (its [Name property](https://wiki.genexus.com/commwiki/wiki?6985)).

## [Description](#Description)

This — read-only — property is intended to provide a quick way to identify an object, as several objects can have the same value for the [Name property](https://wiki.genexus.com/commwiki/wiki?6985) if they have a different [Module path](https://wiki.genexus.com/commwiki/wiki?22437).

## [Samples](#Samples)

Consider the following Product [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

`[imagen omitida: wiki id 25102]`

It will have the Qualified Nameproperty set as follows: Purchases.Stock.Product

`[imagen omitida: wiki id 25101]`

## [See Also](#See+Also)

[Module object](https://wiki.genexus.com/commwiki/wiki?22411)   
[Name property](https://wiki.genexus.com/commwiki/wiki?6985)


|  |
| --- |
| **Backlinks** |
| [GetInternalURI method](https://wiki.genexus.com/commwiki/wiki?52480) | [HowTo: Create a Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52874) | [Import style rule](https://wiki.genexus.com/commwiki/wiki?49346) |
| [Category:Module object](https://wiki.genexus.com/commwiki/wiki?22411) | [Table of contents:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Modules - Grammar](https://wiki.genexus.com/commwiki/wiki?25609) | [Modules - Known Limitations](https://wiki.genexus.com/commwiki/wiki?22492) |
| [Modules - Object names](https://wiki.genexus.com/commwiki/wiki?22483) | [Modules - URL Syntax](https://wiki.genexus.com/commwiki/wiki?25224) | [Modules vs. Folders](https://wiki.genexus.com/commwiki/wiki?22470) | [Type Property](https://wiki.genexus.com/commwiki/wiki?43861) |
| [Which objects can be defined in a module?](https://wiki.genexus.com/commwiki/wiki?23850) |

---
