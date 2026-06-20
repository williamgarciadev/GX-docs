---
title: "HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications"
source_id: 21661
source_url: https://wiki.genexus.com/commwiki/wiki?21661
genexus_version: "18"
---

# HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications

This tutorial is a guide for using the ScanBarcode method offered by the [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316).

`[imagen omitida: wiki id 54849]`

The ScanBarCode method returns a [VarChar](https://wiki.genexus.com/commwiki/wiki?6778)(200).

### [Step 1](#Step+1)

In this example you will use the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

`[imagen omitida: wiki id 15883]`

### [Step 2](#Step+2)

Apply the [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) to it.

### [Step 3](#Step+3)

Go to the Section (General) node located under the Detail node. From the Layout tab, right-click on the Application Bar and insert a button as follows:

`[imagen omitida: wiki id 54850]`

### [Step 4](#Step+4)

Add the following behavior to the "Scan Now!" event:

```
Event 'Scan Now!'
    Composite
         &VarCode = Scanner.ScanBarcode()
         Proc(&varCode, ProductId)
    EndComposite
EndEvent
```

The &VarCode definition is:

`[imagen omitida: wiki id 15884]`

The ScanBarcode method returns the value scanned. This value is returned in a [VarChar](https://wiki.genexus.com/commwiki/wiki?6778)(200)

After scanning the barcode you will want to use that value.

Therefore, you can call a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that uses that information. (This is one way to use the information obtained, there are many ways to use it).

Suppose the called Procedure contains the following Parm rule:

```
parm(&varCode, ProductId);
```

And its Source contains the following code:

```
For Each Product
       where ProductId = &ProductId
             ProductNumber = &varCode             
EndFor
```

Done. When scanning a code, a Procedure will be called to store the number in the ProductNumber attribute.


|  |
| --- |
| **Backlinks** |
| [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316) |

---
