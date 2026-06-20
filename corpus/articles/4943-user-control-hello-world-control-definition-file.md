---
title: "User Control - Hello World Control Definition File"
source_id: 4943
source_url: https://wiki.genexus.com/commwiki/wiki?4943
genexus_version: "18"
---

# User Control - Hello World Control Definition File

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

This document specifies the definition file (\*.control) that defines general aspects of the User Control called [Hello World](https://wiki.genexus.com/commwiki/wiki?4880), such as name, icon, resources.

```
<?xml version="1.0"?>
<ControlDefinition xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance|http://www.w3.org/2001/XMLSchema-instance]" xmlns:xsd="[http://www.w3.org/2001/XMLSchema|http://www.w3.org/2001/XMLSchema]">
  <IncludeInControlInfo>false</IncludeInControlInfo>
  <SupportFiles />
  <RuntimeRender>HelloWorldRender.js</RuntimeRender>
  <HeightPropertyName>Height</HeightPropertyName>
  <WidthPropertyName>Widht</WidthPropertyName>
  <ResizeSupported>true</ResizeSupported>
  <ObjClass>HelloWorld</ObjClass>
  <Description>HelloWorld</Description>
  <Id>00000000-0000-0000-0000-000000000000</Id>
  <Name>HelloWorld</Name>
  <ShowMethod>show</ShowMethod>
  <ReferencedFiles />
  <Constructor>
    <Parameters />
    <Name>HelloWorld</Name>
  </Constructor>
  <PropertiesDefinition>HelloWorldProperties.xml</PropertiesDefinition>
  <DesignRender>HelloWorldRender.xsl</DesignRender>
  <ToolboxIcon>HelloWorldIcon.ico</ToolboxIcon>
</ControlDefinition>
```


|  |
| --- |
| **Backlinks** |
| [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
