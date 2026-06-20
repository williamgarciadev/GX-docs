---
title: "GxFtpPut function"
source_id: 8400
source_url: https://wiki.genexus.com/commwiki/wiki?8400
genexus_version: "18"
---

# GxFtpPut function

**Alert**: FTP does not encrypt the channel. It is recommended to use a protocol that encrypts the channel such as SFTP or FTPS.

Uploads to an FTP server.

### [Syntax](#Syntax)

**Call**(**'GxFtpPut'**, &*Source*, &*Target*, &*Mode*)

**Where:**  
*Source*  
    Character. Full name of the source file (with the path).

*Target*  
    Character. Target file’s name. When left empty, the same name of the source file is assumed in the directory by default. When only the directory is indicated (ending in \), the same file’s name is assumed.

*Mode*  
    Character. Transference mode. It can be 'A' (Ascii) or 'B' (Binary).

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[FTP functions](https://wiki.genexus.com/commwiki/wiki?8393)


|  |
| --- |
| **Backlinks** |
| [FTP functions](https://wiki.genexus.com/commwiki/wiki?8393) | [GxFtpError function](https://wiki.genexus.com/commwiki/wiki?8397) |

---
