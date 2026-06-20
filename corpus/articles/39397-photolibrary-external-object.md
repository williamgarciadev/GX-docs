---
title: "PhotoLibrary external object"
source_id: 39397
source_url: https://wiki.genexus.com/commwiki/wiki?39397
genexus_version: "18"
---

# PhotoLibrary external object

The Photo Library API enables you to interact with the photo gallery of the device.

As the [Camera external object](https://wiki.genexus.com/commwiki/wiki?31298) enables an app to interact with the photo camera of the device, this API allows the application to save or get an image or a video from the native photo gallery. This article focuses on what this API does and gives an example of how to use it in a Native Mobile application.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [Save method](#Save+method)

The Save method enables the application to store an image on the device's native photo gallery application.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Image:[Image](https://wiki.genexus.com/commwiki/wiki?15204) |

### [Save Video method](#Save+Video+method)

The SaveVideo method enables the application to store a video on the device's native photo gallery application.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Video:[Video](https://wiki.genexus.com/commwiki/wiki?16608) |

### [ChooseImage method](#ChooseImage+method)

This method invokes the native photo gallery app and lets the user choose one image to be used in the application.  
It returns a variable based on Image data type.

|  |  |
| --- | --- |
| **Return value** | [Image](https://wiki.genexus.com/commwiki/wiki?15204) |
| **Parameters** | None |

**Note**: This method does not work using the emulator. It only works on Apple devices.

### [ChooseVideo method](#ChooseVideo+method)

This method invokes the native photo gallery app and lets the user choose one video to be used in the application.  
It returns a variable based on [Video data type](https://wiki.genexus.com/commwiki/wiki?16608).

|  |  |
| --- | --- |
| **Return value** | [Video](https://wiki.genexus.com/commwiki/wiki?16608) |
| **Parameters** | None |

### [ChooseImages method](#ChooseImages+method)

This method invokes the native photo gallery app and lets the user choose several images to be used in the application.   
It returns a collection of items based on Image data type.

|  |  |
| --- | --- |
| **Return value** | ImagesCollection |
| **Parameters** | None |

**Note**: This method does not work using the emulator. It only works on Apple devices.

## [Events](#Events)

It does not have any.

## [Structured Data Types](#Structured+Data+Types)

### [ImagesCollection](#ImagesCollection)

A collection of [Image data type](https://wiki.genexus.com/commwiki/wiki?15204).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) (only for [ChooseImage](https://wiki.genexus.com/commwiki/wiki?39397) and [ChooseImages](https://wiki.genexus.com/commwiki/wiki?39397) methods). |

## [Availability](#Availability)

This external object is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

* The ChooseImages method is available as of [GeneXus 15 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?37491,,).

## [Notes](#Notes)

* As of GeneXus 17, the PhotoLibrary external object uses the new [PHPicker](https://developer.apple.com/documentation/photokit/phpickerviewcontroller) when running in iOS 14 and above, which improves user privacy regarding the application access to the photo library and replaces the now deprecated UIImagePickerViewController.

## [See also](#See+also)

* [HowTo: Using PhotoLibrary external object for Smart Devices](https://wiki.genexus.com/commwiki/wiki?26933)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Using PhotoLibrary external object for Smart Devices](https://wiki.genexus.com/commwiki/wiki?26933) |
| [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
