---
title: "Create a Stripe Object"
source_id: 37957
source_url: https://wiki.genexus.com/commwiki/wiki?37957
genexus_version: "18"
---

# Create a Stripe Object

There are three basic steps:

1. Setting up create options
2. Creating the object using the StripeSDKMain External Object
3. Loading the response or handling errors

## [Setting up Create Options](#Setting+up+Create+Options)

Each object has (its own) Create Options, an SDT where different properties are set and sent to Stripe to determine how the object will be created. (E.g, in a charge, you determine the customer, currency, amount, etc).

## [Creating the object using the StripeSDKMain External Object](#Creating+the+object+using+the+StripeSDKMain+External+Object)

To make the API call using StripeSDKMain External Object, you just need to create a   
StripeSDKMain variable and call one of its methods, which usually receive 5 parameters:

* ApiKey (your secret key) <in>
* JSON (charge create options) <in>
* Response (Json of the response from stripe servers) <out>
* Errors (Json of StripeError SDT if errors exist) <out>
* ErrorCode (numeric, 0 is ok, 1 means there was an error on Stripe servers) <out>

## [Load Response or Handle Errors](#Load+Response+or+Handle+Errors)

If the call was successful, ErrorCode will return 0. The response will be loaded with a stripeCreateXxxxxxResponse JSON, which can be loaded to its corresponding SDT to handle information.

If there was an error on Stripe's end, ErrorCode will return 1 and no response will be loaded, instead, Errors will be loaded, describing what went wrong. This JSON can be loaded to StripeError SDT to display and handle error information.

```
    //Set up create options
    &stripeChargeCreateOptions.Amount = 4500
    &stripeChargeCreateOptions.Currency = "usd"
    &stripeChargeCreateOptions.SourceTokenOrExistingSourceId = StripeCardControl.StripeCardToken

    //Make the API call
    &JSON = &stripeChargeCreateOptions.ToJson()
    &StripeSDKMain.CreateCharge(&Api_Key,&JSON,&Response,&Errors,&ErrorCode)
    
    //Handle Errors
    if(&ErrorCode = 0)
        &StripeChargeCreateResponse.FromJson(&Response)
        Msg(&StripeChargeCreateResponse.ToJson())
    else
        &StripeError.FromJson(&Errors)
        Msg(&StripeError.ToJson())
    endif
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for Stripe](https://wiki.genexus.com/commwiki/wiki?37967) |

---
