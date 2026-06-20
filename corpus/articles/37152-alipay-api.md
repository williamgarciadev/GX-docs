---
title: "Alipay API"
source_id: 37152
source_url: https://wiki.genexus.com/commwiki/wiki?37152
genexus_version: "18"
---

# Alipay API

Alipay API for GeneXus consists of an External Object and a group of Procedures, SDTs and Domains which can be used to interact with the Alipay [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545) to integrate payment capabilities when using Alipay in the generated applications; for Android and iOS.

## [Versions](#Versions)

Version 1.0 (Dec 11, 2017) - [Download](https://wiki.genexus.com/commwiki/wiki?37153,,).

## [Structure](#Structure)

`[imagen omitida: wiki id 37170]`

## [External Object](#External+Object)

### [**AlipayProvider**](#AlipayProvider)

*Method*

|  |  |
| --- | --- |
| **Name** | Pay |
| **Description** | Used to perform the payment transaction with Alipay |
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
| **Description** | Triggered when the payment transaction in Alipay is completed |
| **Parameters** | *PaymentResult*: SDT(PaymentResult) |
| **Returns** | None |

## [Domains](#Domains)

### [**Environment (CommonPay)**](#Environment+%28CommonPay%29)

The environment where the payment transaction will be executed.

|  |  |
| --- | --- |
| **Value** | **Description** |
| *Production* | Production environment, transactions are real. |
| *Sandbox* | Test environment. Only available for Android applications |

### [**TradeStatus (Alipay)**](#TradeStatus+%28Alipay%29)

Transaction status received in the payment notification service.

|  |  |
| --- | --- |
| **Value** | **Description** |
| *Closed* | TRADE\_CLOSED |
| *Finished* | TRADE\_FINISHED |
| *Success* | TRADE\_SUCCESS |
| *WaitBuyerPaid* | WAIT\_BUYER\_PAID |

### [**FundChannel (Alipay)**](#FundChannel+%28Alipay%29)

Fund channel used in the transaction, received in the payment notification service.

|  |  |
| --- | --- |
| **Value** | **Description** |
| *AlipayAccount* | ALIPAYACCOUNT |
| *BusinessCard* | MCARD |
| *Coupon* | COUPON |
| *Discount* | DISCOUNT |
| *FinanceAccount* | FINANCEACCOUNT |
| *MerchantCoupon* | MCOUPON |
| *MerchantDiscount* | MDISCOUNT |
| *PCredit* | PCREDIT |
| *PrepaidCard* | PCARD |
| *Point* | POINT |

### [**VoucherType (Alipay)**](#VoucherType+%28Alipay%29)

Voucher type used in the transaction received in the payment notification service.

|  |  |
| --- | --- |
| **Value** | **Description** |
| *Discount* | ALIPAY\_DISCOUNT\_VOUCHER |
| *Fix* | ALIPAY\_FIX\_VOUCHER |
| *Item* | ALIPAY\_ITEM\_VOUCHER |

## [Structured data types](#Structured+data+types)

### [**Configuration (CommonPay)**](#Configuration+%28CommonPay%29)

Used to set all the configuration needed to perform the payment transactions.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| AppId | | | VarChar(40) | Application ID obtained when the application was [registered](https://wiki.genexus.com/commwiki/wiki?37154,,) in the Alipay developer's site. |
| Environment | | | Environment | Environment where the payment transaction will be executed |
| CertificateFilename | | | VarChar(200) | Name of the PFX file used to sign the payment information. Check [this document for more detail](https://wiki.genexus.com/commwiki/wiki?37155,,). |
| CertificatePassword | | | VarChar(40) | Password of the PFX file used to sign the payment information. |
| CallbackURL | | | URL | URL of the payment notification service. |
| Timeout | | | Numeric(4.0) | Timeout in minutes for the payment transaction |
| MerchantId | | | VarChar(40) | *Not used for Alipay* |
| MerchantKey | | | VarChar(80) | *Not used for Alipay* |
| AdditionalConfig | | | *<Collection>* | Additional information for the application configuration |
|  | Name | | VarChar(40) | Name of the additional information |
|  | Value | | VarChar(200) | Value of the additional information |

### [**PaymentResult (CommonPay)**](#PaymentResult+%28CommonPay%29)

Information sent to the *OnPaymentFinished* event of the AlipayProvider ExternalObject

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ErrorCode | | | Numeric(4.0) | Error code for the payment transaction result |
| ErrorDescription | | | VarChar(200) | Error description for the payment transaction result |
| OrderNumber | | | VarChar(40) | Order number of the payment transaction finished. Can be used for payment processing in the application |
| AdditionalInfo | | | LongVarChar(2M) | Additional information returned from the payment transaction |

### [**PaymentApplicationData (Alipay)**](#PaymentApplicationData+%28Alipay%29)

Used to set the payment data by the user (product descriptions, amount) and input of the *GetPaymentInformation* procedure.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ProductCode | | | Character(20) | Description of the product or products involved in the payment |
| TotalAmount | | | Amount | Amount of the payment transaction |
| Subject | | | Character(256) | Subject to describe the transaction |
| Body | | | Character(400) | Details of the payment transaction |
| TimeoutExpress | | | Character(20) | *Not set by the user.* Timeout for the payment transaction |
| NotifyURL | | | URL | *Not set by the user.* URL of the notification service |
| OrderNumber | | | Character(64) | *Not set by the user.* Order number for the payment transaction |

### [**PaymentInfoParameters (Alipay)**](#PaymentInfoParameters+%28Alipay%29)

The structure used by the *GetPaymentInformation* procedure. It is managed automatically by the API, and there is no need for the developer to handle it while coding the integration.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| AppId | | | Character(20) | Application ID obtained when the application was [registered](https://wiki.genexus.com/commwiki/wiki?37154,,) in the Alipay developer's site. |
| PaymentData | | | PaymentApplicationData | Payment data provided by the user |
| Charset | | | Character(20) | *Fixed value : utf-8* |
| Method | | | URL | *Fixed value : alipay.trade.app.pay* |
| SignType | | | SignType | *Fixed value : RSA2* |
| Timestamp | | | DateTime | Timestamp of the payment transaction. |
| Version | | | Character(20) | *Fixed value : 1.0* |
| CertificatePath | | | Character(500) | Name of the PFX file used to sign the payment information  Make sure to use a FullPath to reference your PFX file |
| CertificatePassword | | | Character(20) | Password of the PFX file used to sign the payment information |

### [**PaymentInformation (Alipay)**](#PaymentInformation+%28Alipay%29)

Information returned by the *GetPaymentInformation* procedure to be sent to Alipay to perform the payment.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ErrorCode | | | Numeric(10.0) | Error code returned by the *GetPaymentInformation* procedure |
| ErrorDescription | | | Character(200) | Error description returned by the *GetPaymentInformation* procedure |
| Parameters | | | LongVarChar(2M) | Payment information parameters to be sent to Alipay |
| Environment | | | Environment | Environment where the payment transaction will be executed |
| OrderNumber | | | VarChar(40) | Order number for the payment transaction |

### [**PaymentNotificationInfo (Alipay)**](#PaymentNotificationInfo+%28Alipay%29)

Information sent by Alipay to the asynchronous payment notification service. This information can be used by the developer in the *CallbackHandler* procedure.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| NotifyTime | | | DateTime |  |
| NotifyType | | | Character(64) |  |
| NotifyId | | | Character(128) |  |
| AppId | | | Character(32) |  |
| Charset | | | Character(10) |  |
| Version | | | Character(3) |  |
| SignType | | | Character(10) |  |
| Sign | | | Character(256) |  |
| AlipayTradeNumber | | | Character(64) |  |
| OutTradeNumber | | | Character(64) |  |
| MerchantId | | | Character(64) |  |
| BuyerId | | | Character(16) |  |
| BuyerLogonId | | | Character(100) |  |
| SellerId | | | Character(30) |  |
| SellerEmail | | | Email |  |
| TradeStatus | | | TradeStatus |  |
| TotalAmount | | | Amount |  |
| ReceiptAmount | | | Amount |  |
| InvoiceAmount | | | Amount |  |
| BuyerPayAmount | | | Amount |  |
| PointAmount | | | Amount |  |
| RefundFee | | | Amount |  |
| Subject | | | Character(256) |  |
| Body | | | Character(400) |  |
| CreationDateTime | | | DateTime |  |
| PaymentDateTime | | | DateTime |  |
| RefundDateTime | | | DateTime |  |
| CloseDateTime | | | DateTime |  |
| FundBillList | | | *<Collection>* |  |
| Amount | | | Amount |  |
| FundChannel | | | FundChannel |  |
| PassBackParameters | | | Character(512) |  |
| VoucherDetailList | | | *<Collection>* |  |
| Name | | | Character(64) |  |
| Type | | | VoucherType |  |
| Amount | | | Amount |  |
| MerchantContribute | | | Amount |  |
| OtherContribute | | | Amount |  |
| Memo | | | Character(256) |  |

## Procedures

### [**LoadConfig (CommonPay)**](#LoadConfig+%28CommonPay%29)

Loads the configuration needed to perform the payment with Alipay. By default, it reads the information from the Alipay\_Config.xml file.

|  |  |
| --- | --- |
| **Parameters** | *PaymentProvider*: Alipay |
| **Returns** | *Configuration*:SDT(Configuration) |

### [**GetPaymentInformation (Alipay)**](#GetPaymentInformation+%28Alipay%29)

Processes the payment data given by the user and returns all the required information (signed) ready to be sent to Alipay.

|  |  |
| --- | --- |
| **Parameters** | *PaymentApplicationData*: SDT(PaymentApplicationData) |
| **Returns** | *PaymentInformation*: SDT(PaymentInformation) |

### [**OnAboutToPay (Alipay)**](#OnAboutToPay+%28Alipay%29)

Used to process the payment data just before it is sent to Alipay. One common use is to store the payment information (especially the OrderNumber) in the application database tables.

|  |  |
| --- | --- |
| **Parameters** | *PaymentApplicationData*: SDT(PaymentApplicationData) |
| **Returns** | - |

### [**CallbackService (Alipay)**](#CallbackService+%28Alipay%29)

HTTP Procedure. Asynchronous payment notification service that Alipay servers call after the payment process finishes. It does not return data; it turns the HTTP information into an SDT (PaymentNotificationInfo) and calls CallbackHandler procedure.

### [**CallbackHandler (Alipay)**](#CallbackHandler+%28Alipay%29)

Used to process the data sent by Alipay servers when calling the asynchronous payment notification service.

|  |  |
| --- | --- |
| **Parameters** | *PaymentNotificationInfo*: SDT(PaymentNotificationInfo) |
| **Returns** | - |

####


|  |
| --- |
| **Backlinks** |
| [HowTo: Pay using Alipay in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?37146) |

---
