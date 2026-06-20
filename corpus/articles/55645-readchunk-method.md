---
title: "ReadChunk method"
source_id: 55645
source_url: https://wiki.genexus.com/commwiki/wiki?55645
genexus_version: "18"
---

# ReadChunk method

Reads data from a response flow in chunks.

### [Syntax](#Syntax)

**&**DataType**.ReadChunk()**

**Type Returned:**  
String

**Where:**  
*&DataType*  
     Variable name based on an [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

### [Description](#Description)

Returns a string representing a chunk of data read from the service response flow.

The ReadChunk method allows incremental reading of data from the service response flow.

Each call to this method retrieves a chunk of data from the flow. If the flow still has data available, subsequent calls will retrieve new chunks until the end of the flow is reached.

To check if there are any chunks left to read from the response flow, you can use the [EOF Property](https://wiki.genexus.com/commwiki/wiki?6975).

### [Scope](#Scope)

**Extended data types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
**Generators:**[Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Availability](#Availability)

This method is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).

### [See Also](#See+Also)

[Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) |

---
