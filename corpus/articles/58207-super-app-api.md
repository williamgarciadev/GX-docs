---
title: "Super App API"
source_id: 58207
source_url: https://wiki.genexus.com/commwiki/wiki?58207
genexus_version: "18"
---

# Super App API

The Super App API creates a communication interface in the Super App to allow Mini Apps hosted by it to interact. This is done without the need to implement the functionalities provided in the API separately for each Mini App, thus enhancing security.

### [Description](#Description)

GeneXus' Super App API offers an efficient way to achieve integration between the [Super Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) and [Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,). This interface acts as a bridge for Mini Apps to communicate with, and send data to, the Super App. You will also define methods, parameters, and data structures within the Super App, in addition to using the [Super App Source](https://wiki.genexus.com/commwiki/wiki?53457) section to expose services that Mini Apps can access.

With the setup of this interface, Mini Apps can efficiently communicate with the host Super App, enabling integration and data exchange. Mini Apps can access specific functionality and data provided by the Super App through the exposed API, ensuring a cohesive user experience.

### [HowTo: Create a GeneXus Super App API](#HowTo%3A+Create+a+GeneXus+Super+App+API)

The following refers to the sample started in [HowTo: Create a Super App](https://wiki.genexus.com/commwiki/wiki?50906), which considers the [Verdant Bank Super App Sample](https://wiki.genexus.com/commwiki/wiki?56766) that emulates a wallet.

Mini Apps are activated from this Super App to facilitate the purchase of various products or services. During the payment process, each Mini App invokes the Super App through the defined API to complete the payment in the Super App, where the user has already registered various payment methods.

`[imagen omitida: wiki id 55926]`

In the Super App [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), there is a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) named PaymentPanel that presents the user's different payment methods. Once a payment method is selected, the corresponding payment is processed.

To expose this Panel via API for invocation from Mini Apps, add the following code to the Super App Source section:

```
Payment {
     NewPayment(in:&ExternalReference, in:&Amount, out:&Success, out:&PaymentId)
               => PaymentPanel(&ExternalReference, &Amount, &Success, &PaymentId);
}
```

For more details, see [Super App Source](https://wiki.genexus.com/commwiki/wiki?53457) and its [considerations](https://wiki.genexus.com/commwiki/wiki?53457).

### [Package and distribute to Mini App Developers](#Package+and+distribute+to+Mini+App+Developers)

To ensure that Mini Apps can access this interface developed in different Knowledge Bases, export them as a package module.

1) Right-click on SampleVerdantBankApi module.  
2) Select [Package Module](https://wiki.genexus.com/commwiki/wiki?46751)…  
3) The following window will appear to configure:

`[imagen omitida: wiki id 58213]`

Complete all the necessary fields and click on the Package & Publish button.

**Note**: In this section, you must select an environment that has the [Generate Android property](https://wiki.genexus.com/commwiki/wiki?18654) and [Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656) predefined in the Front End node of the Preferences window in GeneXus.

### [HowTo: Create a non-GeneXus Super App API](#HowTo%3A+Create+a+non-GeneXus+Super+App+API)

If you have an application (that is not developed with GeneXus) converted into a Super App using GeneXus technology, follow the examples of the following non-GeneXus Super Apps to create a Super App API:

* [Android Super App Example](https://github.com/genexus-books/gx-super-app/blob/main/Android/MiniAppCaller/README.md)
* [iOS Super App Example](https://github.com/genexus-books/gx-super-app/blob/main/iOS/SampleExternalObject/README.md)

### [How to communicate with Super App API from Mini Apps](#How+to+communicate+with+Super+App+API+from+Mini+Apps)

Follow these samples according to the type of Mini App:

* [Native Mini App](https://wiki.genexus.com/commwiki/wiki?58185)
* [Web Mini App](https://wiki.genexus.com/commwiki/wiki?57430)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [GeneXus Super App Render](https://wiki.genexus.com/commwiki/wiki?58435) | [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |
| [HowTo: Call a Super App API from a Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58185) | [HowTo: Call a Super App API from a Web Mini App](https://wiki.genexus.com/commwiki/wiki?57430) | [HowTo: Create a Super App](https://wiki.genexus.com/commwiki/wiki?50906) | [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172) |
| [Super App API External Object property](https://wiki.genexus.com/commwiki/wiki?57944) | [Super App API Mock property](https://wiki.genexus.com/commwiki/wiki?57943) | [Super App API Mocking](https://wiki.genexus.com/commwiki/wiki?58219) | [Category:Super App object](https://wiki.genexus.com/commwiki/wiki?53457) |

---
