---
title: "Standard and non standard functions"
source_id: 8565
source_url: https://wiki.genexus.com/commwiki/wiki?8565
genexus_version: "18"
---

# Standard and non standard functions

All functions1 implemented for any GeneXus generator are called Standard Functions, and they are classified into 3 groups:

* **Normal:** Functions existing for all generators. E.g.: YMDTOD, GXMLines.

* **Non-Portable:** Functions existing only for certain generators. E.g.: WriteRegKey, functions for text handling: dfw and dfr.

* **Deprecated:** Functions for which there is a substitute. E.g.:  XTOD, UDF.

Differences are indicated with varied colors in the GeneXus editor. Normal functions are shown in Brown, Non-Portable ones in Red, and Deprecated functions in Light Brown.

In order to save Non-standard functions, the ‘Function’ preference/property must be modified, either at the model or at the object level. Otherwise, the error message will appear upon saving or specifying the object.

1 In this context, FUNCTIONS means either the functions themselves, or the properties, methods and event control supported by GeneXus. All the functions, properties and methods included built-in GeneXus will work without changing the default value of the [Standard Functions property at Object level](https://wiki.genexus.com/commwiki/wiki?8013).

### Non Standard Functions

All functions which are not build in GeneXus are considered non standard and in order to be able to work with them is needed to set the [Standard Functions Property](https://wiki.genexus.com/commwiki/wiki?8013) to "Allow non standard functions"

*When is it needed to use non standard function?*

The typical case is when using an external functionality, implemented throught web services or native objects (Java classes, .Net assemblies, etc.).

### **How to apply changes**

Rebuild all objects.

### See also

[Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719)


|  |
| --- |
| **Backlinks** |
| [Business Component Check method](https://wiki.genexus.com/commwiki/wiki?23401) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403) | [Standard Functions property at Object level](https://wiki.genexus.com/commwiki/wiki?8013) |

---
