---
title: "A07:2021 - Identification and authentication failures"
source_id: 50187
source_url: https://wiki.genexus.com/commwiki/wiki?50187
genexus_version: "18"
---

# A07:2021 - Identification and authentication failures

This document focuses on showing the Identification and Authentication Failures that can create vulnerabilities in your application.

Confirmation of the user's identity, authentication, and session management is critical to protect against authentication-related attacks. Below you can find the most frequent ones according to OWASP and ways to prevent them.

Read more at: [Identification and Authentication Failures - OWASP Documentation](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)

### [Authentication](#Authentication)

[Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus provides a security module called [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746). This module implements different [Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) and [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508).

#### [Actions by Developers](#Actions+by+Developers)

* Use GAM or implement a security module.

### [Password strength controls](#Password+strength+controls)

[Implement proper password strength controls](https://www.owasp.org/index.php/Authentication_Cheat_Sheet#implement-proper-password-strength-controls)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GAM provides the developer with the tools to implement an adequate password control policy. Read more at: [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574)

#### [Actions by Developers](#Actions+by+Developers)

* Configure GAM or the external security module to implement the selected password control properly.

### [Password recovery mechanism](#Password+recovery+mechanism)

[Implement secure password recovery mechanism](https://www.owasp.org/index.php/Authentication_Cheat_Sheet#implement-secure-password-recovery-mechanism)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GAM provides the developer with an implementation for the [password recovery mechanism](https://wiki.genexus.com/commwiki/wiki?16923).

#### [Actions by Developers](#Actions+by+Developers)

* Adapt the GAM reference implementation to the company's security policy or properly configure the chosen security module. The use of the  [OWASP guidelines](https://www.owasp.org/index.php/Authentication_Cheat_Sheet#implement-secure-passwor-recovery-mechanism) is recommended.

### [Authentication and error messages](#Authentication+and+error+messages)

[Authentication and error messages](https://www.owasp.org/index.php/Authentication_Cheat_Sheet#authentication-and-error-messages)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GAM provides the developer with an implementation for the [password recovery mechanism](https://wiki.genexus.com/commwiki/wiki?16923) and [login](https://wiki.genexus.com/commwiki/wiki?19269).

#### [Actions by Developers](#Actions+by+Developers)

* Error messages must be generic and avoid providing an attacker with any user's information.

### [Session management](#Session+management)

[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus uses the session management mechanisms provided by the base language. Also, it provides cipher mechanisms to [Encrypt URL parameters](https://wiki.genexus.com/commwiki/wiki?8068) for the objects exposed, and implements cipher mechanisms for the AJAX queries and responses.
* The session with the AJAX authentication key expires on a configurable time-lapse.

#### [Actions by Developers](#Actions+by+Developers)

* Verify that all objects accessible by HTTP/HTTPS receive ciphered parameters.

  + Security Scanner helps to detect this scenario with case codes #100, #105 & #107.
* If GeneXus Evolution 1 is used, check the [Ajax requests security](https://wiki.genexus.com/commwiki/wiki?11603,,) property is set to High.
* If GeneXus Evolution 2 is used, check the [Javascript Debug Mode](https://wiki.genexus.com/commwiki/wiki?17384) property is set to No.

  + Security Scanner helps to detect this scenario with case code #106.
* Configure the [On session timeout](https://wiki.genexus.com/commwiki/wiki?17458) property properly.
* Implement some re-authentication mechanisms to use before sensitive operations.
* Avoid the default names of the [cookies](https://wiki.genexus.com/commwiki/wiki?21582) used for session identifiers.

  + Security Scanner helps to detect this scenario with case code #116.
* Avoid short session identifiers.
* Use [cookies](https://wiki.genexus.com/commwiki/wiki?21582) that have the attributes Secure, HTTP-Only, SameSite, Domain, and Path configured.

  + Security Scanner helps to detect this scenario with case code #116.
* [Destroy](https://wiki.genexus.com/commwiki/wiki?6813) the web session within the logout process.
* Set the expiration time for the web session on the application server.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
