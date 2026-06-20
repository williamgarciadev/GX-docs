---
title: "GetEncryptionKey function"
source_id: 8385
source_url: https://wiki.genexus.com/commwiki/wiki?8385
genexus_version: "18"
---

# GetEncryptionKey function

Generates an encryption key in hexadecimal format with a length of 32 characters.

### [Syntax](#Syntax)

**GetEncryptionKey()**

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This function generates a new encryption key in hexadecimal format with a length of 32 characters.

The key value returned is used to initialize encryptions.

This function must be run again in order to generate a new key.

### [Sample](#Sample)

```
&Key=GetEncryptionKey()
```

`[imagen omitida: wiki id 14723]`

### [See Also](#See+Also)

[Encrypt64 function](https://wiki.genexus.com/commwiki/wiki?8386)  
[Decrypt64 function](https://wiki.genexus.com/commwiki/wiki?8382)


|  |
| --- |
| **Backlinks** |
| [Decrypt64 function](https://wiki.genexus.com/commwiki/wiki?8382) | [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) |
| [Encrypt64 function](https://wiki.genexus.com/commwiki/wiki?8386) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
