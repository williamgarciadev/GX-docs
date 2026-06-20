---
title: "User Control - Hello World Design Render File"
source_id: 4949
source_url: https://wiki.genexus.com/commwiki/wiki?4949
genexus_version: "18"
---

# User Control - Hello World Design Render File

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

This document specifies how the User Control called [Hello World](https://wiki.genexus.com/commwiki/wiki?4880) must be displayed at design time in the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272).

```
<?xml version='1.0'?>
<xsl:stylesheet version="1.0" xmlns:xsl="[http://www.w3.org/1999/XSL/Transform|http://www.w3.org/1999/XSL/Transform]"
 xmlns:msxml="urn:schemas-microsoft-com:xslt"
 xmlns:gx="urn:shemas-artech-com:gx"
 exclude-result-prefixes="msxml gx"
 xmlns:gxca="urn:GXControlAdap">
  <xsl:output method="html"/>
  <xsl:template match="/" >
    <xsl:apply-templates select="/GxControl"/>
  </xsl:template>
  <xsl:template match="GxControl">
    <xsl:choose>
      <xsl:when test="@type = 'HelloWorld'">
        <xsl:call-template name="RenderHelloWorld"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <!-- HelloWorld design render -->
  <!-- ///////////////////  Implement your render here  ///////////////////-->
  <xsl:template name="RenderHelloWorld">
    <span atomicselection="true">
      <xsl:call-template name="AddStyleAttribute"/>
      Hello World control    
    </span>

  </xsl:template>

  <!-- Helpers Templates -->

  <xsl:template name="AddStyleAttribute" >
    <xsl:variable name="Style">
      <xsl:text>width: </xsl:text>
      <xsl:value-of select="gxca:GetPropertyValueInt('Width')"/>
      <xsl:text>; </xsl:text>
      <xsl:text>height: </xsl:text>
      <xsl:value-of select="gxca:GetPropertyValueInt('Height')"/>
      <xsl:text>; </xsl:text>
      <xsl:text>border-style: solid; border-width: 2px;</xsl:text>
    </xsl:variable>
    <xsl:attribute name="style">
      <xsl:value-of select="$Style"/>
    </xsl:attribute>
  </xsl:template>
</xsl:stylesheet>
```


|  |
| --- |
| **Backlinks** |
| [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
