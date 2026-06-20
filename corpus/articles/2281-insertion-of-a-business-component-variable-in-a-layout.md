---
title: "Insertion of a Business Component variable in a Layout"
source_id: 2281
source_url: https://wiki.genexus.com/commwiki/wiki?2281
genexus_version: "18"
---

# Insertion of a Business Component variable in a Layout

It is possible to insert a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) variable in a Layout by selecting the **Insert > Variable** option from the GeneXus main menu or by dragging the control from the [Toolbox](https://wiki.genexus.com/commwiki/wiki?10000).

The following dialog appears and you can clear the [properties](https://wiki.genexus.com/commwiki/wiki?2276) that you don't want to show in the Layout:

`[imagen omitida: wiki id 50109]`

If the Business Component variable has nested levels (as the previous image shows), they will be inserted in grids. For example, if the &Invoice Business Component variable is inserted in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) Layout, it looks as follows:

`[imagen omitida: wiki id 50110]`

As the variables in Web Panels are editable by default, all the &Invoice properties are editable as well.

Now, suppose you want to allow the user to enter an invoice ID value, and load all the invoice data by pressing a button. The following implementation solves this scenario:

`[imagen omitida: wiki id 50111]`

```
Event 'Get'
    &Invoice.Load(&Invoice.InvoiceId)
Endevent
```


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
