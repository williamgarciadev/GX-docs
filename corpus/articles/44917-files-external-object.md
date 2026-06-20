---
title: "Files external object"
source_id: 44917
source_url: https://wiki.genexus.com/commwiki/wiki?44917
genexus_version: "18"
---

# Files external object

The Files external object enables you to programmatically select files from your device to be assigned to [Blob](https://wiki.genexus.com/commwiki/wiki?6704) and [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420) attributes and variables.

|  |  |
| --- | --- |
|  |  |

## [**Properties**](#Properties)

It does not have any.

## [**Methods**](#Methods)

### [**ChooseFile method**](#ChooseFile+method)

Selects a file from the device.

|  |  |
| --- | --- |
| **Return value** | [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420) |
| **Parameters** | [ acceptedTypes:[VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) ] |

The method will display the available sources in the device to select a file. In the case of iOS applications, these sources will be:

* Local file (files in the application's sandbox)
* [Files application](https://support.apple.com/en-us/HT206481) (introduced from iOS 11)
* Image gallery

`[imagen omitida: wiki id 44919]`

The optional *acceptedTypes* parameter must be specified as a comma-separated list of mime types, such as:

* *"image/\*"* to indicate that only images files can be selected,
* "*application/pdf*" for PDF files, or
* "*image/\*,application/pdf*" to allow selecting images and PDF files.

Note: the *acceptedTypes* parameter is available in Android since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,). It is not yet available in iOS.

If the *acceptedTypes* parameter is not present, then all file types are shown.

### [**SaveToFolder method**](#SaveToFolder+method)

Saves the specified File to the device system folder.

**Return Value**[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)

**Parameters** fileUri**:**[URL](https://wiki.genexus.com/commwiki/wiki?15668), destination:DeviceFolder, /\* saveMode: SaveMode \*/.

The parameter saveMode is optional. The default behavior is Rename.

### [**IsDeviceFolderAvailable method**](#IsDeviceFolderAvailable+method)

Determines if the specified system folder is available on the device running the application.

Return value: [Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

Parameters: destination:DeviceFolder.

Note: The Android implementation always returns True. iOS may return False if there is no iCloud account configured on the device.

## [**Events**](#Events)

It does not have any

## [**Domains**](#Domains)

**DeviceFolder**

Values: Documents, Dowloads.

**SaveMode**

Values:

Rename: If a file already exists in destination, creates a copy.  
Replace: If a file already exists in destination, will replace the content if possible. If not possible for secure reason, do a Renamed  
AskUser: If file already exists in destination, will ask the user if to do a Replacement or Rename.

## [**Considerations**](#Considerations)

If the file already exists in the destination folder, by default it is renamed so that both files are kept. Override with the new name is composed by the original name, an index between parentheses, and the file extension.  
For example, when saving Name.ext, if it already exists, it will be saved as Name(1).ext. If Name(1).ext also exists, Name(2).ext will be used. And so on.

If SaveMode is Replace, If the file already exists in the destination folder, it is overriding with the new content if possible. If not, a Renamed is performing.

## [**Example**](#Example)

```
Event 'SelectFile'
  Composite
    &BlobFile = Files.ChooseFile()
    SaveFile(&BlobFile)
  EndComposite
EndEvent

Event 'SaveToFolder'

&fileUrl = Reporte("MyPublicReport")
Files.SaveToFolder( &fileUrl, DeviceFolder.Documents)

EndEvent
```

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices |


|  |
| --- |
| **Backlinks** |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
