---
title: "Update a Stripe Object"
source_id: 37958
source_url: https://wiki.genexus.com/commwiki/wiki?37958
genexus_version: "18"
---

# Update a Stripe Object

Updating an object is similar to creating one. The same 3 steps should be followed:

* Setting up update options
* Updating the object using the StripeSDKMain External Object
* Loading the response or handling errors

Additionally, you need the object Id, which is sent as a parameter on the API call.

```
    //Set up Update Options 
    &StripeSubscriptionUpdateOptions.Customer = &CustomerId
    &StripeSubscriptionUpdateOptions.Quantity = &SubscriptionQuantity
    
    //Make the API call
    &JSON = &StripeSubscriptionUpdateOptions.ToJson()
    
    &StripeSDKMain.UpdateSubscription(&Api_Key,&SubscriptionId,&JSON,&Response,&Errors,&ErrorCode)
    
    //Handle Errors
    if &ErrorCode = 0
        &StripeSubscriptionUpdateResponse.FromJson(&Response)
        Msg(&StripeSubscriptionUpdateResponse.ToJson())
        &SubscriptionId = &StripeSubscriptionUpdateResponse.id
    else
        &StripeError.FromJson(&Errors)
        Msg(&StripeError.ToJson())
    EndIf
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for Stripe](https://wiki.genexus.com/commwiki/wiki?37967) |

---
