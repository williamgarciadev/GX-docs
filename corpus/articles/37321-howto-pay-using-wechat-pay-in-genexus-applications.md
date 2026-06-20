---
title: "HowTo: Pay using WeChat Pay in GeneXus applications"
source_id: 37321
source_url: https://wiki.genexus.com/commwiki/wiki?37321
genexus_version: "18"
---

# HowTo: Pay using WeChat Pay in GeneXus applications

## [What is WeChat Pay?](#What+is+WeChat+Pay%3F)

[WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay) is a mobile payment platform included with the Chinese social media application [WeChat](https://www.wechat.com/en/). It was developed by Tencent and currently has more than 900 million users in China and other countries. It has a significant share of the mobile payment market in China and, as a result, integration with WeChat Pay is a standard requirement for mobile applications. For that purpose, [WeChat Open Platform](https://open.weixin.qq.com/) must be used.

## [Integration with GeneXus](#Integration+with+GeneXus)

From Upgrade 8 of GeneXus 15, payment functions with WeChat Pay can be integrated into the generated Android and iOS applications using an [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545) included in the GeneXus installation and importing the [Payment API](https://wiki.genexus.com/commwiki/wiki?37322).

## [Step-by-step instructions](#Step-by-step+instructions)

### [1 - Register the application on the WeChat Open Platform site](#1+-+Register+the+application+on+the+WeChat+Open+Platform+site)

Developers need to be registered in the WeChat Open Platform site and need to register all the applications that will integrate the payment functions. In this process, developers get the application credentials required to integrate with WeChat Pay. Check [this document](https://wiki.genexus.com/commwiki/wiki?37323,,) for detailed information about the registration process.

### [2 - Set configuration information](#2+-+Set+configuration+information)

The first "programming" step is to set the configuration information. By default, the WeChat Pay API loads the configuration information from an XML file called WeChatPay\_Config, using the procedure LoadConfig. Modifying this file is enough to set all the configurations needed to integrate the application with WeChat Pay. Following is a description of the WeChatPay\_Config.xml file structure.

```
<Configuration>     
   <AppId />     
   <Environment />     
   <CallbackURL />     
   <Timeout />     
   <MerchantId />     
   <MerchantKey />     
   <AdditionalConfig /> 
</Configuration>
```

* **AppId:** Identifier obtained when the application was registered in WeChat Pay.
* **Environment:** Possible values are *Production / Sandbox*. Execution environment that will be used to execute the payment transactions.
* **CallbackURL:** URL of the payment notification service that WeChat Pay will call to complete the payment transaction. By default, the URL of the procedure CallbackService included in the [WeChat Pay API](https://wiki.genexus.com/commwiki/wiki?37322) is used.
* **Timeout:** Timeout in minutes for the payment transactions.
* **MerchantId**: Identifier of the user registered in WeChat Open Platform.
* **MerchantKey**: Key assigned to the application in the WeChat Open Platform.
* **AdditionalConfig :** List of additional information.

When the application where we are integrating WeChat Pay is going to be generated for iOS, we need to make an additional configuration step. The Smart Device main object property, [WeChat Pay Application Id](https://wiki.genexus.com/commwiki/wiki?37001) has to be set with the same value we set in AppId tag in the configuration file.

### [3 - Prepare payment data](#3+-+Prepare+payment+data)

The next step is to prepare the payment data to send it to WeChat  Pay. First, the user needs to set some values in a variable based on *PaymentApplicationData* SDT from the [WeChat Pay API](https://wiki.genexus.com/commwiki/wiki?37322) (product code, product description, currency and amount). This variable will be the input of the procedure *GetPaymentInformation* which returns the processed information ready to be sent to WeChat Pay.

There is an intermediate step performed by the *GetPaymentInformation* procedure; it allows processing the ready-to-send payment information (which includes the generated order number) by the user, for example, to store it in the application database tables. These actions can be edited in the procedure *OnAboutToPay* from the [WeChat Pay API](https://wiki.genexus.com/commwiki/wiki?37322).

### [4 - Send payment information to WeChat Pay](#4+-+Send+payment+information+to+WeChat+Pay)

Now the user is ready to send the payment information to WeChat Pay, using the Pay method from the External Object *WeChatPayProvider* included in the [WeChat Pay API](https://wiki.genexus.com/commwiki/wiki?37322). This method receives the processed payment information returned by the procedure *GetPaymentInformation* in the previous step in a variable based on the *PaymentInformation* SDT.

The following is an example code in a GeneXus Smart Device object event with the actions from steps 4 and 5:

```
Event 'Pay with WeChat Pay'
   Composite
      &PaymentApplicationData.ProductCode = 'Product name'
      &PaymentApplicationData.ProductDescription = 'Product description'
      &PaymentApplicationData.Currency = 'CNY'
      &PaymentApplicationData.Amount = 1000
      GeneXus.Common.UI.Progress.ShowWithTitleAndDescription("Please Wait...","Preparing payment information...")
      WeChatPay.GetPaymentInformation(&PaymentApplicationData, &PaymentInformation)
      GeneXus.Common.UI.Progress.Hide()
      if &PaymentInformation.ErrorCode > 0
          Msg("Error: " + &PaymentInformation.ErrorDescription)
      else
          WeChatPayProvider.Pay(&PaymentInformation)
      endif
   EndComposite
Endevent
```

### [5 - Process payment result](#5+-+Process+payment+result)

The user needs to code two actions to process a WeChat Pay payment result. The first one is the *WeChatPayProvider* External Object event called *OnPaymentFinished*. This event receives a variable based on the *PaymentResult* SDT which contains an ErrorCode, ErrorDescription, and OrderNumber of the completed payment. Check detailed information about the [WeChat Pay API here](https://wiki.genexus.com/commwiki/wiki?37322).

The following is an example code of this event:

```
Event WeChatPayProvider.OnPaymentFinished(&PaymentResult)
   Composite
      if &PaymentResult.ErrorCode = 0
         GeneXus.Common.UI.Progress.ShowWithTitleAndDescription("Please Wait...","Finishing transaction...")
         SetSaleStatus(&PaymentResult.OrderNumber, PaymentStatus.Paid)
         ClearCart()
         GeneXus.Common.UI.Progress.Hide()
         ConfirmationPanel()
      else
         SetSaleStatus.Call(&PaymentResult.OrderNumber, PaymentStatus.Error)
         Msg(&PaymentResult.ErrorDescription)
      endif
   EndComposite
EndEvent
```

### [6 - Asynchronous payment notification service](#6+-+Asynchronous+payment+notification+service)

The last step is executed by WeChat Pay servers, which call a payment notification service provided by the application developer. This service URL is what we indicate in the configuration using the CallbackURL parameter. By default, this URL refers to a procedure called *CallbackService* that is included in the [WeChat Pay API](https://wiki.genexus.com/commwiki/wiki?37322). This procedure receives the HTTP data and converts it to an SDT structure (*PaymentNotificationInfo*); next, it calls another procedure called *CallbackHandler* to process that SDT with the notification information.

### [In sum](#In+sum)

Having registered the application, the GeneXus developer only needs to modify the following objects to integrate WeChat Pay into the application:

* Set configurations in *WeChatPay\_Config.xml* file.
* Code the process of the payment data just before sending it to WeChat Pay in the *OnAboutToPay* procedure.
* Set payment data, call *GetPaymentInformation* procedure and call Pay method of the *WeChatPayProvider* EO in the Smart Device object.
* Code the WeChatPayProvider EO *OnPaymentFinished* event in the Smart Device object.
* Code the notification service processing in the *CallbackHandler* procedure.

## [Sample](#Sample)

A complete sample can be downloaded from [here](https://wiki.genexus.com/commwiki/wiki?37202,,).


|  |
| --- |
| **Backlinks** |
| [Application Id property (WeChat Pay)](https://wiki.genexus.com/commwiki/wiki?37001) |

---
