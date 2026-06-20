---
title: "GXCompressor External Object"
source_id: 60620
source_url: https://wiki.genexus.com/commwiki/wiki?60620
genexus_version: "18"
---

# GXCompressor External Object

The GXCompressor [External Object](https://wiki.genexus.com/commwiki/wiki?5669) provides methods for immediate compression and decompression of files and archives.

Once the [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) is installed, you can find the GXCompressor External Object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), under the module node.

## [Methods](#Methods)

It includes three methods for different scenarios: Compress, Decompress, and progressive compression.

### [Compress method](#Compress+method)

Compresses a list of files into an archive.

**Return Value:** Boolean  
**Parameters:**

* FilePaths: [VarChar](https://wiki.genexus.com/commwiki/wiki?6778)(100)
* ArchiveDestinationPath: VarChar(100)
* CompressionConfiguration: [CompressionConfiguration](https://wiki.genexus.com/commwiki/wiki?60619) (GeneXusCompression)
* Messages: Messages (GeneXus.Common)

```
&Success = &GXCompressor.Compress(&FilePaths, &ArchiveDestinationPath, &CompressionConfiguration, &Messages)
```

#### [Considerations](#Considerations)

The archive format is determined by the file extension of ArchiveDestinationPath.

The method enforces validation:

* Files must exist and comply with configured size constraints.
* Total archive size and file count must not exceed configured limits.
* Target and source paths are checked against directory traversal attempts.
* If &CompressionConfiguration.TargetDirectory is set, all file paths must reside within it.

### [Decompress method](#Decompress+method)

Decompresses an archive into a target directory.

**Return Value:** Boolean  
**Parameters:**

* ArchivePath: VarChar(100)
* DecompressionDestinationPath: VarChar(100)
* CompressionConfiguration: [CompressionConfiguration](https://wiki.genexus.com/commwiki/wiki?60619) (GeneXusCompression)
* Messages: Messages (GeneXus.Common)

```
&Success = &GXCompressor.Decompress(&ArchivePath, &DecompressionDestinationPath, &CompressionConfiguration, &Messages)
```

#### [Considerations](#Considerations)

* The archive must exist and be non-empty.
* Format is inferred from the file extension.
* The method verifies:
  + No directory traversal in archive entries or destination path.
  + Archive must contain files.
  + File count, individual file size, and estimated total decompressed size must comply with configuration limits, if set.
  + If &CompressionConfiguration.TargetDirectory is set, extraction must remain within this directory.

### [NewCompression method](#NewCompression+method)

Creates a compression session for interactively adding files.

**Return Value:** Compression  
**Parameters:**

* ArchiveDestinationPath: VarChar(100)
* CompressionConfiguration: [CompressionConfiguration](https://wiki.genexus.com/commwiki/wiki?60619) (GeneXusCompression)  
  Messages: Messages (GeneXus.Common)

```
&NewCompression = &GXCompressor.NewCompression(&ArchiveDestinationPath, &CompressionConfiguration, &Messages)
```

## [Events](#Events)

It does not have any.

## [Security tips](#Security+tips)

Avoid the use of end user's data on paths or sanitize them.

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

This module is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) | [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) |

---
