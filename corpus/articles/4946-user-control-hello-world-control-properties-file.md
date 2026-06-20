---
title: "User Control - Hello World Control Properties File"
source_id: 4946
source_url: https://wiki.genexus.com/commwiki/wiki?4946
genexus_version: "18"
---

# User Control - Hello World Control Properties File

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

This document defines the control's properties of the [Hello World](https://wiki.genexus.com/commwiki/wiki?4880) User Control example.

```
<?xml version="1.0"?>
<Content xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance|http://www.w3.org/2001/XMLSchema-instance]" xmlns:xsd="[http://www.w3.org/2001/XMLSchema|http://www.w3.org/2001/XMLSchema]">
  <Object id="HelloWorld">
    <Group>
      <Name>General</Name>
      <Type>Main</Type>
      <Childs>
        <Prop>
          <Id>Width</Id>
          <Name>Width</Name>
          <Type>Integer</Type>
          <Default>100</Default>
          <Metadata />
        </Prop>
        <Prop>
          <Id>Height</Id>
          <Name>Height</Name>
          <Type>Integer</Type>
          <Default>100</Default>
          <Metadata />
        </Prop>
        <Prop>
          <Id>FontFace</Id>
          <Name>FontFace</Name>
          <Type>Combo</Type>
          <Metadata />
          <Values>
            <Value id="Arial" desc="Arial" />
            <Value id="Verdana" desc="Verdana" />
            <Value id="Comic Sans MS" desc="Comic Sans MS" />
          </Values>
        </Prop>
        <Prop>
          <Id>FontColor</Id>
          <Name>FontColor</Name>
          <Type>Text</Type>
          <Default>#000000</Default>
          <Metadata />
        </Prop>
        <Prop>
          <Id>FontSize</Id>
          <Name>FontSize</Name>
          <Type>Text</Type>
          <Default>10</Default>
          <Metadata />
        </Prop>
      </Childs>
    </Group>
  </Object>
</Content>
```


|  |
| --- |
| **Backlinks** |
| [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
