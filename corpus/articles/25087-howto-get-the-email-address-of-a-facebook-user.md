---
title: "HowTo: Get the email address of a Facebook user"
source_id: 25087
source_url: https://wiki.genexus.com/commwiki/wiki?25087
genexus_version: "18"
---

# HowTo: Get the email address of a Facebook user

When the [GAM Facebook Authentication](https://wiki.genexus.com/commwiki/wiki?29007) is used, you can retrieve the user's email when they register. That is, when they log into the application for the first time using their Facebook account.

To get the user's email when they log in using Facebook Authentication Type, you just need to add the "email" in the [Additional Scope](https://wiki.genexus.com/commwiki/wiki?21584,,) to the Authentication Type configuration, as shown below:

`[imagen omitida: wiki id 54619]`

When using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535), the code is as follows:

```
&AuthenticationTypeFacebook.Facebook.AdditionalScope= "email"
```

**Where:**

*&AuthenticationTypeFacebook*  
      Is a variable based on GAMAuthenticationTypeFacebook external object - distributed by [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

Then, the user's email in GAM will be the same email that is configured in the Facebook account.

**Note**: Once the user has logged in for the first time, the email address won't be updated or changed when logging in again.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
