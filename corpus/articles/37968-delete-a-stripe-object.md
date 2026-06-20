---
title: "Delete a Stripe Object"
source_id: 37968
source_url: https://wiki.genexus.com/commwiki/wiki?37968
genexus_version: "18"
---

# Delete a Stripe Object

You will need the object’s Id:

1. Call the API using StripeSDKMain External Object
2. Load Response or Handle Errors

```
    //Make the API call
    &StripeSDKMain.DeletePlan(&Api_Key,&PlanId,&Response,&Errors,&ErrorCode)
    
    //Handle Errors
    if &ErrorCode = 0
        &StripePlanDeleteResponse.FromJson(&Response)
        Msg(&StripePlanDeleteResponse.ToJson())
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
