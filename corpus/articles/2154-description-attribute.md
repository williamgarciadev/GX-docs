---
title: "Description attribute"
source_id: 2154
source_url: https://wiki.genexus.com/commwiki/wiki?2154
genexus_version: "18"
---

# Description attribute

The Description attribute is the attribute that has the greatest semantic meaning in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

In other words, it is the attribute that best describes (or represents) the Transaction.

By default, the first attribute in the Transaction structure with a character data type is defined as **Description attribute**.

The icon with a magnifying glass stands for the Description attribute:

`[imagen omitida: wiki id 52138]`

For example, in the Category Transaction, the CategoryName attribute is the Description attribute.

You can define a different attribute as the Description one using the corresponding pop-up menu, or define no Description attribute at all.

 A good Description attribute must follow these properties:

* Uniqueness. An attribute can be the Description attribute of only one Transaction.
* Just one attribute. A [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868) can be composed of many attributes, but a Description attribute must be just one attribute.
* Meaningful for users. For example, CustomerName is better than CustomerId.
* Not ubiquitous. Not all transactions have a Description Attribute.

Because of these properties, a Description attribute is usually a [Candidate Key](https://wiki.genexus.com/commwiki/wiki?2199,,).

The Description attribute is automatically considered and used when GeneXus generates applications. For example, when applying the [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) to [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s that are automatically generated show the Description attributes with a link that opens a layout that displays more information related to the record involved.

### [Notes](#Notes)

* There can be a Description attribute per level.
* Not all Transactions (or levels) must have a Description attribute.


|  |
| --- |
| **Backlinks** |
| [Image Attribute Property](https://wiki.genexus.com/commwiki/wiki?15153) | [Orders property](https://wiki.genexus.com/commwiki/wiki?25472) | [Orders property (GeneXus 18 upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55997) |
| [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) | [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) | [Work With for Web View node](https://wiki.genexus.com/commwiki/wiki?5646) |

---
