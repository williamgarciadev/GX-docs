---
title: "HowTo: Call a Super App API from a Native Mobile Mini App"
source_id: 58185
source_url: https://wiki.genexus.com/commwiki/wiki?58185
genexus_version: "18"
---

# HowTo: Call a Super App API from a Native Mobile Mini App

GeneXus' Super App API offers an efficient way to achieve integration between [Super Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) and [Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) without the need to implement the API's functionalities separately for each Mini App, thus enhancing security.

In this article, you will find full samples of how a [Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58298) can call a [Super App API](https://wiki.genexus.com/commwiki/wiki?58207).

### [HowTo: Call a GeneXus Super App API](#HowTo%3A+Call+a+GeneXus+Super+App+API)

In these samples, it is assumed that:

1) You have a GeneXus Super App exposing the following method in its API for handling payments:

```
Payment {
     NewPayment(in:&ExternalReference, in:&Amount, out:&Success, out:&PaymentId)
               => PaymentPanel(&ExternalReference, &Amount, &Success, &PaymentId);
}
```

2) The [Super App object](https://wiki.genexus.com/commwiki/wiki?53457) is placed within a module under the Root module, which is packaged and distributed.

You can check the [Verdant Bank - GeneXus Super App Sample](https://wiki.genexus.com/commwiki/wiki?56766) KB available for download.

To interact with this Super App API, make the following changes in your Native Mobile Mini App KB:

* Go to [Knowledge Manager](https://wiki.genexus.com/commwiki/wiki?5679) > [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172).
* Install your Super App API Module (in this case: SampleVerdantBankAPI).

`[imagen omitida: wiki id 58193]`

Once the module is installed:

3) Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with a Button to interact with the Super App, as shown below:

`[imagen omitida: wiki id 58195]`

4) In the Events section of the Panel object, write the following:

```
Event 'Pay'
    Composite
SampleVerdantBankAPI.SuperAppVerdantBank.NewPayment(&Reference,&Amount,&Success,&PaymentId)
    If &Success
        msg(format("Successful payment %1",&PaymentId))
    Else
        msg('Sorry, your order has been rejected')
    Endif
        
    EndComposite
Endevent
```

You can check all these Mini Apps KBs available for download with Super App API call examples:

* [The Movies](https://wiki.genexus.com/commwiki/wiki?56785): This Mini App facilitates the purchase of movie tickets.
* [Frosty Delights](https://wiki.genexus.com/commwiki/wiki?56786): Users can order a variety of ice cream flavors through this Mini App.
* [Coffee and Muffins](https://wiki.genexus.com/commwiki/wiki?56784): This Mini App allows users to order coffee and sandwiches from a coffee store.

By following these steps, you can integrate your Mini Apps with the GeneXus Super App.

### [HowTo: Call a non-GeneXus Super App API](#HowTo%3A+Call+a+non-GeneXus+Super+App+API)

In this case, the examples of non-GeneXus Super Apps published on GitHub will be followed: [Android](https://github.com/genexus-books/gx-super-app/blob/main/Android/MiniAppCaller/README.md) and [iOS](https://github.com/genexus-books/gx-super-app/blob/main/iOS/SampleExternalObject/README.md).

Both non-GeneXus Super Apps expose the following methods in their API:

```
PayWithUI(int amount, string reference)

PayWithoutUI(int amount, string reference)
```

To interact with this Super App API, make the following changes in your Native Mobile Mini App KB:

1) Create a new [External Object](https://wiki.genexus.com/commwiki/wiki?5669); in this case, named Payments.

2) Declare two new methods: **PayWithUI** and **PayWithoutUI** with the following configuration:

`[imagen omitida: wiki id 58196]`

**Note**: The number of parameters received by each method (one of Numeric/Integer type), the type returned (VarChar/String) and the “Is Static” property with its value set to “True”.

3) Reference the new External Object from a button event programmed in the Checkout Panel:

`[imagen omitida: wiki id 58197]`

```
Event 'PayWithoutUI'
    &Reference = Payments.PayWithoutUI(&Amount)
    msg(&Reference)
Endevent

Event 'PayWithUI'
    &Reference = Payments.PayWithUI(&amount)
    msg(&Reference)
Endevent
```

You can check this Mini App KB available for download with Super App API call examples.  
[Mini App Payments](https://wiki.genexus.com/commwiki/wiki?58157): This Mini App implements a non-GeneXus Super App API call.

### [See Also](#See+Also)

[Super App API](https://wiki.genexus.com/commwiki/wiki?58207)  
[HowTo: Call a Super App API from a Web Mini App](https://wiki.genexus.com/commwiki/wiki?57430)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172) | [Super App API](https://wiki.genexus.com/commwiki/wiki?58207) |
| [Super App API Mocking](https://wiki.genexus.com/commwiki/wiki?58219) |

---
