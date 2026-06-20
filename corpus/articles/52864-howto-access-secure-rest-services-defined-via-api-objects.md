---
title: "HowTo: Access secure REST services defined via API Objects"
source_id: 52864
source_url: https://wiki.genexus.com/commwiki/wiki?52864
genexus_version: "18"
---

# HowTo: Access secure REST services defined via API Objects

When you have defined an [API object](https://wiki.genexus.com/commwiki/wiki?46151) with a [security scheme](https://wiki.genexus.com/commwiki/wiki?52550) and this scheme has already been configured, it is possible to connect to the service in different ways.

Suppose that an API object has been defined with a security scheme, as shown in the article [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840).

In addition, the configuration process has been performed in the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Backend, as shown in the article [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854).

Then, you have a Client Id and Client Secret information. You can connect to the server through one of the following three ways:

1. Using the [Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315).
2. Using YAML via Postman.
3. Using the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

### [1. Using the LaunchPad Tool Window](#1.+Using+the+LaunchPad+Tool+Window)

To prototype using the [Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315), follow the steps below:

**1.** Press F5 to generate the Launchpad Tool Window. Select the APIS Tab and click on Authorize:

`[imagen omitida: wiki id 52553]`

**2.** A pop-up screen like the one below will open. In that window, you have to:

1. Add the same username and password you used to log in to the GAM Backend.
2. Select the "Request body" value in the combo box titled "Client credentials location."
3. Paste in the "Client\_id" and "client\_secret" fields the data you saved in step 2 of figure 2 in [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854).
4. Click on the link "Select all" offered in the "Scopes" section.

`[imagen omitida: wiki id 52554]`

**3.** Finally, you will be able to enter the CustomerId, AccountId, and the AccountPasword to view the customer's account information in the Launchpad:

`[imagen omitida: wiki id 52555]`

If you try to get the information of a certain customer, but you have not previously performed the authentication or authorization process, you will get a 401 error with the following message:

```
{
  "error": {
    "code": "0",
    "message": "This service needs an Authorization Header"
  }
}
```

### [2. Using YAML via Postman](#2.+Using+YAML+via+Postman)

**1.** In the API object, set the [REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254) = True and the [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) = Yes.

**2.** Next, run the API object by right-clicking on it. By doing this, GeneXus understands that it must generate the YAML file with the security information.

**3.** Then, you can follow the steps listed in the following articles:

* [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)
* [HowTo: Use Postman to access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?50055)

### [3. Using the HttpClient data type](#3.+Using+the+HttpClient+data+type)

With GeneXus, you can consume any REST service (generated with GeneXus or not) with a security scheme. In this case, you can use the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

As in the previous case, you can configure the necessary properties and obtain a YAML file with the security information. Then you can use the [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) to import the generated YAML file to a different KB. Consuming a REST Service is also possible by following the steps described in the article [Consuming a Rest Service with GeneXus](https://wiki.genexus.com/commwiki/wiki?44405,,).

In any case, it is necessary to create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) and add the mandatory *Authorization* header. Use the [GetAgentServiceHeader method of GAM object](https://wiki.genexus.com/commwiki/wiki?43221) to get the correct one for your use case. You could also do the calling manually, using the [Access\_token GAM Service](https://wiki.genexus.com/commwiki/wiki?45320). So, include in the Procedure source:

```
&httpclient.AddHeader('Authorization', &access_token)
```

When you have the token information, you can follow the steps shown in the article [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918).

**Note**:  It is possible to specify an expiration time for the token. Read more in [OAuth token expire (minutes)](https://wiki.genexus.com/commwiki/wiki?18577).

### [See Also](#See+Also)

[API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550)


|  |
| --- |
| **Backlinks** |
| [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [Toc:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854) |
| [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) |

---
