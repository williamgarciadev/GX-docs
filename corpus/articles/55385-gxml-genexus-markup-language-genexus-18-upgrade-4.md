---
title: "GXML (GeneXus Markup Language) (GeneXus 18 Upgrade 4)"
source_id: 55385
source_url: https://wiki.genexus.com/commwiki/wiki?55385
genexus_version: "18"
---

# GXML (GeneXus Markup Language) (GeneXus 18 Upgrade 4)

GeneXus Markup Language (GXML) is an XML-like descriptive language for describing GeneXus' objects.

The drag-and-drop concept in GeneXus makes it far easier for the average user to understand how to design apps by describing their components in an abstract way, without worrying about the lines of code that it may entail. Either way, for those adventured users, the GXML syntax aims to be very simple to understand, providing views, controls, and layout structures for declaring your app's user interface. This document pretends to be a guideline for those intrigued users that wants to analyze a GeneXus object from another point of view.

## [Overview](#Overview)

The GXML format can be used for defining User Interface (UI) objects such as Panels, Stencils, Themes, and ColorPalette objects. This format aims to be simple to read for developers.

The main structure of every GXML is as follows:

```
<Root>
    <!-- Object description -->
</Root>
```

The content of the Root tag will depend on what kind of object you are modeling.

In the case of **Panels** and **Stencils**, it will contain the definition of every object in the Layout (delimited by a Controls tag), the Variables involved (by a Variables tag), and the Code section (by a Code tag). Also, it allows you to define a set of data objects on which it depends (delimited by SDTs tag and DataProviders tag). For instance:

```
<Root ImportFor="SD">
    <Controls>
        <!-- Controls description -->
    </Controls>
    <Variables>
        <Variable name="MyVar">
            <!-- Variable definition -->
        </Variable>
        ...
    </Variables>
    <Code>
    <![CDATA[
    // Code events
    ]]>
    </Code>
    <SDTs>
        <!-- Structure Data Type definition -->
    </SDTs>
    <DataProviders>
        <!-- Data Providers definition -->
    <DataProviders>
</Root>
```

In the case of a **Design System object** definition, the GXML structure will contain a DesignSystems tag where you are able to define a set of theme objects by a DesignSystem tag (usually one), and each DesignSystem tag is defined by two sections: Tokens tag for describing the token-groups and Styles for describing style-classes. For instance:

```
<Root>
    <DesignSystems>
        <DesignSystem name="MyMobileDesignSystem">
            <Tokens>
                <!-- Tokens definition in raw text -->
            </Tokens>   
            <Styles>
                <!-- Styles definition in raw text -->
            </Styles>
        </DesignSystem>
        <DesignSystem name="MyWebDesignSystem">
            <!-- Token/Style sections definitions -->
        </DesignSystem>
    </DesignSystems>
</Root>
```

## [Advantages](#Advantages)

1. The [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) tool will basically generate the appropriate GXML files from your Sketch files (translate them) in order to import them into GeneXus. In that sense, when GeneXus displays the preview of what are you going to import, you can see a [Code tab](https://wiki.genexus.com/commwiki/wiki?46882) with the GXML to be imported.
2. In the Layout tab of a (Web) Panel, you can copy any Table (except the Main Table) and paste it into a text editor in order to see the GXML representation and vice versa.  
     
   For example, if you have the following layout and copy the highlighted control.  
   `[imagen omitida: wiki id 46982]`  
     
   And you paste it into a text editor, it will show you something as follows:

   ```
   <Root>
       <Controls>
           <table controlName="Table1" 
                  columnsStyle="100%;60dip" 
                  class="Search">
               <row rowHeight="60dip">
                   <cell>
                       <data attribute="&amp;Search" />
                   </cell>
                   <cell colSpan="1">
                       <action controlName="Search" 
                               onClickEvent="'Search'" 
                               image="Search_icon" />
                   </cell>
               </row>
           </table>
       </Controls>
       <Variables>
           <Variable Name="Search">
               <Properties>
                   <Property>
                       <Name>Name</Name>
                       <Value>Search</Value>
                   </Property>
                   <Property>
                       <Name>OBJ_TYPE</Name>
                       <Value>id_OTYPE_VAR</Value>
                   </Property>
                   <Property>
                       <Name>ATTCUSTOMTYPE</Name>
                       <Value>bas:VarChar</Value>
                   </Property>
                   <Property>
                       <Name>Type</Name>
                       <Value>VARCHAR</Value>
                   </Property>
               </Properties>
           </Variable>
       </Variables>
   </Root>
   ```

## [Formal specification](#Formal+specification)

Under construction.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | .NET, .NET Core, Java, Android, Apple, Angular |

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877)
