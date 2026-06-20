---
title: "CompressionConfiguration External Object"
source_id: 60619
source_url: https://wiki.genexus.com/commwiki/wiki?60619
genexus_version: "18"
---

# CompressionConfiguration External Object

The CompressionConfiguration [External Object](https://wiki.genexus.com/commwiki/wiki?5669) defines compression and decompression constraints.

Once the [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) is installed, you can find the CompressionConfiguration External Object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), under the module node.

## [Properties](#Properties)

### [maxCombinedFileSize](#maxCombinedFileSize+)

Maximum total size of all files. Use -1 to disable the check.

### [maxIndividualFileSize](#maxIndividualFileSize)

Maximum size for any single file. Use -1 to disable the check.

### [maxFileCount](#maxFileCount)

Maximum number of files. Use -1 to disable the check.

### [targetDirectory](#targetDirectory)

Root directory constraint. Use "" to disable path validation.

## [Methods](#Methods)

It does not have any.

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

This external object is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).


|  |
| --- |
| **Backlinks** |
| [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) | [GXCompressor External Object](https://wiki.genexus.com/commwiki/wiki?60620) |

---
