---
title: "How to start using GeneXus SDK for Paypal?"
source_id: 39116
source_url: https://wiki.genexus.com/commwiki/wiki?39116
genexus_version: "18"
---

# How to start using GeneXus SDK for Paypal?

To get started:

* Create a new KB using GeneXus 15.
* Then go to the menu option 'Create KB From Server' and select this KB  [PayPalSDK](https://wiki.genexus.com/commwiki/wiki?39143)
* Build All to start familiarizing with the SDK.
* Under the 'Example' module you will find some objects that allow you to test all the main functionalities described in this documentation: one-time payments, plans, and agreements.
* Add your credentials to GetAccountCredentials procedure under PayPal->Requests. See [Get Paypal crendentials](https://wiki.genexus.com/commwiki/wiki?39121) for more information.
* To be able to receive tokens and execute payments/agreements, your application needs to be on a public URL (not localhost) so it's reachable by PayPal. You can easily achieve this by enabling "Deploy to Cloud" property in your generator properties.
* Once you have decided to integrate this SDK into your system, export the PayPal module and import it into your KB.
* When you are ready to start your production environment, change the host from sandbox to production in GetHost procedure (both URLs are there).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for PayPal](https://wiki.genexus.com/commwiki/wiki?39115) |

---
