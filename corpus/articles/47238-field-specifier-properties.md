---
title: "Field Specifier properties"
source_id: 47238
source_url: https://wiki.genexus.com/commwiki/wiki?47238
genexus_version: "18"
---

# Field Specifier properties

The concept of “field specifiers” is widely used in the GeneXus’ Native Mobile generators. You’ll find several of these “field specifier” properties in the documentation, such as the Video control’s [Thumbnail Field Specifier property](https://wiki.genexus.com/commwiki/wiki?47171,,) or the Map control’s [Pin Image Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42214).

But, what is a"field specifier"?

When a control needs to reference the value stored inside an attribute or a variable, it defines an “attribute” property, such as the [Thumbnail Attribute property](https://wiki.genexus.com/commwiki/wiki?47170,,) or the [Pin Image Attribute property](https://wiki.genexus.com/commwiki/wiki?42213) to use the same examples as before.

In GeneXus’ IDE, when you edit one of these “attribute” properties, you can always choose a SDT-based variable. But then, which member from the SDT should be used?

That’s when the “field specifier” is needed.

An “attribute” property has always a matching “field specifier” property, so that, when you choose an SDT-based variable, you can specify which field to use.

### [Example](#Example)

Suppose you have a &places variable that has a member named Location that is a GeoPoint, and you are showing that variable on a Map.

To use that location for the pins in the map, you should set:

* [Location Attribute](https://wiki.genexus.com/commwiki/wiki?42209): &places
* [Location Field Specifier](https://wiki.genexus.com/commwiki/wiki?42210): Item(0).Location

Note the use of "item(0)" placeholder in the field specifier. That 0 value means the current item in the collection.


|  |
| --- |
| **Backlinks** |
| [Data Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42192) |

---
