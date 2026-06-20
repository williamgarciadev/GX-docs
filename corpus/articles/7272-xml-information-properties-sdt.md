---
title: "XML Information Properties (SDT)"
source_id: 7272
source_url: https://wiki.genexus.com/commwiki/wiki?7272
genexus_version: "18"
---

# XML Information Properties (SDT)

[Structured Data Type (SDT) objects](https://wiki.genexus.com/commwiki/wiki?10021) allow you to provide or use structured information when working with web services. They simplify the automatic reading and writing of XML.

The following set of properties is available for each Structured Data Type object to set several aspects of its XML representation:

* [XML Type Property](https://wiki.genexus.com/commwiki/wiki?7251)
* [XML Name Property](https://wiki.genexus.com/commwiki/wiki?7268)
* [XML Namespace Property](https://wiki.genexus.com/commwiki/wiki?7270)
* [XML SoapType property](https://wiki.genexus.com/commwiki/wiki?7451)
* [XML Null Serialization property](https://wiki.genexus.com/commwiki/wiki?14497)

By configuring these properties in a Structured Data Type object, you can create XML like the following—without the need for using the [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938):

```
<SDT1 xmlns="Namespace" ItemAttribute="1">
    <itemElement>1</itemElement>
    <itemCdata<![CDATA[1]]></itemCdata>
        value
    <MyName xmlnls="MYNAMESPACE">1</MyName>
</SDT1>
```


|  |
| --- |
| **Backlinks** |
| [Category:Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) | [XML Name property (SDT)](https://wiki.genexus.com/commwiki/wiki?7268) | [XML Namespace property (SDT)](https://wiki.genexus.com/commwiki/wiki?7270) |
| [XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497) | [Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451) | [XML Type property (SDT)](https://wiki.genexus.com/commwiki/wiki?7251) |

---
