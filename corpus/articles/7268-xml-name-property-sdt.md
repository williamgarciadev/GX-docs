---
title: "XML Name property (SDT)"
source_id: 7268
source_url: https://wiki.genexus.com/commwiki/wiki?7268
genexus_version: "18"
---

# XML Name property (SDT)

Sets an XML Name for a simple member of a structured data type.

### [Scope](#Scope)

**Level:** [SDT member](https://wiki.genexus.com/commwiki/wiki?10021)

### [Description](#Description)

If this property value is not set, the default value (the SDT member name) used will be XMLName.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following Strucutured Data Type:

SDT1

   Item1 Num(4)  
   Item2 Char(20)

which is populated throughout the following code:

```
SDT1
{
   item1 = 1 
   item2 = 'Value'
}
```

When the Item1 XML Name property value is set to "MYNAME" (and [XML Type Property](https://wiki.genexus.com/commwiki/wiki?7251) = Element), the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >
   <MYNAME>1</MYNAME>
   <item2>Value</item2>
</SDT1>
```

### [See Also](#See+Also)

[XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272)  
[XML Type property (SDT)](https://wiki.genexus.com/commwiki/wiki?7251)  
[XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270)  
[Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451)  
[XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497)


|  |
| --- |
| **Backlinks** |
| [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) | [XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272) | [XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270) |
| [XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497) | [Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451) | [XML Type property (SDT)](https://wiki.genexus.com/commwiki/wiki?7251) |

---
