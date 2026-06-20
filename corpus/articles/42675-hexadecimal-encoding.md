---
title: "Hexadecimal Encoding"
source_id: 42675
source_url: https://wiki.genexus.com/commwiki/wiki?42675
genexus_version: "18"
---

# Hexadecimal Encoding

This is part of [SecurityAPI Encoders](https://wiki.genexus.com/commwiki/wiki?42668). It encodes and decodes the Hexadecimal representation of characters on Strings. It is based on Bouncy Castle Hex Encoder and iterates between bytes on low-level implementation.

## [HexaEncoder](#HexaEncoder)

Hexadecimal strings management functions.

### [ToHexa](#ToHexa)

```
HexaEncoder.ToHexa(plainText)
```

* Input: VarChar(256) plain text
* Returns: VarChar(256) hexadecimal representation of a text

Receives a character and returns the hexadecimal representation of the text.

It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

```
Example:

&hexaText = &HexaEncoder.ToHexa("hello world")
```

### [FromHexa](#FromHexa)

```
HexaEncoder.FromHexa(stringHexa)
```

* Input: VarChar(256) hexadecimal representation of a text
* Returns: VarChar(256) plain text

Receives a hexadecimal character and returns the plain text version of the input.

```
Example:

&plainText = &HexaEncoder.FromHexa("0956D2FBD5D5C29844A4D21ED2F76E0C")
```

### [IsHexa](#IsHexa)

This method is available since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,)

```
HexaEncoder.IsHexa(stringHexa)
```

* Input: VarChar(256) string hexadecimal to verify
* Returns: Boolean true if it is a valid hexadecimal

Receives a string and verifies if it is a correct hexadecimal representation.

```
Example:

&isHexa = &HexaEncoder.IsHexa("0956D2FBD5D5C29844A4D21ED2F76E0C")
```


|  |
| --- |
| **Backlinks** |
| [About key, IV, and nonce encoding](https://wiki.genexus.com/commwiki/wiki?46572) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
