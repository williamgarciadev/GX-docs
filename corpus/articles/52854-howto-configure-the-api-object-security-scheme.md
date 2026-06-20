---
title: "HowTo: Configure the API object security scheme"
source_id: 52854
source_url: https://wiki.genexus.com/commwiki/wiki?52854
genexus_version: "18"
---

# HowTo: Configure the API object security scheme

API object security is based on the [OAuth 2.0 protocol](datatracker.ietf.org/doc/html/rfc6749). So, when an API object with a security scheme has been defined, it is necessary to make some configurations in the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935).

Suppose you have an [API object in which a security scheme has been defined](https://wiki.genexus.com/commwiki/wiki?52840). Then, you must follow the steps described below.

### [Step 1](#Step+1)

Select **Build > Run GAM Backend**in the GeneXus Toolbar. This will direct you to a tab in your browser where you should add the following information:

User: admin  
Password: admin123

When you click on "SIGN IN", you will be directed to Applications to select the KB. In this case, it is KBAPIObjectSecurityScheme:

`[imagen omitida: wiki id 52551]`

### [Step 2](#Step+2)

Click on "EDIT," and in Configuration, follow the steps below:

1. Enable "Allow authentication v.2.0?" and "Can get user roles?".
2. Copy Client ID and Client secret.
3. Click on Confirm.

`[imagen omitida: wiki id 52552]`

To be able to connect to that server from anywhere, you will have to add the Client ID and Client secret data, so you will have to copy that data into memory.

### [See Also](#See+Also)

[API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550)  
[HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864)


|  |
| --- |
| **Backlinks** |
| [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [Toc:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) |
| [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) | [SecurityPermission annotation](https://wiki.genexus.com/commwiki/wiki?55422) |

---
