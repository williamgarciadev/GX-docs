---
title: "Access Validator property"
source_id: 60421
source_url: https://wiki.genexus.com/commwiki/wiki?60421
genexus_version: "18"
---

# Access Validator property

Indicates the Procedure object that implements custom access control for a Query. The Procedure must receive the same parameters as the Query object and return a Boolean value indicating whether access is allowed (true) or denied (false).

### [Scope](#Scope)

**Objects:** [Query object](https://wiki.genexus.com/commwiki/wiki?9026)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

This [Query object](https://wiki.genexus.com/commwiki/wiki?9026) property allows you to indicate a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that implements custom validation to determine whether the Query object can be accessed.

The default value of the property is (none).

When a Query object is executed through [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) services, the Procedure object indicated in the **Access Validator property** is called. The Procedure must receive the same input parameters as the Query and it must return true (allow access) or false (deny access). If the Procedure returns true, the Query runs; otherwise, access is denied.

**Note**: This validation mechanism is independent of the [GAM](https://wiki.genexus.com/commwiki/wiki?24746) security system. It applies even if GAM is not enabled.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,)
