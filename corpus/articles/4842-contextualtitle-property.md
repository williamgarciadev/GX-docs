---
title: "ContextualTitle property"
source_id: 4842
source_url: https://wiki.genexus.com/commwiki/wiki?4842
genexus_version: "18"
---

# ContextualTitle property

The Contextual Title Property applies to attributes. It holds a description that is "meaningful" only when the "context" is set.

### [Description](#Description)

Besides defaults, you may use it when designing your forms using [dynamic property values](https://wiki.genexus.com/commwiki/wiki?4835).  
  
The default contextual title is calculated in the following way:

* If the name of the attribute (or variable) contains only one "word" (words are delimited by uppercase characters), then the name is used (Name -> Name).
* If the name contains exactly two words, then the second one is used (CustomerId -> Id)
* If the name contains more than two words, the last two are used (CompanyLegalName -> Legal Name; for ClientIdNameForUse -> For Use).

#### [Note](#Note)

In transactions, when the default web form is not applied, new attributes that are added to the web form use [ColumnTitle](https://wiki.genexus.com/commwiki/wiki?7235) instead, because "context" isn't meaningful.

In case of double byte characters it behaves the same way as lowercase characters.

### [Samples](#Samples)

Say attribute CustomerAddress is on a form. What label should it have? Well, it depends on the context. If the form is the Customer Transaction form, then you may want to use just "Address". If the form is the Invoice Transaction Form you may want to use "Customer Address" instead. This is the idea behind the Contextual Title property.  
  
An attribute is assumed to be "in context" if it logically belongs to the transaction level that is being processed. This excludes foreign keys and inferred attributes (with some exceptions).

For example in the following Transaction:

Customer

{  
      CustomerId\*  
      CustomerName  
      CustomerAddress  
      CountryId  (FK)  
      CountryName  
}

The attributes belonging to the Customer Transaction that will be taking Contextual Title property are: CustomerId, CustomerName and CustomerAddress.

So, CountryId and CountryName will be taking Title property.

This behavior happen both for Transactions and Work With Patterns.

### [Scope](#Scope)

**Objects:** Transaction


|  |
| --- |
| **Backlinks** |
| [Description property](https://wiki.genexus.com/commwiki/wiki?7446) | [Dynamic Property Values](https://wiki.genexus.com/commwiki/wiki?4835) | [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) |

---
