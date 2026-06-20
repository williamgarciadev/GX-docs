---
title: "Directory data type"
source_id: 6567
source_url: https://wiki.genexus.com/commwiki/wiki?6567
genexus_version: "18"
---

# Directory data type

Directory is a data type that allows the management of system directories. It simplifies the development of applications that need to execute actions over system directories and files.

Use Directory data type for typical operations such as creating, copying, moving, renaming and deleting directories. You can also use the Directory data type to obtain the directory attributes such as modification date, time and size.

By defining variables based on this data type you are able to set and use the following properties and methods.

## [Properties](#Properties)

|  |  |
| --- | --- |
| * Source | Selects the directory in the specified path. |
| * [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) | Returns the result of the last operation. It has one of the following values:  **0**: Operation completed successfully.  **1**: Invalid directory instance - when the Source property was not set.  **2**: Directory does not exist.  **3**: Directory already exists.  **4**: Directory not empty.  **100**: Security error.  **-1**: Undefined error |
| * [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) | Returns the result description of the last operation |

## [Static properties](#Static+properties)

|  |  |
| --- | --- |
| * ApplicationDataPath | The directory where files related to the application are stored. |
| * TemporaryFilesPath | The directory where temporary files of the application are stored.  C# - It is implemented using [Path.GetTempPath()](https://msdn.microsoft.com/en-us/library/system.io.path.gettemppath(v=vs.110).aspx) method.  Java - It returns the value of System.getProperty("java.io.tmpdir"). |
| * ExternalFilesPath | The path to the external storage device, if it exists, otherwise this property has the value of the property "ApplicationDataPath". |
| * CacheFilesPath | The directory where the cache files of the application are stored. |

For more information about the static properties of this data type please refer to [Directory Data Type Static properties](https://wiki.genexus.com/commwiki/wiki?27388).

Note: CacheFilesPath are available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,) for iOS generator.

CacheFilesPath are available since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,) for Android generator.

## [Methods](#Methods)

### [Create](#Create)

Creates a new directory in the specified source.

##### [Parameters](#Parameters)

Directory name (character)

##### [Sample](#Sample)

```
&directory.Source="c:\temp"
&directory.create()
```

### [Delete](#Delete)

Deletes the source directory.

##### [Sample](#Sample)

```
&directory.delete()
```

### [Exists](#Exists)

Checks whether the directory specified in source exists.

##### [Returned values](#Returned+values)

Boolean

##### [Sample](#Sample)

```
If &directory.exists() 
    Msg("The directory exists!")
Else
    Msg("The directory does not exist!")
EndIf
```

### [GetName](#GetName)

Returns the source directory's name.

##### [Returned values](#Returned+values)

Character

##### [Sample](#Sample)

```
&directory.Source = "c:\temp"
Msg(&directory.GetName()) // screen shows: temp
```

### [GetAbsoluteName](#GetAbsoluteName)

Returns the absolute name of the source directory.

##### [Returned values](#Returned+values)

Character

##### [Sample](#Sample)

```
&directory.Source="c:\temp"
Msg(&directory.GetAbsoluteName()) // screen shows: c:\temp
```

### [Rename](#Rename)

Renames the source directory. It can be also used to move the directory changing its current path.

##### [Parameters](#Parameters)

The new name of the directory (Character).

##### [Sample](#Sample)

```
&directory.Rename("d:\temp2")
```

### [GetFiles](#GetFiles)

Returns the names of files in the source directory. Also, a filter can be specified using extension-wildcards or end-with patterns.

##### [Parameters](#Parameters)

Filter (Character)

##### [Sample](#Sample)

```
for &auxFile in &directory.GetFiles('*.txt')
   // do something with .txt auxFile 
endfor
```

where &auxFile is defined as a File variable.

### [GetDirectories](#GetDirectories)

Returns the names of every directory in the source directory.

##### [Sample](#Sample)

```
for &auxDir in &directory.GetDirectories()
  // do something with auxDir
endfor
```

where &auxDir is defined as a Directory variable.

## [Directory Data Type and External Storage](#Directory+Data+Type+and+External+Storage)

Directory data type handles directories that are in the local file system by default. But when it is returned by a method of the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087), then it refers to a directory located in the external storage.

### [Examples when using External Storage](#Examples+when+using+External+Storage)

Suppose you have a bucket named 'mytest' and a folder named 'petsFolder' created using the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087), and use StorageAPI.GetDirectory(). Here is a list of the output of each method:

| Method | Returns |
| --- | --- |
| GetName | *petsFolder* |
| GetAbsoluteName | *mytest**:\petsFolder\* |

Refer to [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) for related sample code.

## [Restrictions](#Restrictions)

Mapped Drives and Network Drives are not supported in web environments

## [Security tips](#Security+tips)

When a property or method is used to assign a file's path do not use user's inputs concatenations or sanitize the user's entries to avoid path traversal or path manipulation vulnerability risks.

## [See Also](#See+Also)

* [File data type](https://wiki.genexus.com/commwiki/wiki?6915)
* [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087)

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Android](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Objects:** | [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) |


|  |
| --- |
| **Backlinks** |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Directory Data Type Static properties](https://wiki.genexus.com/commwiki/wiki?27388) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [Category:Extended data types](https://wiki.genexus.com/commwiki/wiki?6560) | [File data type](https://wiki.genexus.com/commwiki/wiki?6915) | [File data type: Text file handling](https://wiki.genexus.com/commwiki/wiki?24070) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) |

---
