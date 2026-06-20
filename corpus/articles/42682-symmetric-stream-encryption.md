---
title: "Symmetric Stream Encryption"
source_id: 42682
source_url: https://wiki.genexus.com/commwiki/wiki?42682
genexus_version: "18"
---

# Symmetric Stream Encryption

**Note**: This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

Warning! Not all available stream encryptions and modes of operation are safe. Most of them are included for legacy integration compatibility. If you are planning to select an algorithm for a brand new application, choose wisely. Read the OWASP or NIST bibliography and recommendations if you are not certain about what to choose for your application.

## [SymmetricStreamAlgorithm Domain](#SymmetricStreamAlgorithm+Domain)

Values:

```
RC4, HC128, CHACHA20, SALSA20, XSALSA20, ISAAC, VMPC
```

## [SymmetricStreamCipher](#SymmetricStreamCipher)

### [DoEncrypt](#DoEncrypt)

```
SymmetricStreamCipher.DoEncrypt(symmetricStreamAlgorithm, key, iv, plainText)
```

* Input symmetricStreamAlgorithm: SymmetricStreamAlgorithm Domain value
* Input key: VarChar(256) hexadecimal
* Input IV: VarChar(256) hexadecimal
* Input plainText: VarChar(256) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Returns: VarChar(256) Base64 encoded

Encrypts the plain text with the given parameters using a stream cipher type.

Warning! Key values in this document are just examples; do not use them in your applications.

```
Example:

&plainText = "Lorem ipsum dolor sit amet"
&key = "2e46d078d3c4fc21b389a9625ec603894bbea7c35f0a352da56e0c65f52f47798a933b7e06b26249c0374e0f563c14d3edda85c89105dcc7317c77135ece62c4acb07322a32b717939bd8255c979ec310abe7dab16beca41bb8473f1e7c413e20d435a73748c71e702b88160be1516e9c9ce32f770ffa817d2928fec4c7fcaf4a409dca776353a5ea3fda72531fd46fecf059b628e8012720db8d25fd6306ab3321205f9732a2ffee0abb99e317f9d59dcf833b3486aaa940891ea506a607d05fe621eca69476acb6aace42ddb99faf59c355d9e79b9df199e5091fc7f67eea9ca827c6a9a346a7d2eb54069a8974406f9e389abf9fa1e10064e0b1c05761dcc"

&encrypted = &SymmetricStreamCipher.DoEncrypt(SymmetricStreamAlgorithm.RC4, &key, &IV, &plainText)
```

### [DoDecrypt](#DoDecrypt)

```
SymmetricStreamCipher.DoDecrypt(symmetricStreamAlgorithm, key, IV, encryptedInput)
```

* Input symmetricStreamAlgorithm: SymmetricStreamAlgorithm Domain value
* Input key: VarChar(256) hexadecimal
* Input IV: VarChar(256) hexadecimal
* Input encryptedInput: VarChar(256) Base64 encoded
* Returns: VarChar(256) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Decrypts the encrypted input with the given parameters using a stream cipher type.

Warning! Key and nonce values in this document are just examples; do not use them in your applications.

```
Example:

&encrypted = "oxJY9ID8pMxQ3P0C39EY044K18gTSa3iMBg="
&plainText = "Lorem ipsum dolor sit amet"
&key = "2e46d078d3c4fc21b389a9625ec603894bbea7c35f0a352da56e0c65f52f47798a933b7e06b26249c0374e0f563c14d3edda85c89105dcc7317c77135ece62c4acb07322a32b717939bd8255c979ec310abe7dab16beca41bb8473f1e7c413e20d435a73748c71e702b88160be1516e9c9ce32f770ffa817d2928fec4c7fcaf4a409dca776353a5ea3fda72531fd46fecf059b628e8012720db8d25fd6306ab3321205f9732a2ffee0abb99e317f9d59dcf833b3486aaa940891ea506a607d05fe621eca69476acb6aace42ddb99faf59c355d9e79b9df199e5091fc7f67eea9ca827c6a9a346a7d2eb54069a8974406f9e389abf9fa1e10064e0b1c05761dcc"

&decrypted = &SymmetricStreamCipher.DoDecrypt(SymmetricStreamAlgorithm.RC4, &key, &encrypted)
```

### [Implementation - specific details](#Implementation+-+specific+details)

| Algorithm | Key Size (bits) | IV Size (bits) |
| --- | --- | --- |
| RC4 | 1024 | N/A |
| HC128 | 128 | N/A |
| HC256 | 256 | 128 or 256 |
| SALSA20 | 128 or 256 | 64 |
| CHACHA20 | 128 or 256 | 64 |
| XSALSA20 | 256 | 192 |
| ISAAC | 32 or 6144 | N/A |
| VMPC | 8 or 6144 | up to 6144 |


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
