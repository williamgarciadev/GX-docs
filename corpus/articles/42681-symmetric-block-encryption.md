---
title: "Symmetric Block Encryption"
source_id: 42681
source_url: https://wiki.genexus.com/commwiki/wiki?42681
genexus_version: "18"
---

# Symmetric Block Encryption

**Note**: This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

Warning! Not all available block encryptions, paddings or modes of operation are safe. Most of them are included for legacy integration compatibility. If you are planning to select an algorithm for a brand new application, choose wisely. Read the OWASP or NIST bibliography and recommendations if you are not certain about what to choose for your application.

## [SymmetricBlockAlgorithm Domain](#SymmetricBlockAlgorithm+Domain)

Values:

```
AES, BLOWFISH, CAMELLIA, CAST5, CAST6, DES, TRIPLEDES, DSTU7624_128, DSTU7624_256, DSTU7624_512, GOST28147, NOEKEON, RC2, RC532, RC564, RC6, RIJNDAEL_128, RIJNDAEL_160, RIJNDAEL_192, RIJNDAEL_224, RIJNDAEL_256, SEED, SERPENT, SKIPJACK, SM4, TEA, THREEFISH_256, THREEFISH_512, THREEFISH_1024, TWOFISH, XTEA
```

* THREEFISH keys must be of the same length as the block and the input must be the same length or longer than the block
* DSTU7624 the input must be of the same length or longer than the block.

## [SymmetricBlockMode Domain](#SymmetricBlockMode+Domain)

Values:

```
ECB, CBC, CFB, CTR, CTS, GOFB, OFB, OPENPGPCFB, SIC, /* AEAD */ AEAD_EAX, AEAD_GCM, AEAD_CCM
```

* ECB and OPENPGPCFB do not use an IV; the IV parameter will be ignored (actually, OPENPGPCFB uses an initialization vector (IV) of all zeros).
* AEAD\_CCM nonce length must be between 56 and 104 bits and only applies to 128-bit blocksize ciphers; it works with 64 and 128-bit MAC sizes.
* AEAD\_GCM cannot be used with ciphers that have less than 128 bits block sizes; it works with 128, 120, 112, 104 and 96-bit MAC sizes.
* AEAD\_EAX key sizes must be 128, 192 or 256 bits long, and MAC sizes must be in a range from 8 to 128 bits (recommended: 8, 16, 64 or 128-bit MAC sizes); it only works with 64 and 128 bits blocksize ciphers.
* CFB and OFB modes do not work with algorithms with 160 or 224 block lenghts.

## [SymmetricBlockPadding Domain](#SymmetricBlockPadding+Domain)

Values:

```
NOPADDING, PKCS7PADDING, ISO10126D2PADDING, X923PADDING, ISO7816D4PADDING, ZEROBYTEPADDING, WITHCTS
```

* NOPADDING is available, but when using this option the input must be a multiple of 8 because it will not pad the input automatically. If NOPADDING is used and the input is not a multiple of 8, it will throw a runtime exception like this: "org.bouncycastle.crypto.DataLengthException: data not block size aligned."

## [SymmetricBlockCipher](#SymmetricBlockCipher)

### [DoEncrypt](#DoEncrypt)

```
SymmetricBlockCipher.DoEncrypt(symmetricBlockAlgorithm, symmetricBlockMode, symmetricBlockPadding, key, IV, plainText)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input symmetricBlockPadding: SymmetricBlockPadding Domain value
* Input key: VarChar(256) hexadecimal
* Input IV:  VarChar(256) hexadecimal
* Input plainText: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Returns: VarChar(9999) Base64 encoded

Encrypts the plain text with the given parameters.

Warning! Key and IV values in this document are just examples; do not use them in your applications.

```
Example: 

&plainText = "Lorem ipsum dolor sit amet"
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&IV = "10dd993308d37a15b55f64a0e763f353"

&encrypted = &SymmetricBlockCipher.DoEncrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.CBC, SymmetricBlockPadding.PKCS7PADDING, &key, &IV, &plainText)
```

### [DoDecrypt](#DoDecrypt)

```
SymmetricBlockCipher.DoDecrypt(symmetricBlockAlgorithm, symmetricBlockMode, symmetricBlockPadding, key, IV, encryptedInput)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input symmetricBlockPadding: SymmetricBlockPadding Domain value
* Input key: VarChar(256) hexadecimal
* Input IV:  VarChar(256) hexadecimal
* Input encryptedInput: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Decrypts the encrypted input with the given parameters.

Warning! Key and IV values in this document are just examples; do not use them in your applications.

```
Example:

&encrypted = "yLpJb86/rLA/9KKylktzY9i9hfFUeFduawKwyyYUFsk="
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&IV = "10dd993308d37a15b55f64a0e763f353"

&decrypted = &SymmetricBlockCipher.DoDecrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.CBC, SymmetricBlockPadding.PKCS7PADDING, &key, &IV, &encrypted)
```

### [DoAEADEncrypt](#DoAEADEncrypt)

