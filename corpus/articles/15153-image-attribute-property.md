---
title: "Image Attribute Property"
source_id: 15153
source_url: https://wiki.genexus.com/commwiki/wiki?15153
genexus_version: "18"
---

# Image Attribute Property

Like the [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154) the Image Attribute is the attribute that best describes (or represents) a Transaction. For example, in the Customer Transaction, CustomerImage is usually the Image Attribute.

In Smart Devices Applications , the image attribute usually is the one that appears in the List view (Think on the Contact Image in the Contacts app of your phone)

A good Image attribute must follow these properties:

Uniqueness. An attribute can be the Image Attribute of only one Transaction.  
Just one attribute. A [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868) can be composed of many attributes, but a Image Attribute must be just one attribute.  
Meaningful for users. E.g. CustomerImage is better than CustomerId.  
Not ubiquitous. Not all transactions have an Image Attribute.

Notes:

There can be an Image Attribute per Level  
Not all Transactions (or Levels) must have an Image Attribute.
