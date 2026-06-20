---
title: "Stripe Customer Object"
source_id: 37962
source_url: https://wiki.genexus.com/commwiki/wiki?37962
genexus_version: "18"
---

# Stripe Customer Object

You can create customers on Stripe. They are useful for identifying the buyer of a product, creating subscriptions, or performing recurring charges associated with the same customer.

Considerations:

* You should have your own Customer DataBase, where you also store the customer's Stripe Id (returned in the response when creating a customer object), used to manage customers on Stripe's platform.
* Stripe does not check for repeated E-Mails, so you must do so (there can be more than one customer with the same E-Mail on Stripe's platform).

To create a customer use:

* Create Options: StripeCustomerCreateOptions
* Response: StripeCustomerCreateResponse
* Errors: StripeError

To update a customer use:

* Update Options: StripeCustomerUpdateOptions
* Response: StripeCustomerUpdateResponse
* Errors: StripeError

To retrieve a customer use:

* Response: StripeCustomerRetrieveResponse
* Errors: StripeError

To delete a customer use:

* Response: StripeCustomerDeleteResponse
* Errors: StripeError


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for Stripe](https://wiki.genexus.com/commwiki/wiki?37967) |

---
