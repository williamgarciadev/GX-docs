---
title: "Dynamic Property Values"
source_id: 4835
source_url: https://wiki.genexus.com/commwiki/wiki?4835
genexus_version: "18"
---

# Dynamic Property Values

When a Web Form is created by default certain control properties are initialized dynamically using an expression referencing an attribute or variable descriptive property. This way, the layout of controls such as *Textblocks* and *Grid Columns* which generally are related to attributes or variable in the Web Form are completely in synch with their related control appearence properties.  
  
When inserting a list of attributes\variables to the form:

* each *Textblock* control associated to each attribute/variable holds it's *Title* property.
* each *Grid Column* control associated to each element the *ColumnTitle* property.

Everytime you change these attribute or variable properties, the change will be automatically propagated to all Web Forms using these dynamic property values.

### [Syntax](#Syntax)

*PropertyValue*

```
 = expression
```

Where:

*expression*

{*literalconstant* | *attributeproperty*} [ + *expression* ]

*literalconstant*

```
 \?[^\?\n]*\?
```

*attributeproperty*

```
 {attribute | variable}.propertyname
```

*propertyname*

**Title** | **Description** | **ColumnTitle**

### [Examples](#Examples)

For example, there is a Product transaction textblock. Note how every Textblock in the *Caption* property references it's associated [ContextualTitle](https://wiki.genexus.com/commwiki/wiki?4842) attribute property. The IDE translates "*=ProductName.ContextualTitle*" and displays the associated value in the WebForm.

`[imagen omitida: wiki id 7253]`

At runtime you will se the corresponding property value:

`[imagen omitida: wiki id 7255]`

In the same example, when using a grid check how all columns from the Invoice transaction grid, references in the *Title* property the related *ColumnTitle* attribute property.

`[imagen omitida: wiki id 7254]`

At runtime you will se the following:

`[imagen omitida: wiki id 7256]`

### [More examples](#More+examples)

|  |  |  |
| --- | --- | --- |
| **Textblock Caption or Grid Column Title** | **What do you see on the form at design and run-time?** | **Notes** |
| =CustomerId.Description | Customer | Assuming the Description property of attribute CustomerId is "Customer" |
| ="-" + CustomerName.Title + "by " + CountryName.Description | -customers by country name | Assuming the Title property of CustomerName is "customers" and the Description property of CountryName is "country name". |
| CustomerId: | CustomerId: | This is not an expression just a plain text, dynamic property value not used. |

### [Notes](#Notes)

* The expression is evaluated at design time.
* The translation process is not affected by expressions. The expression is first evaluated and its actual value is then translated.


|  |
| --- |
| **Backlinks** |
| [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) | [ContextualTitle property](https://wiki.genexus.com/commwiki/wiki?4842) |

---
