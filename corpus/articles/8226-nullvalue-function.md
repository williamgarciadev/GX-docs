---
title: "Nullvalue function"
source_id: 8226
source_url: https://wiki.genexus.com/commwiki/wiki?8226
genexus_version: "18"
---

# Nullvalue function

Retrieves the “null” value of an attribute or variable. That value may be empty or the Null itself, depending on the context where the function is used.

### [Syntax](#Syntax)

**Nullvalue(***attribute* | *&variable***)**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol

### [Description](#Description)

It can be used in assignments and conditions with slightly different results:

Assignments

* To assign an empty value to an attribute or set it as Null. It depends on the [Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986).
* To avoid the property dependence use the SetNull() or SetEmpty() methods.
* To initialize variables with their empty value.

Conditions

* Using the function with variables means that the corresponding empty value will be considered.
* Using the function with attributes will depend on whether the condition is evaluated on the server or the client.

### [Samples](#Samples)

```
For Each
     Where Att = Nullvalue(Att)
EndFor
```

In this case the For Each considers those records with an empty ATT.

```
For Each
     If Att = Nullvalue(Att)
        ....
     EndIf
EndFor
```

In this case the For Each retrieves records where Att is empty or Null.

Note that in this case the function does not take into account the [Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986).

If nullvalue is assigned to an attribute in a [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417), it will set an empty value instead of null.

### [See Also](#See+Also)

[Null function](https://wiki.genexus.com/commwiki/wiki?8421)  
[IsNull function](https://wiki.genexus.com/commwiki/wiki?2357)  
[SetNull method](https://wiki.genexus.com/commwiki/wiki?12730)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [IsNull function](https://wiki.genexus.com/commwiki/wiki?2357) | [IsNull method](https://wiki.genexus.com/commwiki/wiki?12735) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Null function](https://wiki.genexus.com/commwiki/wiki?8421) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |

---
