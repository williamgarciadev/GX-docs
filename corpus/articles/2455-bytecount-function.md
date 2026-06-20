---
title: "ByteCount function"
source_id: 2455
source_url: https://wiki.genexus.com/commwiki/wiki?2455
genexus_version: "18"
---

# ByteCount function

Gets the numbers of bytes needed to represent a specific character expression using a specific encoding.

### [Syntax](#Syntax)

*Ret-value =* **ByteCount**(*character-expression , encoding*);  
  
**Type Returned:**  
Numeric  
  
**Where:**  
*Character-expression*  
    Character type. Is the input string.  
  
*Encoding*  
    Character type. Is the encoding to be used.  
  
*Ret-value*  
    Numeric type. Is the number of bytes needed to represent the given character expression with the specified encoding.

### [Scope](#Scope)

**Objects:**

[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908),
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916),
[Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)   
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) (iOS offline support is available since GeneXus15)

### [Samples](#Samples)

Suppose you want to know how many bytes are needed to represent "hello world" using the UTF-8 encoding.

```
&charVar = 'hello world'
&encoding = 'UTF-8'
&result = byteCount(&charVar,&encoding)
```

The value of &result will be 11 because in UTF-8 a character is stored in a byte.

### [See Also](#See+Also)

[Java supported encodings](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html)  
[.NET supported encodings](https://msdn.microsoft.com/en-us/library/system.text.encoding.getencodings(v=vs.110).aspx)


|  |
| --- |
| **Backlinks** |
| [Encodings in GeneXus](https://wiki.genexus.com/commwiki/wiki?19316) |

---
