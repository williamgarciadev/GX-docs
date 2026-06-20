---
title: "Microsoft Exchange OAuth 2.0 for emails: Generation and data collection from the Administrator"
source_id: 50396
source_url: https://wiki.genexus.com/commwiki/wiki?50396
genexus_version: "18"
---

# Microsoft Exchange OAuth 2.0 for emails: Generation and data collection from the Administrator

In this article, you will find the necessary steps to provide data to connect to the mailbox through [Microsoft Exchange OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.lightning_sync_admin_security_connection_oauth.htm&type=5).

Example: Application administrators have to provide the necessary data to the programmers (at their request) so that they can connect to their mailbox.

## [Steps](#Steps)

You need to follow these 3 steps to provide data through Microsoft Exchange OAuth:

1. [OAuth Application Registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application)
2. [Authentication Code Generation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application)
3. [Refresh Token Generation](https://wiki.genexus.com/commwiki/wiki?50396)

### [**1. OAuth Application Registration**](#1.+OAuth+Application+Registration)

A) Follow this tutorial from Microsoft: [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application). Execute all steps of the "Register an application" section (8 steps in total).

B) Now you have to configure the platform settings. To do so, follow these steps: [Configure platforms settings](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#configure-platform-settings) (4 steps in total).

C) In step 4, select "Mobile and desktop Applications" as Platform and continue.

D) A new window called Configure Desktop + devices is opened.

Select the Redirect URI: https://login.microsoftonline.com/common/oauth2/nativeclient and confirm.

### 

### [**2. Authentication Code Generation**](#2.+Authentication+Code+Generation)

After registering the application, you can start the code authorization request process.

A) Get the Application (client) ID of the newly created Application:

`[imagen omitida: wiki id 50405]`

You can find it by clicking on the **overview** window, below "Display Name."

B) Open a browser and execute the following URL. The "Client\_id" data must be replaced by that of the newly created Application:

```
https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?
client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
&response_type=code
&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient
&response_mode=form_post
&scope=offline_access%20https%3A%2F%2Foutlook.office.com%2FSMTP.Send%20https%3A%2F%2Foutlook.office.com%2FPOP.AccessAsUser.All
&state=12345
```

C) Log in with your Microsoft account and accept the following permissions:

`[imagen omitida: wiki id 50407]`

D) After accepting, the browser will be redirected to the **Redirect URI** (https://login.microsoftonline.com/common/oauth2/nativeclient). You will see a blank screen.

E) After you are redirected to that blank screen, open the browser **DeveloperTools** (F12 in Chrome).

F) Go to **Network Tab** and refresh the page.

G) Once in the **Network Tab**, select the Request and copy the "code" of the Request.

`[imagen omitida: wiki id 53797]`

### 

### [**3. Refresh Token Generation**](#3.+Refresh+Token+Generation)

Read more about this topic in this article: [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438).

To generate the Refresh Token in Windows you must execute a POST to

*https://login.microsoftonline.com/**{tenant}**/oauth2/v2.0/token*

The ***tenant*** can be obtained by following the steps detailed in [How to find your Azure Active Directory tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant).

In addition, you should keep in mind the following:

* Body Content-Type: *x-www-form-urlencoded*
* Post Parameters (Body)
  + client\_id: Application (client) ID.
  + scope: Same scope as in step 2 (must not be URL-encoded, and the "offline\_access" scope does not need to be added as it is inferred from the authorization code request).
  + code: Authorization Code obtained from the previous step.
  + grant\_type: *"authorization\_code".*

#### [Sample](#Sample)

```
curl --location --request POST "https://login.microsoftonline.com/5ec7bbf9-1872-46c9-b201-a1e181996b35/oauth2/v2.0/token" ^
--header "Content-Type: application/x-www-form-urlencoded" ^
--data-urlencode "scope=https://outlook.office.com/SMTP.Send https://outlook.office.com/POP.AccessAsUser.All" ^
--data-urlencode "code=0.xxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" ^
--data-urlencode "client_id=xxxxx-xxxxx-xxxxx-xxxxx-xxxxxxx" ^
--data-urlencode "grant_type=authorization_code" ^
--data-urlencode "redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient"
```

The response obtained after executing the above request is as follows:

`[imagen omitida: wiki id 53350]`

Finally, you will need to save the ClientId and the RefreshToken.

### [**4. Enable STMP AUTH in Azure Portal for Selected Mailboxes**](#4.+Enable+STMP+AUTH+in+Azure+Portal+for+Selected+Mailboxes)

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission#enable-smtp-auth-for-specific-mailboxes

This step is required. If not enable AUTH, the following error would ocurr:

> System.Net.Mail.SmtpException: The SMTP server requires a secure connection or the client was not authenticated. The server response was: 5.7.57 Client not authenticated to send mail. Error: 535 5.7.139 Authentication unsuccessful, SmtpClientAuthentication is disabled for the Tenant. Visit **<https://aka.ms/smtp_auth_disabled> for more information. [[CP6P284CA0086.BRAP284.PROD.OUTLOOK.COM](http://cp6p284ca0086.brap284.prod.outlook.com/)](<a href="http://cp6p284ca0086.brap284.prod.outlook.com/">CP6P284CA0086.BRAP284.PROD.OUTLOOK.COM</a>)**  
>    at System.Net.Mail.MailCommand.CheckResponse(SmtpStatusCode statusCode, String response)

### [See also](#See+also+)

[Google OAuth 2.0 process for Mails](https://wiki.genexus.com/commwiki/wiki?50408)


|  |
| --- |
| **Backlinks** |
| [Google OAuth 2.0 process for emails: Generation and data collection by the Administrator](https://wiki.genexus.com/commwiki/wiki?50408) | [Microsoft Exchange OAuth 2.0 for emails: Generation and data collection from the Administrator](https://wiki.genexus.com/commwiki/wiki?50396) | [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) |

---
