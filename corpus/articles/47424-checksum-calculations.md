---
title: "Checksum calculations"
source_id: 47424
source_url: https://wiki.genexus.com/commwiki/wiki?47424
genexus_version: "18"
---

# Checksum calculations

## [Checksums in a nutshell](#Checksums+in+a+nutshell)

A checksum is a value derived from a block of digital data used to verify the integrity of a file or a data transfer but is not relied upon to verify data authenticity. In other words, it is a sum that checks the validity of data. Checksums are typically used to compare two sets of data to make sure they are the same. Some common applications include verifying a disk image or checking the integrity of a downloaded file. If the checksums don't match those of the original files, the data may have been altered or corrupted. Checksum functions are related to a hash function, fingerprints, randomization functions, and cryptographic hash functions. ([Source](https://en.wikipedia.org/wiki/Checksum#::text=A%20checksum%20is%20a%20small,upon%20to%20verify%20data%20authenticity.))

### [Differences between CRCs and Hash functions](#Differences+between+CRCs+and+Hash+functions)

### [CRC](#CRC)

CRCs are a type of error-detecting code used to implement checksums. CRCs are specifically designed to satisfy the property that they can detect transmission errors in data. CRC helps to find data corruption in every few bytes so that they can be immediately corrected (using error correction calculation); also, the bytes can be re-read or re-transmitted immediately.

CRC is computationally much less complex than a hash function. Using a hash function like MD5 is probably overkill for random error detection. However, using CRC for any kind of security check would be much less secure than a more complex hashing function such as MD5.

Using CRC in large amounts of data (MBs / GBs) is not recommended because the remainder operation is very easily repeatable.

### [Hashes](#Hashes)

Hashing’s purpose is to uniquely obfuscate data and make a tiny reliable hash (so that uniqueness or match can be checked but data would not be retrievable).

Since hashing is comparatively costly, it cannot be used often for every few characters to immediately detect errors. Nevertheless, its strength lies in its uniqueness. It can be used to pretty much guarantee that the entire sequence of several MBs/GBs is unique and unaltered (because even if a single byte changes, the hash will turn out different). This uniqueness also means that sometimes (for small snippets of data) it can be possible to reverse engineer the data from the hash depending on the collision probability of the hash function. There will usually be no de-hashing function.

Also, if you have selected a particular hashing function, it is so reliable that you can discard the original data and only verify the hash for a match.

## [Considerations](#Considerations)

* This module does not support large-size files.
* The CRC is computed dynamically.

## [Availability](#Availability)

Checksum objects are available since GeneXus 17 u2


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
