---
title: "GeneXusCompression Module"
source_id: 60613
source_url: https://wiki.genexus.com/commwiki/wiki?60613
genexus_version: "18"
---

# GeneXusCompression Module

The GeneXusCompression module handles file compression and decompression using standard archive formats. It supports immediate and interactive operations with validation options.

To install the GeneXusCompression module, go to [Knowledge Manager Menu](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?5679,,) > [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) in the GeneXus menu.

This module provides three External objects:

**1. [Compression External Object](https://wiki.genexus.com/commwiki/wiki?60618):** Creates and manages interactive compression sessions. It allows files to be added progressively before generating the final archive.

**2. [CompressionConfiguration External Object](https://wiki.genexus.com/commwiki/wiki?60619):** Defines the rules and limits for compression and decompression, such as maximum file size, number of files, and allowed directories. It ensures that operations are safe and validated.

**3. [GXCompressor External Object](https://wiki.genexus.com/commwiki/wiki?60620):** Provides a main entry point for direct compression and decompression. It provides methods for quickly compressing or extracting files without creating a session.

### [Supported Formats](#Supported+Formats)

#### [Java Implementation](#Java+Implementation)

* zip
* 7z
* tar
* gz
* jar

#### .NET Implementation

* zip
* tar
* gz
* jar

### [Dependencies (Java only)](#Dependencies+%28Java+only%29)

The Java version relies on the following libraries:

Apache Commons Compress 1.27.1: https://commons.apache.org/proper/commons-compress/  
XZ 1.10: https://github.com/tukaani-project/xz

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

This module is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).


|  |
| --- |
| **Backlinks** |
| [Compression External Object](https://wiki.genexus.com/commwiki/wiki?60618) | [CompressionConfiguration External Object](https://wiki.genexus.com/commwiki/wiki?60619) | [GXCompressor External Object](https://wiki.genexus.com/commwiki/wiki?60620) |

---
