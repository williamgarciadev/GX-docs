---
title: "Modules - Dynamic calls"
source_id: 22585
source_url: https://wiki.genexus.com/commwiki/wiki?22585
genexus_version: "18"
---

# Modules - Dynamic calls

Many GeneXus commands and functions support dynamic execution of objects (see [Call command](https://wiki.genexus.com/commwiki/wiki?8260), [Link command](https://wiki.genexus.com/commwiki/wiki?8446), etc. for details). This article describes how dynamic execution interacts with [Module object](https://wiki.genexus.com/commwiki/wiki?22411) properties.

### [Dynamic execution of [Private objects](https://wiki.genexus.com/commwiki/wiki?22591)](#Dynamic+execution+of+wiki%3F22591%2CPrivate%2Bobject+Private+objects)

Even though it isn't a recommended technique, you \_can\_ dynamically execute an object that you cannot execute statically.

Say, for example, that object X is private to the Module M (see [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473)) and object Y (out of module M) tries to execute it.

If Y uses a static call:

```
M.X()
```

It gets an error message "Validation of Procedure 'CallPrivate' failed. error: Program 'X' does not exist." when saving Y, or at specification time. However, if Y uses a dynamic call:

```
&MX = "M.X"
Call( &MX)
```

There will be no errors either at specification or execution time, related to object privacy.

### [Modules and [Expand dynamic calls property](https://wiki.genexus.com/commwiki/wiki?8569)](#Modules+and+wiki%3F8569%2CExpand%2Bdynamic%2Bcalls%2Bproperty+Expand+dynamic+calls+property)

When dynamic calls are expanded, objects that are not accessible by the caller (i.e. private to other modules) are not included.


|  |
| --- |
| **Backlinks** |
| [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) | [Working with Modules](https://wiki.genexus.com/commwiki/wiki?25607) |

---
