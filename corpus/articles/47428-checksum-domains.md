---
title: "Checksum Domains"
source_id: 47428
source_url: https://wiki.genexus.com/commwiki/wiki?47428
genexus_version: "18"
---

# Checksum Domains

## [InputType Domain](#InputType+Domain)

Values:

```
BASE64, HEX, TXT, ASCII, LOCAL_FILE
```

* If the TXT option is set, the Encoding configured by [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) will be used to process the input.
* The LOCAL\_FILE domain is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,)

## [ChecksumAlgorithm Domain](#ChecksumAlgorithm+Domain)

Values:

CRC8, CRC8\_CDMA2000, CRC8\_DARC, CRC8\_DVB\_S2, CRC8\_EBU, CRC8\_I\_CODE, CRC8\_ITU, CRC8\_MAXIM, CRC8\_ROHC, CRC8\_WCDMA, CRC16\_AUG\_CCITT, CRC16\_CCITT\_FALSE, CRC16\_ARC, CRC16\_BUYPASS, CRC16\_CDMA2000, CRC16\_DDS\_110, CRC16\_DECT\_R, CRC16\_DECT\_X, CRC16\_DNP, CRC16\_EN\_13757, CRC16\_GENIBUS, CRC16\_MAXIM, CRC16\_MCRF4XX, CRC16\_RIELLO, CRC16\_T10\_DIF, CRC16\_TELEDISK, CRC16\_TMS\_37157, CRC16\_USB, CRC\_A, CRC16\_KERMIT, CRC16\_MODBUS, CRC16\_X\_25, CRC16\_XMODEM, CRC32, CRC32\_BZIP2, CRC32C, CRC32D, CRC32\_MPEG\_2, CRC32\_POSIX, CRC32Q, CRC32\_JAMCRC, CRC32\_XFER, MD5, SHA1, SHA256, SHA512

### [CRC implementation details](#CRC+implementation+details)

**CRC Parameters table**

| Algorithm | Polynomial | Initialization | ReflectIn | ReflectOut | XOR Out |
| --- | --- | --- | --- | --- | --- |
| CRC8 | 0x07 | 0x00 | false | false | 0x00 |
| CRC8\_CMDA2000 | 0x9B | 0xFF | false | false | 0x00 |
| CRC8\_DARC | 0x39 | 0x00 | true | true | 0x00 |
| CRC8\_DVB-S2 | 0xD5 | 0x00 | false | false | 0x00 |
| CRC8\_EBU | 0x1D | 0xFF | true | true | 0x00 |
| CRC8\_I\_CODE | 0x1D | 0xFD | false | false | 0x00 |
| CRC8\_ITU | 0x07 | 0x00 | false | false | 0x55 |
| CRC8\_MAXIM | 0x31 | 0x00 | true | true | 0x00 |
| CRC8\_ROHC | 0x07 | 0xFF | true | true | 0x00 |
| CRC8\_WCDMA | 0x9B | 0x00 | true | true | 0x00 |
| CRC16\_CCITT\_FALSE | 0x021 | 0xFFFF | false | false | 0x0000 |
| CRC16\_ARC | 0x1021 | 0x1D0F | true | true | 0x0000 |
| CRC16\_AUG\_CCITT | 0x1021 | 0x1D0F | false | false | 0x0000 |
| CRC16\_BUYPASS | 0x8005 | 0x0000 | false | false | 0x0000 |
| CRC16\_CDMA2000 | 0xC867 | 0xFFFF | false | false | 0x0000 |
| CRC16\_DDS-110 | 0x8005 | 0x800D | false | false | 0x0000 |
| CRC16\_DECT\_R | 0x0589 | 0x0000 | false | false | 0x0001 |
| CRC16\_DECT\_X | 0x0589 | 0x0000 | false | false | 0x0000 |
| CRC16\_DNP | 0x3D65 | 0x0000 | true | true | 0xFFFF |
| CRC16\_EN\_13757 | 0x3D65 | 0x0000 | false | false | 0xFFFF |
| CRC16\_GENIBUS | 0x1021 | 0xFFFF | false | false | 0xFFFF |
| CRC16\_MAXIM | 0x8005 | 0x0000 | true | true | 0xFFFF |
| CRC16\_MCRF4XX | 0x1021 | 0xFFFF | true | true | 0x0000 |
| CRC16\_RIELLO | 0x1021 | 0xB2AA | true | true | 0x0000 |
| CRC16\_T10\_DIF | 0x8BB7 | 0x0000 | false | false | 0x0000 |
| CRC16\_TELEDISK | 0xA097 | 0x0000 | false | false | 0x0000 |
| CRC16\_TMS37157 | 0x1021 | 0x89EC | true | true | 0x0000 |
| CRC16\_USB | 0x8005 | 0xFFFF | true | true | 0xFFFF |
| CRC\_A | 0x1021 | 0xC6C6 | true | true | 0x0000 |
| CRC16\_KERMIT | 0x1021 | 0x0000 | true | true | 0x0000 |
| CRC16\_MODBUS | 0x8005 | 0xFFFF | true | true | 0x0000 |
| CRC16\_X\_25 | 0x1021 | 0xFFFF | true | true | 0xFFFF |
| CRC16\_XMODEM | 0x1021 | 0x0000 | false | false | 0x0000 |
| CRC32 | 0x04C11DB7 | 0xFFFFFFFF | true | true | 0xFFFFFFFF |
| CRC32\_BZIP2 | 0x04C11DB7 | 0xFFFFFFFF | false | false | 0xFFFFFFFF |
| CRC32C | 0x1EDC6F41 | 0xFFFFFFFF | true | true | 0xFFFFFFFF |
| CRC32D | 0xA833982B | 0xFFFFFFFF | true | true | 0xFFFFFFFF |
| CRC32\_MPEG\_2 | 0x04C11DB7 | 0xFFFFFFFF | false | false | 0x000000000 |
| CRC32\_POSIX | 0x04C11DB7 | 0x00000000 | false | false | 0xFFFFFFFF |
| CRC32Q | 0x814141AB | 0x00000000 | false | false | 0x00000000 |
| CRC32\_JAMCRC | 0x04C11DB7 | 0xFFFFFFFF | true | true | 0x00000000 |
| CRC32\_XFER | 0x0000000AF | 0x00000000 | false | false | 0x00000000 |


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
