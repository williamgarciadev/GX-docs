---
title: "Base64 Encoding"
source_id: 42676
source_url: https://wiki.genexus.com/commwiki/wiki?42676
genexus_version: "18"
---

# Base64 Encoding

This is part of [GeneXusCryptography Module Encoders](https://wiki.genexus.com/commwiki/wiki?42668). It encodes and decodes the Base64 representation of characters on Strings. It is based on Bouncy Castle Base64 Encoder

## [Base64Encoder](#Base64Encoder)

ToBase64

```
Base64Encoder.ToBase64(text)
```

* Input: VarChar(9999) plain text
* Returns: VarChar(9999) Base64 encoded

Receives a  plain text and returns the Base64 encoded representation of that text.

It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

```
Example: 

&base64Text = &Base64Encoder.ToBase64("hello world")
```

### [ToPlainText](#ToPlainText)

```
Base64Encoder.ToPlainText(base64Text)
```

* Input: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) plain text

Receives a Base64 encoded text and returns the UTF-8 encoded plain text representation of that text.

It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

```
Example:

&plainText = &Base64Encoder.ToPlainText("aGVsbG8gd29ybGQ=")
```

### [ToStringHexa](#ToStringHexa)

```
Base64Encoder.ToStringHexa(base64Text)
```

* Input: VarChar(9999) Base64 encoded text
* Returns: VarChar(9999) hexadecimal representation of a text

Receives a Base64 encoded text and returns the hexadecimal representation of that text.

```
Example:

&hexaText = &Base64Encoder.ToStringHexa("aGVsbG8gd29ybGQ")
```

### [FromStringHexaToBase64](#FromStringHexaToBase64)

```
Base64Encoder.ToStringHexaToBase64(stringHexa)
```

* Input: VarChar(9999) hexadecimal representation of a text
* Returns: VarChar(9999) Base64 encoded text

Recieves the hexadecimal representation of a text and returns the base64 encoded text.

```
Example:

&base64Text = &Base64Encoder.ToStringHexaToBase64("68656C6C6F20776F726C64")
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
