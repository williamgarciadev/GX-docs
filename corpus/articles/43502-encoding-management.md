---
title: "Encoding Management"
source_id: 43502
source_url: https://wiki.genexus.com/commwiki/wiki?43502
genexus_version: "18"
---

# Encoding Management

All [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) functions use UTF-8 (single-byte) encoding for input/output string/byte manipulation by default.

The default configuration can be changed using the EncodingType Domain and the EncodingUtil Object.

## [EncodingType Domain](#EncodingType+Domain)

Available values:

```
UTF_8, UTF_16, UTF_16BE, UTF_16LE, UTF_32, UTF_32BE, UTF_32LE, SJIS, GB2312
```

* UTF8 - Is the default configuration, and it should solve the majority of use cases.

## [CryptographyEncodingUtil](#CryptographyEncodingUtil)

Available function

### [SetEncoding](#SetEncoding)

* Sets the global module's encoding that will be used for all module functions.

```
Example: &CryptographyEncodingUtil.SetEncoding(EncodingType.UTF-16)
```

This line must be added before using the module's functions when other encoded characters are expected.


|  |
| --- |
| **Backlinks** |
| [Asymmetric Encryption Block Cipher](https://wiki.genexus.com/commwiki/wiki?42686) | [Asymmetric Signing](https://wiki.genexus.com/commwiki/wiki?42687) | [Base64 Encoding](https://wiki.genexus.com/commwiki/wiki?42676) |
| [Base64UrlEncoder](https://wiki.genexus.com/commwiki/wiki?55420) | [Checksum Domains](https://wiki.genexus.com/commwiki/wiki?47428) | [Encodings in GeneXus](https://wiki.genexus.com/commwiki/wiki?19316) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |
| [Hexadecimal Encoding](https://wiki.genexus.com/commwiki/wiki?42675) | [Symmetric Block Encryption](https://wiki.genexus.com/commwiki/wiki?42681) | [Symmetric Key Generation Utils](https://wiki.genexus.com/commwiki/wiki?42683) | [Symmetric Stream Encryption](https://wiki.genexus.com/commwiki/wiki?42682) |

---
