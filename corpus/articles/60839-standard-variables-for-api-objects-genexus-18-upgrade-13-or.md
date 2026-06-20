---
title: "Standard Variables for API Objects (GeneXus 18 Upgrade 13 or prior)"
source_id: 60839
source_url: https://wiki.genexus.com/commwiki/wiki?60839
genexus_version: "18"
---

# Standard Variables for API Objects (GeneXus 18 Upgrade 13 or prior)

[Standard Variables](https://wiki.genexus.com/commwiki/wiki?7386) allow you to access predefined values that GeneXus reserves for use in different [objects](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1866,,). If you try to create a variable with one of these names, GeneXus automatically applies the standard definition and does not allow you to modify its type or redefine it.

In [API object](https://wiki.genexus.com/commwiki/wiki?46151), standard variables are used within the Events section of the object.

**Available Standard Variables in API Object events:**

* &RestCode: sets the HTTP status code returned by the endpoint. If not configured, GeneXus assigns a default code, such as 200 (OK), to indicate success.

### [Availability](#Availability)

**RestCode** is available since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).
