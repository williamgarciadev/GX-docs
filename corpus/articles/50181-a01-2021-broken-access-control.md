---
title: "A01:2021 - Broken access control"
source_id: 50181
source_url: https://wiki.genexus.com/commwiki/wiki?50181
genexus_version: "18"
---

# A01:2021 - Broken access control

This article focuses on providing guidance in the event of the failure of access control mechanisms. This guidance is based on OWASP (Open Web Application Security Project).

### [Insecure Direct Object Reference](#Insecure+Direct+Object+Reference)

[Insecure Direct Object Reference Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus ciphers the parameters sent over the URL if the [Encrypt URL parameters](https://wiki.genexus.com/commwiki/wiki?8068) property is properly set by the developer.
* [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) verifies the authorization over the web objects.

#### [Actions by Developers](#Actions+by+Developers)

* Web object parameters must be ciphered.

  + Security Scanner helps to detect this scenario with case codes #100, #105 & #107.
* Check that every object verifies authorization.
* Change the default parameter cipher key on deployment.

### [AJAX requests](#AJAX+requests)

[AJAX Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AJAX_Security_Cheat_Sheet.html#Don.27t_rely_on_client_logic_for_security)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* [Suggests](https://wiki.genexus.com/commwiki/wiki?8800) and [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) can be invoked by AJAX Requests. GeneXus prevents this if the [Ajax requests security](https://wiki.genexus.com/commwiki/wiki?11603,,) property (for GeneXus Evolution 1) or the [Javascript Debug Mode](https://wiki.genexus.com/commwiki/wiki?17384) (for GeneXus Evolution 2 and above) property is properly set by the developer.

#### [Actions by Developers](#Actions+by+Developers)

* If GeneXus Evolution 1 is used, check the Ajax Request Security property is set to High.
* If GeneXus Evolution 2 is used, check the Javascript Debug Mode property is set to No.

  + Security Scanner helps to detect this scenario with case code #106.
* If a custom [User Control](https://wiki.genexus.com/commwiki/wiki?5273) is used, secure the AJAX requests manually.

### [Improper temporary files generation and path traversal](#Improper+temporary+files+generation+and+path+traversal)

[Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus manages temporary files by separating private and public files through the [Temp media directory](https://wiki.genexus.com/commwiki/wiki?7628) and [Blob local storage directory](https://wiki.genexus.com/commwiki/wiki?6979) properties.

#### [Actions by Developers](#Actions+by+Developers)

* Avoid storing sensitive data in intermediate files. Consider using [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) to write and send the data directly instead. If it is unavoidable, then verify that those files are erased from the server after being sent.
* Configure the application server with the minimum permission required and avoid exposing the Temp media directory and/or other temp directories by HTTP/HTTPS.
* Generate the files over an external directory, and return them via a [GeneXus Procedure](https://wiki.genexus.com/commwiki/wiki?6293) avoiding paths and executing an authorization check before retrieving the file. This Procedure must receive an identifier to associate with the file over a table on the server to avoid returning paths.
* Verify the file management over the application.

  + Security Scanner helps to detect this scenario with case codes #104, #109, #111, #112, #129 & #132.

### [Leaving functions without access control](#Leaving+functions+without+access+control)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus validates data on the client side and validates the data again on the server side.
* GAM verifies the authorization over the web objects.

#### [Actions by Developers](#Actions+by+Developers)

* Check every object verifies authorization over the object and over each event.

  + Security Scanner helps to detect this scenario with case code #102 over [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Transaction objects](https://wiki.genexus.com/commwiki/wiki?1908).
  + Security Scanner helps to detect this scenario with case code #107 over [Web Component objects](https://wiki.genexus.com/commwiki/wiki?1864) with the [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) set to False.
* Check the access control over data on the client side.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
