---
title: "OAuth Module"
source_id: 50438
source_url: https://wiki.genexus.com/commwiki/wiki?50438
genexus_version: "18"
---

# OAuth Module

The OAuth [module](https://wiki.genexus.com/commwiki/wiki?22414) is distributed as part of the [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) to let you work with the OAuth protocol. This first version of the module is based on the Authorization Code flow.

There are two steps to be carried out by different roles:

* **Step 1:** [Initial configuration and data collection by an administrator](https://wiki.genexus.com/commwiki/wiki?50408)
* **Step 2:** With the data given by the administrator, you (developer) can work with the OAuth module.

As a developer, you must ask the administrator for three pieces of information (client ID, client secret, and refresh token) to pass them as parameters to the module in order to receive a valid access token.

As shown in the Sample section below, these parameters must be passed specifically to the RefreshToken method. This method executes the API call to refresh the access token.

The RefreshToken Procedure [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) contains the following parameters:

1. (in) OAuthAuthorizationConfig: SDT
2. (in) RefreshToken: String
3. (out) OAuthAccessToken: Oauth20AccessTokenSDT
4. (out) DateTimeTokenExpire: Datetime
5. (out) OutMessages: Messages
6. (out) Success: Boolean

1. The OAuthAuthorizationConfig SDT structure is as follows:

`[imagen omitida: wiki id 50449]`

where the first member refers to the Identity Provider (IdP); for example, Google, Microsoft, GAM. To fill this field, an [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) named "AccessTokenProvider" is offered within the module containing some of the most common IdPs.

The second and third members must be filled with the client ID and client secret data given by the administrator.

2. The RefreshToken parameter must be the refresh token given by the administrator.

3. The OAuthAccessToken SDT will be returned containing the access token requested. The following image shows its structure:

`[imagen omitida: wiki id 50450]`

4. The DateTimeTokenExpire parameter will be returned containing the date and time the received access token expires.

5. The OutMessages parameter will return an empty string if the Success parameter is true. On the other hand, it will contain a description of the issue.

6. The out Success parameter will inform whether the request was successful or not.

### [Sample](#Sample)

```
&OAuthAuthorizationConfig.AccessTokenUrl  = OAuth.v2.AccessTokenProvider.Google  //https://oauth2.googleapis.com/token
&OAuthAuthorizationConfig.ClientId        = "ClientId"
&OAuthAuthorizationConfig.ClientSecret    = "SecretKey" //If the server is microsoft, this is not necessary - &OAuthAuthorizationConfig.ClientSecret = """

&Success = OAuth.v2.RefreshToken(&OAuthAuthorizationConfig, &RefreshToken, &OAuthAccessToken, &DateTimeTokenExpire, &Messages)

if (&Success)
    &AccessTokenString = &OAuthAccessToken.access_token
else
    Log.Error(&Messages)
endif
```

How does the above relate to sending Messages using Oauth?

```
&OAuthAuthorizationConfig.AccessTokenUrl  = OAuth.v2.AccessTokenProvider.Google  //https://oauth2.googleapis.com/token
&OAuthAuthorizationConfig.ClientId        = "ClientId"
&OAuthAuthorizationConfig.ClientSecret    = "SecretKey" //If the server is microsoft, this is not necessary - &OAuthAuthorizationConfig.ClientSecret    = """
```

```
for each User
   where UserID = &UserId
   
   &OAuthAccessToken.FromJSON(UserAccessToken)  //This is optional. For Token reuse
   &Success = OAuth.v2.RefreshToken(&OAuthAuthorizationConfig, &RefreshToken, &OAuthAccessToken, &DateTimeTokenExpire, &Messages)

   if (NOT &Success)
      Log.Error(&Messages)
      return
   endif
   
   UpdateAccessToken(UserId, &OAuthAccessToken)   //This is optional. For Token reuse

   &AccessTokenString = &OAuthAccessToken.access_token
   &SMTPSession.Host = 'smtp.gmail.com' 
   &SMTPSession.Port = 465 
   &SMTPSession.Timeout = 20 
   &SMTPSession.Secure = 1 
   &SMTPSession.Authentication = 1
   &SMTPSession.UserName = 'Info@gmail.com'
   &SMTPSession.Password = &AccessTokenString
   &SMTPSession.AuthenticationMethod = "XOAUTH2"  
   &SMTPSession.Login()

   &MailMessage.Subject="Email Subject XXX"    //&MailMessage is based on the MailMessage Data Type
   &MailMessage.Text="Message body" 
   &MailRecipient.Address = "xxx@gmail.com"   //&MailRecipient is based on the MailRecipient Data Type
   &MailRecipient.Name = "xxx"    
   &MailMessage.To.Add(&MailRecipient)
   
   &SMTPSession.Send(&MailMessage)
endfor
```

**Note**: The [AuthenticationMethod property](https://wiki.genexus.com/commwiki/wiki?50349) can be used since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,) and is required when using OAuth2. However, this property only works if the correct email libraries are active. By default, GeneXus uses older libraries that do not support OAuth2. To enable support:

1. Create a file named **config.gx** in the root of the Knowledge Base.  
2. Add the following lines:

```
SMTPSession=MailKit
OpenPOP=MailKit
```

This activates modern libraries that support OAuth2 authentication:

For .NET, use MailKit  
For Java, use JakartaMail

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,).

### [See Also](#See+Also)

[SAC #50932: Soporte de OAUTH para envío y recepción de emails en cuentas de Google y Office 365](https://www.genexus.com/es/developers/websac?data=50932;;)  
[Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227)  
[Microsoft Exchange OAuth 2.0 for emails: Generation and data collection from the Administrator](https://wiki.genexus.com/commwiki/wiki?50396)  
[Google OAuth 2.0 process for emails: Generation and data collection by the Administrator](https://wiki.genexus.com/commwiki/wiki?50408)


|  |
| --- |
| **Backlinks** |
| [Google OAuth 2.0 process for emails: Generation and data collection by the Administrator](https://wiki.genexus.com/commwiki/wiki?50408) |
| [Microsoft Exchange OAuth 2.0 for emails: Generation and data collection from the Administrator](https://wiki.genexus.com/commwiki/wiki?50396) | [Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227) |

---
