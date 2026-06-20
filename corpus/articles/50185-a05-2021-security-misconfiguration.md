---
title: "A05:2021 - Security misconfiguration"
source_id: 50185
source_url: https://wiki.genexus.com/commwiki/wiki?50185
genexus_version: "18"
---

# A05:2021 - Security misconfiguration

This article describes inappropriate configurations that can impact the security of an application. Below you can find guidance on how to solve them.

Read more at: [Security Misconfiguration - OWASP Documentation](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus does not take any actions in the production environment.

#### [Actions by Developers](#Actions+by+Developers)

* Some GeneXus properties can disable controls. Inspect the property values manually before deploying.
* Set the [Javascript Debug Mode](https://wiki.genexus.com/commwiki/wiki?17384) property to No.

  + Security Scanner helps to detect this scenario with case code #106.
* Keep the server software up to date.
* Avoid installing unnecessary functionalities on the server.
* Set permissions properly over the application web directories. Check permissions given for the application Temp directories (see [Temp media directory](https://wiki.genexus.com/commwiki/wiki?7628) and [Blob local storage directory](https://wiki.genexus.com/commwiki/wiki?6979) properties).
* Set permissions appropriately for the database user at the minimum needed.
* Application server and framework hardening are recommended. Some secure deployment configurations can be found in: [Configuration for secure deployment using GAM](https://wiki.genexus.com/commwiki/wiki?47243).
* Change the default cipher keys. Random key generation is advised.
* Use different cipher keys for each application.
* Must not have any development/test credentials over the production environment.
* Security Scanner - Detections:

  + Communication: Check Http Protocol (#105), checking for variables of HttpResponse type (#109).

### [XML External Entities (XXE)](#XML+External+Entities+%28XXE%29)

[XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus does not execute External Entities by default on Web Services.
* If the [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) is used, it does not execute External Entities by default. Nevertheless, when using a GeneXus version prior to Evolution 2 Upgrade 5 and using the Java generator, [the value is 1 (true) by default and needs to be manually changed](https://www.genexus.com/es/developers/websac?data=35388%3b%3b).

#### [Actions by Developers](#Actions+by+Developers)

* Check if the XMLReader [ReadExternalEntities Property](https://wiki.genexus.com/commwiki/wiki?6967) is configured to 1 or True.

Security Scanner helps to detect this scenario with case code #133.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
