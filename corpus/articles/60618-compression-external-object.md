---
title: "Compression External Object"
source_id: 60618
source_url: https://wiki.genexus.com/commwiki/wiki?60618
genexus_version: "18"
---

# Compression External Object

The Compression [External Object](https://wiki.genexus.com/commwiki/wiki?5669) allows progressive file addition and delayed compression.

Once the [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) is installed, you can find the Compression External Object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), under the module node.

## [Methods](#Methods)

### [AddElement method](#AddElement+method)

Adds a file to be included in the archive.

**Return Value:** None  
**Parameters:**ElementPath: [Character](https://wiki.genexus.com/commwiki/wiki?6777)(100).

```
&Compression.AddElement(&ElementPath)
```

### [SetDestinationPath method](#SetDestinationPath+method)

Sets the target path for the compressed file.

**Return Value:** None  
**Parameters:**DestinationPath: Character(100).

```
&Compression.SetDestinationPath(&DestinationPath)
```

### [Clear method](#Clear+method)

Clears the current session, resetting the destination path, file list, and configuration.

**Return Value:** None  
**Parameters:**None

### [Save method](#Save+method)

Executes the compression operation using all previously added files and returns whether it succeeded.

**Return Value:** Boolean  
**Parameters:**None

## [Events](#Events)

It does not have any.

## [Security tips](#Security+tips)

Avoid the use of end user's data on paths or sanitize them.

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

This External Object is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) | [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) |

---
