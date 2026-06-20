---
title: "ClientInformation external object (GeneXus 18 Upgrade 13 or prior)"
source_id: 60693
source_url: https://wiki.genexus.com/commwiki/wiki?60693
genexus_version: "18"
---

# ClientInformation external object (GeneXus 18 Upgrade 13 or prior)

The ClientInformation external object contains a set of properties intended to provide access to the client machine information (browser or device) where the application is running.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

**Note**: Only the AppVersionCode and AppVersionName properties apply to the Angular generator.

### [Id property](#Id+property)

Returns an acceptable device identifier in most implementations.  
Read more at [ClientInformation.Id property](https://wiki.genexus.com/commwiki/wiki?20198).

### [OSName property](#OSName+property)

Returns the operating system name running on the device.

|  |  |
| --- | --- |
| **Return value** | [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778). Returned values are: "iPad", "iPhone", "iPod" and "Android". |
| **Parameters** | None |

### [OSVersion property](#OSVersion+property)

Returns the version of the operating system running on the device.

|  |  |
| --- | --- |
| **Return value** | [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778). The returned value format depends on the operating system. |
| **Parameters** | None |

### [Language property](#Language+property)

Returns the device language.

|  |  |
| --- | --- |
| **Return value** | Character(20) with '<locale>,<language>' format (e.g. 'en-US,en'). |
| **Parameters** | None |

A possible use case, for example, is to measure the number of devices accessing the application that lack language settings not provided by the application. In this way, priorities can be established to make the application international.

Note that the application will be automatically displayed in the language more appropriate for the user, depending on the device language and the languages available on the Knowledge Base. The [GetLanguage function](https://wiki.genexus.com/commwiki/wiki?18751) must be used to determine programmatically the language used to display the application.

### [DeviceType property](#DeviceType+property)

Returns the Device Type.

|  |  |
| --- | --- |
| **Return value** | One of the possible values of the "SmartDeviceType" [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207): Android, Apple, Web |
| **Parameters** | None |

### [PlatformName property](#PlatformName+property)

Returns the platform name of the device as completely as possible.

|  |  |
| --- | --- |
| **Return value** | [VarChar(128)](https://wiki.genexus.com/commwiki/wiki?6778). The platform name is composed of three device features (OS, Type, and Size). See below a table with the possible device features. |
| **Parameters** | None |

**Device features**

|  |  |  |
| --- | --- | --- |
| **OS** | **Type** | **Size** |
| Android | Phone |  |
| Tablet | 7'' |
| 10'' |
| Apple | iPad |  |
| iPhone |  |

PlatformName property value sample: *Android Tablet 10"*

### [AppVersionCode property](#AppVersionCode+property)

Returns the version number of the application set in the [Android Version Code property](https://wiki.genexus.com/commwiki/wiki?58703), [Apple Version Code property](https://wiki.genexus.com/commwiki/wiki?39496), or [Web Frontend Version Code property](https://wiki.genexus.com/commwiki/wiki?50807) (according to your platform).

```
&AppVersionCode = ClientInformation.AppVersionCode
```

### [AppVersionName property](#AppVersionName+property)

Returns the version name of the application set in the [Android Version Name property](https://wiki.genexus.com/commwiki/wiki?37261), [Apple Version Name property](https://wiki.genexus.com/commwiki/wiki?58704), or [Web Frontend Version Name property](https://wiki.genexus.com/commwiki/wiki?50808) (according to your platform).

```
&AppVersionName = ClientInformation.AppVersionName
```

### [ApplicationId property](#ApplicationId+property)

Returns the application identifier. This is the [package name](https://wiki.genexus.com/commwiki/wiki?17814) in the case of Android applications and the [bundle identifier](https://wiki.genexus.com/commwiki/wiki?37617) in the case of Apple applications.

**Note**: This property is available since [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44454,,).

## [Methods](#Methods)

It does not have any.

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
