---
title: "CORS settings with environment variables"
source_id: 52127
source_url: https://wiki.genexus.com/commwiki/wiki?52127
genexus_version: "18"
---

# CORS settings with environment variables

### [What is CORS?](#What+is+CORS%3F)

[Cross Origin Resource Sharing - CORS](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52092,,) is a standard that allows servers to relax the same-origin policy. This is used to allow some cross-origin requests explicitly while rejecting others. For example, if a site offers an embeddable service, it may be necessary to relax certain restrictions.

When CORS is not enabled, and the Application and Service URL are in different domains, the WebBrowser will print the following error in the Console:

Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://some-url-here. (Reason: additional information here).

Fortunately, GeneXus supports handling CORS-required headers in order to ensure the correct behavior of the Application.

Typically this is necessary for [Angular application](https://wiki.genexus.com/commwiki/wiki?42539)s, which call REST Services that are eventually deployed in another domain.

### [How to enable CORS headers in a GeneXus Application](#How+to+enable+CORS+headers+in+a+GeneXus+Application)

The environment variable GX\_CORS\_ALLOW\_ORIGIN enables CORS for the selected host.

The values accepted by the variable are URL or "\*". For example, https://foo.example.

**Note**: In the .NET Generator, it is possible to assign a comma-separated list of domains to the variable. For example, GX\_CORS\_ALLOW\_ORIGIN=https://foo.example**,**https://another.domain.

When GX\_CORS\_ALLOW\_ORIGIN environment variable is enabled, the generated Application will return the following headers, according to the CORS specification:

* #### [Access-Control-Allow-Methods](#Access-Control-Allow-Methods)

  + Will return all the supported methods that the currently called service supports.
* #### [Access-Control-Allow-Headers](#Access-Control-Allow-Headers)

  + All requested Headers on the incoming request will be allowed
* #### [Access-Control-Allow-Origin](#Access-Control-Allow-Origin)

  + Environment Variable GX\_CORS\_ALLOW\_ORIGIN will be returned
* #### [Access-Control-Allow-Credentials](#Access-Control-Allow-Credentials)

  + “true” is the default returned value
* #### [Access-Control-Max-Age](#Access-Control-Max-Age)

  + 86400 is the default returned value

Example Response of an OPTIONS Request to a GeneXus REST Endpoint:

Access-Control-Allow-Origin: https://myapp.domain.com  
Access-Control-Allow-Headers: GET, POST  
Access-Control-Max-Age: 86400  
Access-Control-Allow-Credentials: true

**Warning**: Make sure the value of GX\_CORS\_ALLOW\_ORIGIN exactly matches the value of the Origin header sent in the request, otherwise you can get an error, which may be 504 Gateway error.

### [CORS in .NET Framework Generator](#CORS+in+.NET+Framework+Generator)

When the GX\_CORS\_ALLOW\_ORIGIN environment variable is defined, the preflight OPTIONS request may not return the expected headers (as defined above).

It may be due to the configuration of handler mappings in IIS. To fix it, configure the OPTIONSVerbHandler to execute after wcf handlers (svc-Integrated-4.0).

1. In IIS console, select "Handler Mappings" (either on server level or site level; beware that on the site level it will redefine all the handlers for your site and ignore any change done at the server level after that. Of course, on the server level, this could break other sites if they need their own handling of options verb).
2. In Action pane, select "View ordered list..." Seek OPTIONSVerbHandler, and move it down until it is below svc-Integrated-4.0 handler.

**Note**: If OPTIONSVerbHandler is removed, it will break the response to preflight OPTIONS request for API objects.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).

### [See Also](#See+Also+)

[Environment variables definition](https://wiki.genexus.com/commwiki/wiki?39459)  
[Methods for reading environmental variables](https://wiki.genexus.com/commwiki/wiki?33076)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) |

---
