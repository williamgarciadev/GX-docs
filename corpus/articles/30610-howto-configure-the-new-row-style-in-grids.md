---
title: "HowTo: Configure the New Row style in grids"
source_id: 30610
source_url: https://wiki.genexus.com/commwiki/wiki?30610
genexus_version: "18"
---

# HowTo: Configure the New Row style in grids

The [New Row](https://wiki.genexus.com/commwiki/wiki?6816) style in grids is configured by using the *New Row Class property* available in the Theme.

*New Row Class* is a class property in the Theme available for [Grids](https://wiki.genexus.com/commwiki/wiki?15104,,) and Free Style Grids, whose purpose is to configure the class that will determine the settings of the grids "new row" link. See the image below where the "new row" link is highlighted:

`[imagen omitida: wiki id 30613]`

### [How to use the New Row Class property](#How+to+use+the+New+Row+Class+property+)

First, check the class associated with the grid (in the example it is the Grid class), and edit the *New Row Class* property for the Grid class in the Theme.

`[imagen omitida: wiki id 30612]`

`[imagen omitida: wiki id 30611]`

By default, the value of New Row Class is GridNewRow, which is a descendant of the Texblock class.

There, you can change the settings of the GridNewRow class as desired. For example, changing the Font Size would be as follows:

`[imagen omitida: wiki id 32494]`

**Note:**

If you want to change the text or position of the "new row" functionality, you need to use a control to execute that action:

* Drag a control to the form (it can be a button or text block in which the user can click on), and assign it the caption and the Theme class more convenient to your design
* Use the AddLines method the make GeneXus know that the default "New Row" link has to be eliminated and it will be replaced by your link.

See [HowTo: Work with rows in a Transaction Grid](https://wiki.genexus.com/commwiki/wiki?6816) for more information about this topic.

### [Samples](#Samples)

Here, a button to the form has been added, whose On Click Event is "AddLines".

`[imagen omitida: wiki id 30620]`

The control name of the transaction's grid is GridCustomer\_Address so the AddLines event is as follows:

```
Event 'AddLines'
    GridCustomer_Address.AddLines(1)
Endevent
```

At runtime:

`[imagen omitida: wiki id 30619]`
