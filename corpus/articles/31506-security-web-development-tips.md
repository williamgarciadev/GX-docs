---
title: "Security Web Development tips"
source_id: 31506
source_url: https://wiki.genexus.com/commwiki/wiki?31506
genexus_version: "18"
---

# Security Web Development tips

There are some tips and things to consider, regarding security, when developing a web application.  
In this document, we gather some of them.

## [Overview](#Overview)

There are three types of actions that can be made to handle a security risk in a GeneXus application. In most cases, the three of them play an important role in the development and distribution of a secure web application.

* #### [Actions handled by GeneXus](#Actions+handled+by+GeneXus)

These are actions automatically handled by GeneXus at generation time. Some examples are as follows: GeneXus generates parameterized SQL sentences to avoid SQL injection. Also, it generates automatic security checks for each HTTP Post to detect whether read-only data has been changed.

* #### [Things to be considered by the GeneXus user](#Things+to+be+considered+by+the+GeneXus+user)

User actions when programming in GeneXus. These actions should be taken into account by the GeneXus developer when performing development tasks.

* #### [User actions outside GeneXus](#User+actions+outside+GeneXus)

These actions are the responsibility of the people in charge of infrastructure (for example, server configuration).

## [Rationale](#Rationale)

Although GeneXus handles many actions automatically, the developer has to consider some aspects regarding security, and they both have to be combined to obtain a web application where no security fails can be found.

First of all, you must read [Managing OWASP 2013 Top 10 Security Risks in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?21889,,), [Managing OWASP Top 10 2017 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?39915,,)

### [Protecting sensitive data used client side](#Protecting+sensitive+data+used+client+side)

Sometimes, sensitive data (such as credit cards, user IDs, etc) need to be exposed because they are used to perform some actions on the client-side.  
Here we focus on the scenario where this data is not expected to be entered or modified by the user. If it is, other security mechanisms should be considered, such as having a login process and using secure channel communication.

The data that is transmitted from the client to the server should always be validated server-side.  
The [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) is only used for masking the parameters, and should not be used as the basis of security features.

Besides, the validation of data input is not enough if it's done client side. Client side validations are for the purpose of making a more usable UI.

There are three types of data:

1. Data that can be modified by the client. This scenario is out of the scope of this section.
2. Data that should be shown to the client, but cannot be modified.  
     
   For example, in a funds transfer, the sender's account is shown to the user, so he can select from a combo box the account from where to make the transfer. However, the information should be checked server side again, to verify that the account belongs to the user who is logged in. The GeneXus user is responsible for performing this check.
3. Data that should neither be visible nor modifiable by the client.   
     
   For example, when transferring data that is needed to perform an action, but that the user shouldn't be allowed to access, even for reading. This kind of data must not be included in the form. The [Visible property](https://wiki.genexus.com/commwiki/wiki?8849) is a UI property and should not be used for security purposes. It should only be used in the user interface. Even though the data is included in the form and hidden, it is persisted in the HTML, so it's accessible.  
     
   This data shouldn't be retrieved in user events of the web panel. Nevertheless, related security improvements have been done in [GeneXus X Evolution 3 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?33413,,) and [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,) ([SAC #40775](https://www.genexus.com/developers/websac?en,,,40775")). Procedures or data providers accessing it should be used instead.

Let's call the issues 2 and 3 "read-only sensitive data issues".

### [Some tips on the read-only sensitive data](#Some+tips+on+the+read-only+sensitive+data)

1. When the data is part of the parameters of the web panel, consider using the IN operator in the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862).

The IN operator prevents the developer from changing the parameters by code. Besides, in runtime, the IN parameters cannot be changed in transit, otherwise, if someone tries to do it, an **HTTP 403 error** is thrown. This is valid for data which is displayed on the screen or not.

Notes:  
For Smooth [Web User Experience](https://wiki.genexus.com/commwiki/wiki?22449) this is available as since GeneXus 15.  
In the case of GeneXus Evolution 3 and Previous Versions Compatible Web User Experience see [SAC #39716](https://www.genexus.com/developers/websac?en,,,39716;;).

2. Regarding read-only data on the screen which is not modifiable, GeneXus adds automatic security checks in Web Transactions and Web Panels (including Web Components and Master Pages), which prevent read-only sensitive data from being changed. If it is changed, the POST is canceled and throws an HTTP 403 error.  
In Web transactions, the condition for an attribute to be considered as read-only sensitive data is to have:

* An unconditional [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) for this attribute or
* A [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) conditioned to the mode (the mode is received as a parameter)
* The transaction's key must not be included in the form.

If the web transaction adds a noaccept rule and the attribute is enabled in any event, the following spec message could be thrown, warning that an HTTP 403 error may be thrown at runtime: **spc0204** : ''Enabled'' property assignment over attribute %1%2 conflicts with ''%3'' rule.'

In Web Panels, any variable which participates in a rule like the following:  noaccept(&var) is checked to not change in runtime. The same happens to read-only controls (controls which have [ReadOnly property](https://wiki.genexus.com/commwiki/wiki?8826) = Yes at design-time).

For these security checks, we use a session key that is the same as the one taken from the [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) when it's set to Session Key value.

### [See Also](#See+Also)

[Security considerations in Smooth models](https://wiki.genexus.com/commwiki/wiki?25356)  
[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746)  
Troubleshooting: [SAC 41179](https://www.genexus.com/developers/websac?en,,,41179;;)


|  |
| --- |
| **Backlinks** |
| [Security considerations in Smooth models](https://wiki.genexus.com/commwiki/wiki?25356) |
| [What is error 403?](https://wiki.genexus.com/commwiki/wiki?45483) |

---
