---
title: "Super App API Mocking"
source_id: 58219
source_url: https://wiki.genexus.com/commwiki/wiki?58219
genexus_version: "18"
---

# Super App API Mocking

[Super App API](https://wiki.genexus.com/commwiki/wiki?58207) mocking is a technique used to simulate the structure and behavior of the real Super App API during the development process of a Mini App.

This technique, which uses the [GeneXus Project Navigator (GPN)](https://wiki.genexus.com/commwiki/wiki?14974), allows you to work independently on the Mini App without relying on the actual implementation of the Super App API.

## [Description](#Description)

The key feature of a Super App is its ability to load and execute Mini Apps (smaller, independent applications) within a unified user experience. To achieve this, Super Apps expose an API that allows Mini Apps to interact with their services and screens.

Mocking a Super App API involves creating a simulated version of the API that replicates its structure, behavior, and responses.

This provides a simulated environment where you can work on your Mini Apps efficiently, reduce costs, and ensure thorough testing during the development stage. However, it is crucial to conduct final tests against the real Super App API before deployment to production, as mocks are not a substitute for validating the actual integration.
`[imagen omitida: wiki id 58249]`

## [Benefits of Mocking the Super App API](#Benefits+of+Mocking+the+Super+App+API)

* **Independent development:** Work independently of the Super App, reducing dependencies and saving time.
* **Avoid altering Mini App code:** This solution requires creating additional objects, as you will see in the sample below. However, the goal is to avoid altering Mini App code to work against the Mock or the real Super App API.
* **Controlled testing environment:** Mocking provides a consistent and controlled environment for testing, ensuring that tests are reliable and repeatable. Relying on a live API can lead to inconsistencies due to changes or data variations in the API. Mocking ensures a stable environment, facilitating more reliable and consistent testing.
* **Early testing:** Allows for early testing of Mini Apps, even if the Super App API is still under development.

## [Usage Sample](#Usage+Sample)

Below is described how to implement a Mock of the Super App API in a [Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58298).
For [Web Mini Apps](https://wiki.genexus.com/commwiki/wiki?57422), mocking the calls using JavaScript is enough.

### [Case 1: Mock Super App API in GeneXus](#Case+1%3A+Mock+Super+App+API+in+GeneXus)

Consider the [Verdant Bank Super App Sample](https://wiki.genexus.com/commwiki/wiki?56766) that emulates a wallet.

This Super App exposes in its API the following method:

```
Payment {
     NewPayment(in:&ExternalReference, in:&Amount, out:&Success, out:&PaymentId)
               => PaymentPanel(&ExternalReference, &Amount, &Success, &PaymentId);
}
```

SampleVerdantBankAPI module will be used in Native Mobile Mini App to interact with the Super App API as follows:

```
SampleVerdantBankAPI.SuperAppVerdantBank.NewPayment(&Reference,&Amount,&Success,&PaymentId)
```

You can check all these Mini Apps KBs available for download with Mock Super App API samples:

* [The Movies:](https://wiki.genexus.com/commwiki/wiki?56785) This Mini App facilitates the purchase of movie tickets.
* [Frosty Delights:](https://wiki.genexus.com/commwiki/wiki?56786) Users can order a variety of ice cream flavors through this Mini App.
* [Coffee & Muffins:](https://wiki.genexus.com/commwiki/wiki?56784) This Mini App allows users to order coffee and sandwiches from a coffee store.

Read more at: [HowTo: Call a Super App API from a Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58185).

#### [Steps to Mock Super App API in Native Mobile Mini App KB](#Steps+to+Mock+Super+App+API+in+Native+Mobile+Mini+App+KB)

1) Create objects that serve as Mocks for the methods exposed in the Super App API. They must respect the same parameters as the object they are mocking. Since they are mocks, the implementation can be simple.

1.1) To emulate the call of an object with an interface, create a Panel called **MockNewPayment**, for example, that simply adds 2 buttons to its layout with the following events:

```
parm(in:&ExternalReference,in:&Amount,out:&Success,out:&PaymentId);
```

`[imagen omitida: wiki id 58229]`

```
Event 'Pay'
      Composite
           &Success = true
           &PaymentId = Random()
           return
       EndComposite
Endevent

Event 'Reject'
         Composite
             &Success = false
             &PaymentId.SetEmpty()
             return
          EndComposite
Endevent
```

2) Create a Main Object called **SuperAppDummy**. There is no need to configure any other properties or add code. The generator will use it for its correct operation and metadata generation.

`[imagen omitida: wiki id 58230]`

3) Create a Super App object named **SuperAppVerdantBankMock**, which will serve as a mock of the Super App API.

3.1) In the Source section, define the API while respecting the structure, but calling the mock objects created in step 1.

```
Payment {
NewPayment(in:&ExternalReference,in:&Amount,out:&Success,out:&PaymentId)
    => MockNewPayment(&ExternalReference,&Amount,&Success,&PaymentId);
}
```

3.2) In the [Main Object property](https://wiki.genexus.com/commwiki/wiki?50342), set the **SuperAppDummy** object created in step 2.

`[imagen omitida: wiki id 58231]`

4) Create a Mini App object named **MiniAppCoffeeMuffins**.

4.1) Set the [Main Object property](https://wiki.genexus.com/commwiki/wiki?53629) to **CoffeeHome**: this should be the Main Object of the Mini App.

4.2) Configure the [Super App API Mock property](https://wiki.genexus.com/commwiki/wiki?57943) to **SuperAppVerdantBankMock**: this should be the Super App object created in step 3.

`[imagen omitida: wiki id 58232]`

### [Case 2: Mock of non-GeneXus Super App API](#Case+2%3A+Mock+of+non-GeneXus+Super+App+API)

Consider the following non-GeneXus Super App examples: [Android Super App Example](https://github.com/genexus-books/gx-super-app/blob/main/Android/MiniAppCaller/README.md) and [iOS Super App Example](https://github.com/genexus-books/gx-super-app/blob/main/iOS/SampleExternalObject/README.md).

Both Super Apps expose in their APIs the following methods:

```
PayWithUI(int amount, string reference)

PayWithoutUI(int amount, string reference)
```

Payments External Object will be used in Mini App to interact with the Super App API as follows:

```
&Reference = Payments.PayWithUI(&Amount)

&Reference = Payments.PayWithoutUI(&Amount)
```

You can check this Mini App KB available for download with Mock Super App API examples: [Mini App Payments - This Mini App implements a Super App API call.](https://wiki.genexus.com/commwiki/wiki?58157)

For more information, read: [HowTo: Call a Super App API from a Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58185).

#### [Steps to Mock Super App API in a Mini App KB](#Steps+to+Mock+Super+App+API+in+a+Mini+App+KB)

1) Create objects that serve as Mocks for the methods exposed in the Super App API. They must respect the same parameters as the object they are mocking. Since they are mocks, the implementation can be simple.

1.1) Create a Panel called **MockNewPayment** that simply adds 2 buttons to its Layout with the following events:

```
parm(in:&Amount,out:&Reference);
```

`[imagen omitida: wiki id 58238]`

```
Event 'Pay'
        &Reference = !'Mock: '+GUID.NewGuid().ToString()
        Return
Endevent

Event 'Reject'
       &Reference = !'Mock: Rejected error #0001'
        Return
Endevent
```

1.2) Define a Procedure called **MockPayProc** as follows:

