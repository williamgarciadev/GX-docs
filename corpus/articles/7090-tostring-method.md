---
title: "ToString method"
source_id: 7090
source_url: https://wiki.genexus.com/commwiki/wiki?7090
genexus_version: "18"
---

# ToString method

Returns a String.

### [Syntax](#Syntax)

**&***DataType***.ToString()**  
  
**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:**[Blob](https://wiki.genexus.com/commwiki/wiki?6704), [Boolean](https://wiki.genexus.com/commwiki/wiki?4374), [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371), [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370), [Geography](https://wiki.genexus.com/commwiki/wiki?32408), GeoLine, GeoPoint, GeoPolygon, GUID, [Numeric](https://wiki.genexus.com/commwiki/wiki?6793)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
&httpclient.execute("GET","/servlet/hclientes")
&html = &httpclient.ToString()
```

It returns the HTML code of the webpanel clients in the &html variable.

```
&TxtYMDHMStoT = &DateTime.ToString()

&Num_10_2=1.5 // &Num_10_2 is Numeric Type variable with length 10 and 2 decimals.
&Char20 = &Num_10_2.ToString()
```

The result in &Char20 is "      1.50".  
  
The ToString method returns blanks to the left of the number and 0's after the decimals, depending on the definition of the variable . In this case, there are 10 characters and 2 decimals.

### [See Also](#See+Also)

[FromString method](https://wiki.genexus.com/commwiki/wiki?12694)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933)

[TtoC function](https://wiki.genexus.com/commwiki/wiki?8361)  
[DtoC function](https://wiki.genexus.com/commwiki/wiki?7475)  
[Str function](https://wiki.genexus.com/commwiki/wiki?7474)


|  |
| --- |
| **Backlinks** |
| [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) | [Execute method](https://wiki.genexus.com/commwiki/wiki?7047) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) |
| [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) | [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) | [Val function](https://wiki.genexus.com/commwiki/wiki?8528) |

---
