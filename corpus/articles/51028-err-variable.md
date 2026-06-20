---
title: "Err variable"
source_id: 51028
source_url: https://wiki.genexus.com/commwiki/wiki?51028
genexus_version: "18"
---

# Err variable

It is used to assign an error code returned by a function or a method. Also, it is automatically loaded when using the [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853), [Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238), or [New command](https://wiki.genexus.com/commwiki/wiki?6714).

**Data Type:**  
Numeric(3)

### [Description](#Description)

You can use this [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) to assign to it the result returned by a function or a method.  
In addition, it is automatically loaded when using the [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853), [Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238), or [New command](https://wiki.genexus.com/commwiki/wiki?6714).

### [Samples](#Samples)

The [Login method](https://wiki.genexus.com/commwiki/wiki?6963) returns an error code, so you can call it as follows:

```
&Err = &DataType.Login()
```

The [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) returns an error code, so you can call it as follows:

```
&Err = &DataType.Delete()
```

### [See Also](#See+Also)

[ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125)  
[Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853)  
[Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238)  
[New command](https://wiki.genexus.com/commwiki/wiki?6714)


|  |
| --- |
| **Backlinks** |
| [ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125) | [Error handling when Composite command is not used](https://wiki.genexus.com/commwiki/wiki?51603) | [HowTo: Using the ShowError method from Interop in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?51446) |
| [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |

---
