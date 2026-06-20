---
title: "HowTo: Sign out from mobile applications using GAM"
source_id: 60753
source_url: https://wiki.genexus.com/commwiki/wiki?60753
genexus_version: "18"
---

# HowTo: Sign out from mobile applications using GAM

This article describes the [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) endpoint used to sign out from mobile applications.

It is a REST service that invalidates (kills) the access\_token obtained at sign-in.

### [Endpoint](#Endpoint)

**Method: POST**  
The endpoint is: https://<domain>/<virtual\_directory>**/oauth/logout**

**Headers**

* **Content-Type:** Type of content that will be returned. Use application/x-www-form-urlencoded.
* **Authorization:**<access\_token>; it is required to send the access\_token obtained during sign-in.

### [Sample](#Sample)

```
&httpclient = new()
&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddHeader("Authorization",<access_token>)
```

### [Response](#Response)

A successful logout returns the following response:

```
{
  "code": "200"
}
```

If the endpoint execution is successful, it will return "code": "200", indicating that the logout operation was completed successfully.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
