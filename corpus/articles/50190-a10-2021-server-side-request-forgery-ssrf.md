---
title: "A10:2021 - Server-side request forgery (SSRF)"
source_id: 50190
source_url: https://wiki.genexus.com/commwiki/wiki?50190
genexus_version: "18"
---

# A10:2021 - Server-side request forgery (SSRF)

In this document, you can find information and actions to take regarding the Server-Side Request Forgery vulnerability.

SSRF (Server-Side Request Forgery) flaws occur whenever a web application (server) obtains a remote resource without validating the URL, which is fully or partially provided by the user. It allows an attacker to make the application send a request to an unintended destination, even if it is protected by a firewall, VPN, or other network access control list.

[Server-Side Request Forgery - OWASP Documentation](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* In scenarios where the application must perform HTTP requests, GeneXus does not perform validations on the destination URLs. The developer is responsible for securing the URLs that the server uses.

#### [Actions by Developers](#Actions+by+Developers)

* Using the [FromURL](https://wiki.genexus.com/commwiki/wiki?9644) method with user input as a parameter may result in the server making requests to unexpected destinations. It is recommended to:

  + Use fixed URLs, avoiding external resources if possible.
  + Avoid using the functionality.
  + Make strict validations on which data is used in the final URL.
* Identify the SOAP web service invocation with a [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) variable, particularly in the [Host](https://wiki.genexus.com/commwiki/wiki?6999), [BaseUrl](https://wiki.genexus.com/commwiki/wiki?7008), and [Port](https://wiki.genexus.com/commwiki/wiki?5019) properties.
* Identify [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) variables and how their properties are loaded; in particular, look for the Host, BaseUrl, Port, [ProxyServerHost, ProxyServerPort](https://wiki.genexus.com/commwiki/wiki?6988) properties and check the parameters used in the [Execute method](https://wiki.genexus.com/commwiki/wiki?7047).
* General recommendations:

  + Use strictly fixed URLs.
  + Obtain the base URL from a trusted source.

    - Never let the user provide a whole URL.
    - Avoid using the [BaseUrl](https://wiki.genexus.com/commwiki/wiki?7008) property of [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) for this purpose because it can be manipulated in the raw HTTP request.
  + Validate every input used in a URL:

    - Using regular expressions.
    - Using custom validation libraries, which are well-known.
    - Verify validated target domain/IP with a list of allowed targets by string-based and case-sensitive strict comparison.
  + Restrict which IPs the server can access (outbound traffic) at network level. This can be done through the operating system firewall or a separate firewall component on the network.


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
