---
title: "GAM - Local Authentication Type"
source_id: 20703
source_url: https://wiki.genexus.com/commwiki/wiki?20703
genexus_version: "18"
---

# GAM - Local Authentication Type

In Local Authentication Type user credentials are stored in the "User" [GAM](https://wiki.genexus.com/commwiki/wiki?24746) table.

GAM does not store the password of the user, but it stores a [hash](http://en.wikipedia.org/wiki/Hash_function) of it. A hash is an algorithm such that given a string, produces always the same resulting string, and given the resulting string you cannot get the original.

The hash is obtained from a unique key for each user and an algorithm named SHA-512 (Secure Hash Algorithm).

This means that when you retrieve GAM Users from the repository, the password property will always have an empty value.


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) |
| [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - Two Factor Authentication (2FA)](https://wiki.genexus.com/commwiki/wiki?48254) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) |
| [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
