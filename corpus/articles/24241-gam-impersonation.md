---
title: "GAM - Impersonation"
source_id: 24241
source_url: https://wiki.genexus.com/commwiki/wiki?24241
genexus_version: "18"
---

# GAM - Impersonation

When the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) allows end users to authenticate with different identity providers (for example using a web service and Twitter), by default they are mapped to different GAM Users.

Due to security concerns, users may authenticate using different mechanisms depending, for example, on whether they are accessing from an intranet. However, the login information has to be mapped to the same GAM logical User.

It is explained, in this article, what to do when a single GAM User is required, regardless of whether users enter the system using one [authentication type](https://wiki.genexus.com/commwiki/wiki?16508) or the other.

Impersonateallows the repository to have two different authentication mechanisms, but both converge on the same user. It is useful for cases in which it is not possible to use the same type of authentication from the intranet and the internet, for example, but you want the user to be the same. It is also used when you want to migrate from one type of authentication to another, the type of "impersonated" authentication is the one to which you are migrating in that case.

### [Scenarios](#Scenarios)

The following are some of the possible scenarios. There are others, like Facebook, Twitter, Google Authentication types impersonating another one.

#### [I. Impersonate External Authentication to Local Authentication](#I.+Impersonate+External+Authentication+to+Local+Authentication)

Consider a scenario where you need to have all the users defined as [local](https://wiki.genexus.com/commwiki/wiki?20703) GAM users in the GAM database, regardless of whether the login is local or external.

In other words, users should be able to authenticate using an external mechanism, such as a certificate, as well as one local to GAM (depending on the physical location of the user). In both cases, the login should map to the same GAM User.

A user who has logged into the application using an external mechanism shouldn't be defined as a different user in the GAM database. Instead, this user should impersonate the local user who has the same username (or email) in [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), if it exists. If a user logs in using external authentication, and it does not exist in GAM, it will be [registered](https://wiki.genexus.com/commwiki/wiki?19913,,) in GAM as a local user.

The article [Impersonate external authentication to local authentication](https://wiki.genexus.com/commwiki/wiki?24441,,) explains in more detail the scenario where any [External Authentication](https://wiki.genexus.com/commwiki/wiki?21755) impersonates to local authentication.

#### [II: Impersonate External Authentication to any other type of external authentication](#II%3A+Impersonate+External+Authentication+to+any+other+type+of+external+authentication)

Any combination of impersonation is supported. That is, any Authentication Type can impersonate any other (except the local authentication type, which can only be impersonated).

Suppose that the Custom Authentication Type defined in the Repository impersonates to [Twitter](https://wiki.genexus.com/commwiki/wiki?17208). This means that end users use their Twitter login to authenticate to [Custom external authentication](https://wiki.genexus.com/commwiki/wiki?21751), and after a successful login they are mapped to Twitter users in GAM.

### [Implementation Details](#Implementation+Details)

Suppose that you have X impersonate Y, where X and Y are authentication types. When a login is made using X, if the user exists with authentication type Y, that is taken. If not, it is searched whether the user exists associated with the X authentication type, and the authentication type is changed to Y. A new user is not created in this case.  
If the above is not fulfilled either (it does not exist with authentication type X and can be considered the same user), a new user is created (with authentication type Y). The criterion to know if a user can be considered to be the same differs according to the type of authentication.

#### [Criteria for mapping users](#Criteria+for+mapping+users)

Here, the criteria used is detailed:

#### [GAM Remote](#GAM+Remote)

For the case of [GAM Remote](https://wiki.genexus.com/commwiki/wiki?25355) with impersonating Y, it is mapped by user GUID, [external ID](https://wiki.genexus.com/commwiki/wiki?21734,,), and finally email. An exception is handled for the username that is the following:  
If you have a user with the username "A" in the [Identity Provider](https://wiki.genexus.com/commwiki/wiki?37038) (IDP), and the same username in the client. In addition, the GUID of the user is different in the GAM client and in the IDP, as well as the email that is different in both.  
In that case, you cannot map the users and consider them the same, even if you have the same username, so when the user tries to log in to the IDP "*The Username already exists. Error (GAM49)*" occurs.  
This implies that the administrator must decide if it is the same user or not configuring any of the elements that are used to consider them the same (External ID, email).

#### [Facebook, Twitter, Google, OAuth 2.0](#Facebook%2C+Twitter%2C+Google%2C+OAuth+2.0)

First, a user is searched for the type of Impersonated authentication with the same ExternalID as the returned one.  
If it does not exist, look for a user that has the same ExternalID in the original authentication type (it is used when you add Impersonate and migrate the users).  
In the third case, the type of Impersonated authentication is searched, a user that has the same Email.  
Finally, if it does not exist, a user with the same Email will be searched in the original authentication type after the login.

#### [OAuth 2.0 and SAML 2.0 with local impersonate peculiarities](#OAuth+2.0+and+SAML+2.0+with+local+impersonate+peculiarities)

To prevent the username from overwriting the local user, there is a difference in OAuth 2.0 behavior.

It can be done because in this case in the configuration it is decided whether or not to update the UserName field of the user.

If in the configuration of the [OAuth 2.0 Authentication](https://wiki.genexus.com/commwiki/wiki?39484) (Response) the field "User Name Tag" is not mapped, the following can happen:

* If you have impersonate to local, and the user exists, the UserName field is NOT overwritten
* If you have impersonate to local, and the user is new, the UserName field is loaded with the ExternalID

This only works for local impersonation. If you have Impersonate to a type other than local, and the user exists, the UserName field is loaded with the ExternalID.

This behavior solves another issue, which is that Facebook does not return a value in the user name field. If you have OAuth 2.0 Authentication (using Facebook) with Local impersonate, the user name can be the local user.

Otherwise, if the "User Name Tag" field is filled in the configuration of the OAuth 2.0 Authentication Type (Response), the UserName is always overwritten.

### [Characteristics of the providers](#Characteristics+of+the+providers)

#### [Facebook](#Facebook)

The username is a GUID, which the GAM matches with the ExternalId given by FB. This criterion is used because the email is not always returned to FB.  
The External ID in FB varies according to the Facebook Application (For two users to be the same, you must create a company in FB).

#### [Google](#Google)

The username in Google is the email.

**Notes:**

* Whenever a user logs in using a certain type of external authentication (such as [Facebook](https://wiki.genexus.com/commwiki/wiki?29007), GAM remote, OAuth 2.0, [Web services](https://wiki.genexus.com/commwiki/wiki?16512)), the external provider sends user information, which overwrites the user's existing data. These data (the basic ones) are username, email, external ID. That is, if you have a user with Authentication Type = Custom with a certain External ID, when you set up Custom impersonate Google, the user takes External ID from Google and loses the one it originally had. The same goes for the rest of the data.
* GAM Impersonate works for [Auto register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) also.


|  |
| --- |
| **Backlinks** |
| [GAM - Apple Authentication type](https://wiki.genexus.com/commwiki/wiki?44478) | [GAM - One Time Password (OTP)](https://wiki.genexus.com/commwiki/wiki?48197) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) |

---
