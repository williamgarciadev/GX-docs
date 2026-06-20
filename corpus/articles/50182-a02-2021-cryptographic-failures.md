---
title: "A02:2021 - Cryptographic failures"
source_id: 50182
source_url: https://wiki.genexus.com/commwiki/wiki?50182
genexus_version: "18"
---

# A02:2021 - Cryptographic failures

This article describes Cryptographic failures and how to prevent/ fix the exposure of sensitive data in your applications.

Read more at: [Cryptographic Failures - OWASP Documentation](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

Actions by GeneXus

* GeneXus does not cipher sensitive data.

Actions by Developers

* If a shared secret is needed, it must be hashed before being saved to a file or database.

  + Save a modified (salted) hash to sensitive data.
* Use a secure hash function. The use of SHA2 256 or 512 is recommended.
* Cipher the data on the application layer.
* Cipher the cipher key. For this, the GeneXus Site Key can be used. The use of AES with 128 or 256-bit keys is recommended.
* Avoid storing sensitive data in logs. If it is unavoidable, the sensitive data must be hashed or masked.
* Avoid storing sensitive data in intermediate files. Consider using [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) to write and send the data directly instead. If it is unavoidable, verify that those files are erased from the server after being sent.
* Configure the application server with the minimum permission required and avoid exposing the [Temp media directory](https://wiki.genexus.com/commwiki/wiki?7628) and/or other temp directories by HTTP/HTTPS.
* Use secure channels.

  + Use HTTPS strictly, even for static content.

    - Security Scanner helps to detect this scenario with case code #105.
  + Use LDAPS instead of LDAP.
  + Use TLS or WS-Security for server-to-server communication or other shared resources.
  + Use valid certificates.
* Avoid weak cipher algorithms.
* Avoid sending sensitive data to the browser if it is not needed. Avoid hidden content with sensitive data on forms. Select the necessary information on the server side.
* Security Scanner - Detections:

  + Shared secrets: Checking IsPassword property use (#119).
  + Intermediate files: Check Parameterless LINK Command on source code (#104); checking for variables of HttpResponse type (#109); checking for variables of Directory type (#111); checking for variables of File type (#112); check use of PathToUrl on source code (#132).

## [Intermediate and browser cache](#Intermediate+and+browser+cache)

Actions by GeneXus

* GeneXus adds HTTP Headers for all web pages and automatically generated static content that indicate what can or cannot be cached.

Actions by Developers

* If the HttpResponse data type is used to create a custom web page, the developer must specify if the response is public, if it can be cached, and for how long.

  + Security Scanner helps to detect this scenario with case code #109.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
