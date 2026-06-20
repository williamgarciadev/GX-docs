---
title: "In-App Purchase Sample - Classified Ads"
source_id: 20010
source_url: https://wiki.genexus.com/commwiki/wiki?20010
genexus_version: "18"
---

# In-App Purchase Sample - Classified Ads

This document describes a ["One-time-purchase"](https://wiki.genexus.com/commwiki/wiki?20003,,) example in a GeneXus-generated [smart devices](https://wiki.genexus.com/commwiki/wiki?20427,,) application using the [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320).

### [Sample application description](#Sample+application+description)

The application is about Classified Ads of multiple types. Users may publish their own ads to sell their cars, trucks or motorcycles, and have to pay $ 0.99 for each published ad. The execution of this functionality is as follows:

**1.** The application shows a list of Ads and a 'Publish Ad' action which allows us to publish our own Ad (by paying $0.99).  
`[imagen omitida: wiki id 33915]`

**2.** The "Publish Ad" button triggers the purchase transaction. The end user must buy a "new advertising" to insert a new ad in the system.  
`[imagen omitida: wiki id 33916]`

**3.** If the purchase is successfully completed, the Insert panel of the WWSD object is displayed and the user can fill the form to insert a new ad.  
After the task is completed the new Ad is displayed in the list.  
`[imagen omitida: wiki id 33917]`  
`[imagen omitida: wiki id 33918]`

### [How do we implement this functionality?](#How+do+we+implement+this+functionality%3F)

* Before you start developing in GeneXus, **configure the application** In-App Purchase on the platform store.
  + [How to configure In-App Purchases in an iOS application](https://wiki.genexus.com/commwiki/wiki?20043).
  + [How to configure In-App Billing in an Android application](https://wiki.genexus.com/commwiki/wiki?21330).
* Define the **Ads transaction**.  
  `[imagen omitida: wiki id 33907]`
* Apply the **WorkWithDevices pattern** to the Ads transactions. Then, in the List node, **add an action** **called "Publish Ad"** (it will replace the default action "Insert" - the developer must delete this action to continue).
* Write the following **code** in the "Publish Ad" event section. Basically, it will purchase a product item (that we've called '*publish\_my\_ad\_id*' and was previously registered at [Google developer console](http://console.developers.google.com) or [Apple iTunes connect](https://itunesconnect.apple.com)). With the information retrieved from the platform store, If the purchase is successfully completed, we call the WWDS associated with the Ads transaction object for Insert.

```
Event 'Publish Ad'
     Composite
           &ProductId = 'publish_my_ad_id'
           &PurchaseResult = StoreManager.PurchaseProduct(&ProductId)
           if &PurchaseResult.Success
                  WorkWithDevicesAds.Ads.Detail.Insert()
           else
                  msg('There was an error making product purchase.')
           endif
    EndComposite
Endevent
```

* **And that's all !!**

All the user interaction with the store and payment procedures are managed by the platform store; you do not need to worry about it. In addition, in this particular case, since it is a one-time-purchase product, storing purchase information in our application becomes optional because if the same user wants to obtain the functionality (product) again, he has to make a purchase all over again.

[Download this sample](https://wiki.genexus.com/commwiki/wiki?33914,,)

### [See Also](#See+Also)

[In-App Purchase Sample - My Kitchen](https://wiki.genexus.com/commwiki/wiki?20021)


|  |
| --- |
| **Backlinks** |
| [In-App Purchase Sample - My Kitchen](https://wiki.genexus.com/commwiki/wiki?20021) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320) |

---
