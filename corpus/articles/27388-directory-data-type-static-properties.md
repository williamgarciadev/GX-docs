---
title: "Directory Data Type Static properties"
source_id: 27388
source_url: https://wiki.genexus.com/commwiki/wiki?27388
genexus_version: "18"
---

# Directory Data Type Static properties

GeneXus has specific data types such as [Directory](https://wiki.genexus.com/commwiki/wiki?6567) and [File](https://wiki.genexus.com/commwiki/wiki?6915) that allow working directly with the file system. However, in Smart Devices several restrictions exist in relation to which directories can be manipulated by the application, either in [Apple](https://wiki.genexus.com/commwiki/wiki?14917) or [Android](https://wiki.genexus.com/commwiki/wiki?14453) smart devices.

The [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567) has 3 static, read-only properties which help the developer to work with the file system in Smart Devices and Web/Win applications.

### [**ApplicationDataPath**](#ApplicationDataPath)

The directory where the files related to the application are stored.

In iOS offline applications, this path matches the “Documents” folder path inside the application.

In Android offline applications, this path matches the “Private Storage” folder path of the application.

For the other generators (Web or Win) this path matches the “%USERPROFILE%” directory.

### [**TemporaryFilesPath**](#TemporaryFilesPath)

The directory where temporary files of the application are stored.

For offline applications, either iOS or Android, files and folders in this directory may be removed by the operating system. In addition, it is important for the developer to check if these files or directories have been correctly removed.

For the other generators (Web or Win) this path matches the “%TEMP%” directory.

### [**ExternalFilesPath**](#ExternalFilesPath)

The path to the external storage device, if it exists; otherwise, this property has the value of the property "ApplicationDataPath".

In iOS, because there are no devices with external storage, this property has the same value as the “ApplicationDataPath” property. The same happens to Android devices when they don't have an external storage device.

### [**CacheFilesPath**](#CacheFilesPath)

Indicates the directory where the application cache is located.  
  
In iOS, it corresponds to the "Library\Caches" directory of the application. The data stored within the cache directory can be deleted by the operating system at any time, but it is expected that they persist throughout several executions of the application.  
  
**Note:**  
This functionality is only available for the iOS as of [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,) generator.

### [**Considerations**](#Considerations)

#### [File separator at the end of the paths](#File+separator+at+the+end+of+the+paths)

All these properties do NOT include the file separator character at the end of the path. Therefore, the developer has to include it by using the Separator method of the [File data type](https://wiki.genexus.com/commwiki/wiki?6915).

#### [Server-side events](#Server-side+events)

In smart device applications with Online architecture, the Start, Refresh and Load events run on the server-side. Therefore, if these properties are used in these events, their values will use the server property values mentioned above. See [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234) for more information.

#### [Relative paths](#Relative+paths)

If the specified path is relative, the default directory is “Directory.ApplicationDataPath”.

Therefore, this line of code:

```
&file.Source = "someFile.txt"
```

… is equal to this line of code:

```
&file.Source = Directory.ApplicationDataPath + &file.Separator + "someFile.txt"
```

#### [Absolute paths](#Absolute+paths)

In Android Smart Devices, absolute paths are supported and they always start with the character “/”. For instance:

```
&file.Source = "/sdcard/image.jpg"
```

In iOS Smart Devices, absolute paths are not supported by the platform.

#### [Platform-specific paths](#Platform-specific+paths)

In iOS, access is supported to the directory where the KB images are located by using a variable path called “$RESOURCES”. For example, if the Knowledge Base has an image called “MyImage.png”, you can use this stub of code to use the image:

```
&file.Source = "$RESOURCES/MyImage.png"
&destPath = Directory.TemporaryFilesPath + &file.Separator + "MyImageCopy.png"
&file.Copy(&destPath)
```

### [**Availability**](#Availability)

These properties are available as from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [**See also**](#See+also)

* [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567)
* [File data type](https://wiki.genexus.com/commwiki/wiki?6915)


|  |
| --- |
| **Backlinks** |
| [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567) | [HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846) |

---
