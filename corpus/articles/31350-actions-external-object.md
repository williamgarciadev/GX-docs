---
title: "Actions external object"
source_id: 31350
source_url: https://wiki.genexus.com/commwiki/wiki?31350
genexus_version: "18"
---

# Actions external object

The Actions external object provides an API that encapsulates common actions to be executed programmatically.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [Login method](#Login+method)

Use this action if you need to execute the standard batch login against the OAuth server. It returns the success of the operation.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | User:[Character(40)](https://wiki.genexus.com/commwiki/wiki?6777), Password:[Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [LoginExternal method](#LoginExternal+method)

This action executes the batch login against the OAuth server for an External login type. Additional parameters can be added.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | Type:[Character(4)](https://wiki.genexus.com/commwiki/wiki?6777), User:[Character(4)](https://wiki.genexus.com/commwiki/wiki?6777), Password:[Character(4)](https://wiki.genexus.com/commwiki/wiki?6777) [, AddionalParameters:LoginExternalAddionalParameters] |

### [Logout method](#Logout+method)

Use this action to execute the standard logout against the OAuth server.  
If the object where the actions are performed requires authentication, the Login object configured on [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) will be called.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [GoHome method](#GoHome+method)

Resets the application to the main object.  
Split [navigation style](https://wiki.genexus.com/commwiki/wiki?16229) does not apply, it will return to the first object who was called on the right pane whenever possible.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [ReturnTo method](#ReturnTo+method)

Returns to the object specified in the parameter. If it is present more than once in the call stack, it will return to the most recent instance. The case does not apply when the object is not present on the left frame of the Split [navigation style](https://wiki.genexus.com/commwiki/wiki?16229).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [Save method](#Save+method)

This action executes the standard save operation in the current edit form. Check the following [use case](https://wiki.genexus.com/commwiki/wiki?16015).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [Cancel method](#Cancel+method)

This action returns to the object caller and quits the execution of the Composite Block. Check the following [use case](https://wiki.genexus.com/commwiki/wiki?18363).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [Delete method](#Delete+method)

This action executes the standard delete operation in the edit form.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [TakeApplicationScreenshot method](#TakeApplicationScreenshot+method)

Takes an application screenshot for further use like sharing, save in library, etc.

|  |  |
| --- | --- |
| **Return value** | [Image](https://wiki.genexus.com/commwiki/wiki?15204) |
| **Parameters** | None |

## [Events](#Events)

It does not have any.

## [Structure Data Types](#Structure+Data+Types)

### [LoginExternalAddionalParameters](#LoginExternalAddionalParameters)

This structure contains a set of additional information that the login request must send to the external program for validation.

* Property:Collection
  + Id:[Character(40)](https://wiki.genexus.com/commwiki/wiki?6777)  
    Property identifier (or key).
  + Value:[Character(40)](https://wiki.genexus.com/commwiki/wiki?6777)  
    Property value.

## [Notes](#Notes)

* The Return() and Refresh() methods in the previous version are substituted by [Return command](https://wiki.genexus.com/commwiki/wiki?31353) and [Refresh command](https://wiki.genexus.com/commwiki/wiki?25060).
* Since GeneXus 16 Upgrade 3, the behavior of the GoHome method has been changed for iOS. Now when executing the method it will cancel the actions still executing in the SDPanel. See [SAC#4522](https://www.genexus.com/developers/websac?es,,,45225)[6](https://www.genexus.com/developers/websac?es,,,45226).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | SmartDevices(Android,iOS)1 |

1 - Make sure to use this API from user events, otherwise the following error will occur:

```
error spc0200: External Object GeneXus\SD\Actions does not implement method 'MethodName' for Android|iOS environment.
```

## [See also](#See+also)

* [HowTo: Use the Cancel Method from Actions in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18363)
* [HowTo: Use Save method from Actions external object](https://wiki.genexus.com/commwiki/wiki?16015)
* [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512)
* [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007)
* [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208)
* [GAM - Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013)


|  |
| --- |
| **Backlinks** |
| [Back event](https://wiki.genexus.com/commwiki/wiki?24950) | [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) |
| [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007) | [GAM - Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013) | [GAM - One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50664) | [GAM - Time Based One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50708) |
| [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) | [GAM - Two factor Authentication for mobile](https://wiki.genexus.com/commwiki/wiki?50726) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [HowTo: Use Save method from Actions external object](https://wiki.genexus.com/commwiki/wiki?16015) | [Real-time translation of RTL languages](https://wiki.genexus.com/commwiki/wiki?54482) | [Real-time translation of RTL languages (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54495) | [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757) |
| [SetLanguage function (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54431) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
