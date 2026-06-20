---
title: "XML Null Serialization property (SDT)"
source_id: 14497
source_url: https://wiki.genexus.com/commwiki/wiki?14497
genexus_version: "18"
---

# XML Null Serialization property (SDT)

Changes the behavior of the XML representation for each item of a Structured Data Type.

### [Values](#Values)

|  |  |
| --- | --- |
| **Empty Tag** | The item is always serialized. This is the default value. |
| **Nil Tag** | The item is serialized using the nil tag. |
| **No Tag** | The item is not serialized when it has no value. |

### [Description](#Description)

This property is located at SDT\ItemName\Properties\Xml information section\Xmltype.

`[imagen omitida: wiki id 32709]`

It is also available at Version level, under the Defaults section:

`[imagen omitida: wiki id 32710]`

#### [Availability](#Availability)

The Nil Tag value and the property at Version level are available as from GeneXus X Evolution 2 Upgrade 2.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following Structured Data Type:

SDT1  
-------  
Item1 Num(4)  
Item2 Char(20)

Which is populated through the following code:

```
SDT1
{
item1 = 1
}
```

When the Item2 XML serialize property value is set = "Empty Tag", the default value, the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >
  <item1>1</item1>
  <item2/>
</SDT1>
```

When the Item2 XML Serialize property value is set = "No Tag", the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >
  <item1>1</item1>
</SDT1>
```

When the Item2 XML Serialize property value is set = "Nil Tag", the SDT XML representation will be as follows:

```
<SDT1 xmlns="Knowledge Base" >
  <item1>1</item1>
  <item2 xsi:nil='true'></item2>
</SDT1>
```

Where the xsi prefix is ​​a namespace located at http://www.w3.org/2001/XMLSchema-instance

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, rebuild all the [Structured Data Type (SDT) objects](https://wiki.genexus.com/commwiki/wiki?10021).

### [See Also](#See+Also)

[XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272)  
[XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268)  
[XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270)  
[Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451)


|  |
| --- |
| **Backlinks** |
| [Json Null Serialization property](https://wiki.genexus.com/commwiki/wiki?36980) | [XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272) |
| [XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268) | [XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270) | [Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451) | [XML Type property (SDT)](https://wiki.genexus.com/commwiki/wiki?7251) |

---
