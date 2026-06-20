---
title: "CryptoHash data type"
source_id: 33457
source_url: https://wiki.genexus.com/commwiki/wiki?33457
genexus_version: "18"
---

# CryptoHash data type

**Warning**: This data type will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace this data type. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

CryptoHash belongs to the [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980).

### [CryptoHash methods](#CryptoHash+methods)

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Compute(**text:String[,key:String]**)** | Returns the text resulting from the application of the hash function on the text entered.  As [Keyed-Hash Message Authentication Code](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code) is supported, a key can be optionally passed to the method. |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Algorithm**:String | Allows us to specify the hash algorithm that will be applied when the Compute(String,[key]) method is invoked. The SHA256 is used by default.  CryptoHashAlgorithm is a predefined enumerated domain containing the Hash algorithms supported. |

### [Example](#Example)

The example below uses the Hash algorithm SHA1.

```
&CryptoHash.Algorithm = CryptoHashAlgorithm.SHA1 //&CryptoHash is of CryptoHash type.
&resultstringSHA1 = &CryptoHash.Compute(&text)
```

The following example uses the HMAC SHA512 algorithm.

```
&CryptoHash.Algorithm = CryptoHashAlgorithm.HMACSHA512 //&CryptoHash is of CryptoHash type.
&resultingstringHMACSHA512 = &CryptoHash.Compute(&text,&key)
```

### [Notes](#Notes)

* The SHA256 is used by default since GeneXus Evolution v15 U10. The previous versions use SHA1
* When using a Non-Keyed-Hash Message Authentication code in Compute method, if a key is specified the following error is thrown:  
  *3.00 Algorithm does not support Hashing with Key. Please use HMAC instead or remove the Key parameter*
* When using sing Keyed-Hash Message Authentication code, the &CryptoHash.Algorithm property should be set to HMACSHA256, HMACSHA1, HMACSHA384, HMACSHA512, or HMACMD5.  
  In such case, if &CryptoHash.Algorithm is set to any of these values and no key is specified, the following error is thrown:  
  *4.00 Key must be specified.*  
  Another possible error is the following:  
  *5.00 Invalid Key.*

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java, Apple |

### [Availability](#Availability)

The availability of the Keyed-Hash Authentication is as of [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,).  
For Native Mobile environments, is available as of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) |

---
