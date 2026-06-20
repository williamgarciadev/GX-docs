---
title: "File data type: Text file handling"
source_id: 24070
source_url: https://wiki.genexus.com/commwiki/wiki?24070
genexus_version: "18"
---

# File data type: Text file handling

You can use the [File data type](https://wiki.genexus.com/commwiki/wiki?6915) to handle text files. Besides the basic file operations -like copying, deleting, etc.- it allows you to manage the content of text files (reading and writing file's content).

It is quite useful for scenarios where the file contents must be dumped directly into a memory variable, or in the case of writing a log file with the contents of a string variable.

Below are the methods available for the [File data type](https://wiki.genexus.com/commwiki/wiki?6915), meant for reading or writing text files.

### [Methods for reading or writing text files](#Methods+for+reading+or+writing+text+files)

The following methods are for reading or writing text files. The operation is done in a single step: the file is opened, the contents are read from or written to the file, and then the file is closed.

This is very useful for small files. For larger files, methods for reading and writing line by line are provided.

|  |  |
| --- | --- |
| **Method** | **Description** |
| ReadAllText([encoding]):String | Opens a text file, reads all text in the file, and closes the file, using the optionally specified [encoding](https://wiki.genexus.com/commwiki/wiki?19316) (UTF-8 when not specified). |
| ReadAllLines([encoding]):StringCollection | Opens a text file, reads all lines in the file, and closes the file. Each item in the collection is a line from the file, using the optionally specified [encoding](https://wiki.genexus.com/commwiki/wiki?19316) (UTF-8 when not specified). The value returned is a Character Collection. |
| WriteAllText(String[, encoding]) | Opens the file, writes the string to the file, and closes the file. If the file existed, it is overwritten, using the optionally specified encoding (UTF-8 when not specified). |
| WriteAllLines(StringCollection[, encoding]) | Opens the file, writes the string collection to the file -each item followed by a line terminator-, and closes the file. If the file existed, it is overwritten, using the optionally specified encoding (UTF-8 when not specified). |
| AppendAllText(String[, encoding]) | Opens the file, appends the specified string to the end of the file, and closes the file, using the optionally specified encoding (UTF-8 when not specified). |
| AppendAllLines(StringCollection[, encoding]) | Opens the file, appends the specified string collection to the end of the file -each string followed by a line terminator-, and closes the file, using the optionally specified encoding (UTF-8 when not specified). |

#### [Example I](#Example+I)

In this example, you search for files with HTML extension and load their contents into the database. To scan the files you have to use a &File variable (based on the [File data type](https://wiki.genexus.com/commwiki/wiki?6915)), and a &Directory variable (based on the [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567)), and then use the ReadAllText method to dump the contents of the file into the database.

```
For &File in &Directory.GetFiles("*.html")
   New
      ContentHtml = &File.ReadAllText()
   EndNew
​EndFor
```

#### [Example II](#Example+II)

In this example, a log file was written with data from a Business Component.

```
&LogLines = new()  //&LogLines is a string collection.
&LogLines.Add(Format("[%1] Error updating Customer", Now()))
&LogLines.Add(&CustomerBC.ToJson())
&LogFile.AppendAllLines(&LogLines) //&LogFile is File Data Type.
```

### [Methods for reading or writing lines in the text file](#Methods+for+reading+or+writing+lines+in+the+text+file)

The following methods are used to read or write a file by line.

|  |  |
| --- | --- |
| **Method** | **Description** |
| ReadLine(): String | Reads a line of characters from the file. The string returned does not contain the terminating carriage return or line feed. The file must be opened before using this method (using OpenRead or Open method). |
| WriteLine(String) | Writes the specified string followed by a line terminator. The file must be opened before using this method (using OpenWrite or Open method). |

In this case, the file must be opened prior to performing the operation. Following is a detail of the methods to be used for opening the file.

|  |  |
| --- | --- |
| **Method** | **Description** |
| Open([encoding]) | Opens a file with reading/writing access, using the optionally specified encoding (UTF-8 when not specified). If the file exists, the content to write is appended to the file. Otherwise, a new file is created. |
| OpenWrite([encoding]) | Opens a file for writing to append content, or creates a new file when one does not exist, using the optionally specified encoding (UTF-8 when not specified). |
| OpenRead([encoding]) | Opens a file for reading, using the optionally specified encoding (UTF-8 when not specified). |

### [Methods for creating and closing a text file](#Methods+for+creating+and+closing+a+text+file)

|  |  |
| --- | --- |
| **Method** | **Description** |
| Create() | Creates a file in the path specified in the Source property. The file is not opened.  If the file already exists, it sets ErrCode = 1, and the file is not created nor truncated. |
| Close() | Closes the file. |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Name** | **Description** |
| EOF | True if the end of the file has been reached. Before using this property, the file must be opened for reading. |

#### [Example III](#Example+III)

Processing a file by line.

```
&File.Source = "C:\Files\Data.txt" //&File is File Data Type.
&File.OpenRead()
do while not &File.EOF
    ProcessLine(&File.ReadLine())
enddo
&File.Close()
```

### [FromJsonFile and FromXMLFile Methods](#FromJsonFile+and+FromXMLFile+Methods+)

The following methods allow to return and load a SDT or an XML variable from the contents of a file into this format (JSON or XML).

|  |  |
| --- | --- |
| **Method** | **Description** |
| FromJsonFile(File) | Opens a JSON file, parses its content, loads the SDT, and closes the file. |
| FromXMLFile(File) | Opens a XML file, parses its content, loads the SDT, and closes the file. |

#### [Example IV](#Example+IV)

In the following example the file content is in JSON format, and it is compatible with the structure of CustomerSDT.

```
&File.Source = "C:\Files\data.json" //&File is File Data Type
&CustomerSDT.FromJsonFile(&File) //&CustomerSDT is a SDT variable
```

Note:

Since GeneXus 15 Release version, FromJsonFile and FromXMLFile can optionally return a Boolean value and a variable Message for error checking.

Example:

```
&File.Source = "C:\Files\data.json" //&File is File Data Type
&Boolean = &CustomerSDT.FromJsonFile(&File, &Message) //&CustomerSDT is a SDT variable
```

### [Availability](#Availability)

Genexus Tilo RC (X Ev3)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| **Languages** | .NET, Java, Ruby |
| **Applies to** | Web, Smart Devices |

These methods run in [Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?20286).

### [See also](#See+also)

[File data type](https://wiki.genexus.com/commwiki/wiki?6915)  
[Directory data type](https://wiki.genexus.com/commwiki/wiki?6567)


|  |
| --- |
| **Backlinks** |
| [File data type](https://wiki.genexus.com/commwiki/wiki?6915) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
