---
title: "Open method"
source_id: 6992
source_url: https://wiki.genexus.com/commwiki/wiki?6992
genexus_version: "18"
---

# Open method

Opens the specified document.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.Open(***FileName***)**  
  
**Where:**  
  
&*VarBasedOnExtendedDataType*  
     Is a variable based on one of the following data types: [ExcelDocument](https://wiki.genexus.com/commwiki/wiki?2476), [WordDocument](https://wiki.genexus.com/commwiki/wiki?2478,,) , [File](https://wiki.genexus.com/commwiki/wiki?6915) , [XMLReader](https://wiki.genexus.com/commwiki/wiki?6928), [XMLWriter](https://wiki.genexus.com/commwiki/wiki?6938) , [Window](https://wiki.genexus.com/commwiki/wiki?7112).  
  
*FileName*  
     Is the path and name of the document. If only the name is specified, the document will be created in the default directory (DataXXX model directory).

**Type Returned:**

* For ExcelDocument and WordDocument data types, a Numeric type is returned. So, it is possible to call it as a function:

```
 &ErrorCode = &DataType.Open(…)
```

* When it is applied to the ExcelDocument data type, one of the following values is returned:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | OK |
| **4** | Invalid template |
| **10** | Could not open file |

* When it is applied to the WordDocument data type, one of the following values is returned:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | OK |
| **6** | Could not open file |
| **10** | Could not complete operation |

* For XMLWriter, XMLReader and File data types, no value is returned. So, for these data types the only way to know if the method has run successfully or not is by evaluating the [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) and the [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) like the following code shows as a basic example:

```
if &File.ErrCode<>0 
   msg(&File.ErrDescription) //or other action
endif
```

These properties are valid for all the data types for which the Open method applies except for the Window data type.

* For the Window data type, neither the method does not return a value nor the properties are valid.

### [Scope](#Scope)

**Extended Data Types:** [ExcelDocument](https://wiki.genexus.com/commwiki/wiki?2476), [WordDocument](https://wiki.genexus.com/commwiki/wiki?2478,,) , [File](https://wiki.genexus.com/commwiki/wiki?6915) , [XMLReader](https://wiki.genexus.com/commwiki/wiki?6928) , [XMLWriter](https://wiki.genexus.com/commwiki/wiki?6938), [Window](https://wiki.genexus.com/commwiki/wiki?7112)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method opens the path specified in the parameter (*FileName*).

If the path corresponds to an Excel document or Word document:

* If the specified document does not exist, it is created by using the template specified in the [Template property](https://wiki.genexus.com/commwiki/wiki?6991).
* When you open a document with the *Open* method, it is not displayed on the screen. To show it, you must use the [Show method](https://wiki.genexus.com/commwiki/wiki?7065).
* If you need to know if the spreadsheet already exists you can use [file.exists()](https://wiki.genexus.com/commwiki/wiki?6915).

### [See Also](#See+Also)

[Complete list of error Codes and Messages returned by all the methods for ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?6939)  
[Complete list of error Codes and Messages returned by all the methods for WordDocument data type](https://wiki.genexus.com/commwiki/wiki?6944)


|  |
| --- |
| **Backlinks** |
| [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) | [ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040) | [Extended Data Types Read-Only property](https://wiki.genexus.com/commwiki/wiki?2565) |
| [OpenFromString method](https://wiki.genexus.com/commwiki/wiki?7050) | [Template property](https://wiki.genexus.com/commwiki/wiki?6991) | [Unbind method](https://wiki.genexus.com/commwiki/wiki?7053) |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
