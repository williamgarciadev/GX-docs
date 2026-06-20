---
title: "Retrieve a Stripe Object"
source_id: 37959
source_url: https://wiki.genexus.com/commwiki/wiki?37959
genexus_version: "18"
---

# Retrieve a Stripe Object

To retreive a Stripe object, you need its Id:

* Retreive the object using StripeSDKMain External Object
* Load Response or Handle Errors

```
    //Make the API call
    &StripeSDKMain.RetreiveSubscription(&Api_Key,&SubscriptionId,&Response,&Errors,&ErrorCode)
    
    //Handle Errors
    if &ErrorCode = 0
        &StripeSubscriptionRetreiveResponse.FromJson(&Response)
        Msg(&StripeSubscriptionRetreiveResponse.ToJson())
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
