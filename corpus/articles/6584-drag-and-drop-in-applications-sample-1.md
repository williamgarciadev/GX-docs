---
title: "Drag and Drop in Applications Sample 1"
source_id: 6584
source_url: https://wiki.genexus.com/commwiki/wiki?6584
genexus_version: "18"
---

# Drag and Drop in Applications Sample 1

Consider a shopping form where the products available for purchase are loaded in a freestyle grid. By dragging the product photo to the cart image you add that product to your shopping cart.

`[imagen omitida: wiki id 6588]`

##### [How To Do It..](#How+To+Do+It..)

1. Define two variables called &productsdt and &productsdtitem, based on the following SDT:

`[imagen omitida: wiki id 6589]`

2. Code the "Drag" Event. The "photo" is an image control loaded for each product in the grid. In the drag event the &productsdtitem is by default an "out" parameter, and is loaded with the productid and productname values.

```
Event photo.Drag(&productsdtitem)  
   &productsdtitem.productid = &ProductId  
   &productsdtitem.productname = &ProductName  
EndEvent
```

3. Code the "Drop" Event. "Cart" is the image where products are dropped to be purchased. The "in" parameter for this event should be the &productsdtitem, or any variable based on the same SDT that &productsdtitem is based on.

```
Event cart.Drop(&productsdtitem)  
    msg('Buy ' + &productsdtitem.productname)  
EndEvent
```

Related links: [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) | [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) |

---
