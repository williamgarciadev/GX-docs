---
title: "Empty Grid Background Image property"
source_id: 17385
source_url: https://wiki.genexus.com/commwiki/wiki?17385
genexus_version: "18"
---

# Empty Grid Background Image property

Shows an image when the Grid has no data.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) called Customer:

**Customer  
{**  
   CustomerId\*  
   CustomerName  
   CustomerAddress  
   CustomerPhone  
**}**

Suppose you want to show the customer's list. To do so, apply the Work With for Smart Devices pattern to the Customer Transaction. After that, create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and add to it an entry point that calls the WorkWithDevicesClient.Client.List().

When the Menu object is executed and the entry point is taped, if there are customers in the database, the customer's list will be shown. However, if there are no records, the list will appear empty. If this last case occurs, to avoid showing an empty space you can complete the **Empty Grid Background Image property** with an image and you will see it like shown below:

:`[imagen omitida: wiki id 17405]`

### [See Also](#See+Also)

[Empty Grid Text property](https://wiki.genexus.com/commwiki/wiki?20224)  
[Empty Grid Text Class property](https://wiki.genexus.com/commwiki/wiki?20226)  
[Empty Grid Background Class property](https://wiki.genexus.com/commwiki/wiki?20227)


|  |
| --- |
| **Backlinks** |
| [Empty Grid Background Class property](https://wiki.genexus.com/commwiki/wiki?20227) | [Empty Grid Text Class property](https://wiki.genexus.com/commwiki/wiki?20226) | [Empty Grid Text property](https://wiki.genexus.com/commwiki/wiki?20224) |
|

---
