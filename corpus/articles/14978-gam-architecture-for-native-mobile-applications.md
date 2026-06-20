---
title: "GAM architecture for Native Mobile applications"
source_id: 14978
source_url: https://wiki.genexus.com/commwiki/wiki?14978
genexus_version: "18"
---

# GAM architecture for Native Mobile applications

The architecture of a Native Mobile application consists basically of a "client application" which is installed on the device and a "server application" (implemented using [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) which solve the business logic of the application). See [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) for details.

### [Secure Access with GAM and OAuth](#Secure+Access+with+GAM+and+OAuth)

The architecture, as it is, allows any HTTP client to access the REST services hosted in the application server.

As a consequence, in many cases (depending on the security needed) it's important to consider that [REST Web Services](https://wiki.genexus.com/commwiki/wiki?28213) should only be accessible from the devices, not from other HTTP clients (at least for POST, PUT, DELETE actions).

[GAM](https://wiki.genexus.com/commwiki/wiki?14960) solves this security problem, it implements a security mechanism based on OAuth which allows only authenticated and authorized users to access the resources exposed as REST services in the application server.

`[imagen omitida: wiki id 18966]`

### [Integration and Token Management](#Integration+and+Token+Management)

The following explains what happens after activating integrated security to the application ([Enable Integrated Security Property](https://wiki.genexus.com/commwiki/wiki?14706)).

After the user performs the login on the application, the device sends a token to the OAuth server stored in the same server where [GAM](https://wiki.genexus.com/commwiki/wiki?14960) is located.  
The user name and password entered by the user are validated to then return an Access Token (a value that is generated for each entry) that can either remain unchanged while the user is connected or be reset regularly depending on the value of the [Oauth token expire](https://wiki.genexus.com/commwiki/wiki?18577) property (available as an option of the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935), so the administrator user may set this property according to the [GAM Security Policies](https://wiki.genexus.com/commwiki/wiki?18521)).

`[imagen omitida: wiki id 50942]`

Following its admission, the Dashboard (or entry point of the application) is opened, and the AccessToken is validated for every REST Web Service request. This occurs permanently throughout the whole session.

### [See Also](#See+Also)

[Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052)  
[Online Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?14981)


|  |
| --- |
| **Backlinks** |
| [GAM - Native Mobile Authentication](https://wiki.genexus.com/commwiki/wiki?15222) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
