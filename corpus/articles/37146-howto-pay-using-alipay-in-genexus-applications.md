---
title: "HowTo: Pay using Alipay in GeneXus applications"
source_id: 37146
source_url: https://wiki.genexus.com/commwiki/wiki?37146
genexus_version: "18"
---

# HowTo: Pay using Alipay in GeneXus applications

## [What is Alipay?](#What+is+Alipay%3F)

[Alipay](https://intl.alipay.com/open/index.htm) is a Chinese mobile payment platform. It was created by [Alibaba Group](http://www.alibabagroup.com/en/global/home) (e-commerce company) and currently has more than 500 million active users and a daily rate of more than 175 million payment transactions. It is widely used in China for any business and, as a result, integration with Alipay is a common requirement for mobile applications. For that purpose, the platform offers a complete integration [API](https://open.alipay.com/developmentAccess/developmentAccess.htm).

## [Architecture](#Architecture)

A basic architecture schema of Alipay integration is described in the following picture:

`[imagen omitida: wiki id 37147]`

Details:

1. A payment order is created from a third-party mobile application
2. Application Server processes the order and returns the information needed to perform the payment with Alipay
3. Mobile Application starts the payment process by calling the Alipay Application
4. Alipay Application makes the payment using Alipay servers
5. Alipay server returns the payment result to the Alipay Application
6. Alipay Application returns the payment result to the mobile application
7. Alipay server sends an asynchronous payment notification to the Application Server.

## [Integration with GeneXus](#Integration+with+GeneXus)

From Upgrade 8 of GeneXus 15, payment functions with Alipay can be integrated into the generated Android and iOS applications using an [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545) included in the GeneXus installation and importing the [Payment API](https://wiki.genexus.com/commwiki/wiki?37152).

## [Step-by-step instructions](#Step-by-step+instructions)

### [1 - Register the application in the Alipay developer site](#1+-+Register+the+application+in+the+Alipay+developer+site)

Developers need to be registered in the Alipay developer site and need to register all the applications that will integrate the payment functions. In this process, developers get the application credentials and signing information that is required to integrate with Alipay. Check [this document](https://wiki.genexus.com/commwiki/wiki?37154,,) for detailed information about the registration process.

### [2 - Create a PFX file](#2+-+Create+a+PFX+file)

Alipay requires signing the payment information in each transaction with the credentials obtained when the application was registered in the Alipay developer site. For every application, Alipay creates public and private keys in plain text. In order to use those credentials in the integration with GeneXus using the [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980), we need to create a PFX file (Personal Information Exchange). This can be done executing a set of [OpenSSL](https://www.openssl.org/) commands. [Here](https://wiki.genexus.com/commwiki/wiki?37155,,) is a detailed list of those commands and a utility file that can be downloaded to simplify this process. This is a one-time process; once we have the PFX file for an application, we do not need to generate it again in future builds.

### [3 - Set configuration information](#3+-+Set+configuration+information)

The first "programming" step is to set the configuration information. By default, the Alipay API loads the configuration information from an XML file named Alipay\_Config, using the procedure LoadConfig. Just modifying this file is enough to set all the configurations needed to integrate the application with Alipay. Following is a description of the Alipay\_Config.xml file structure.

```
<Configuration>     
    <AppId />
    <Environment />
    <CertificateFilename />
    <CertificatePassword />
    <CallbackURL />     
    <Timeout /> 
    <AdditionalConfig />
</Configuration>
```

* **AppId:** Identifier obtained when the application was registered in Alipay
* **Environment:** Possible values are *Production / Sandbox*. Execution environment where the payment transactions will be placed. The sandbox environment is only available for Android; in iOS, only the Production environment can be used.
* **CertificateFilename:** Name of the PFX file created in the previous step
* **CertificatePassword:** Password of the PFX file created in the previous step
* **CallbackURL:** URL of the payment notification service that Alipay will call to complete the payment transaction (point 7 in architecture listing above). By default, the URL of the procedure CallbackService included in the [Alipay API](https://wiki.genexus.com/commwiki/wiki?37152) is used.
* **Timeout:** Timeout in minutes for the payment transactions
* **AdditionalConfig :** List of additional information

### [4 - Prepare payment data](#4+-+Prepare+payment+data)

The next step is to prepare the payment data to send it to Alipay. First, the user needs to set some values in a variable based on *PaymentApplicationData* SDT from the [Alipay API](https://wiki.genexus.com/commwiki/wiki?37152) (product code, subject, body and amount). This variable will be the input of the procedure *GetPaymentInformation* which returns the processed information ready to be sent to Alipay.

There is an intermediate step performed by the *GetPaymentInformation* procedure; it allows processing the ready-to-send payment information (which includes the generated order number) by the user, for example, to store it in the application database tables. These actions can be edited in the procedure *OnAboutToPay* from the [Alipay API](https://wiki.genexus.com/commwiki/wiki?37152).

### [5 - Send payment information to Alipay](#5+-+Send+payment+information+to+Alipay)

Now the user is ready to send the payment information to Alipay, using the Pay method from the External Object *AlipayProvider* included in the [Alipay API](https://wiki.genexus.com/commwiki/wiki?37152). This method receives the processed payment information returned by the procedure *GetPaymentInformation* in the previous step in a variable based on the *PaymentInformation* SDT.

The following is an example code in a GeneXus Smart Devices object event with the actions from steps 4 and 5:

```
Event 'Pay with Alipay'
   Composite
      &PaymentApplicationData.ProductCode = 'Product name'
      &PaymentApplicationData.TotalAmount = 1000
      &PaymentApplicationData.Subject = 'Subject'
      &PaymentApplicationData.Body = 'Purchase information'
      GeneXus.Common.UI.Progress.ShowWithTitleAndDescription("Please Wait...","Preparing payment information...")
      Alipay.GetPaymentInformation(&PaymentApplicationData, &PaymentInformation)
      GeneXus.Common.UI.Progress.Hide()
      if &PaymentInformation.ErrorCode > 0
          Msg("Error: " + &PaymentInformation.ErrorDescription)
      else
          AlipayProvider.Pay(&PaymentInformation)
      endif
   EndComposite
Endevent
```

### [6 - Process payment result](#6+-+Process+payment+result)

The user needs to code two actions to process an Alipay payment result. The first one is the *AlipayProvider* External Object event called *OnPaymentFinished*. This event receives a variable based on the *PaymentResult* SDT which contains an ErrorCode, ErrorDescription, and OrderNumber of the completed payment. Check detailed information about the [Alipay API here](https://wiki.genexus.com/commwiki/wiki?37152).

The following is an example code of this event:

```
Event AlipayProvider.OnPaymentFinished(&PaymentResult)
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

### [7 - Asynchronous payment notification service](#7+-+Asynchronous+payment+notification+service)

The last step is executed by Alipay servers, which call a payment notification service provided by the application developer. This service URL is what we indicate in the configuration using the CallbackURL parameter. By default this URL refers to a procedure named *CallbackService* included in the [Alipay API](https://wiki.genexus.com/commwiki/wiki?37152). This procedure receives the HTTP data and converts it to an SDT structure (*PaymentNotificationInfo*); next, it calls another procedure named *CallbackHandler* to process that SDT with the notification information.

### [In sum](#In+sum)

Having registered the application and created the PFX file, the GeneXus developer only needs to modify the following objects to integrate Alipay into his application:

* Set configurations in *Alipay\_Config.xml* file
* Code the process of the payment data just before sending it to Alipay in the *OnAboutToPay* procedure.
* Set payment data, call *GetPaymentInformation* procedure and call Pay method of the *AlipayProvider* EO in the Smart Device object.
* Code the AlipayProvider EO *OnPaymentFinished* event in the Smart Device object.
* Code the notification service processing in the *CallbackHandler* procedure

## [Sample](#Sample)

A complete sample can be downloaded from [here](https://wiki.genexus.com/commwiki/wiki?37202,,).
