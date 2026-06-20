---
title: "GAM - Time Based One Time Password (TOTP)"
source_id: 49974
source_url: https://wiki.genexus.com/commwiki/wiki?49974
genexus_version: "18"
---

# GAM - Time Based One Time Password (TOTP)

Using Time Based One Time Passwords (TOTP) to authenticate users to the system offers the advantage that they do not need to remember a password since a new code is generated every time they want to log in. In addition, it adds another level of security because the code is valid for a short time.

When you add to this the fact that users need an application on their smartphone to get these codes —depending on the security of the users’ smartphones— it also adds another level of difficulty if someone tries to authenticate with a username that doesn’t belong to them.

Time Based One Time Password (TOTP) is an algorithm that generates [One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?48197) keys that use the current time as a source of uniqueness. Therefore, in the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) TOTP is found as a [One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?48197) Code generation type.

It is important to clarify that while the code generated in the Authenticator application on the phone is valid (approximately 1 minute), this code can be used multiple times to log in until this code expires.

`[imagen omitida: wiki id 52654]`

Once this code generation method has been chosen, the following parameters can be configured (the image shows their default values):

`[imagen omitida: wiki id 52652]`

* **Code expiration timeout:** This is the maximum time (in seconds) available for the user to enter a code.
* **Maximum daily number of codes:** Number of times per day that a code can be entered (after clicking on the NEXT button).
* **Number of unsuccessful retries to lock the OTP:** Number of unsuccessful retries to block access.
* **Automatic OTP unlock time:** Time for automatic unlocking of OTP codes.
* **Number of unsuccessful retries to block user based on number of OTP locks:** Number of times OTP codes can be locked before blocking the User.

### [Configuration of a User's Authenticator app](#Configuration+of+a+User%27s+Authenticator+app)

With this type of authentication, each user must configure an Authenticator (pairing of the user's account with the Authenticator application). To do so, follow the steps below:

1. Go to the profile of the user whose Authenticator you want to configure. In the menu on the right, you will find the **Enable authenticator** button. `[imagen omitida: wiki id 52647]`**Note:**This button will be visible in user profiles once an [OTP](https://wiki.genexus.com/commwiki/wiki?48197) authentication type has been created with TOTP Authenticator as Code generation type.
2. By clicking on the above button, you will be directed to a window similar to the following:`[imagen omitida: wiki id 52649]`
3. The selected Authenticator must be used to scan the QR code or use the Secret Key provided to synchronize the Authenticator code generation with the application.
4. Lastly, you need to enter a code provided by the Authenticator (on time) in the **Type a code** field and click on the **Enable** button. `[imagen omitida: wiki id 52648]` Below is what the screen looks like once this operation has been successfully performed: `[imagen omitida: wiki id 52655]`

### [Configuration of TOTP as first and second factor](#Configuration+of+TOTP+as+first+and+second+factor)

Since [One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?48197) can be used as either first or second authentication factor, TOTP inherits this property. Remember that to define whether you want to use the authentication type as first or second factor, you must take into account the property **Use For First Factor Authentication?**inside it.

`[imagen omitida: wiki id 52656]`

This property is cleared by default; if left unchanged, it generates an authentication type that can be used as a second factor. On the other hand, when this property is selected, it generates an authentication type that can be used as a first factor.

### [Additional steps: how to configure TOTP as a second factor](#Additional+steps%3A+how+to+configure+TOTP+as+a+second+factor)

Once the TOTP authentication type has been created, another authentication type must be configured that will use the newly configured authentication as a second factor. In this case, for example, Local authentication is set to use TOTP as a second factor.

Once in edit mode, within the authentication type, select the **Enable Two Factor Authentication?** property. In **Authentication Type Name**, select the second factor authentication type previously created.

`[imagen omitida: wiki id 52650]`

In addition, two more properties can be modified (in the image, they have their default values):

* **First factor authentication expiration:** Maximum time available for the user to confirm the second factor after passing the first factor.
* **Force 2FA for all users?:** Allows forcing all users to use two authentication factors.

The last step for a user to authenticate using this two factor configuration is to go to the user's profile in edit mode and select the option **Enable Two factor authentication?**

`[imagen omitida: wiki id 52651]`

**Note:** This step is NOT necessary if the **Force 2FA for all users?** property mentioned in the previous step is selected. In addition, it should be clarified that if all users are forced to use 2FA, any user who doesn’t have an Authenticator configured will not be able to log in.

### [**Length of the secret key to be generated**](#Length+of+the+secret+key+to+be+generated)

The length of the secret key generated by GeneXus for each user can be modified by going to the menu *Repository Configuration > Users Tab > TOTP secret key length*, as shown in the image below.

`[imagen omitida: wiki id 52653]`

* **TOTP secret key length**: Property indicating the maximum length of the secret key generated for Authenticator applications (16 is the default value).

### [Considerations](#Considerations)

On the iPhone —in particular, for the Google Authenticator application— the password length cannot exceed 16 characters ([ref](https://github.com/google/google-authenticator/issues/332)).

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49616,,).

### [See Also](#See+Also)

[GAM - One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?48197)  
[GAM - Time Based One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50708)


|  |
| --- |
| **Backlinks** |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [GAM - One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50664) | [GAM - Time Based One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50708) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
