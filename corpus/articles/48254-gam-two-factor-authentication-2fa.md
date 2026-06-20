---
title: "GAM - Two Factor Authentication (2FA)"
source_id: 48254
source_url: https://wiki.genexus.com/commwiki/wiki?48254
genexus_version: "18"
---

# GAM - Two Factor Authentication (2FA)

It is possible to authenticate and verify, in a second step, the user who is trying to log in. This is known as Two Factor Authentication (2FA) and 2 Step Verification (2SV).

2FA is commonly used when a password or username is entered, and a second validation step is performed by sending an email or SMS to mitigate brute force attacks.

The second factor authentication can only be [One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?50664) verification, including OTP Custom.

### [How does it work?](#How+does+it+work%3F)

To improve security, the user is required to validate twice before accessing. The first step involves entering a username and password, and the second step performs another validation (like the one mentioned above).

In both cases, in a web or mobile application, if the user has this functionality enabled, there are two steps that the user will have to follow each time they log in. This means that while logging in, the user has to successfully pass the second factor to stay logged in to the app.

### [Considerations](#Considerations)

Two Factor Authentication can be configured with the following authentication types: OTP, [Local](https://wiki.genexus.com/commwiki/wiki?20703), [Custom](https://wiki.genexus.com/commwiki/wiki?21751), [WebService](https://wiki.genexus.com/commwiki/wiki?16512), [GAMRemoteRest](https://wiki.genexus.com/commwiki/wiki?44833).

### [Steps to set up Two Factor Authentication](#Steps+to+set+up+Two+Factor+Authentication)

In this example, Local Authentication is set as the first factor authentication and OTP is the second factor authentication.

* Step 1: Add the second factor authentication by choosing OTP. [Read Steps to set up OTP](https://wiki.genexus.com/commwiki/wiki?48197) to fully understand OTP configuration.

To use OTP only as second factor authentication, the checkbox "Use For First Factor Authentication?" must be kept unchecked.

`[imagen omitida: wiki id 48263]`

* Step 2: In this example, the first factor authentication is going to be Local. Local is the default authentication in GAM, so you have to edit it.

`[imagen omitida: wiki id 52348]`

In the edit form of Local Authentication, the check box "Enable Two Factor Authentication?" has to be selected.

In the "Authentication Type Name" Combo Box, choose the OTP that was added in step 1.

The checkbox "Force 2FA for all users?" is selected. This option sets 2FA for all the users in the application.

`[imagen omitida: wiki id 52349]`

By selecting the checkbox "Force 2FA for all users?" in the first factor authentication, every user of the app is set with the "Enable two factor authentication?" checkbox selected.

If "Force 2FA for all users?" is not selected, you must select the "Enable two factor authentication?" checkbox in the settings of every user that you want to use 2FA.

`[imagen omitida: wiki id 52347]`

### [2FA properties](#2FA+properties)

Besides the configuration shown above, 2FA properties can also be set in the GeneXus IDE. For this, you will have to refer to the properties by the following names:

* &AuthenticationTypeLocal.TwoFactorAuthentication.Enable
* &AuthenticationTypeLocal.TwoFactorAuthentication.AuthenticationTypeName
* &AuthenticationTypeLocal.TwoFactorAuthentication.FirstAuthenticationFactorExpiration (seconds): Numeric 9. Default = 900.
* &AuthenticationTypeLocal.TwoFactorAuthentication.ForceForAllUsers: If set to false, every user can enable this.
* &UserEnableTwoFactorAuth = Boolean (allows null)

### [Email server configuration](#Email+server+configuration)

Read this article: [Email server configuration with GAM](https://wiki.genexus.com/commwiki/wiki?48197) to learn more about it.

### [How to use 2FA through REST Services](#How+to+use+2FA+through+REST+Services)

1. Access Token  
  
**The Endpoint is:** https://<domain>/<virtual\_directory>/oauth/gam/v2.0/access\_token  
  
**FIRST POST  
  
Body:**

**client\_id:** Client ID of the application, required.  
**client\_secret:** Client Secret of the application, required.  
**grant\_type=password:** It is required.  
**scope**: Scope of the user account you want to access. It's only required when "&GAMApplication.ClientAuthenticationRequestMustIncludeUserScopes" is True.  
**username:** Username of the user with 2FA enabled, required.  
**password:** Password of the User to be authenticated, required.  
**authentication\_type\_name:** Name of the authentication type with 2FA configured at the server, required.

**POSTMAN Example:**  
  
`[imagen omitida: wiki id 56367]`  
  
After this request, you will receive an email with the code you will use in the SECOND POST.

**SECOND POST  
  
client\_id:** Client ID of the application, required.  
**client\_secret:** Client Secret of the application, required.  
**grant\_type=password:** It is required.  
**scope**: Scope of the user account you want to access. It's only required when "&GAMApplication.ClientAuthenticationRequestMustIncludeUserScopes" is True.  
**password:** OTP Code requested in the FIRST POST, required.  
**username:**Username of the user with 2FA enabled, required.  
**authentication\_type\_name:** Name of the authentication type with 2FA configured at the server, required.  
**use\_2fa=true:**It is required.  
**otp\_step=2:** It is required.  
  
**POSTMAN Example:**  
  
`[imagen omitida: wiki id 56366]`  
  
2. User Info

**The Endpoint is:** https://<domain>/<virtual\_directory>/**oauth/gam/v2.0/userinfo**

**GET**

**Headers**

**Content-Type:** Type of content that will be returned. Use application/x-www-form-urlencoded, required.  
**Authorization:** *access\_token* obtained in the SECOND POST, required.  
  
`[imagen omitida: wiki id 56356]`  
  
**Response:**

```
{
    "guid": "4c921af0-6805-4f51-9cfe-4d6cd6821e05",
    "username": "juan",
    "email": "jperez@genexus.com",
    "verified_email": true,
    "first_name": "Juan",
    "last_name": "Perez",
    "external_id": "",
    "gender": "M",
    "url_image": "",
    "url_profile": "",
    "phone": "099 888 888",
    "address": "",
    "city": "",
    "state": "",
    "post_code": "",
    "language": "",
    "timezone": "",
}
```

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [GAM - Two factor Authentication for mobile](https://wiki.genexus.com/commwiki/wiki?50726) |
| [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
