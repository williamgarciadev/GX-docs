---
title: "JWT Utils"
source_id: 43986
source_url: https://wiki.genexus.com/commwiki/wiki?43986
genexus_version: "18"
---

# JWT Utils

**Note**: This is part of the [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) and provides different utilities...

## [PrivateClaims](#PrivateClaims)

### [SetClaim](#SetClaim)

Adds a String private claim.

```
SetClaim(privateClaimKey, privateClaimValue)
```

* Input privateClaimkey: Character(100)
* Input privateClaimValue: Character(100)
* Returns: Boolean true if the claim was added correctly.

Example:

```
&isOK = &PrivateClaims.SetClaim(&key, &value)
```

### [SetNestedClaim](#SetNestedClaim)

(This method is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,))

Adds nested private claims on multiple levels as an arborescent structure

```
SetNestedClaim(privateClaimKey, privateClaimObject)
```

* Input privateClaimKey: Character(100)
* Input privateClaimObject: PrivateClaim
* Returns: Boolean true if the claim was added correctly.

Example:

```
&isOK = &PrivateClaimsFather.SetNestedClaim(&key, &PrivateClaimsSon)
```

### [SetNumericClaim](#SetNumericClaim)

(This method is available since GeneXus 17 Upgrade 2)

Adds a Numeric private claim.

```
SetNumericClaim(privateClaimKey, privateClaimValue)
```

* Input privateClaimkey: Character(100)
* Input privateClaimValue: Numeric(8.0)
* Returns: Boolean true if the claim was added correctly.

Example:

```
&isOK = &PrivateClaims.SetNumericClaim(&key, &value)
```

### [SetBooleanClaim](#SetBooleanClaim)

(This method is available since GeneXus 17 Upgrade 2)

Adds a Boolean private claim.

```
SetBooleanClaim(privateClaimKey, privateClaimValue)
```

* Input privateClaimkey: Character(100)
* Input privateClaimValue: Boolean
* Returns: Boolean true if the claim was added correctly.

Example:

```
&isOK = &PrivateClaims.SetBooleanClaim(&key, &value)
```

### [SetDateClaim](#SetDateClaim)

(This method is available since GeneXus 17 Upgrade 2)

Adds a Date private claim.

```
SetDateClaim(privateClaimKey, privateClaimValue)
```

* Input privateClaimkey: Character(100)
* Input privateClaimValue: Numeric(11.0)
* Returns: Boolean true if the claim was added correctly.

Example:

```
&isOK = &PrivateClaims.SetDateClaim(&key, &value)
```

* JWT uses an integer defined as [UNIX time](https://en.wikipedia.org/wiki/Unix_time) format, which is the number of seconds since the 1st of January of 1970 at 00.00.00. The complexity of this calculation is transparent to the user.

## [Revocation List](#Revocation+List)

Defines a revocation list to be used on token verification.

### [DeleteFromRevocationList](#DeleteFromRevocationList)

Deletes a token ID from the revocation list.

```
DeleteFromRevocationList(id)
```

* Input id: Character(100)
* Returns: Boolean, true if it was successfully removed.

Example:

```
&RList.DeleteFromRevocationList(&id)
```

### [AddIDToRevocationList](#AddIDToRevocationList)

Adds a token ID to the revocation list.

```
AddIDToRevocationList(id)
```

* Input id: Character(100)
* Returns void

Example:

```
&RList.AddIDToRevocationList(&id)
```

### [IsInRevocationList](#IsInRevocationList)

Verifies if a given ID is included in the revocation list.

```
IsInRevocationList(id)
```

* Input id: Character(100)
* Returns true if the ID is present in the revocation list.

## [GUID](#GUID)

Deprecated since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,), use [GeneXus GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) instead.

GUID generator utility for token ID generation.

### [Generate](#Generate)

Generates a string GUID using platform default implementation.

```
Generate()
```

* Returns Character(100) GUID

Example

```
 &guid = &GUID.Generate()
```

Implementation details:

* Java - uses java.util.UUID implementation
* .Net - uses System.Guid implementation

## [DateUtil](#DateUtil)

Deprecated since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,), use [GeneXus DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) instead.

It retrieves system date and time using seconds to calculate registered time validating claims on the string format yyyy/MM/dd HH:mm:ss specific for the module definition.

This utility is made to bring a tool to manage Dates and Times in a human-readable form.

JWT uses an integer defined as [UNIX time](https://en.wikipedia.org/wiki/Unix_time) format, which is the number of seconds since the 1st of January of 1970 at 00.00.00. The complexity of this calculation is transparent to the user.

### [GetCurrentDate](#GetCurrentDate)

Gets the current system date.

```
GetCurrentDate()
```

* Returns Character(100) current date and time using seconds on the yyyy/MM/dd HH:mm:ss specific format.

Example:

```
&date = &DateUtil.GetCurrentDate()
```

### [CurrentPlusSeconds](#CurrentPlusSeconds)

Gets the system's current date and adds the specified seconds returning a string with the specific format for the module definition.

```
CurrentPlusSeconds(seconds)
```

* Input seconds: Numeric(12.0)
* Returns Character(100) string date formatted as yyyy/MM/dd HH:mm:ss

Example:

```
&date = &DateUtil.CurrentPlusSeconds(&seconds)
```

### [CurrentMinusSeconds](#CurrentMinusSeconds)

Gets the system's current date and subtracts the specified seconds returning a string with the specific format for the module definition.

```
CurrentMinusSeconds(seconds)
```

* Input seconds: Numeric(12.0)
* Returns Character(100)  string date formated yyyy/MM/dd HH:mm:ss

Example:

```
&date = &DateUtil.CurrentMinusSeconds(&seconds)
```

## [UnixTimestampCreator](#UnixTimestampCreator)

Available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)

It creates a matching Unix Timestamp from a Date.

### [Create](#Create)

It creates a matching Unix Timestamp from a string date formated yyyy/MM/dd HH:mm:ss.

```
Create(date)
```

* Input VarChar(9999) string date formated yyyy/MM/dd HH:mm:ss
* Returns VarChar(9999) string Unix Timestamp

Example:

```
&timestamp = &UnixTimestapCreator.Create("2023/07/24 12:42:00")
```

Expected behavior:

* If Java generator is used it creates a timestamp using GMT0.
* If .Net or Net Framework generators are used it takes the server´s GMT deviation.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
