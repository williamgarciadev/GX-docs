---
title: "GetSOAPErr function"
source_id: 7021
source_url: https://wiki.genexus.com/commwiki/wiki?7021
genexus_version: "18"
---

# GetSOAPErr function

Returns the error code of the last operation.

### [Syntax](#Syntax)

**GetSOAPErr()**  
  
**Type Returned:**   
Numeric(6)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), 
[Android](https://wiki.genexus.com/commwiki/wiki?14453) (since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,)), 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) (since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,))

### [Description](#Description)

The GetSOAPErr function returns the error code of the last SOAP operation. That is, when you have a Location variable and a location name is assigned to it, or when you make a SOAP call.

### [Samples](#Samples)

```
&Err = GetSOAPErr()
If &err <> 0 Or null(&location.Host)
    Do Case
    Case &err = -20007
        &error = "Unknown error to set a web service, unknown location:" + &LocName + newline() + GetSOAPErrMsg()
    Case &err > 0
        &error = "Unknown error to set a web service:" + &LocName + newline() + GetSOAPErrMsg()
    Otherwise
        &error = "Error from unknown host to set a web service:" + &LocName
    EndCase
    Return
EndIf
```

### [See Also](#See+Also)

[Location](https://wiki.genexus.com/commwiki/wiki?6981)  
[SOAP](https://wiki.genexus.com/commwiki/wiki?10369,,)  
[GetSOAPErrMsg](https://wiki.genexus.com/commwiki/wiki?7022)  
[Error Codes and Messages for Location](https://wiki.genexus.com/commwiki/wiki?7106)


|  |
| --- |
| **Backlinks** |
| [Cancel caller execution on error property](https://wiki.genexus.com/commwiki/wiki?36669) | [CancelOnError Property](https://wiki.genexus.com/commwiki/wiki?7020) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [GetSOAPErrMsg function](https://wiki.genexus.com/commwiki/wiki?7022) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |

---