```
SymmetricBlockCipher.DoAEADEncrypt(symmetricBlockAlgorithm, symmetricBlockMode, key, macSize, nonce, plainText)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input key: VarChar(256) hexadecimal
* Input macSize: Numeric(9.0) bit
* Input nonce: VarChar(256) hexadecimal
* Input plainText: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Returns: VarChar(9999) Base64 encoded

Encrypts the plain text with the given parameters using AEAD type mode of operation.

Warning! Key and nonce values in this document are just examples; do not use them in your applications.

```
Example:

&plainText = "Lorem ipsum dolor sit amet"
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&nonce = "10dd993308d37a15b55f64a0e763f353"

&encrypted = &SymmetricBlockCipher.DoAEADEncrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.AEAD_EAX, &key, 128, &nonce, &plainText)
```

### [DoAEADDecrypt](#DoAEADDecrypt)

```
SymmetricBlockCipher.DoAEADDecrypt(symmetricBlockAlgorithm,  symmetricBlockMode, key, macSize, nonce, encryptedInput)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input key: VarChar(256) hexadecimal
* Input macSize: Numeric(9.0) bit
* Input nonce: VarChar(256) hexadecimal
* Input encryptedInput: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Decrypts the encrypted input with the given parameters using AEAD type mode of operation.

Warning! Key and nonce values in this document are just examples; do not use them in your applications.

```
Example:

&encrypted = "7TZOJ29QeyA5pkSHKdPKVmG35HWzG/rZrVPZjMK0XLVJB6hMfpjH9Mdo"
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&nonce = "10dd993308d37a15b55f64a0e763f353"

&decrypted = &SymmetricBlockCipher.DoAEADDecrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.AEAD_EAX, &key, 128, &nonce, &encrypted)
```

### [DoEncryptFile](#DoEncryptFile)

This method is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066)

```
SymmetricBlockCipher.DoEncryptFile(symmetricBlockAlgorithm, symmetricBlockMode, symmetricBlockPadding, key, IV, pathInputFile, pathOutputFile)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input symmetricBlockPadding: SymmetricBlockPadding Domain value
* Input key: VarChar(256) hexadecimal
* Input IV:  VarChar(256) hexadecimal
* Input pathInputFile: VarChar(9999) path of the file to encrypt.
* Input pathOutputFile VarChar(9999) path of the resulting encrypted file.
* Returns: Boolean true if it was successful

Encrypts the file with the given parameters.

Warning! Key and IV values in this document are just examples; do not use them in your applications.

```
Example: 

&plainText = "Lorem ipsum dolor sit amet"
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&IV = "10dd993308d37a15b55f64a0e763f353"
&pathInputFile = "C:\temp\file.txt"
&pathOutputFile = "C:\temp\encryptedfile"

&encrypted = &SymmetricBlockCipher.DoEncrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.CBC, SymmetricBlockPadding.PKCS7PADDING, &key, &IV, &pathInputFile, &pathOutputFile)
```

### [DoDecryptFile](#DoDecryptFile)

This method is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066)

```
SymmetricBlockCipher.DoDecrypt(symmetricBlockAlgorithm, symmetricBlockMode, symmetricBlockPadding, key, IV, pathInputFile, pathOutputFile)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input symmetricBlockPadding: SymmetricBlockPadding Domain value
* Input key: VarChar(256) hexadecimal
* Input IV:  VarChar(256) hexadecimal
* Input pathInputFile: VarChar(9999) path of the encrypted file
* Input pathOutputFile: VarChar(9999) path of the resulting decrypted file
* Returns: Boolean true if it was successful

Decrypts the encrypted file with the given parameters.

Warning! Key and IV values in this document are just examples; do not use them in your applications.

```
Example:

&encrypted = "yLpJb86/rLA/9KKylktzY9i9hfFUeFduawKwyyYUFsk="
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&IV = "10dd993308d37a15b55f64a0e763f353"
&pathInputFile = "C:\temp\encryptedFile"
&pathOutputFile = "C:\temp\decryptedFile.txt"

&decrypted = &SymmetricBlockCipher.DoDecrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.CBC, SymmetricBlockPadding.PKCS7PADDING, &key, &IV, &pathInputFile, &pathOutputFile)
```

### [DoAEADEncryptFile](#DoAEADEncryptFile)

This method is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066)

```
SymmetricBlockCipher.DoAEADEncrypt(symmetricBlockAlgorithm, symmetricBlockMode, key, macSize, nonce, pathInputFile, pathOutputFile)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input key: VarChar(256) hexadecimal
* Input macSize: Numeric(9.0) bit
* Input nonce: VarChar(256) hexadecimal
* Input pathInputFile: VarChar(9999) path of the file to be encrypted
* Input pathOutputFile: VarChar(9999) path of the resulting encrypted file
* Returns: Boolean true if it was successful

Encrypts the file with the given parameters using AEAD type mode of operation.

Warning! Key and nonce values in this document are just examples; do not use them in your applications.

```
Example:

