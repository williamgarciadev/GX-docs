---
title: "Analytics external object (GeneXus 18 Upgrade 2 or prior)"
source_id: 54509
source_url: https://wiki.genexus.com/commwiki/wiki?54509
genexus_version: "18"
---

# Analytics external object (GeneXus 18 Upgrade 2 or prior)

Analytics external object enlarge those scenarios that can be solved using [Enable (Google) Analytics property](https://wiki.genexus.com/commwiki/wiki?21716) on client-side events.

**Warning**: All methods are not available in objects without UI, such as [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) or [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270).

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any

## [Methods](#Methods)

### [TrackView method](#TrackView+method)

It allows tracking a certain view by indicating its name. The most natural way of tracking views is by using the [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | ViewName:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [TrackEvent method](#TrackEvent+method)

It allows tracking events through their features in order to obtain relevant data of consumers.  
These features and their meanings are described below.

* *Category* - Name of the category that the event belongs to. Its aim is just to group these events by category for reporting.
* *Action* - Name of the action that identifies the event.
* *Label* - A label associated with the event.
* *Value* - A numerical weighted value for the event. Its objective is to allow managing reports (such as total, averages, etc.).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Category:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777), Action:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777), Label:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777), Value:[Numeric(18.2-)](https://wiki.genexus.com/commwiki/wiki?6793) |

### [TrackPurchase method](#TrackPurchase+method)

For e-commerce porpuses. It allows sending *in-app purchase* data to be statistically processed. This information is loaded through the *AnalyticsPurchase* SDT.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | PurchaseInfo:AnalyticsPurchase |

### [SetUserId method](#SetUserId+method)

It allows univocally identifying end users when they access the main platform through more than one smart device, or at least one smart device and the web page.  
This identifier must be provided by the developer (e.g. an authentication token, a username or an e-mail, but not the device ID).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | UserId:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777) |

## [Events](#Events)

It does not have any.

## [Structured Data Types](#Structured+Data+Types)

### [AnalyticsPurchase](#AnalyticsPurchase)

Stores temporary information about an *in-app purchase* made by the end user to be analytically processed.

* TransactionId:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Unique identifier for that sale.
* Affiliation:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Unique affiliation identifier that the sale must be associated with.
* Revenue:[Numeric(18.2-)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Deposit amount.
* Tax:[Numeric(18.2-)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Tax amount.
* Shipping:[Numeric(18.2-)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Shipping cost amount.
* CurrencyCode:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Currency code for the transaction (e.g. 'USD' for American Dolars).
* Items:Collection  
  A collection of purchased items with their associated data.
* Id:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)    
  Product Identifier.
* Name:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Product name.
* Category:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Category name that the product belongs to.
* Price:[Numeric(18.2-)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Product unit price.
* Quantity:[Numeric(18.2-)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Product quantity bought.
* CurrencyCode:[Character(100)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Currency code for the price stipulated.

## [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

## [See also](#See+also)

[Google Analytics in Native Mobile and Angular front end Applications](https://wiki.genexus.com/commwiki/wiki?21716)  
[Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847)
