---
title: "ChecksumCreator"
source_id: 47425
source_url: https://wiki.genexus.com/commwiki/wiki?47425
genexus_version: "18"
---

# ChecksumCreator

Implements checksum functions.

## [GenerateChecksum](#GenerateChecksum)

```
ChecksumCreator.GenerateChecksum(input, inputType, checksumAlgorithm)
```

* Input input: VarChar(256), the string to calculate the checksum or the path to a file if LOCAL\_FILE domain is used
* Input inputType: InputType Domain value
* Input checksumAlgorithm: ChecksumAlgorithm Domain value
* Returns VarChar(256) hexadecimal

Calculates the checksum value with the given parameters.

The LOCAL\_FILE domain is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,)

```
Example1: &checksum = &ChecksumCreator.GenerateChecksum("123456789", InputType.ASCII, ChecksumAlgorithm.CRC8)
Example2: &checksum = &ChecksumCreator.GenerateChecksum("123456789", InputType.TXT, ChecksumAlgorithm.CRC8)
Example3: &checksum = &ChecksumCreator.GenerateChecksum("MTIzNDU2Nzg5", InputType.BASE64, ChecksumAlgorithm.CRC8)
Example4: &checksum = &ChecksumCreator.GenerateChecksum("313233343536373839", InputType.HEX, ChecksumAlgorithm.CRC8)
Example5: &checksum = &ChecksumCreator.GenerateChecksum("C:\temp\file.txt", InputType.LOCAL_FILE, ChecksumAlgorithm.CRC8)
```

## [VerifyChecksum](#VerifyChecksum)

```
ChecksumCreator.VerifyChecksum(input, inputType, checksumAlgorithm, checksum)
```

* Input input: VarChar(256) the string to calculate the checksum or the path to a file if LOCAL\_FILE domain is used
* Input inputType: InputType Domain value
* Input checksumAlgorithm: ChecksumAlgorithm Domain value
* Input checksum: VarChar(256) hexadecimal
* Returns Boolean true if the checksum is correct

The LOCAL\_FILE domain is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,)

Verifies if the checksum is correct for the input with the given parameters.

```
Example1: &verification = &ChecksumCreator.VerifyChecksum("123456789", InputType.ASCII, ChecksumAlgorithm.CRC8, "F4")
Example2: &verification = &ChecksumCreator.VerifyChecksum("123456789", InputType.TXT, ChecksumAlgorithm.CRC8, "F4")
Example3: &verification = &ChecksumCreator.VerifyChecksum("MTIzNDU2Nzg5", InputType.BASE64, ChecksumAlgorithm.CRC8, "F4")
Example4: &verification = &ChecksumCreator.VerifyChecksum("313233343536373839", InputType.HEX, ChecksumAlgorithm.CRC8, "F4")
Example5: &ChecksumCreator.VerifyChecksum("C:\temp\file.txt", InputType.LOCAL_FILE, ChecksumAlgorithm.CRC8, "F4")
```

## [Security tips](#Security+tips)

* Avoid letting the end-user manipulate the path to the file or sanitize it accordingly, the application won't sanitize the path by default.
* Avoid letting the end-user manipulate files of the server file system. Check for mime types, extensions and verify/sanitize upload paths.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
