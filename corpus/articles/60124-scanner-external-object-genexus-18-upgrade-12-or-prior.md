---
title: "Scanner external object (GeneXus 18 Upgrade 12 or prior)"
source_id: 60124
source_url: https://wiki.genexus.com/commwiki/wiki?60124
genexus_version: "18"
---

# Scanner external object (GeneXus 18 Upgrade 12 or prior)

The Scanner external object lets you programmatically scan barcodes (2D and QR Codes) using the device's camera.  
See also [Scanner Control](https://wiki.genexus.com/commwiki/wiki?15310) to associate an Edit control (attribute or variable) with the ability to enter barcode information directly into the field from the camera.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [ScanBarcode method](#ScanBarcode+method)

Scans a linear barcode or QR code and optionally filters a specific list of barcodes.

|  |  |
| --- | --- |
| **Return value** | [VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778) |
| **Parameters** | [ barcodeTypes:Collection(BarcodeTypes) ] |

Read more in [HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21661).

### [ScanInLoop method](#ScanInLoop+method)

Scans several barcodes at once, optionally using a specific list of barcodes. No user intervention is required until it stops reading.

|  |  |
| --- | --- |
| **Return value** | ScannedBarcodes |
| **Parameters** | [ beepOnEachRead:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374) ] [ , barcodeTypes:Collection(BarcodeType) ] |

Read more in [HowTo: Use the ScanInLoop method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21663).

## [Events](#Events)

It does not have any.

## [Code example](#Code+example)

In the shopping cart scenario, suppose you have a Scan button in the Layout to read a product barcode, add it automatically to the cart, and finally edit the product in the cart to show the product info and indicate the quantity:

```
Event 'Scan'
  Composite
    &EANBarcodeTypes.Add(BarcodeType.EAN_13)
    &ScanBarcode = ScannerAPI.ScanBarcode(&EANBarcodeTypes)
    &CartItemId = CartItem_InsertButNotConfirmed(&ScanBarcode,&Messages)
    WorkWithDevicesCartItem.CartItem.Detail(&CartItemId, &ScanBarcode)
  EndComposite
EndEvent
```

## [Domains](#Domains)

### [BarcodeType domain](#BarcodeType+domain)

Supported barcode types.

|  |  |
| --- | --- |
| **Aztec** | [Aztec code](https://en.wikipedia.org/wiki/Aztec_Code) linear barcode. |
| **Code128** | [Code 128](https://en.wikipedia.org/wiki/Code_128) linear barcode. |
| **Code39** | [Code 39](https://en.wikipedia.org/wiki/Code_39) linear barcode. |
| **Code39Mod43** | [Code 39 mod 43](https://en.wikipedia.org/wiki/Code_39#Code_39_mod_43) linear barcode. |
| **Code93** | [Code 93](https://en.wikipedia.org/wiki/Code_93) linear barcode. |
| **DataMatrix** | [Data Matrix](https://en.wikipedia.org/wiki/Data_Matrix) 2D barcode. |
| **EAN\_13** | [European Article Number 13-digit code](https://en.wikipedia.org/wiki/International_Article_Number#EAN-13_encoding) linear barcode. |
| **EAN\_8** | [European Article Number 8-digit code](https://en.wikipedia.org/wiki/International_Article_Number) linear barcode. |
| **Interleaved2of5** | [Interleaved 2 of 5 code](https://en.wikipedia.org/wiki/Interleaved_2_of_5) linear barcode. |
| **ITF14** | [ITF-14 code](https://en.wikipedia.org/wiki/ITF-14) linear barcode. |
| **PDF417** | [PDF147 code](https://en.wikipedia.org/wiki/PDF417) 2D barcode. |
| **QR** | [QR code](https://en.wikipedia.org/wiki/QR_code) 2D barcode. |
| **UPC\_E** | [UPC-E](https://en.wikipedia.org/wiki/Universal_Product_Code#UPC-E) linear barcode. |

## [Structured Data Types](#Structured+Data+Types)

### [ScannedBarcodes](#ScannedBarcodes)

* Collection( Barcode:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778) )  
  A set of scanned barcode values.

## [Scenarios](#Scenarios)

The device's camera can be used in multiple scenarios to enter information more easily without the user having to type. For instance:

* Retrieve the store's product information from its linear barcode and add it to the shopping cart.
* Add contact information by reading personal cards/tags, including QR Codes.
* Read a sequence of several codes (linear or QR codes) until the user decides to stop reading. This can be useful to emulate a supermarket cashier.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

## [Availability](#Availability)

This external object is available since [GeneXus X Evolution 2 Upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22061,,).

* For [GeneXus X Evolution 2 Upgrade 2](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?19995,,) or older versions, refer to [HowTo: Using ScanBarcode Method from Interop in SDApi for Smart Devices](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15882,,).
* barcodeTypes filter parameter for ScanBarcode and ScanInLoop methods in Android generator as of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?40782,,). Code39Mod43 and Interleaved2of5 methods are not supported.
* beepOnEachRead parameter for ScanInLoop method is only available for the iOS generator. In Android, the beep sound is always played if the device is not muted.
* Since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39737,,), in Android apps, there is no need to have an external application installed to scan the barcodes.

## [See Also](#See+Also)

* [HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21661)
* [HowTo: Use the ScanInLoop method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21663)
