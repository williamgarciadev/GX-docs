---
title: "RemoteConfig external object"
source_id: 48160
source_url: https://wiki.genexus.com/commwiki/wiki?48160
genexus_version: "18"
---

# RemoteConfig external object

RemoteConfig external object allows interacting with a remote configuration service to fetch new configuration values and apply them, and also to read the values for a given configuration.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [LastSuccessfulFetch property](#LastSuccessfulFetch+property)

Indicates the timestamp of the last time the configuration was fetched successfully from the server.

|  |  |
| --- | --- |
| **Return value** | [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) |

Note:

* if the Remote Configuration Property is set to None, or if the values haven’t been fetched yet, it returns the empty DateTime. If the last fetch resulted in an error, the DateTime returned corresponds to the previous fetch.
* this property also takes into account fetch operations performed automátically.

### [LastFetchStatus property](#LastFetchStatus+property)

Returns the last fetch status.

|  |  |
| --- | --- |
| **Return value** | [FetchStatus](https://wiki.genexus.com/commwiki/wiki?48160) |

## [Methods](#Methods)

### [HasValue method](#HasValue+method)

Returns True if there is a value with the given key (being it a default value or a value fetched from the server), False otherwise.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

### [GetStringValue method](#GetStringValue+method)

Returns the configured value for the given key as a String.

|  |  |
| --- | --- |
| **Return value** | [VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

Considerations:

* If the value has been fetched from the server, it returns that value. If not, the default value is returned. If there is no value from the server, nor a default value, the empty String is returned.
* If the Remote Configuration Provider is set to None, this method returns the empty string.

### [GetIntegerValue method](#GetIntegerValue+method)

Returns the configured value for the given key as a number without decimals.

|  |  |
| --- | --- |
| **Return value** | [Numeric(9.0)](https://wiki.genexus.com/commwiki/wiki?6793) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

Considerations: same consideration as from GetStringValue apply.

### [GetDecimalValue method](#GetDecimalValue+method)

Returns the configured value for the given key as a number with decimals.

|  |  |
| --- | --- |
| **Return value** | [Numeric(12.3)](https://wiki.genexus.com/commwiki/wiki?6793) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

Considerations: same consideration as from GetStringValue apply.

### [GetBooleanValue method](#GetBooleanValue+method)

Returns the configured value for the given key as boolean.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

Considerations: same consideration as from GetStringValue apply.

### [GetDateValue method](#GetDateValue+method)

Returns the configured value for the given key as a date.

|  |  |
| --- | --- |
| **Return value** | [Date](https://wiki.genexus.com/commwiki/wiki?7373) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

Considerations: same consideration as from GetStringValue apply.

### [GetDatetimeValue](#GetDatetimeValue)

Returns the configured value for the given key as a date-time.

|  |  |
| --- | --- |
| **Return value** | [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) |
| **Parameters** | Key: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |

Considerations: same consideration as from GetStringValue apply.

### [Fetch method](#Fetch+method)

Tries to get the values synchronically from the server. Returns True if successful, False otherwise.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | (none) |

If the Remote Configuration Provider is set to None, this method returns False and finishes immediately.

### [Apply method](#Apply+method)

Tries to apply the values fetched by the last fetch operation (being it automatic or manual). Returns True if successful, False otherwise.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | (none) |

If the Remote Configuration Provider is set to None or if there are no fetched values, this method returns False and finishes immediately.

## [Domains](#Domains)

### [FetchStatus domain](#FetchStatus+domain)

Enumerated domain returned by the LastFetchStatus property.

| Value | Description |
| --- | --- |
| None | The Fetch operation has never been performed |
| Sucess | The last Fecth operation ended successfuly |
| Failure | The last Fecth operation could not be completed |

## [Code Examples](#Code+Examples)

See the [Examples section in Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Native Mobile (Android, iOS) |

## [Availability](#Availability)

This external object is available as form [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

## [See also](#See+also)

* [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101)


|  |
| --- |
| **Backlinks** |
| [Application of Fetched Values property](https://wiki.genexus.com/commwiki/wiki?48144) | [Default Values property](https://wiki.genexus.com/commwiki/wiki?48142) | [Fetching of Remote Values property](https://wiki.genexus.com/commwiki/wiki?48143) |
| [Minimum Fetch Interval property](https://wiki.genexus.com/commwiki/wiki?48145) | [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101) | [Remote Configuration Provider property](https://wiki.genexus.com/commwiki/wiki?48146) | [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
