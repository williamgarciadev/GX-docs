---
title: "HowTo: Use GAM as an OAuth 2.0 provider"
source_id: 45493
source_url: https://wiki.genexus.com/commwiki/wiki?45493
genexus_version: "18"
---

# HowTo: Use GAM as an OAuth 2.0 provider

This document explains how to use GAM as an Identity Provider (IDP), using the OAuth 2.0 Authentication Type, for the cases when this solution has to be implemented.

Generally speaking, you need to define a [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) in the server, and configure the [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) in the clients in order to use GAM as an OAuth 2.0 provider from GeneXus KBs using GAM.

However, another possibility is to use [OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) in the clients.

The recommendation is to use GAM Remote authentication type, as its configuration should be much easier and there are some features that will not be covered when using the other solution. However, by using OAuth 2.0 you have the possibility to configure a different URL to get the user information, or the access token, that is not possible if you use GAM Remote.

### [Step 1](#Step+1)

Define the GAM Application in the server. Get the client ID and Client secret credentials. This step is the same as what is explained in [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038).

`[imagen omitida: wiki id 55556]`

Note that in this case, the properties "Can get user roles" and "Private Encryption Key" will be ignored. Do not check "Private Encryption Key" because there is no way to send the information encrypted from the client.

### [Step 2](#Step+2)

Define a OAuth 2.0 Authentication Type in the client, as shown in the following images:

**General**

`[imagen omitida: wiki id 55557]`

**Authorization**

Configure the URL http://<domain-url>/<base-url>/oauth/gam/signin?oauth=auth of the IDP.

`[imagen omitida: wiki id 55558]`

Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)

**Token**

Configure the URL http://<domain-url>/<base-url>/oauth/gam/access\_token service of the IDP.

Note the other configuration in the advanced configuration option.

`[imagen omitida: wiki id 55559]`

`[imagen omitida: wiki id 55560]`

**User Information**

Configure the URL http://<domain-url>/<base-url>/oauth/gam/userinfo service of the IDP.

`[imagen omitida: wiki id 55561]`

Note the other information required, in the advanced configuration section.

`[imagen omitida: wiki id 55562]`

**Note:**

In order to get additional information of the user from the IDP, see [HowTo: Get user's additional information from the GAM Identity Provider](https://wiki.genexus.com/commwiki/wiki?37703). In this case, you have to define the additional information as Custom User Attributes (as shown in the image above) so as the client application can receive it.

The received information will be saved as [extended attributes](https://wiki.genexus.com/commwiki/wiki?19634) of the user.

* The Attribute Name in the form above is the **Id** of the GAM extended user attribute, to be saved at the GAM database (you can retrieve the information by using that Id).
* The Attribute Tag is the service JSON response tag, that returns the user information. It's always "CustomInfo" when you use GAM as the OAuth 2.0 IDP.  
  See [Userinfo service response](https://wiki.genexus.com/commwiki/wiki?45316) to see the JSON response of the GAM service that returns the information of the user.


|  |
| --- |
| **Backlinks** |
| [GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) | [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603) | [GAM - OAuth User Scopes (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55820) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server](https://wiki.genexus.com/commwiki/wiki?55623) |

---
