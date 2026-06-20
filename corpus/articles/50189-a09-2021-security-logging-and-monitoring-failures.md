---
title: "A09:2021 - Security logging and monitoring failures"
source_id: 50189
source_url: https://wiki.genexus.com/commwiki/wiki?50189
genexus_version: "18"
---

# A09:2021 - Security logging and monitoring failures

This document provides security information to protect your applications against attacks that can result from insufficient system and application logging and monitoring.

[Security Logging and Monitoring Failures - OWASP Documentation](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus provides the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) module that by default logs the Login, Password Change, and Password Recovery events.

#### [Actions by Developers](#Actions+by+Developers)

* If [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) is not used, a customized access control module and the corresponding logging actions must be developed. The following events should be logged:

  + Login
  + Password change
  + Password recovery
  + User is authorized
  + User is not authorized
  + Create/Update/Delete users.
  + Create/Update/Delete roles and permissions.
* If GAM is used, the first three items of the previous list are covered by default

  + See the following [document](https://wiki.genexus.com/commwiki/wiki?32698) to learn how to solve the other points with GAM.
* In any case, high-impact Transactions need to be identified and logged as they are business-specific and GeneXus cannot perform these actions automatically.
* Must establish a monitoring process and effective alerts to act in an acceptable time window. Also, a response plan like [NIST 800-61 rev. 2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) or later.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
