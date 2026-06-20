---
title: "Base64UrlEncoder"
source_id: 55420
source_url: https://wiki.genexus.com/commwiki/wiki?55420
genexus_version: "18"
---

# Base64UrlEncoder

This is part of [GeneXusCryptography Module Encoders](https://wiki.genexus.com/commwiki/wiki?42668). It encodes and decodes the Base64 Url representation of characters on Strings. It is based on Bouncy Castle UrlBase64 Encoder

## [Base64UrlEncoder](#Base64UrlEncoder)

Available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)

### [ToBase64](#ToBase64)

```
Base64UrlEncoder.ToBase64(text)
```

* Input: VarChar(9999) plain text
* Returns: VarChar(9999) Base64 Url encoded

Receives a  plain text and returns the Base64 Url encoded representation of that text.

It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Example:

```
&base64UrlText = &Base64UrlEncoder.ToBase64("hello world")
```

### [ToPlainText](#ToPlainText)

```
Base64UrlEncoder.ToPlainText(base64UrlText)
```

* Input: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) plain text

Receives a Base64 encoded text and returns the UTF-8 encoded plain text representation of that text.

It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Example:

```
&plainText = &Base64UrlEncoder.ToPlainText("aGVsbG8gd29ybGQ.")
```

### [ToStringHexa](#ToStringHexa)

```
Base64UrlEncoder.ToStringHexa(base64UrlText)
```

* Input: VarChar(9999) Base64 Url encoded text
* Returns: VarChar(9999) hexadecimal representation of a text

Receives a Base64 Url encoded text and returns the hexadecimal representation of that text.

Example:

```
&hexaText = &Base64Encoder.ToStringHexa("aGVsbG8gd29ybGQ")
```

### [FromStringHexaToBase64](#FromStringHexaToBase64)

```
Base64UrlEncoder.ToStringHexaToBase64(stringHexa)
```

* Input: VarChar(9999) hexadecimal representation of a text
* Returns: VarChar(9999) Base64 Url encoded text

Receives the hexadecimal representation of a text and returns the base64 Url encoded text.

Example:

```
&base64UrlText = &Base64UrlEncoder.ToStringHexaToBase64("68656C6C6F20776F726C64")
```

### [Base64UrlToBase64](#Base64UrlToBase64)

```
Base64UrlEncoder.Base64UrlToBase64(Base64UrlEncodedText)
```

* Input: VarChar(9999) Base64 Url encoded text
* Returns: VarChar(9999) Base64 encoded text

Receives a Base64 Url encoded text and returns the Base64 encoded text

Example:

```
&base64Text = &Base64UrlEncoder.Base64UrlToBase64("aGVsbG8gd29ybGQ.")
```

### [Base64toBase64Url](#Base64toBase64Url)

```
Base64UrlEncoder.Base64ToBase64Url(Base64EncodedText)
```

* Input: VarChar(9999) Base64 encoded text
* Returns: Varchar(9999) Base64 Url encoded text

Receives a Base64 encoded text and returns the Base64 Url encoded text

Example:

```
&base64UrlText = &Base64UrlEncoder.Base64ToBase64Url("aGVsbG8gd29ybGQ=")
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
