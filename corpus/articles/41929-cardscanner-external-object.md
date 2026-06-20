---
title: "CardScanner External Object"
source_id: 41929
source_url: https://wiki.genexus.com/commwiki/wiki?41929
genexus_version: "18"
---

# CardScanner External Object

|  |  |
| --- | --- |
|  |  |

Enables the easy extraction of information from a credit card.

Takes a cropped photo of the credit card and automatically captures the card number. This is possible only in the case of engraved figures. For the case of printed numbers, the manual entry of the credit card numbers will be required. The information obtained is stored in the CardInformation SDT.

## [**Properties**](#Properties)

### [**IsAvailable**](#IsAvailable+)

Enables us to know if the External Object may be used on the device. Returns True if it's possible. Otherwise, it returns False.

### [**CollectCardholderName**](#CollectCardholderName)

When the value of this property is set up as True, the external object will request the user of the application to enter the Cardholder Name of the credit card.

### [**CollectCVV**](#CollectCVV)

When the property value is set as True, the external object will request the user of the application to enter the Card Verification Value of the credit card.

### [**CollectExpiry**](#CollectExpiry)

When the property value is set as True, the external object will request the user of the application to enter the credit card's expiry date.

### [**CollectPostalCode**](#CollectPostalCode)

When the value of this property is set as True, the external object will request the user of the application to enter the postal code associated with the card.

### [**DetectionMode**](#DetectionMode)

Allows changes between the various scan modes for the credit card using the CardDetectionMode domain.

### [**DisableManualEntry**](#DisableManualEntry)

When the value of this property is set as True, the option for the user to enter the card number manually is disabled.

### [**RestrictPostalCodeNumeric**](#RestrictPostalCodeNumeric)

When the value of this property is set as True, only numbers are allowed as entry for the postal code value.

### [**ScanExpiry**](#ScanExpiry)

When the value of this property is set as True, there is an attempt to read the card's expiry date. This is possible only when the date has been engraved. It does not work for cases with printed expiry dates. By default, the value of this property is set as True.

### [**ScanInstructionsText**](#ScanInstructionsText)

Allows customizing the instructions shown on screen.

### [**SuppressScanConfirmation**](#SuppressScanConfirmation)

When the value of this property is set as True, the confirmation is eliminated following the card's scan. The EXO's behavior will enable the capture of the credit card and it will end the action. When this property is set as False, following the card's scan, it will enable the user to enter additional data manually. The default value of this property is True.

## [**Methods**](#Methods)

### [**ScanCard**](#ScanCard)

## [**Domains**](#Domains)

### [**CardDetectionMode**](#CardDetectionMode)

|  |  |
| --- | --- |
| **Image&Number** | Allows taking a photo of the credit card and capturing its number automatically (as long as figures are engraved, but not printed). Default value of property DetectionMode. |
| **Image Only** | Only takes a photo of credit card and then requests the manual entry of card number. |
| **Automatic** | By default, it has the same behavior as if it had value Image&Number, though in case it becomes impossible to capture card numbers, it will photograph the card after a period of time and then it will request the manual entry of numbers. In GeneXus v16 Upgrade 2, this option is supported only by the iOS generator. |

## [**Structure Data Type**](#Structure+Data+Type)

### [**Card Information**](#Card+Information)

**CardNumber:**Varchar(40)

Stores number of the card scanned.

**RedactedCardNumber:** Varchar(40)

This will be the field for storage in cases where the number is entered manually.

**ExpiryMonth:** Numeric(2.0)

Stores the month of expiry.

**ExpiryYear:** Numeric(2.0)

Stores the year of expiry.

**CVV:** Varchar(40)

Stores the Card Verification Value.

**PostalCode:**Varchar(40)

Stores the postal code value.

**CardHolderName:** Varchar(200)

Stores the name of the credit card holder.

**CardImage:** Image

Stores the photo of the credit card scanned.

**CardType:** CreditCardType

Stores the payment company for the credit card (Visa, Mastercard, etc.)

**CardLogo:** Image

Stores the logo of the payment company for the credit card.

## [**Example**](#Example)

The example below shows a possible implementation for this External Object. The idea behind it is to act as an example for readers.

You will create a Panel for Smart Devices where you will place variables like the following.

|  |
| --- |
|  |

Due to panel customization reasons, it was decided that Card Information SDT will not be used directly, so that there is more control over the view of the panel.

The properties of the EXO are now set up in the following manner:

```
Event ClientStart 
    Composite
        CardScanner.CollectCardholderName        = True
        CardScanner.CollectCVV                   = True
        CardScanner.CollectExpiry                = True
        CardScanner.CollectPostalCode            = True
        CardScanner.SuppressScanConfirmation     = False
    EndComposite
Endevent
```

We will now include the following code in the event of the Scan Creditcard button:

```
Event 'ScanCreditcard'
     Composite
        If CardScanner.IsAvailable
            &CardInformation    = CardScanner.ScanCard()
        Else
            msg("Scan isn't available", nowait)
        EndIf
    
        &CVV                = &CardInformation.CVV
        &Name               = &CardInformation.CardHolderName
        &Month              = &CardInformation.ExpiryMonth
        &Year               = &CardInformation.ExpiryYear
        &CardNumber         = &CardInformation.CardNumber
        &PostalCode         = &CardInformation.PostalCode
        
    EndComposite
Endevent
```

When the event is triggered, we will view a screen so that (these images are provided for illustrative purposes only):

|  |
| --- |
|  |

In this screen, the user of the application has the option of capturing an image of the credit card or the alternative of entering data manually by tapping on the Keyboard button.

Once the credit card data has been scanned, a view like the following will be shown on screen (in our example, it would show the credit card number and the expiry date):

|  |
| --- |
|  |

## [**Scope**](#Scope)

|  |  |
| --- | --- |
| **Platforms** | SmartDevices(Android, iOS) |
