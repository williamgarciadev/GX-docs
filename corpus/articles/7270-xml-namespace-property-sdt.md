---
title: "XML Namespace property (SDT)"
source_id: 7270
source_url: https://wiki.genexus.com/commwiki/wiki?7270
genexus_version: "18"
---

# XML Namespace property (SDT)

A string that represents the XML namespace.

### [Scope](#Scope)

**Level:** [SDT member](https://wiki.genexus.com/commwiki/wiki?10021)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following Structured Data Type:

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

When the Item1 XML Namespace property value is set to "MYNAMESPACE," the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >
   <Item1 xmlnls="MYNAMESPACE">1</Item1>
   <item2>Value</item2>
</SDT1>
```

**Considerations**

* If this property value is not set, the default value (the SDT namespace) will be XMLNamespace.
* If an XML Name value is set, but the XML Namespace is not set, the namespace is NOT inherited and an empty namespace is used.
* If the XML Name is not set, the namespace is not passed along.

### [See Also](#See+Also)

[XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272)  
[XML Type property (SDT)](https://wiki.genexus.com/commwiki/wiki?7251)  
[XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268)  
[Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451)  
[XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497)


|  |
| --- |
| **Backlinks** |
| [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) | [XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272) | [XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268) |
| [XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497) | [Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451) | [XML Type property (SDT)](https://wiki.genexus.com/commwiki/wiki?7251) |

---
