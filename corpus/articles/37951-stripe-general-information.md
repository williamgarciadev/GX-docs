---
title: "Stripe General Information"
source_id: 37951
source_url: https://wiki.genexus.com/commwiki/wiki?37951
genexus_version: "18"
---

# Stripe General Information

For each functionality, there are SDTs with options to configure (some mandatory, some optional) (eg StripeChargeCreateOptions), which define how the action is going to be performed.

Most API calls need these parameters:

* API Key: your secret key (GetSecretKey()) (in)
* JSON: Json of the Options SDT (in)
* Response: Json of the Response to the call. There are SDTs for each response, to be able to load and handle all data (out)
* Errors: JSON of the StripeError  SDT, returned by Stripe’s server (out)
* ErrorCode: 0 is OK, response was loaded. 1 is Error, Errors where loaded (no response in this case) (out)

There are domains for each of the mentioned parameters:

* Api\_Key
* JSON
* Response
* Errors
* ErrorCode

StripeSDKMain is the ExternalObject which communicates with Stripe’s API. You will need to create a variable of this type, to interact with Stripe’s API.

You can download the Source Code to add extra functionality to the external object from <https://github.com/genexuslabs/genexus-sdk-for-stripe>

## [Considerations](#Considerations)

Stripe has a test and live mode. When going to live mode make sure to use the HTTPS protocol, more information [here](https://stripe.com/docs/keys#test-live-modes).

```
You may test your integration over HTTP. However, live integrations must use HTTPS.
```

For troubleshooting always check the browser javascript console.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for Stripe](https://wiki.genexus.com/commwiki/wiki?37967) |

---
