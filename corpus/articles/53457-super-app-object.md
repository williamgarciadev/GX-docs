---
title: "Super App object"
source_id: 53457
source_url: https://wiki.genexus.com/commwiki/wiki?53457
genexus_version: "18"
---

# Super App object

Designates the Main Object as a Super App, specifies the Mini App Center URL and its corresponding Super App version to retrieve their Mini Apps. It is also where you declare the API functionalities for interacting with its Mini Apps.

## [Description](#Description)

The Super App object has three main objectives:

1. To indicate which app ([Main Object](https://wiki.genexus.com/commwiki/wiki?5770)) is a Super App.
2. To indicate which [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) it needs to connect to, and from there, determine the corresponding Super App Version (from this information, the list of Mini Apps published for this Super App from the Mini App Center is obtained).
3. To declare the API with functionalities that the Super App will expose to interact with its Mini Apps.

Once created, you will see that it contains the following tabs:

`[imagen omitida: wiki id 57555]`

### [Super App Source](#Super+App+Source)

Here is where you define the [Super App API](https://wiki.genexus.com/commwiki/wiki?58207) (Application Programming Interface) for a set of functions that you want to make accessible to the Mini Apps. You can create a mapping for each service you want to expose, connecting its external name (used as a service) to the internal implementation within the Knowledge Base. The notation used here is similar to that of the API Object.

The internal objects that the API calls can include [Panels](https://wiki.genexus.com/commwiki/wiki?24829), [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), and [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270).

#### [**Properties**](#Properties)

By setting certain object properties you are able to:

* Identify the Super App in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290).
* Define the associated [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) ([Panel](https://wiki.genexus.com/commwiki/wiki?24829) or [Menu](https://wiki.genexus.com/commwiki/wiki?16321)) for that Super App. This ensures that appropriate information is generated during the Main object's generation process to execute the application as a Super App.
* At runtime, they provide information to retrieve the list of its Mini Apps from the Mini App Center and verify the signature when loading a Mini App.

Below are some properties that allow you to achieve the above objectives:

* [Super App Identifier](https://wiki.genexus.com/commwiki/wiki?50308)
* [Super App Version](https://wiki.genexus.com/commwiki/wiki?50312)
* [Provisioning Url](https://wiki.genexus.com/commwiki/wiki?50313)
* [Android Public Key File](https://wiki.genexus.com/commwiki/wiki?53602)
* [iOS Public Key File](https://wiki.genexus.com/commwiki/wiki?53603)
* [Main Object](https://wiki.genexus.com/commwiki/wiki?50342)
* Mini Apps Cache
  + [Maximum Mini apps count](https://wiki.genexus.com/commwiki/wiki?50310)
  + [Number of days to keep](https://wiki.genexus.com/commwiki/wiki?50311)

### [Events](#Events)

For each API function, you can define a 'Before' and 'After' user event, which will be executed before and after each function execution in the Super App.  
In addition, for each API function, you can define '<function name>.Before|After' events. Therefore, every time a function is invoked from the Mini App, the following will be executed:

* Event 'Before'
* Event '<function>.Before'
* The object corresponding to the implementation of the function, referenced in the 'Super App Source'
* Event '<function>.After'
* Event 'After'

## [Sample](#Sample)

Consider the [Verdant Bank Super App Sample](https://wiki.genexus.com/commwiki/wiki?56766) that emulates a wallet. Mini Apps are activated from within this Super App to facilitate the purchase of various products or services. During the payment process, each Mini App invokes the Super App through the defined API to complete the payment within the Super App, where the user has registered various payment methods.

In the Super App Knowledge Base, there is a Panel named PaymentPanel that presents the user's different payment options. Once a payment option is selected, the corresponding payment is executed.

To expose this Panel via API for invocation from Mini Apps, add the following code to the Super App Source:

```
Payment {
     NewPayment(in:&ExternalReference, in:&Amount, out:&Success, out:&PaymentId)
               => PaymentPanel(&ExternalReference, &Amount, &Success, &PaymentId);
}
```

Additionally, if you wish to call a Procedure (e.g., "GetUserInfoProc") that retrieves user information, you can include it in the Super App Source:

```
Payment {
     GetUserInformation(in:&UserName, out:&UserAddress, out:&UserPhone)
               => GetUserInfoProc(&UserName, &UserAddress, &UserPhone);
}
```

Alternatively, you can implement this as a Data Provider (e.g., "GetUserInfoDP") that returns an SDT with user information:

```
Payment {
     GetUserInformationDP(in:&UserName, out:&UserInfoSDT)
               => GetUserInfoDP(&UserName, &UserInfoSDT);
}
```

Also, you can use Super App Events, for instance, to obtain the Current Mini App ID before calling the SuperApp API.

```
Event GetPaymentMethods.Before
    &MiniAppId = GeneXusSuperApps.MiniApps.CurrentMiniAppId
EndEvent
```

In this case, you want to check the different payment methods available for each Mini App.

```
Payment {
     GetPaymentMethods(out:&PaymentMethodsSDT)
               => GetPaymentMethodsAvailablesForMiniApp(&MiniAppId, &PaymentMethodsSDT);
}
```

## [Considerations](#Considerations)

* The Super App object must be placed within a module under the Root module, which is packaged and then installed in the KBs where Mini Apps are developed.
* Objects invoked from the API (Super App Source) should be added to the Additional References property in the Main Object associated with the Super App object (Temporary restriction. See [SAC #53472](https://www.genexus.com/en/developers/websac?data=53472)).
* If an SDT is used as a parameter when exposing a Data Provider in the API, it must reside within the module.
* In the Mini App KB, API methods can only be invoked from user events (client-side).

## [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)
