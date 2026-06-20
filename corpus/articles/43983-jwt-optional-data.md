---
title: "JWT Optional Data"
source_id: 43983
source_url: https://wiki.genexus.com/commwiki/wiki?43983
genexus_version: "18"
---

# JWT Optional Data

**Note**: This is part of the [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980)..

## [JWTOptions](#JWTOptions)

It is used to add optional values for token creation and validation.

### [AddRegisteredClaim](#AddRegisteredClaim)

Adds a standard registered claim value to the JWTOptions.

```
AddRegisteredClaim(registeredClaimkey,  registeredClaimValue)
```

* Input registeredClaimkey: RegisteredClaim domain value
* Input registeredClaimValue: Character(100), if it is a Date use Posix NumericDate format as it is defined on the [RFC](https://tools.ietf.org/html/rfc7519)
* Returns: Boolean, true if it was successfully added.

Example:

```
&result = &JWTOptions.AddRegisteredClaim(RegisteredClaim.iss, "GX SA")
```

### [AddPublicClaim](#AddPublicClaim)

Adds a standard public claim value to the JWTOptions.

```
AddPublicClaim(publicClaimkey, publicClaimDomain)
```

* Input publicClaimKey: Character(20)
* Input publicClaimDomain: VarChar(256)
* Returns: Boolean, true if it was successfully added.

Example:

```
 &result = &JWTOptions.AddPublicClaim(&key, &Uri)
```

### [SetSecret](#SetSecret)

Adds a secret to be used to sign or verify the token with a symmetric algorithm.

```
SetSecret(value)
```

* Input value: VarChar(256) Hexadecimal secret for symmetric algorithm
* Returns void

Example:

```
&JWTOptions.SetSecret(&secret)
```

### [AddCustomTimeValidationClaim](#AddCustomTimeValidationClaim)

Adds a Registered Claim for time validation with tolerance in seconds.

```
AddCustomTimeValidationClaim(String registeredClaimKey, String value, String customTime)
```

* Input registeredClaimKey: RegisteredClaim domain value of time validation type (exp, nbf or iat).
* Input value: Character(100) Date with the specific format yyyy/MM/dd HH:mm:ss.
* Input customTime: Character(100) time in seconds to define tolerance for claim validation.
* Returns: Boolean, true if it was successfully added.

Example:

```
&JWTOptions.AddCustomTimeValidationClaim(RegisteredClaim.iat, DateUtil.getCurrentDate(), "20")
```

### [SetPrivateKey](#SetPrivateKey)

Adds a private key to be used on the token signature using an asymmetric algorithm.

```
SetPrivateKey(privateKey)
```

* Input privateKey: PrivateKey type value
* Returns void

Example:

```
&JWTOptions.SetPrivateKey(&PrivateKey)
```

### [SetCertificate](#SetCertificate)

Adds a public key to be used on the token verification using an asymmetric algorithm.

```
SetCertificate(certificate)
```

* Input certificate: Certificate type value
* Returns void

Example:

```
&JWTOptions.SetCertificate(&Certificate)
```

### [AddRevocationList](#AddRevocationList)

Adds a revocation list to be verified on token verification.

```
AddRevocationList(revocationList)
```

* Input revocationList: RevocationList type value
* Returns void

Example:

```
&JWTOptions.AddRevocationList(&revocationList)
```

### [DeleteRevocationList](#DeleteRevocationList)

Deletes the revocation list contained in this instance of the JWTOptions.

```
DeleteRevocationList()
```

* Returns void

Example:

```
&JWTOptions.DeleteRevocationList()
```

### [AddHeaderParameter](#AddHeaderParameter)

This method is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)

Generic method to add parameters to the token's header. It does not allow nested headers.

```
AddHeaderParameters(name, value)
```

* Input name. Character(100)
* Input value. Character(100)
* Returns void

Example:

```
&JWTOptions.AddHeaderParameter(&name, &value)
```

### [SetPublicKey](#SetPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

Adds a public key to be used on the token signature using an asymmetric algorithm.

```
SetPublicKey(publicKey)
```

* Input publicKey: PublicKey type value
* Returns void

Example:

```
&JWTOptions.SetPublicKey(&publicKey)
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
