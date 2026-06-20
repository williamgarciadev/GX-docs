---
title: "EOF Property (GeneXus 18 Upgrade 6 or prior)"
source_id: 55641
source_url: https://wiki.genexus.com/commwiki/wiki?55641
genexus_version: "18"
---

# EOF Property (GeneXus 18 Upgrade 6 or prior)

Indicates whether the end of the document was reached.

### [Syntax](#Syntax)

**&***DataType***.EOF**  
  
**Type Returned:**   
Boolean

### [Description](#Description)

It can be used after invoking the read or readtype methods.

### [Sample](#Sample)

```
if (&DataType.EOF)

....

Endif
```

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [See Also](#See+Also)

[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)
