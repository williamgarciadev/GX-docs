---
title: "Structured Data Type (SDT) object"
source_id: 10021
source_url: https://wiki.genexus.com/commwiki/wiki?10021
genexus_version: "18"
---

# Structured Data Type (SDT) object

Defines a compound data type that groups fields of other data types and collections.

### [Description](#Description)

Largely known as Record, Struct, or Structure in most programming languages, GeneXus offers the **Structured Data Type (SDT) object** to allow defining compound data types.

A Structured Data Type (SDT) object represents data whose structure is made up of several members.

After [creating an SDT object](https://wiki.genexus.com/commwiki/wiki?9931), you are ready to define its structure:

`[imagen omitida: wiki id 10079]`

Also, instead of starting to define the SDT’s members one by one, you can drag a Transaction (in the example, the Customer Transaction) from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) and drop it on the SDT structure. Thus, you obtain in the SDT structure the members automatically created with the same names as the attributes in the Customer Transaction with their data types:

`[imagen omitida: wiki id 45397]`

You can define **only** **variables** based on SDTs. On the other hand, you cannot define attributes based on SDTs because attributes may only store simple data.

When defining a member in an SDT design, you must specify the Name property identifying the member; therefore, there cannot be two members with the same name. The [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) allows selecting among the following data types:

* GeneXus [Basic data types](https://wiki.genexus.com/commwiki/wiki?6905) (Numeric, Character, Date, etc.)
* [GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221)
* Another already defined SDT

The **IsCollection checkbox** allows you to define whether the member has multiple (several) instances or not.

### [See Also](#See+Also)

[Structured Data Type Properties](https://wiki.genexus.com/commwiki/wiki?8081)  
[Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589)  
[Structured Data Type editor](https://wiki.genexus.com/commwiki/wiki?6365)  
[XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Structured Data Types](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/structured-data-types-6104741)


|  |
| --- |
| **Pages** |
| [Exposed name property](https://wiki.genexus.com/commwiki/wiki?8087) | [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296) | [Recursive SDTs](https://wiki.genexus.com/commwiki/wiki?4680) |

---
