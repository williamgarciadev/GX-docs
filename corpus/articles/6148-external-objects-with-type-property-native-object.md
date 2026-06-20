---
title: "External Objects with Type property 'Native Object'"
source_id: 6148
source_url: https://wiki.genexus.com/commwiki/wiki?6148
genexus_version: "18"
---

# External Objects with Type property 'Native Object'

[External Objects](https://wiki.genexus.com/commwiki/wiki?5669) (EO) with their [Type property](https://wiki.genexus.com/commwiki/wiki?53690) set to 'Native Object' store all the information (name, properties, methods, and parameters) about how to access a defined Java class, .NET assembly, or JavaScript source.

They are usually called **Native Objects** and each one of them corresponds exactly to a class of the external resource.

Once you create an External Object and set its Type property to 'Native Object' with the properties and methods exposed by the external resource properly mapped, you can manage these methods and properties inside the GeneXus code.

`[imagen omitida: wiki id 58059]` `[imagen omitida: wiki id 57558]`

When generating with [.NET](https://wiki.genexus.com/commwiki/wiki?38604) and [Java](https://wiki.genexus.com/commwiki/wiki?12258) generators, the following wizards are available to help you to define the [External Object](https://wiki.genexus.com/commwiki/wiki?5669) structure:

* [.Net Assembly Import Wizard](https://wiki.genexus.com/commwiki/wiki?6177)
* [Java Class Import Wizard](https://wiki.genexus.com/commwiki/wiki?6176)

You can access these wizards by selecting **Tools > Application Integration** in GeneXus' main menu.

## [Properties](#Properties)

### [Native Object Properties](#Native+Object+Properties+)

Below are the properties available for the **Native Object**:

`[imagen omitida: wiki id 56448]`

* **Name:** External Object name.
* **Description:** External Object description.
* **[Type](https://wiki.genexus.com/commwiki/wiki?53690):** External Object type (set to 'Native Object').
* **Namespace:** Class namespace.
* **[Module/Folder](https://wiki.genexus.com/commwiki/wiki?25540):**Folder where the External Object is located.
* **[Object Visibility](https://wiki.genexus.com/commwiki/wiki?22473):**Accessibility from other objects located in different Modules.
* **.NET/.NET Framework Information**
  + **.NET/.NET Framework External Name:** Name of the external class (.dll).
  + **.NET/.NET Framework Assembly Name:** Name of the assembly associated with the External Object.
  + **.NET/.NET Framework Constructor Parameters:** Comma-separated list of parameters to be passed to the assembly constructor. The constructor parameters are always constants.
  + **[.NET Package ID](https://wiki.genexus.com/commwiki/wiki?51647):**Uniquely identifies the External Object.
* **Java Information**
  + **Java External Name:** Name of the external class (.class).
  + [**External Package Name**](https://wiki.genexus.com/commwiki/wiki?57626)**:** Name of the package where the class associated with the External Object is located.
  + **Java Constructor Parameters:** Comma-separated list of parameters to be passed to the external class constructor. The class constructor parameters are always constants.

### [Properties of the Native Object types](#Properties+of+the+Native+Object+types)

Below are the properties available for each type defined inside the **Native Object**.

`[imagen omitida: wiki id 58060]`

* **Internal Name:** Internal name to be given to the Type.
* **Description:**Description.
* **[Property Name property](https://wiki.genexus.com/commwiki/wiki?57843):**Name used to display in the properties that are set in the variables.
* **[Valid Types property](https://wiki.genexus.com/commwiki/wiki?57844):** Valid data types separated by commas.
* **[Allow Collection property](https://wiki.genexus.com/commwiki/wiki?57845):**Indicates if it is a collection or not (True, False).
* **[Default Type property](https://wiki.genexus.com/commwiki/wiki?57846):**Default data type to be used when no other data type is specified.

### [Properties of the Native Object properties](#Properties+of+the+Native+Object+properties)

Below are the properties available for each property defined inside the **Native Object**.

`[imagen omitida: wiki id 58061]`

* **Property Type:** Indicates whether it is a read-only, read/write, or member type property.
* **Internal Name:** Internal name to be given to the property.
* **Description:** Description.
* **Type:** Property data type.
* **IsStatic:** Indicates if it is static or not (True, False).
* **[Control Type](https://wiki.genexus.com/commwiki/wiki?9550):** Type of control to be shown.
* **.NET/.NET Framework Information**
  + **.NET/.NET Framework External Name:** External name of the property in the .Net class.
  + **.NET/.NET Framework External Type:** External data type of the property.
* **Java Information**
  + **Java External Name:** External name of the property in the Java class.
  + **Java External Type:** External data type of the property.

### [Properties of the Native Object methods](#Properties+of+the+Native+Object+methods)

Below are the properties available for each method defined inside the **Native Object**.

`[imagen omitida: wiki id 58062]`

* **Internal Name:** Internal name of the method.
* **Description:** Description of the method.
* **Type:** Data type of the returned value, if any.
* **Based on:**Determines if it is based on any other data type.
* **XML Name:**Exposed Name of the method.
* **Is static:**Determines if it is static or not (True, False).
* **External Member Type:**The three possible values are Default, Static, and Instance.
* **.NET/.NET Framework Information**
  + **.NET/.NET Framework External Name:** External name of the method in the .NET class.
  + **.NET/.NET Framework External Type:** External data type of the returned value.
* **Java Information**
  + **Java External Name:** External name of the method in the Java class.
  + **Java External Type:** External data type of the returned value.
  + **Java Method Throws Exceptions:** Indicates whether the method in the external class sends an exception; the default value is No.

### [Properties of the Native Object parameters](#Properties+of+the+Native+Object+parameters)

Below are the properties available for each parameter defined inside the **Native Object**.

`[imagen omitida: wiki id 58064]`

* **Access Type:** Indicates whether the parameter is an input-only, output-only, or input/output parameter.
* **Internal Name:** Internal name of the parameter.
* **Description:** Parameter description.
* **Type:** Parameter data type in GeneXus.
* **External Type:** External data type of the parameter.

### [Events](#Events)

The events should always be defined as static in GeneXus.

## [Example of use of a Native Object](#Example+of+use+of+a+Native+Object)

Suppose that you have the Native Object shown above (called "Maths").

Next, in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) you define a variable called &Maths based on the "Maths" External Object.

In addition, you define an event as follows:

```
Event enter
 &res = &Maths.Sum(&parm1,&parm2) //&parm1 and &parm2 are variables defined in the Web Panel and their values are entered by the end user
EndEvent
```

The Sum method returns the sum of &parm1 and &parm2 values.

## [Deployment](#Deployment)

* **.NET:** In the case of using External Objects to access assemblies, the assembly or assemblies should be copied to the bin directory of the work environment. When the application is deployed, the assemblies must be taken to production.
* **Java:** In the case of Java classes, take the jar/zip containing the external classes that have to be included in the classpath.
* **JavaScript:** The JavaScript resources have to be located within the rest of the static resources of the web application. It needs to be referenced in the GeneXus code.

## [Considerations](#Considerations)

- Vector and matrix values are not supported; only [scalar](https://wiki.genexus.com/commwiki/wiki?7380) variables are supported.  
- Array data types such as String[], Date[] and so on are not supported.  
- Enum data types are not supported.  
- If there is an EO method called Initialized, or another reserved word, it must be defined with another name but keeping the External Name property.

## [Availability](#Availability)

Types node is available as Beta since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

## [See Also](#See+Also)

[External Objects for Android](https://wiki.genexus.com/commwiki/wiki?17878)  
[External Objects for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072)  
[External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064)


|  |
| --- |
| **Backlinks** |
| [.Net Assembly Import Wizard](https://wiki.genexus.com/commwiki/wiki?6177) | [APIs to integrate with payment methods](https://wiki.genexus.com/commwiki/wiki?50600) |
| [Category:External Object](https://wiki.genexus.com/commwiki/wiki?5669) | [Category:External Object (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57996) | [External Objects for Android](https://wiki.genexus.com/commwiki/wiki?17878) | [External Objects for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072) |
| [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) | [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) | [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58043) | [External Package Name property](https://wiki.genexus.com/commwiki/wiki?57626) |
| [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Execute GeneXus events from JS code using External Objects](https://wiki.genexus.com/commwiki/wiki?31075) | [HowTo: Implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066) | [Java Class Import Wizard](https://wiki.genexus.com/commwiki/wiki?6176) |
| [Java Method Throws Exceptions property](https://wiki.genexus.com/commwiki/wiki?37236) | [Javascript External Name property](https://wiki.genexus.com/commwiki/wiki?56499) | [Javascript Module Name property](https://wiki.genexus.com/commwiki/wiki?56496) |
| [Javascript Module Path property](https://wiki.genexus.com/commwiki/wiki?56406) | [Javascript Module Path property in Methods](https://wiki.genexus.com/commwiki/wiki?56478) | [Javascript Module Reference property](https://wiki.genexus.com/commwiki/wiki?56493) | [Should Await For Completion property](https://wiki.genexus.com/commwiki/wiki?56479) |
| [Should Await For Completion property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57562) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690) |
| [XML Namespace property](https://wiki.genexus.com/commwiki/wiki?37241) |

---