```
parm(in:&Amount,out:&Reference);
If &Amount = 0
    &Reference = !'Mock: Invalid amount'
Else
    &Reference = !'Mock: '+Guid.NewGuid().ToString().Trim()
Endif
```

2) Create a Main Object called **SuperAppDummy**. There is no need to configure any other properties or add code. It will be used by the generator for its correct operation and metadata generation.

`[imagen omitida: wiki id 58230]`

3) Create a Super App object named **SuperAppApiMock**, which will serve as a mock of the Super App API.

3.1) In Source section, define the API while respecting the structure, but calling the mock objects created in step 1.

```
Payment {
    PayWithUI(in:&Amount,out:&Reference)
        => MockPayPanel(&Amount,&Reference);
    PayWithoutUI(in:&Amount,out:&Reference)
        => MockPayProc(&Amount,&Reference);
}
```

3.2) In [Main Object property](https://wiki.genexus.com/commwiki/wiki?50342), set the **SuperAppDummy** object created in step 2.

`[imagen omitida: wiki id 58240]`

4) Create a Mini App object named **MiniAppTestMock**.

4.1) Set the [Main Object property](https://wiki.genexus.com/commwiki/wiki?53629) to **Payments**: this should be the Main Object of the Mini App.

4.2) Configure the Super App API Mock property to **SuperAppApiMock**: this should be the Super App object created in step 3.

4.3) Set the Super App API External Object property to **Payments**: this should be the External Object created to call the Super App API.

`[imagen omitida: wiki id 58241]`

## [HowTo: Run the Super App API Mock from a Native Mini App](#HowTo%3A+Run+the+Super+App+API+Mock+from+a+Native+Mini+App)

After performing the above configurations, your Native Mini App is ready to run the Mocks when running in GeneXus Project Navigator.

To use the Mocks, the following is required:

* Apple: GeneXus Project Navigator version 18.10 or higher (Upgrade 10).
* Android: GeneXus Project Navigator version 2.2.0 or higher (Upgrade 9).

When executing code at the event level that calls the Super App API, calling GeneXus Super App through the module:

```
SampleVerdantBankAPI.SuperAppVerdantBank.NewPayment(&Reference,&Amount,&Success,&PaymentId)
```

...or by calling the non-GeneXus Super App through the External Object:

```
&PaymentId = Payments.PayWithUI(&Amount)
&PaymentId = Payments.PayWithoutUI(&Amount)
```

Since it is running on GeneXus Project Navigator, the configured mocks will be executed, allowing the entire Mini App to be tested.

## [Availability](#Availability)

This feature is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

## [See Also](#See+Also)

* [Super App API External Object property](https://wiki.genexus.com/commwiki/wiki?57944)
* [Main Object property (for Super Apps)](https://wiki.genexus.com/commwiki/wiki?50342)
* [Super App object](https://wiki.genexus.com/commwiki/wiki?53457)


|  |
| --- |
| **Backlinks** |
| [KB:Coffee and Muffins - Mini App Sample for Verdant Bank](https://wiki.genexus.com/commwiki/wiki?56784) | [KB:Frosty Delights - Mini App Sample for Verdant Bank](https://wiki.genexus.com/commwiki/wiki?56786) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |
| [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172) | [KB:Mini App Payments - Mini App Sample for non-GeneXus Super App API integration](https://wiki.genexus.com/commwiki/wiki?58157) |
| [KB:The Movies - Mini App Sample for Verdant Bank](https://wiki.genexus.com/commwiki/wiki?56785) |

---
