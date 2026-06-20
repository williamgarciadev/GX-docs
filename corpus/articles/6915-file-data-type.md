---
title: "File data type"
source_id: 6915
source_url: https://wiki.genexus.com/commwiki/wiki?6915
genexus_version: "18"
---

# File data type

The File data type allows you to manage system files.

It helps you to develop applications that need to execute actions to the system files.

It can be used for typical operations such as copying, moving, renaming, and deleting files. You can also use it to get file attributes such as the last modification date, time, and size.

By defining variables based on this data type you are able to set and use the following properties and methods.

## [Properties](#Properties)

|  |  |
| --- | --- |
| **Source** | Assigns a path to the file. The source cannot be read, use GetAbsoluteName(\*) instead. |
| **Separator** | Returns the name separator character depending on the OS. |
| **ErrCode** | Returns the result of the last operation. |
| **ErrDescription** | Returns the result description of the last operation. |

## [Methods](#Methods)

|  |  |
| --- | --- |
| **Copy** | Copies the specified file to a new file. |
| **Delete** | Deletes the specified file. |
| **Exists** | Determines whether the specified file exists. |
| **GetName** | Returns the name of the specified file. |
| **GetAbsoluteName** | Returns the full path name of the specified file. |
| **GetPath** | Returns the path of the parent directory. |
| **GetURI** | Returns the URI to the specified file. (1) |
| **Rename** | Renames the specified file. |
| **GetLastModified** | Returns the date and time the specified file was last modified. |
| **GetLength** | Gets the size of the specified file. |
| **Open** | See [Text file handling methods](https://wiki.genexus.com/commwiki/wiki?24070). |
| **Close** | See [Text file handling methods](https://wiki.genexus.com/commwiki/wiki?24070). |
| **FromBase64String** | Write encoded content into the file(2). |

### [Details and samples about the methods](#Details+and+samples+about+the+methods)

#### **Copy**

Copies the file specified in the source to a new location. If the target file already exists, it will be overridden.

Parameter  
New filename  (Character)

Sample

```
&file.copy("c:\empcopiedFile.txt")
```

#### **Delete**

Deletes the file specified in the source.

Sample

```
&file.delete()
```

#### **Exists**

Checks whether the file specified in source exists

Returned value  
Boolean

Sample

```
If &file.exists()
    msg("The file exists!")
Else 
    msg("The file does not exist!")
EndIf
```

#### **GetName**

Returns the name of the file specified in the source.

Returned value  
Character

Sample

```
&file.Source="c:\myFile.txt"
Msg(&file.GetName()) // screen shows: myFile.txt
```

#### **GetAbsoluteName**

Returns the absolute name of the file specified in the source.

Returned value  
Character

Sample

```
&file.Source="c:\empmyFile.txt"
Msg(&file.GetAbsoluteName()) // screen shows: c:\empmyFile.txt
```

#### **GetPath**

Returns the path of the parent directory.

Returned value  
Character

Sample

```
&file.source = 'c:\temp\folder\emptyFile.txt'
&parentDir = &file.getPath()
Msg(&parentDir) // result: c:\temp\folder
```

#### [**GetURI**](#GetURI)

Returns the URI to the specified file. For local files, it is equivalent to GetAbsoluteName() but differs in external files (files returned by Storage API methods)

Returned value  
Character

Sample

```
&file.Source="c:\empmyFile.txt"
Msg(&file.GetURI()) // screen shows: c:\empmyFile.txt
```

#### **Rename**

Renames the file specified in the source. It can also be used to move the file, changing its current path.

Parameter  
New name of the file (Character)

Sample

```
&file.Rename("d:\empnewFileName.txt")
```

#### **GetLastModified**

Returns the date and time the file specified in the source was last modified.

Returned value  
DateTime

Sample

```
&dateTime = &file.GetLastModified()
```

#### **GetLength**

Returns the size (in bytes) of the file specified in the source.

Returned value  
Numeric

Sample

```
&size = &file.GetLength()
```

#### **FromBase64String**

Convert a Base64-encoded string to a human-readable string, and write it into the file. Optionally, this function returns a boolean value indicating if the operation was successful.

Parameter  
Base64-string

Returned value  
Boolean

Sample

```
&file.FromBase64String(&Base64String)
```

This method is not supported for user events in Native Mobile apps.

## [Error Codes](#Error+Codes)

|  |  |
| --- | --- |
| **0** | Operation completed successfully. |
| **1** | Invalid file instance - if source property was not set. |
| **2** | The file does not exist. |
| **3** | File already exists. |
| **100** | Security error. |
| **-1** | Undefined error. |

## [File data type and External Storage](#File+data+type+and+External+Storage)

File data type handles files that are in the local file system by default. But when it is returned by a method of the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087), then it refers to a file located in the external storage.

If it is returned by the GetFiles() method of the [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567) and that is returned by the GetDirectories() method in the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087), then it refers to a file located in the external storage too.

### [Examples when using External Storage](#Examples+when+using+External+Storage)

Suppose you have a bucket named 'mytest' and uploaded the file named 'cat.jpg' to a folder named 'petsFolder', using the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087).

| Method | Returns |
| --- | --- |
| **GetURI** | https://mytest.s3.amazonaws.com/petsFolder/cat.jpg |
| **GetName** | cat.jpg |
| **GetAbsoluteName** | petsFolder/cat.jpg |
| **GetPath** | petsFolder |

Refer to [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) for related sample code.

## [Security tips](#Security+tips)

When a property or method is used to assign a file's path do not use the user's inputs concatenations or sanitize the user's entries to avoid path traversal or path manipulation vulnerability risks.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Android](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Objects:** | [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) |

## [See Also](#See+Also)

[File data type: Text file handling](https://wiki.genexus.com/commwiki/wiki?24070)  
[Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087)


|  |
| --- |
| **Backlinks** |
| [Blobs in Base64](https://wiki.genexus.com/commwiki/wiki?7374) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567) |
| [Directory Data Type Static properties](https://wiki.genexus.com/commwiki/wiki?27388) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [File data type: Text file handling](https://wiki.genexus.com/commwiki/wiki?24070) |
| [File Upload control](https://wiki.genexus.com/commwiki/wiki?30574) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Open method](https://wiki.genexus.com/commwiki/wiki?6992) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) | [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) |

---
