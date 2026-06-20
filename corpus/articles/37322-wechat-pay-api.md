---
title: "WeChat Pay API"
source_id: 37322
source_url: https://wiki.genexus.com/commwiki/wiki?37322
genexus_version: "18"
---

# WeChat Pay API

WeChat Pay API for GeneXus consists of an External Object and a group of Procedures, SDTs and Domains that can be used to interact with the WeChat Pay [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545) to integrate payment capabilities when using WeChat Pay in the generated applications. For Android and iOS.

## [Versions](#Versions)

Version 1.0 (Dec 11, 2017) - [Download](https://wiki.genexus.com/commwiki/wiki?37325,,).  **Latest!**

## [Structure](#Structure)

`[imagen omitida: wiki id 37326]`

## [External Object](#External+Object)

### [**WeChatPayProvider**](#WeChatPayProvider)

*Method*

|  |  |
| --- | --- |
| **Name** | Pay |
| **Description** | Used to perform the payment transaction with WeChat Pay |
| **Parameters** | *PaymentInformation*: SDT(PaymentInformation) |
| **Returns** | None |

*Properties*

|  |  |
| --- | --- |
| **Name** | **Description** |
| ErrorCode | ErrorCode with the result of Pay method |
| ErrorDescription | ErrorDescription with the result of Pay method |

*Event*

|  |  |
| --- | --- |
| **Name** | OnPaymentFinished |
| **Description** | Triggered when the payment transaction in WeChat Pay is completed. |
| **Parameters** | *PaymentResult*: SDT(PaymentResult) |
| **Returns** | None |

## [Domains](#Domains)

### [**Environment (CommonPay)**](#Environment+%28CommonPay%29)

The environment where the payment transaction will be executed.

|  |  |
| --- | --- |
| **Value** | **Description** |
| *Production* | Production environment, transactions are real |
| *Sandbox* | Test environment |

### [**ReturnCode (WeChatPay)**](#ReturnCode+%28WeChatPay%29)

Return values to send to WeChat Pay in the response to the asynchronous notification service.

|  |  |
| --- | --- |
| **Value** | **Description** |
| *Success* | SUCCESS |
| *Fail* | FAIL |

## [Structured data types](#Structured+data+types)

### [**Configuration (CommonPay)**](#Configuration+%28CommonPay%29)

Used to make all the settings needed to perform the payment transactions.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| AppId | | | VarChar(40) | Application ID obtained when the application was [registered](https://wiki.genexus.com/commwiki/wiki?37323,,) in WeChat Open Platform site. |
| Environment | | | Environment | Environment where the payment transaction will be executed. |
| CertificateFilename | | | VarChar(200) | *Not used for WeChat Pay* |
| CertificatePassword | | | VarChar(40) | *Not used for WeChat Pay* |
| CallbackURL | | | URL | URL of the payment notification service |
| Timeout | | | Numeric(4.0) | Timeout in minutes for the payment transaction |
| MerchantId | | | VarChar(40) | Identifier of the user registered in WeChat Open Platform |
| MerchantKey | | | VarChar(80) | Key assigned to the application in WeChat Open Platform |
| AdditionalConfig | | | *<Collection>* | Additional information for the application configuration |
|  | Name | | VarChar(40) | Name of the additional information |
|  | Value | | VarChar(200) | Value of the additional information. |

### [**PaymentResult (CommonPay)**](#PaymentResult+%28CommonPay%29)

Information sent to the *OnPaymentFinished* event of the WeChatPayProvider ExternalObject

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ErrorCode | | | Numeric(4.0) | Error code for the payment transaction result |
| ErrorDescription | | | VarChar(200) | Error description for the payment transaction result |
| OrderNumber | | | VarChar(40) | Order number of the completed payment transaction. Can be used for payment processing in the application. |
| AdditionalInfo | | | LongVarChar(2M) | Additional information returned from the payment transaction. |

### [**PaymentApplicationData (WeChatPay)**](#PaymentApplicationData+%28WeChatPay%29)

Used to set payment data entered by the user (product descriptions, currency, amount) and input of the *GetPaymentInformation* procedure.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ProductCode | | | Character(128) | Code of the product or products involved in the payment |
| ProductDescription | | | VarChar(200) | Description of the product or products involved in the payment |
| Currency | | | Character(3) | Currency for the payment transaction |
| TotalAmount | | | Amount | Amount of the payment transaction |
| RandomString | | | Character(32) | *Not set by the user.*Random value used in the WeChat Pay communication. |
| OrderNumber | | | Character(64) | *Not set by the user.* Order number for the payment transaction. |

### [**PaymentInfoParameters (WeChatPay)**](#PaymentInfoParameters+%28WeChatPay%29)

Structure used by the *GetPaymentInformation* procedure to make two intermediate actions when preparing the payment transaction. It is managed automatically by the API, and there is no need for the developer to handle it while coding the integration.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| AppId | | | Character(32) | Application ID obtained when the application was [registered](https://wiki.genexus.com/commwiki/wiki?37154,,) in the Alipay developer's site. |
| MerchantId | | | Character(32) | Identifier of the user registered in WeChat Open Platform |
| MerchantKey | | | Character(64) | Key assigned to the application in WeChat Open Platform |
| DeviceId | | | Character(32) | Identifier of the device that is making the transaction (*ClientInformation.Id* value is used) |
| RandomString | | | Character(32) | Random value used in the WeChat Pay communication |
| Signature | | | Character(32) | Signature of the transaction parameters |
| SignatureType | | | SignatureType | *Fixed value : HMACSHA256* |
| ProductDescription | | | Character(128) | Description of the product or products involved in the payment |
| OrderNumber | | | Character(32) | Order number for the payment transaction |
| Currency | | | Character(3) | Currency for the payment transaction |
| TotalAmount | | | Numeric(9.0) | Amount of the payment transaction |
| TransactionStartTime | | | Character(14) | Time when transaction starts |
| NotificationAddress | | | Character(256) | URL of the payment notification service |
| TransactionType | | | Character(16) | *Fixed value: APP* |
| PrepayId | | | Character(32) | Transaction identifier returned by WeChat Pay servers before performing the payment |
| Timestamp | | | Character(20) | Current time when preparing the payment |
| Package | | | Character(128) | *Fixed value: Sign=WXPay.* |

### [**PaymentInformation (WeChatPay)**](#PaymentInformation+%28WeChatPay%29)

Information returned by the *GetPaymentInformation* procedure to be sent to WeChat Pay to perform the payment.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ErrorCode | | | Numeric(10.0) | Error code returned by the *GetPaymentInformation* procedure |
| ErrorDescription | | | Character(128) | Error description returned by the *GetPaymentInformation* procedure |
| AppId | | | Character(32) | Application ID obtained when the application was [registered](https://wiki.genexus.com/commwiki/wiki?37154,,) in the Alipay developer's site. |
| MerchantId | | | Character(32) | Identifier of the user registered in WeChat Open Platform |
| OrderNumber | | | Character(32) | Order number for the payment transaction |
| DeviceId | | | Character(32) | Identifier of the device that is making the transaction (*ClientInformation.Id* value is used) |
| RandomString | | | Character(32) | Random value used in the WeChat Pay communication |
| Signature | | | Character(32) | Signature of the transaction parameters |
| SignatureParameters | | | LongVarChar(2M) | Parameters sent to WeChat Pay that were signed |
| TransactionType | | | Character(16) | *Fixed value: APP* |
| PrepayId | | | Character(64) | Transaction identifier returned by WeChat Pay servers before performing the payment |
| Timestamp | | | Character(20) | Current time when preparing the payment |
| Package | | | Character(20) | *Fixed value: Sign=WXPay* |
| ReturnCode | | | Character(20) | Code returned by the WeChat Pay servers when sending payment information |
| ReturnMessage | | | Character(20) | Message returned by the WeChat Pay servers when sending payment information |
| BusinessResult | | | Character(16) | Additional info returned by the WeChat Pay servers when sending payment information. |

### [**PaymentNotificationInfo (WeChatPay)**](#PaymentNotificationInfo+%28WeChatPay%29)

Information sent by WeChat Pay to the asynchronous payment notification service. This information can be used by the developer in the *CallbackHandler* procedure.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| AppId | | | DateTime |  |
| PaymentBank | | | Character(64) |  |
| CashPaymentAmount | | | Character(128) |  |
| DeviceId | | | Character(32) |  |
| CurrencyType | | | Character(10) |  |
| IsSuscriber | | | Character(3) |  |
| MerchantId | | | Character(10) |  |
| RandomString | | | Character(256) |  |
| UserTag | | | Character(64) |  |
| MerchantTradeNumber | | | Character(64) |  |
| ResultCode | | | Character(64) |  |
| BusinessResult | | | Character(16) |  |
| Signature | | | Character(100) |  |
| PaymentEndTime | | | Character(30) |  |
| TransactionType | | | Email |  |
| TransactionId | | | TradeStatus |  |
| TotalAmount | | | Amount |  |

### [**PaymentNotificationResult (WeChatPay)**](#PaymentNotificationResult+%28WeChatPay%29)

Information used to return a result to WeChat Pay when the asynchronous payment notification service is called. A variable of this type is returned by the *CallbackHandler* procedure.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ReturnCode | | | ReturnCode |  |
| ReturnMessage | | | VarChar(100) |  |

### [**SandboxPaymentInfo (WeChatPay)**](#SandboxPaymentInfo+%28WeChatPay%29)

Information returned by WeChat Pay servers when using the sandbox environment. This information has then to be set in a *PaymentInformation* variable to be returned by the *GetPaymentInformation* procedure.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| AppId | | | Character(32) | Application ID obtained when the application was [registered](https://wiki.genexus.com/commwiki/wiki?37154,,) in the Alipay developer's site. |
| MerchantId | | | Character(32) | Identifier of the user registered in WeChat Open Platform |
| RandomString | | | Character(32) | Random value used in the WeChat Pay communication |
| Signature | | | Character(32) | Signature of the transaction parameters |
| PrepayId | | | Character(64) | Transaction identifier returned by WeChat Pay servers before performing the payment |
| Timestamp | | | Character(20) | Current time when preparing the payment |
| Package | | | Character(20) | *Fixed value: Sign=WXPay.* |

## [Procedures](#Procedures)

### [**LoadConfig (CommonPay)**](#LoadConfig+%28CommonPay%29)

Loads the configuration needed to perform the payment with WeChat Pay. By default, it reads the information from the WeChatPay\_Config.xml file.

|  |  |
| --- | --- |
| **Parameters** | *PaymentProvider*: Alipay |
| **Returns** | *Configuration*:SDT(Configuration) |

### [**GetPaymentInformation (WeChatPay)**](#GetPaymentInformation+%28WeChatPay%29)

Processes the payment data given by the user and returns all the required information (signed) ready to be sent to WeChat Pay.

|  |  |
| --- | --- |
| **Parameters** | *PaymentApplicationData*: SDT(PaymentApplicationData) |
| **Returns** | *PaymentInformation*: SDT(PaymentInformation) |

### [**OnAboutToPay (WeChatPay)**](#OnAboutToPay+%28WeChatPay%29)

Used to process the payment data just before it is sent to WeChat Pay. One common use is to store the payment information (especially the OrderNumber) in the application database tables.

|  |  |
| --- | --- |
| **Parameters** | *PaymentApplicationData*: SDT(PaymentApplicationData) |
| **Returns** | - |

### [**CallbackService (WeChatPay)**](#CallbackService+%28WeChatPay%29)

HTTP Procedure. Asynchronous payment notification service called by WeChat Pay servers after the payment process is completed. It turns the HTTP information into an SDT (*PaymentNotificationInfo*) and calls CallbackHandler procedure.

|  |  |
| --- | --- |
| **Parameters** | *-* |
| **Returns** | *PaymentNotificationResult*: SDT(PaymentNotificationResult) |

### [**CallbackHandler (Alipay)**](#CallbackHandler+%28Alipay%29)

Used to process the data sent by WeChat Pay servers when calling the asynchronous payment notification service.

|  |  |
| --- | --- |
| **Parameters** | *PaymentNotificationInfo*: SDT(PaymentNotificationInfo) |
| **Returns** | *PaymentNotificationResult*: SDT(PaymentNotificationResult) |

####


|  |
| --- |
| **Backlinks** |
| [App Id property](https://wiki.genexus.com/commwiki/wiki?45383) | [HowTo: Pay using WeChat Pay in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?37321) |
|

---
