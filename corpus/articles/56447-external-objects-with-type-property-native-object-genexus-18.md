---
title: "External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 1 or prior)"
source_id: 56447
source_url: https://wiki.genexus.com/commwiki/wiki?56447
genexus_version: "18"
---

# External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 1 or prior)

External Objects (EO) of type Native Object, stores all the information (name, properties, methods and parameters) about how to access a defined class in a Java class, .NET assembly or Javascript source.

Each EO corresponds exactly to a class of the external resource.

Once the EO is defined in GeneXus (and the methods and properties exposed by the external resource are properly mapped), you are able to manage these methods and properties inside the GeneXus source.

`[imagen omitida: wiki id 53719]`

***Note:*** For .NET and Java there exist tools to help in the definition of the EO structure:

1. [.NET Assembly Import Wizard](https://wiki.genexus.com/commwiki/wiki?6177) and
2. [Java Class Import Wizard](https://wiki.genexus.com/commwiki/wiki?6176)

The tools can be accessed from the Tools option in the GeneXus menu (under Application Integration option).

## [Properties](#Properties+)

### [External Object](#External+Object)

`[imagen omitida: wiki id 53720]`

***Name:*** name of the EO  
***Description:*** description  
***[Type](https://wiki.genexus.com/commwiki/wiki?53690)******:*** EO of type (Native Object).  
***Namespace:*** class namespace  
***[Module/Folder](https://wiki.genexus.com/commwiki/wiki?25540):***The folder where the EO is located.  
***[Object Visibility](https://wiki.genexus.com/commwiki/wiki?22473):***accessibility from other objects in different Modules.   
***.NET/.NET Framework Information***  
***.NET/.NET Framework External Name:*** name of the external class (.dll)  
***.NET/.NET Framework Assembly Name:*** name of the assembly associated to the EO  
***.NET/.NET Framework Constructor Parameters:*** list -separated by commas- of parameters to be passed to the assembly constructor. The constructor parameters are always constants.  
***[.NET Package ID](https://wiki.genexus.com/commwiki/wiki?51647):***uniquely identify the EO.  
***Java Information***  
***Java External Name:*** name of the external class (.class)  
***External Package Name:*** name of the package where the class associated to the EO is located  
***Java Constructor Parameters:*** list -separated by commas- of parameters to be passed to the external class constructor. The class constructor parameters are always constants.

### [Properties](#Properties)

`[imagen omitida: wiki id 53721]`

***Property Type:*** it indicates whether it is a read only, read/write or member type property  
***Internal Name:*** internal name to be given to the property  
***Description:*** description  
***Type:*** type of data that the property will have in GeneXus  
***IsStatic*:** determines if is static or not (True , false)  
***[Control Type](https://wiki.genexus.com/commwiki/wiki?9550)*:**type of control to be shown.  
***.NET/.NET Framework Information***  
***.NET/.NET FrameworkInternal Name:*** external name of the property in the .Net class  
***.NET/.NET FrameworkExternal Type:*** external data type of the property  
***Java Information***  
***Java External Name:*** external name of the property in the Java class  
***Java External Type:*** external data type of the property

### [Methods](#Methods)

`[imagen omitida: wiki id 53722]`

***Internal Name:*** internal name of the method  
***Description:*** description  
***Type:*** data type of the returned value, if any  
***Based on:*** determine if is based on any other data type  
***XML Name:*** exposed Name of the method  
***Is static:*** determines if is static or not (True , false)  
***External Member Type:*** Three possible values, default, Static , Instance  
***.NET/.NET Framework Information***  
***.NET/.NET Framework External Name:*** external name of the method in the .NET class  
***.NET/.NET Framework External Type:*** external data type of the returned value  
***Java Information***  
***Java External Name:*** external name of the method in the Java class  
***Java External Type:*** external data type of the returned value  
***Java Method Throws Exceptions:*** it indicates whether the method in the external class sends an exception; the default value is No

### [Parameters](#Parameters)

`[imagen omitida: wiki id 53723]`

**Access Type:** it indicates whether the parameter is an input only, output only, or input/output parameter  
**Internal Name:** internal name of the parameter  
**Description:** description  
**Type:** data type that the parameter will have in GeneXus  
***External Type:*** external data type of the parameter

### [Events](#Events)

The events should always be defined as static in GeneXus.

## [Example of use](#Example+of+use)

Consider that you create a Native Object type EO called "Mathss".  Then you define a Maths variable called &Maths.  
Then, the code looks as the following:

```
Event enter
 &res = &Maths.Sum(&parm1,&parm2)
EndEvent
```

The method returns the sum of both values. The first and second parameter are the values that are going to be added.

## [Deployment](#Deployment)

.NET: In the case of using EOs in order to access assemblies, the assembly or assemblies should be copied to the bin directory of the work Environment. When the application is deployed, the assemblies must be taken to production.

Java: In the case of Java classes, take the jar/zip containg the external classes have to be included in the classpath.

Javascript: The javascript resources have to be located within the rest of static resources of the web application. It needs to be referenced in the GeneXus code as follows:

## [Considerations](#Considerations)

- Vector and matrix values are not supported, only [scalar](https://wiki.genexus.com/commwiki/wiki?7380) variables are supported.  
- Array data types such as String[], Date[] and so on are not supported.  
- Enum data types are not supported.  
- If there is an EO method called Initialized, or another reserved word, it must be defined with another name but keeping the External Name property

## [See also](#See+also)

[External Objects for Android](https://wiki.genexus.com/commwiki/wiki?17878)  
[External Objects for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072)  
[External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064)
