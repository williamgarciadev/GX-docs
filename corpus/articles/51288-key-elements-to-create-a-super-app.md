---
title: "Key elements to create a Super App"
source_id: 51288
source_url: https://wiki.genexus.com/commwiki/wiki?51288
genexus_version: "18"
---

# Key elements to create a Super App

Super Apps can be developed with GeneXus, taking full advantage of the platform's tools and benefits.

In addition, it is also possible to turn any existing application —whether native (developed in Swift for iOS, Kotlin for Android) or created with frameworks such as Flutter or React Native— into a Super App. From now on, these types of applications are referred to as non-GeneXus.

This document focuses on the scenario of creating a Super App using GeneXus. If you are interested in learning how to turn a non-GeneXus application into a Super App, read [How to transform your application into a Super App](https://github.com/genexus-books/gx-super-app/blob/main/docs/HowToTransformYourAppToASuperApp.md).

When creating a Super App with GeneXus, the process is similar to developing any Native Mobile application, but you must also consider the following:

* Provide the communication interface for the Mini Apps that integrate with your Super App
* Design the UX for the Mini Apps discovery within your Super App
* Make available a sandbox version of your Super App for testing

## [Communication interface between Mini Apps and the Super App](#Communication+interface+between+Mini+Apps+and+the+Super+App)

A Mini App may require certain actions from its Super App. To that end, these services are implemented in the Super App (with or without a UI) and then its API is exposed to the Mini Apps.

For example, suppose you have a Super App associated with a financial institution, where users register their different means of payment, among other things.

The Super App offers a variety of services to its users (shopping in stores, paying for transportation, etc.) through different Mini Apps.

When the user enters a purchase process from a Mini App, the payment will be redirected to the Super App for choosing the payment method. Once the payment is completed, the result of the operation is returned to the Mini App. This saves the user the need to enter the payment method for each service, while also ensuring that the Super App will not share that information with the Mini Apps.

## [Design the UX for discovering Mini Apps](#Design+the+UX+for+discovering+Mini+Apps)

The second aspect to consider is how the user will access the Mini Apps. To that end, you must design the UX (screens and interactions) to obtain and display the different Mini Apps.

`[imagen omitida: wiki id 51291]`

For example, you may want to get all available Mini Apps, just those fulfilling specific search criteria, or even those that are close to the user’s location.

To do this, there is a special module called [GeneXusSuperApps](https://wiki.genexus.com/commwiki/wiki?50959), which allows connection to the Mini App Center and obtains the list of Mini Apps through different services.

## [Sandbox Super App for Testing](#Sandbox+Super+App+for+Testing)

Those who develop the Mini Apps that will be integrated with your Super App will require access to the services it displays. To test these services, you’ll have to provide a sandbox version of the Super App, from which they can call the Mini App under development.

For more details, see [HowTo: Create a Super App](https://wiki.genexus.com/commwiki/wiki?50906).


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [Key elements when building a Super App ecosystem](https://wiki.genexus.com/commwiki/wiki?50902) |

---
