---
title: "Special considerations for SMTPSession or Pop3Session with Google Accounts"
source_id: 50227
source_url: https://wiki.genexus.com/commwiki/wiki?50227
genexus_version: "18"
---

# Special considerations for SMTPSession or Pop3Session with Google Accounts

This article describes some specific considerations you need to take into account when sending or receiving emails using a Google Account (Gmail, Google for Business, or any edition).

## [Authentication and Authorization](#Authentication+and+Authorization)

As of May 30th, 2022, Google will no longer provide access to less secure apps ([here](https://support.google.com/accounts/answer/6010255) is the announcement). That is to say, you cannot authenticate by just assigning in the [Username](https://wiki.genexus.com/commwiki/wiki?7001) and [Password](https://wiki.genexus.com/commwiki/wiki?6994) properties of the [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937) or [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966) the email and password of the Google Account.

One solution is to use, instead of the Google Account password, an [Application Specific Password](https://support.google.com/accounts/answer/185833).

### [Using application-specific Password](#Using+application-specific+Password)

App Passwords can only be used with accounts that have [2-Step Verification](https://support.google.com/accounts/answer/185839) turned on.

Sample code snippet setting properties to create a Pop3 session:

```
&Pop3Session.Host = 'pop.gmail.com'
&Pop3Session.Port = 995
&Pop3Session.Timeout = 30
&Pop3Session.UserName = 'myemail@gmail.com'
&Pop3Session.Password = 'abcdabcdabcdabcd' // 16-digit App password given by Google
&Pop3Session.Secure=1
```

Steps to get an App Password:

1. [Turn on 2-Step Verification](https://support.google.com/accounts/answer/185839) in the Google Account
2. [Create an app password](https://support.google.com/mail/answer/185833)
3. Use that password in the application (assigning it to the corresponding [Password property](https://wiki.genexus.com/commwiki/wiki?6994)).

**Note**: The above is valid for all versions of GeneXus.

### [Using OAuth2](#Using+OAuth2)

OAuth2 is the recommended authentication method by Google and is supported in GeneXus since version [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,). To use OAuth2, you must use the [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) and perform additional steps.

To send and receive emails with OAuth2, the latest email libraries must be used:

* In .NET, this means using MailKit.
* In Java, this means using JakartaMail.

These libraries are not enabled by default. You need to manually configure your Knowledge Base to activate them, as explained in [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438).

### [See Also](#See+Also)

[SAC 50932 - OAUTH support for sending and receiving mails](https://www.genexus.com/developers/websac?,,,50932)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)


|  |
| --- |
| **Backlinks** |
| [Google OAuth 2.0 process for emails: Generation and data collection by the Administrator](https://wiki.genexus.com/commwiki/wiki?50408) | [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
