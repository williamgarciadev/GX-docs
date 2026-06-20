---
title: "XML Type property (SDT)"
source_id: 7251
source_url: https://wiki.genexus.com/commwiki/wiki?7251
genexus_version: "18"
---

# XML Type property (SDT)

Sets the behavior of the XML representation for a simple member of a Structured Data Type.

### [Values](#Values)

|  |  |
| --- | --- |
| **Attribute** | The member represents an Attribute. |
| **CData** | The member represents CData. |
| **Element** | The member represents an Element. |
| **Value** | The member represents a Value. |

### [Scope](#Scope)

**Level:** [SDT member](https://wiki.genexus.com/commwiki/wiki?10021)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021):

```
SDT1
    Item1 Num(4)
    Item2 Char(20)
```

Which is populated throughout the following code:

```
SDT1
{
   item1 = 1 
   item2 = 'Value'
}
```

When the Item1 XML Type property value is set to "Element" (the default value), the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >
   <item1>1</item1>
   <item2>Value</item2>
</SDT1>
```

When the Item2 XML Type property value is set to "CData," the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base">
   <item1>1</item1>
   <item2><![CDATA[value]]></item2>
</SDT1>
```

When the Item1 XML Type property value is set to "Value," the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >   
   <item2>Value</item2> 
   1
</SDT1>
```

It is not possible to have more than one "value" by XML node. Otherwise, all values would be concatenated at the end of the node.

When the Item1 XML Type property value is set to "Attribute," the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge xmlns="Knowledge Base" Item1="1"> 
<item2>Value</item2>
</SDT1>
```

### [See Also](#See+Also)

[XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272)  
[XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268)  
[XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270)  
[Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451)  
[XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497)


|  |
| --- |
| **Backlinks** |
| [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) | [XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272) | [XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268) |
| [XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270) | [Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451) |

---
