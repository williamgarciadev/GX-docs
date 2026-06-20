---
title: "User Control - GxChart Control Definition File"
source_id: 5004
source_url: https://wiki.genexus.com/commwiki/wiki?5004
genexus_version: "18"
---

# User Control - GxChart Control Definition File

```
<?xml version="1.0"?>  
<ControlDefinition xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance|http://www.w3.org/2001/XMLSchema-instance]" xmlns:xsd="[http://www.w3.org/2001/XMLSchema|http://www.w3.org/2001/XMLSchema]">  
  <SupportFiles/>  
  <RuntimeRender>gxChart.js</RuntimeRender>  
  <HeightPropertyName>Height</HeightPropertyName>  
  <WidthPropertyName>Width</WidthPropertyName>  
  <ResizeSupported>true</ResizeSupported>  
  <ObjClass>GxChartControl</ObjClass>  
  <Description>Chart</Description>  
  <Id>00000000-0000-0000-0000-000000000000</Id>  
  <Name>GxChartControl</Name>  
  <ShowMethod>show</ShowMethod>  
  <IncludeInControlInfo>false</IncludeInControlInfo>  
  <GxResources>gxChartSdt.xpz</GxResources>  
  <ReferencedFiles/>  
  <Constructor>  
    <Parameters />  
    <Name>gxChart</Name>  
  </Constructor>  
  <Events>  
    <Event>Click</Event>  
    <Event>ClickOnSerie</Event>  
  </Events>  
  <Actions>  
    <Action>  
      <Order>0</Order>  
      <ActionProperties>  
        <Property>  
          <Key>  
            <string>Name</string>  
          </Key>  
          <Value>  
            <string>GxChartData</string>  
          </Value>  
        </Property>  
        <Property>  
          <Key>  
            <string>ATTCUSTOMTYPE</string>  
          </Key>  
          <Value>  
            <string>GxChart</string>  
          </Value>  
        </Property>  
      </ActionProperties>  
      <Data></Data>  
      <ActionType>VarDeclaration</ActionType>  
    </Action>  
    <Action>  
      <Order>1</Order>  
      <ActionProperties>  
        <Property>  
          <Key>  
            <string>Name</string>  
          </Key>  
          <Value>  
            <string>GxChartSerie</string>  
          </Value>  
        </Property>  
        <Property>  
          <Key>  
            <string>ATTCUSTOMTYPE</string>  
          </Key>  
          <Value>  
            <string>GxChart.Serie</string>  
          </Value>  
        </Property>  
      </ActionProperties>  
      <Data>//snippet fldkfjsdlfkj d</Data>  
      <ActionType>VarDeclaration</ActionType>  
    </Action>  
    <Action>  
      <Order>2</Order>  
      <ActionProperties>  
        <Property>  
          <Key>  
            <string>Data</string>  
          </Key>  
          <Value>  
            <string>&GxChartData</string>  
          </Value>  
        </Property>  
      </ActionProperties>  
      <Data></Data>  
      <ActionType>SetPropertyToControl</ActionType>  
    </Action>  
    <Action>  
      <Order>3</Order>  
      <ActionProperties/>  
      <Data>  
        // Sample code for GxChartControl  
        Sub 'GxChartSample'  
          &GxChartData.Categories.Add("2004")  
          &GxChartData.Categories.Add("2005")  
          &GxChartData.Categories.Add("2006")  
          &GxChartSerie.Name = "Sales"  
          &GxChartSerie.Values.Add(3045)  
          &GxChartSerie.Values.Add(4246)  
          &GxChartSerie.Values.Add(6537)  
          &GxChartData.Series.Add(&GxChartSerie)  
        EndSub  
      </Data>  
      <ActionType>CodeSnippet</ActionType>  
    </Action>  
  </Actions>  
  <PropertiesDefinition>PropertiesDefinition.xml</PropertiesDefinition>  
  <DesignRender>Render.xsl</DesignRender>  
  <ToolboxIcon>gxchart.ico</ToolboxIcon>  
  <Html>htmlsource</Html>  
</ControlDefinition>
```