&plainText = "Lorem ipsum dolor sit amet"
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&nonce = "10dd993308d37a15b55f64a0e763f353"
&pathInputFile = "C:\temp\file.txt"
&pathOutputFile = "C:\temp\encryptedFile"

&encrypted = &SymmetricBlockCipher.DoAEADEncrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.AEAD_EAX, &key, 128, &nonce, &pathInputFile, &pathOutputFile)
```

### [DoAEADDecryptFile](#DoAEADDecryptFile)

This method is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066)

```
SymmetricBlockCipher.DoAEADDecrypt(symmetricBlockAlgorithm,  symmetricBlockMode, key, macSize, nonce, pathInputFile, pathOutputFile)
```

* Input symmetricBlockAlgorithm: SymmetricBlockAlgorithm Domain value
* Input symmetricBlockMode: SymmetricBlockMode Domain value
* Input key: VarChar(256) hexadecimal
* Input macSize: Numeric(9.0) bit
* Input nonce: VarChar(256) hexadecimal
* Input pathInputFile: VarChar(9999) path of the encrypted file
* Input pathOutputFile: VarChar(9999) path of the resulting decrypted file
* Returns: Boolean true if it was successful

Decrypts the encrypted file with the given parameters using AEAD type mode of operation.

Warning! Key and nonce values in this document are just examples; do not use them in your applications.

```
Example:

&encrypted = "7TZOJ29QeyA5pkSHKdPKVmG35HWzG/rZrVPZjMK0XLVJB6hMfpjH9Mdo"
&key = "d8367b7d71af45fdf92bcde47aad653366ffdf918350f14539bdda3d2890b69c"
&nonce = "10dd993308d37a15b55f64a0e763f353"
&pathInputFile = "C:\temp\encryptedFile"
&pathOutputFile = "C:\temp\decryptedFile.txt"

&decrypted = &SymmetricBlockCipher.DoAEADDecrypt(SymmetricBlockAlgorithm.AES, SymmetricBlockMode.AEAD_EAX, &key, 128, &nonce, &pathInputFile, &pathOutputFile)
```

## [Security tips](#Security+tips)

When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.

## [Implementation - specific details](#Implementation+-+specific+details)

* IV size must be the same as the block size

| Algorithm | Key size(bits) | Block size (bits) | Comments |
| --- | --- | --- | --- |
| AES | 128, 192, 256 | 128 |  |
| BLOWFISH | up to 448 | 64 | Cannot be used with AEAD modes |
| CAMELLIA | 128, 192, 256 | 128 |  |
| CAST5 | up to 128 | 64 | Cannot be used with AEAD modes |
| CAST6 | up to 256 | 128 |  |
| DES | 64 | 64C | Cannot be used with AEAD modes |
| TRIPLEDES | 128, 192 | 64 | Cannot be used with AEAD modes |
| DSTU7624\_128 | 128 | 128 | Input must be of the same length or longer than the block |
| DSTU7624\_256 | 256 | 256I | Input must be of the same length or longer than the block  Cannot be used with AEAD modes |
| DSTU7624\_512 | 512 | 512 | Input must be of the same length or longer than the block  Cannot be used with AEAD modes |
| GOST28147 | 256 | 64C | Cannot be used with AEAD modes |
| NOEKEON | 128 | 128 |  |
| RC2 | up to 1024 | 64C | Cannot be used with AEAD modes |
| RC6 | up to 256 | 128 |  |
| RC532 | up to 128 | 64 | Cannot be used with AEAD modes |
| RIJNDAEL\_128 | 128, 160, 224, 256 | 128 |  |
| RIJNDAEL\_160 | 128, 160, 224, 256 | 160 | Only supports EAX of the AEAD modes |
| RIJNDAEL\_192 | 128, 160, 224, 256 | 192 | Only supports EAX of the AEAD modes |
| RIJNDAEL\_224 | 128, 160, 224, 256 | 224 | Only supports EAX of the AEAD modes |
| RIJNDAEL\_256 | 128, 160, 224, 256 | 256 | Only supports EAX of the AEAD modes |
| SEED | 128 | 128 |  |
| SERPENT | 128, 192, 256 | 128 |  |
| SKIPJACK | 128 | 128 | Cannot be used with AEAD modes |
| TEA | 128 | 64 | Cannot be used with AEAD modes |
| THREEFISH\_256 | 256 | 256 | Key length must be the same as the block  Input must be of the same length or longer than the block  Cannot be used with AEAD modes |
| THREEFISH\_512 | 512 | 512 | Key length must be the same as the block  Input must be of the same length or longer than the block  Cannot be used with AEAD modes |
| THREEFISH\_1024 | 1024 | 1024 | Key length must be the same as the block  Input must be of the same length or longer than the block  Cannot be used with AEAD modes |
| TWOFISH | 128, 192, 256 | 128 |  |
| XTEA | 128 | 64 | Cannot be used with AEAD modes. |


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
