---
title: "FileExist function"
source_id: 8390
source_url: https://wiki.genexus.com/commwiki/wiki?8390
genexus_version: "18"
---

# FileExist function

Verifies the existence of a file on certain location.

### [Syntax:](#Syntax%3A)

**FileExist(***Exp***)**

**Where:**  
  
*Exp*  
    A string with the name and path of the file.

**Type Returned:**  
Numeric(1)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This function receives a string as parameter, with the path and name of the file to verify. It returns 1 in case of success, and 0 otherwise.

The file search is performed in the machine where the program involing this function is executed.

When used in [Web Objects](https://wiki.genexus.com/commwiki/wiki?1864), it will be searched in the Web Server.  For the rest of the objects, in the case of C/SQL and [Java](https://wiki.genexus.com/commwiki/wiki?12258), the search will be made in the processes server.

**Note**: It’s necessary to have reading access to the files specified in the path.

### [Samples](#Samples)

Relative path:

```
&file = “mydoc\docu.doc”
&res = FileExist(&File)
```

The relative path is taken from the default directory where the program is located.

The case &file = “C:\mydoc\docu.doc” is also of relative path, because it depends on the machine where the program is executed. For example: if it’s a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) it will search the docu.doc file in the Web Server C disk, while if it’s used in a VB procedure it will be the work station C disk.

Absolute path:

```
&file = “\\server\c\mydoc\docu.doc”
&res = FileExist(&file)
```

In the case of Web Objects, the directory is determined by the Web Server, so generally it’s convenient to use absolute paths.

### [See Also](#See+Also)

[DeleteFile function](https://wiki.genexus.com/commwiki/wiki?8388,,)

####


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
