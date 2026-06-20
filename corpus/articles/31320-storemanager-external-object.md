---
title: "StoreManager external object"
source_id: 31320
source_url: https://wiki.genexus.com/commwiki/wiki?31320
genexus_version: "18"
---

# StoreManager external object

The StoreManager external object is a component allows you to manage [In-App Purchases](https://wiki.genexus.com/commwiki/wiki?20003,,) in your applications.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [CanMakePurchases property](#CanMakePurchases+property)

Allows you to know if the device can make purchases (True) or not (False). For example, it can be used to restrict purchases if the device does not admit them.

## [Methods](#Methods)

### [GetProducts method](#GetProducts+method)

Given a list of products, returns a collection with detailed information about them. Useful to get the title in the user's local language and the price in the user's local currency.

|  |  |
| --- | --- |
| **Return value** | StoreProduct |
| **Parameters** | ProductIdentifications:Collection([VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)) |
|  |  |

### [PurchaseProduct method](#PurchaseProduct+method)

Sends the purchase request of the given product to the platform's In-App Purchases store.

**Note**: On Android, the Quantity parameter only accepts the value 1 because every product can be *purchased* or *not purchased*.

|  |  |
| --- | --- |
| **Return value** | StoreProduct |
| **Parameters** | ProductIdentifier:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778), [ , Quantity:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) ] |
|  |  |

### [GetPurchases method](#GetPurchases+method)

Gets a list of information of the user's purchased products.

|  |  |
| --- | --- |
| **Return value** | PurchasesInformation |
| **Parameters** | None |
|  |  |

### [ConsumeProduct method](#ConsumeProduct+method)

Consumes a product for which the user has a purchase and returns the success status.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | ProductIdentifier:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778) |
|  |  |

### [RestorePurchases method](#RestorePurchases+method)

Only available for iOS. Restore the purchases through the device.

|  |  |
| --- | --- |
| **Return value** | PurchasesInformation |
| **Parameters** | None |
|  |  |

## [Events](#Events)

### [PurchaseStateChange event](#PurchaseStateChange+event)

This event only applies to iOS. When a purchase is made, this event will be called indefinitely if the Handled parameter is set to False until the developer sets it to True. The reason for this behavior is that iOS does not persist the information of a purchase (as Android does) when the product type is consumable. A typical scenario might occur when the app crashes without the response of the store platform after a transaction request. In such case, the purchase can be processed when the app is opened again. **It's the responsibility of the developers to persist in their systems the user status in relation to the billings** (in replacement of *EnableProduct* or *DisableProduct* deprecated methods --- see the previous version of this document for details).

|  |  |
| --- | --- |
| **Input** | Purchase:PurchaseResult, PurchaseState:StorePurchaseState, Handled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Output** | None |
|  |  |

## [Domains](#Domains)

### [StorePurchaseState domain](#StorePurchaseState+domain)

Set of state values of a purchase. Only applies for iOS.

|  |  |
| --- | --- |
| **Purchased** | When the purchase was successful. |
| **Failed** | When the purchase fails. |
| **Restored** | When the purchases are restored. |
| **Deferred** | When the purchase depends on parental control. |
|  |  |

### [StorePurchasePlatform domain](#StorePurchasePlatform+domain)

Store platforms where the purchase was made.

|  |  |
| --- | --- |
| **GooglePlay** | Google Play (for Android) as store platform. |
| **iTunes** | iTunes (for iOS) as store platform. |
|  |  |

### [StoreProductType domain](#StoreProductType+domain)

Nature of the purchased product.

|  |  |
| --- | --- |
| **Subscription** | The purchase is a subscription. |
| **Product** | The purchase is a product. |
|  |  |

### [StorePurchaseStatus domain](#StorePurchaseStatus+domain)

Status of a purchase after it has been validated with the platform stores (Google/Apple).

|  |  |
| --- | --- |
| **Invalid** | The purchase is invalid. |
| **Valid** | The purchase is valid. |
| **Expired** | Indicate if the purchase of a subscription has been expired. |
| **Canceled** | On iOS indicate if the purchase has been canceled by the Apple Store Support Team.  On Android, if the purchase has been canceled by the user, or if the purchase is a subscription canceled by the system (e.g. billing problem) |
| **Deferred** | The purchase is waiting for validation of parental control. |
|  |  |

## [Structured Data Types](#Structured+Data+Types)

### [PurchaseResult](#PurchaseResult)

* Success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
  Indicates if the purchase process was successfully completed.
* PurchaseId:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Purchase identifier from the platform store.
* PurchasePlatform:StorePurchasePlatform   
  Store platform where the purchase was made.
* ProductIdentifier:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Purchased product identifier.
* TransactionData:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Encrypted data of the purchase transaction.

### [PurchaseInformation](#PurchaseInformation)

Given a platform store, it keeps the information of a collection of purchases.

* Purchases:Collection( PurchaseResult )  
  Collection of purchase result for each product queried.
* Receipt:[LongVarChar(2M)](https://wiki.genexus.com/commwiki/wiki?7371)  
  Receipt information retrived from Apple.
* PurchasePlatform:StorePurchasePlatform  
  The store platform where the purchase was made.

### [StoreProduct](#StoreProduct)

* LocalizedTitle:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Product title in the user local language.
* LocalizedDescription:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Product description in the user local language.
* LocalizedPriceAsString:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  String with the product price indicated in the user local currency.
* Identifier:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Product identifier.
* Purchased:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
  Indicates if the product has been purchased by the user.

## [Notes](#Notes)

* The concept of "*enable a product*" introduced in the *PurchaseStateChange event* section is only applicable for iOS that manages the purchases on the client-side. Android, on the other hand, centralizes the purchases on the Google Play's servers and it only notices when a product was purchased or not. For example, the "*enable*" concept allows the developer to implement a gift-mechanism on the device (i.e. under certain conditions, it is possible to enable a product for free). The same scenario on Android can be solved from the [Google Play's console](https://play.google.com/apps/publish/) using [In-app Promotion codes](https://developer.android.com/google/play/billing/billing_promotions.html).
* In order to simulate the "deferred" state in iOS, the developer can add the *GXSimulateAskToByInSandbox* key into the generated project adopting boolean value.  
  A typical scenario is when the app is installed in a children's device and the developer uses *Progress.Show()* while the purchase is being validated. If the parent takes a long time to validate or reject the request of its child, the progress status will be displayed indefinitely.

## [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

## [See also](#See+also)

[What is an In-App Purchase](https://wiki.genexus.com/commwiki/wiki?20003,,)  
[How to configure In-App Billing in an Android application](https://wiki.genexus.com/commwiki/wiki?21330)  
[In-App Purchase Sample - Classified Ads](https://wiki.genexus.com/commwiki/wiki?20010)  
[In-App Purchase Sample - My Kitchen](https://wiki.genexus.com/commwiki/wiki?20021)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [How to configure In-App Billing in an Android application](https://wiki.genexus.com/commwiki/wiki?21330) | [In-App Purchase Sample - Classified Ads](https://wiki.genexus.com/commwiki/wiki?20010) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [Use Huawei In App Billing property](https://wiki.genexus.com/commwiki/wiki?47543) |

---
