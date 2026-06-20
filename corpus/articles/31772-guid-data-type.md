---
title: "GUID data type"
source_id: 31772
source_url: https://wiki.genexus.com/commwiki/wiki?31772
genexus_version: "18"
---

# GUID data type

This data type allows you to store [GUID](https://wiki.genexus.com/commwiki/wiki?21842) values.

GUID use is important when working in distributed environments.

## [GeneXus Internal use](#GeneXus+Internal+use)

GeneXus uses this data type internally to uniquely identify each type of object.

What for? The idea is that if an object is exported to another KB and modified there when it is later imported back to the source KB, the object will be identified as corresponding to the originally-exported object. Also, if an object is imported into a KB where an object with the same name but a different GUID already exists, GeneXus will know that even though they both have the same name, the imported object does not correspond to the existing object.

## [Generated applications use](#Generated+applications+use)

In generated applications, there is a very similar need for using it. Imagine, for example, a POS (*Point Of Sale*) type application that works disconnected from the head office, where data is unloaded every night.

A common way to copy the data without having to modify the values of all the keys is to define a combined key that includes the number of the point of sale or branch terminal with the sale number.

Imagine the second or third level of this transaction. It will have a key including an attribute whose only purpose is to help make its key unique because there are many points of sale. Each time it is referenced in another transaction, all the key components must be present, generating unnecessary index maintenance.

Using the GUID data type, you can ensure a unique key and avoid this type of problem.

Its use is not limited to primary keys attributes nor records. It can also be used to help file generation (avoiding the duplication of same-name files), Site Keys generation, and any other cases where obtaining a globally unique identifier are required.

## [How is it used in GeneXus?](#How+is+it+used+in+GeneXus%3F)

### [Static methods](#Static+methods)

* GUID.NewGuid()
* GUID.Empty()
* GUID.FromString(“XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX”)

#### [**Example**](#Example)

```
If &GUID <> GUID.FromString("2ac61739-b024-438e-a6e5-e507d8be4667")
     msg("Bad Site Key")
EndIf
```

### [Functions/ Instance methods](#Functions%2F+Instance+methods)

* ToString() return a string with XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX format.
* FromString() return GUID created by a hexadecimal string, with or without the "-" delimiters.
* IsEmpy()
* IsNull()
* SetEmpty()
* SetNull()

#### [**Example**](#Example)

```
&GUID.FromString("12daa4b3-d7c2-4df4-a634-18bed4f2374c")
msg("GUID: " + &GUID.ToString())
```

### [[Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892)](#wiki%3F40892%2CAutogenerate%2BGuid%2Bproperty+Autogenerate+Guid+property)

Attributes and variables based on the GUID data type offer the [Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892) to set that you want that the GUID value is automatically generated when an insertion is performed.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | Attribute/Variable |
| **Generators:** | [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |
| **Events:** | [Web Panels events](https://wiki.genexus.com/commwiki/wiki?8178), [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234), [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) |

### [See Also](#See+Also)

[Initial value property](https://wiki.genexus.com/commwiki/wiki?11765)


|  |
| --- |
| **Backlinks** |
| [Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892) | [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543) | [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911) |
| [GUID](https://wiki.genexus.com/commwiki/wiki?21842) | [Initial value property](https://wiki.genexus.com/commwiki/wiki?11765) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) |
| [JWT Utils](https://wiki.genexus.com/commwiki/wiki?43986) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
