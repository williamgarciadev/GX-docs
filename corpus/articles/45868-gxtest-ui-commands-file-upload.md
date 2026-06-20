---
title: "GXtest UI Commands - File Upload"
source_id: 45868
source_url: https://wiki.genexus.com/commwiki/wiki?45868
genexus_version: "18"
---

# GXtest UI Commands - File Upload

These commands family allows interacting with upload file controls, check the [Fileupload examples](https://wiki.genexus.com/commwiki/wiki?47224). Note that they can be combined with [File Upload Base Path property]([GXtest - File Upload Base Path Property) usage.

## [FileUpload](#FileUpload)

`[imagen omitida: wiki id 46691]`

Allows uploading a file for a control present on the page.

**Parameters**:

* ControlName: name of the control as defined in the KB
* FileName: the path to the file to be uploaded

**Example**:

```
&driver.FileUpload("&blobVar", "pathToFile/fileName.extension")
```

## [FileUpload](#FileUpload)

`[imagen omitida: wiki id 47320]`

Allows uploading a file for a control inside a grid present on the page.

**Parameters**:

* ControlName: name of the control as defined in the KB
* Row: row number inside the grid
* FileName: the path to the file to be uploaded

**Example**:

```
&driver.FileUpload("&blobVar", 2, "pathToFile/fileName.extension")
```

Also, four HTML selectors are available for this command: ID, Name, CSS, and XPath.

## [FileUploadByID](#FileUploadByID)

`[imagen omitida: wiki id 46692]`

Allows uploading a file to an input file element using its ID.

**Parameters**:

* ID: target input file element's ID
* FileName: the path to the file to be uploaded

**Example**:

```
&driver.FileUploadByID("fileUploadID", "pathToFile/fileName.extension")
```

## [FileUploadByName](#FileUploadByName)

`[imagen omitida: wiki id 46693]`

Allows uploading a file to an input file element using its name attribute.

**Parameters**:

* Name: target input file element's Name
* FileName: the path to the file to be uploaded

**Example**:

```
&driver.FileUploadByName("fileUploadName", "pathToFile/fileName.extension")
```

## [FileUploadByCSS](#FileUploadByCSS)

`[imagen omitida: wiki id 46694]`

Allows uploading a file to an input file element using a CSS selector.

**Parameters**:

* CSS: a CSS selector for target input file element
* FileName: the path to the file to be uploaded

**Example**:

```
&driver.FileUploadByCSS("#vATTACHEBLOB", "pathToFile/fileName.extension")
```

## [FileUploadByXPath](#FileUploadByXPath)

`[imagen omitida: wiki id 46695]`

Allows uploading a file to an input file element using an XPath selector.

**Parameters**:

* XPath: an XPath selector for target input file element
* FileName: the path to the file to be uploaded

**Example**:

```
&driver.FileUploadByXPath("//*[@id='vATTACHEBLOB']", "pathToFile/fileName.extension")
```

Additionally, with this new commands, there is another new command useful to set a base folder where GXtest will use to select files in case you want to use only file names or relative paths in your FileUploadBy commands.

## [SetFileUploadBasePath](#SetFileUploadBasePath)

`[imagen omitida: wiki id 46696]`

Sets a default base directory where FileUpload commands will be looking at files for upload when a relative path is used as FileName parameter.

**Parameters**:

* FileName: a directory path where testing resources are placed.

**Example:**

```
&driver.SetFileUploadBasePath("C:\\testingFiles\\")

&driver.FileUploadByName("fileUploadName", "fileName.extension")
```

**Notes:**

- File upload base path is set automatically through its corresponding environment level property but also you can use this command for a specific test.

-  "File Upload Base Path" property, "SetFileUploadBasePath" and "FileUploadBy" commands does not validate if the path set is valid. For this, it is necessary to carry out validations (Assertions, GetValue, Verify, Contains, EndsWith, etc.) to verify that the file uploaded correctly or not. For Example:

```
&driver.FileUploadByName("fileUploadVar", "C:\testingResources\userForm.pdf")

if (&driver.GetValueByName("fileUploadVar").EndsWith("userForm.pdf")) 
    // File loaded successfully
else
    // File not loaded
endif
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [FileUpload command examples](https://wiki.genexus.com/commwiki/wiki?47224) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [GXtest UI Commands - Property Setters](https://wiki.genexus.com/commwiki/wiki?48468) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
