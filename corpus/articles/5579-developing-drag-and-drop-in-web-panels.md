---
title: "Developing Drag and Drop in Web Panels"
source_id: 5579
source_url: https://wiki.genexus.com/commwiki/wiki?5579
genexus_version: "18"
---

# Developing Drag and Drop in Web Panels

Drag and Drop in [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916) lets the end-user drag the content associated with web controls from one place to another, in order to take some actions.

End-users can, for example, drag a product from a products list to an invoice grid. Or drag products to a shopping cart image.

**Important Note**: The content can be dragged from and to different [Web Components](https://wiki.genexus.com/commwiki/wiki?31172). So, you can have a products Grid in a Web Component and a cart Image in another.

## [Sample](#Sample)

Suppose that you want to define a shopping web layout where the user can drag the products he/she wants to buy to a cart image, in order to add them to the shopping list.

To achieve this you only have to configure the [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) in a "Products" Grid and program the Drop event of the image where the product will be added to the list. That's all!

1. Set the [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) of the "Products" Grid:

`[imagen omitida: wiki id 50458]`

2. Code the following for the "Cart" image.

```
Event Cart.Drop(&ProductId,&ProductDsc)
     //Here is the code to buy the product
     msg('Buy ' + &ProductDsc)
EndEvent
```

3. At runtime, drag the selected Grid row to the image.

`[imagen omitida: wiki id 50459]`

Download the example [here](https://wiki.genexus.com/commwiki/wiki?50424,,)

## [Implementation Details](#Implementation+Details)

### [Drag & Drop events](#Drag+%26+Drop+events)

Supported controls: Image, Text Block, [Table](https://wiki.genexus.com/commwiki/wiki?6001), [Grid](https://wiki.genexus.com/commwiki/wiki?24817) and FreeStyle Grid, [Web Component](https://wiki.genexus.com/commwiki/wiki?31172), [Button](https://wiki.genexus.com/commwiki/wiki?6011).

#### [**Drag event**](#Drag+event)

Syntax: <control>.Drag((out:)parameter)

The parameter is only one and is always an out variable parameter. This parameter will be loaded with the data you want to drag. If you need to drag several elements, you have to load them into an SDT.

#### [**Drop event**](#Drop+event)

Syntax: <control>.Drop(parameters)

The parameters can only be variables. These parameters will be loaded with the corresponding values of the Drag event parameters.

**Note**: There is no difference between the navigation of any user event and the navigation of the Drop event (Drag event). The rules that apply for the former apply also for the latter.

#### 

### [Drag & Drop between different Web objects](#Drag+%26+Drop+between+different+Web+objects)

Remember that the information can be dragged from and to different Web Components. So, there has to be a way to identify the information that is able to be dragged from a control and dropped into another one.

The way of identifying that is the following:

1. If you have the following source code in an object "A":

```
  Event <control>.Drop(&P1,&P2,..,&Pn)

  EndEvent
```

2. Any other object "B" which satisfies the following:

Has a Grid with Allow Drag property set to "Yes", and the columns of the Grid match exactly the parameters of the drop event, and has optionally others:

&P1,&P2,..,&Pn,..(Others)

In this case, the user will be able to drag information from the Grid to the control. The same happens if the columns are attributes named P1, P2,.. Pn.

Graphically:

Drag(X,Y,Z,T) ------------> Drop(X,Y)

**Note**: The same applies to Allow Drop property of Grids. In that case, the Grid which has Allow Drop property set to "Yes" needs to have a subset of the columns of the Grid which has Allow Drag property set to "Yes". The order of columns is not relevant. If any of the variables is based on an SDT, it's matched by DataType only, not by name.

### [Examples links](#Examples+links)

[Drag and Drop in Applications Sample 1](https://wiki.genexus.com/commwiki/wiki?6584)  
[Drag and Drop in Applications Sample 2](https://wiki.genexus.com/commwiki/wiki?6585)  
[Drag and Drop in Applications Sample 3](https://wiki.genexus.com/commwiki/wiki?6586)  
[Drag and Drop in Applications Sample 4](https://wiki.genexus.com/commwiki/wiki?6587)

### [See also](#See+also)

[Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766)  
[Allow Drop property](https://wiki.genexus.com/commwiki/wiki?9765)


|  |
| --- |
| **Backlinks** |
| [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) | [Allow Drop property](https://wiki.genexus.com/commwiki/wiki?9765) | [Category:Drag and Drop](https://wiki.genexus.com/commwiki/wiki?5730) |
| [Drag and Drop in Applications Sample 1](https://wiki.genexus.com/commwiki/wiki?6584) | [Drag and Drop in Applications Sample 2](https://wiki.genexus.com/commwiki/wiki?6585) | [Drag and Drop in Applications Sample 3](https://wiki.genexus.com/commwiki/wiki?6586) | [Drag and Drop in Applications Sample 4](https://wiki.genexus.com/commwiki/wiki?6587) |
| [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) |

---
