---
title: "HowTo: Create a New Pattern"
source_id: 6496
source_url: https://wiki.genexus.com/commwiki/wiki?6496
genexus_version: "18"
---

# HowTo: Create a New Pattern

The goal of this article is to explain how you can set up a methodology that anyone can use to create patterns. Previous knowledge of and experience with [Patterns](https://wiki.genexus.com/commwiki/wiki?2814) is necessary.

### [Step 1. Write a description of the pattern](#Step+1.+Write+a+description+of+the+pattern)

Writing your own pattern is a far more complex task than using an existing one. So, the first thing you have to do before you write anything is to check the [Business Patterns Catalog](https://wiki.genexus.com/commwiki/wiki?1768,,) to see if it doesn't already exist!

Assuming there's nothing similar, write the description of the pattern and store it in the [Business Patterns Catalog](https://wiki.genexus.com/commwiki/wiki?1768,,). Follow the [Pattern Description Guidelines](https://wiki.genexus.com/commwiki/wiki?1841,,).

[Martin Fowler](https://wiki.genexus.com/commwiki/wiki?2931,,) has a good essay on the subject entitled [Writing Software Patterns](https://martinfowler.com/articles/writingPatterns.html).

### [Step 2: Program the canonical example](#Step+2%3A+Program+the+canonical+example)

Go to GX and develop the canonical example. Show it to as many people as possible in order to get valuable feedback.

Some things to take into account:

* When developing the sample, always consider any other areas the pattern will be applied in.
* Try to program in such a way as to achieve the easiest possible generation. For example use *&Var.ToString()* instead of *DTOC(&Var)* (the first one doesn't depend on the variable's type).
* Use as many components as possible. This way there will be less code to generate, thus simplifying the writing of the templates and making the pattern easier to upgrade.

### [Step 3. Define the Pattern specification file](#Step+3.+Define+the+Pattern+specification+file)

Once you have the sample, you need to 'generalize' it.

In other words, you need to define which objects the pattern will generate and what parameters the pattern will have.

There are two types of such parameters:

* **Instance parameters:** These are the parameters the user will set in the Pattern Instance Specification File.
* **General parameters:** These are the parameters that apply to all instance files (eg.: common text, location of gxchart, etc.). These parameters are defined in the Settings Specification file.

In sum, this task consists of defining the structure of these files. You don't need many tech skills to do this, just basic knowledge of XML and, of course, extensive knowledge of the pattern being developed.  
See [PatternBuilder](https://wiki.genexus.com/commwiki/wiki?9816,,)

### [Step 4. Write the template files](#Step+4.+Write+the+template+files)

This is the most technical part.

See [Pattern Template Syntax](https://wiki.genexus.com/commwiki/wiki?2072,,) and using the [Visual Studio Template Editor](https://wiki.genexus.com/commwiki/wiki?2211,,).

### [Step 5. Write the instance file default code](#Step+5.+Write+the+instance+file+default+code)

It's very user-friendly to start a new instance file with most of the values already in place. This is also a highly technical part, which usually requires reading the KB (using the DLLs provided by the pattern tool) to fill the instance file. This can be done in the Implementation Assembly file.

### [Step 6. Use it!](#Step+6.+Use+it%21)

### [Samples](#Samples)

#### [**Category Pattern**](#Category+Pattern)

The implementation of this pattern has been discontinued and removed since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,). Sources are available at <https://github.com/genexuslabs/category-pattern> or the SDK of [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,) or prior.

#### [**Creating a .Pattern File (ie. Category.Pattern)**](#Creating+a+.Pattern+File+%28ie.+Category.Pattern%29)

The Pattern file is the main configuration file where you define the Pattern you want to generate. You need to add the reference to the Instance and Settings xml files.  
Optionally, you can define an Implementation assembly.

**Example of Category.Pattern file:**

```
<InstanceName>Category{0}</InstanceName>
<InstanceSpecification>CategoryInstance.xml</InstanceSpecification>
<SettingsSpecification>CategorySettings.xml</SettingsSpecification>
<Implementation>Artech.Patterns.Category.dll</Implementation>
<AutoUpdate>true</AutoUpdate>
```

After that, you define the ParentObjects of this Pattern. These are the objects where the Pattern should be generated.

```
<ParentObjects>
      <ParentObjectType="Transaction">
      </ParentObject>
</ParentObjects>
```

Also, you can define a *DefaultSetting.xml* where you determine what object will be imported the first time the pattern is applied.

```
<Resources>
      <ResourceId="Resources"Version="0.2"Import="Apply"File="Resources\CategoryResources.xml"/>
</Resources>
```

The main part of this file consists of defining the object to be generated by the pattern.

You can create any type of object, from Attribute, Subtype groups, Transaction, Procedure, WebPanel, etc.

```
<Objects>
      <Object Type="Attribute"Id="CategoryId"Name="{Element.categoryId}"Description="{Element.categoryId}"Element="instance/attributesName"Template="Templates\AttributeCategoryId.dkt" >
</Object>
```

The object element has the following attributes:

* **Type:**The type of object to be generated.
* **Id:**Id of the element.
* **Name:**Name of the generated object.
* **Description:**Description of the generated object.
* **Element** (optional, if left blank, the root element of the instance will be used)**:** An XPath query to match the Element of the Pattern instance which will be used. If the query doesn’t return any element, the object will not be generated.
* **Template:** The template file (.dtk) used to generate this object.

If the object has multiple parts, you need to specify the part you want to define and set the other parts to the default value.

```
<Object Type="Transaction"Id="CategoryRelationTrn"Name="{Element.categoryItem}"Description="{Element.categoryItem}"Element="instance/transactionsName" >
      <Part Type="Structure"Template="Templates\CategoryRelationStructure.dkt" />
      <Part Type="WebForm"Template="Templates\CategoryRelationWebForm.dkt" />
      <Part Type="Rules"Template="Templates\CategoryRelationRules.dkt" />
      <Part Type="Variables"Template="Templates\CategoryRelationVariables.dkt" />
</Object>
```

Again, the Part element has the following attributes:

* **Type:**The type of part that will be generated.
* **Template:** The template file (.dtk) used to generate this part.

#### [**Writing a Template .dkt File (ie. CategoryStructure.dkt)**](#Writing+a+Template+.dkt+File+%28ie.+CategoryStructure.dkt%29)

By default, all the *.dkt* files receive the Element you select in the Element attributes. If no specification is made in the Element attribute, the root element will be received.  
The Instance property is received as a generic Pattern instance. You can convert this pattern instance to the current type of class of your Pattern instance, with a code such as:

```
CategoryInstance catInstance = new CategoryInstance(Instance);
```

Remember that the CategoryInstance class will be created automatically by the pattern engine from your Instance xml definition file.

**Example of CategoryStructure.dkt file:**

```
<%@ Template Language="C#" TargetLanguage="GX" Description="Category Trn" %>
<%@ Assembly Name="Artech.Patterns.Category" %>
<%@ Import Namespace="Artech.Patterns.Category" %>
<%@ Property Name="Object" Type="Artech.Architecture.Common.Objects.KBObject" %>
<%@ Property Name="Part" Type="Artech.Architecture.Common.Objects.KBObjectPart" %>
<%@ Property Name="Instance" Type="Artech.Packages.Patterns.Objects.PatternInstance" %>
<%@ Property Name="Element" Type="Artech.Packages.Patterns.Objects.PatternInstanceElement" %>

<% CategoryInstance catInstance = new CategoryInstance(Instance);%>
<Part type="<%= PartType.Structure %>">
      <Level Name="<%= catInstance.TransactionsName.Category %>" Type="<%= catInstance.TransactionsName.Category %>" Description="<%= catInstance.TransactionsName.Category %>" >
            <Attribute key="True"><%= catInstance.AttributesName.CategoryId %></Attribute>
            <Attribute key="False"><%= catInstance.AttributesName.CategoryName %></Attribute>
            <Attribute key="False" isNullable="True"><%= catInstance.AttributesName.CategoryParentId %></Attribute>
            <Attribute key="False"><%= catInstance.AttributesName.CategoryParentName %></Attribute>
      </Level>
</Part>
```

In this example, the Transaction structure is defined using the values selected by the user in the CategoryId, CategoryName, etc. instance attributes.

```
Creating an InstanceSpecification file (ie. CategoryInstance.xml)
```

In the instance element, define the Element and Attributes that can be changed by the user in each instance of your pattern. For example, the name of the generated object, the way the objects are generated, etc.

**Example of CategoryInstance.xml file:**

```
<?xmlversion="1.0"encoding="utf-8"?>
<PatternName="Category"Version="0.1.0"RootElement="instance"RootType="Instance">
 <ElementTypes>
    <ElementTypeName="Instance"Caption="Category Pattern Instance"ChildrenOrdered="Default">
      <Attributes>
        <AttributeName="showLeafItemsInTreeView"Type="bool"Description="Show Leaf Items In TreeView"DefaultValue="True" />
      </Attributes>
      <ChildrenElements>
        <ChildElementName="attributesName"ElementType="AttributesName"Multiple="false"Optional="false" />
        <ChildElementName="transactionsName"ElementType="TransactionsName"Multiple="false"Optional="false" />
      </ChildrenElements>
    </ElementType>
    <ElementTypeName="AttributesName"Caption="Attributes Names"ChildrenOrdered="Default">
      <Attributes>
        <AttributeName="categoryId"Type="string"Category="General" />
        <AttributeName="categoryName"Type="string"Category="General" />
      </Attributes>
….
```

For example, in the Category Pattern there's a boolean Attribute that defines whether *Leaves* is shown in the *Tree View* or not; and for the Attributes and Transaction to be generated, there is an attribute to define its names.

#### [**Creating a SettingsSpecification (ie. CategorySettings.xml)**](#Creating+a+SettingsSpecification+%28ie.+CategorySettings.xml%29)

The Settings Specification file defines its General parameters. These are parameters that apply to all instance files (eg: common text, location of gxchart, etc.). Here, you can also define default values for the instance element.

#### [**Creating an Implementation Assembly (i.e., Artech.Patterns.Category.dll; this is optional)**](#Creating+an+Implementation+Assembly+%28i.e.%2C+Artech.Patterns.Category.dll%3B+this+is+optional%29)

The Category Pattern has a very simple example of the Implementation assembly. It only sets the default for the Pattern instance object. For a more complex implementation .dll, where some events are used and changes in the KB are made in these events, see the Work With Pattern implementation .dll.
