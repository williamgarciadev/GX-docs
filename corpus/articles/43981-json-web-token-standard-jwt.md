---
title: "JSON Web Token Standard (JWT)"
source_id: 43981
source_url: https://wiki.genexus.com/commwiki/wiki?43981
genexus_version: "18"
---

# JSON Web Token Standard (JWT)

The JSON Web Token standard is defined in [RFC7519](https://tools.ietf.org/html/rfc7519)

## [JSON Web Token in a nutshell](#JSON+Web+Token+in+a+nutshell)

A JWT is composed of 3 Base64 encoded strings concatenated by a dot  (".").

**Header.Payload.Signature**

In this context, the JSON entries are called claims.

### [Header](#Header)

It has 2 mandatory claims and 1 optional claim.

* **alg** - **Mandatory**. It indicates the algorithm used to sign the token.
* **typ** - **Mandatory**. It assigns a type, which in this module will always be "JWT."
* **cty** - **Optional**. It is used to indicate nested JWT; this module does not implement nested JWT.

### [Payload](#Payload)

It can have 3 types of claims: Registered, Public and Private. The last one represents user-defined claims and the others are predefined on the standard.

### [Registered claims](#Registered+claims)

These claims are defined by the standard and each one has its own type and utility also predefined. The names are mostly self-explanatory.

They are **optional**, which means a JWT can be created and be valid without using any of these types of claims.

* **iss** - issuer
* **exp** - expiration time date
* **sub** - subject
* **aud** - audience
* **nbf** -  not before date
* **iat** - issued at date
* **jti** - JWT ID, it must be a GUD

### [Public claims](#Public+claims)

These claims are defined by the standard and must be registered by the IANA or at least represent a unique URI.

They are **optional**, which means a JWT can be created and be valid without using any of these types of claims.

### [Private claims](#Private+claims)

They are used-defined claims and key-value pairs that represent the data being protected.

Private claims are **mandatory**by definition.

### [Signature](#Signature)

Base64 encoded JSON with the signature using the Header's indicated algorithm.

[Source](https://jwt.io/)

### [Date representation on JWT](#Date+representation+on+JWT)

The [RFC](https://tools.ietf.org/html/rfc7519) defines the way dates must be included on JWT.and it is using the NumericDate format which it defines as:

*"A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds. This is equivalent to the IEEE Std 1003.1, 2013 Edition [POSIX.1](https://tools.ietf.org/html/rfc7519#ref-POSIX.1) definition "Seconds Since the Epoch", in which each day is accounted for by exactly 86400 seconds, other than that non-integer values can be represented. See [RFC 3339](https://tools.ietf.org/html/rfc3339) [RFC3339](https://tools.ietf.org/html/rfc3339) for details regarding date/times in general and UTC in particular."*

[More information](https://en.wikipedia.org/wiki/Unix_time#::text=Unix%20time%20(also%20known%20as,UTC%20on%201%20January%201970.)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
