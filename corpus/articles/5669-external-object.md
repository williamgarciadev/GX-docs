---
title: "External Object"
source_id: 5669
source_url: https://wiki.genexus.com/commwiki/wiki?5669
genexus_version: "18"
---

# External Object

Defines the programming interface for an external resource from the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) as if it were just another object.

The external resources can be native classes of the language, assemblies (.dll) if they are developed in .NET, or classes (.class) in the case of Java. In addition, they can be Enterprise Java Beans (EJB), [Stored Procedures](https://wiki.genexus.com/commwiki/wiki?6138) (SP), or [Web Services](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2894,,) (WS).

### [Creation](#Creation)

You can define external objects in two ways: manually or using a Wizard/Inspector.

* #### [Manual definition:](#Manual+definition%3A)

  You can create an EO manually from the [New Object dialog](https://wiki.genexus.com/commwiki/wiki?9931) and define the following according to your needs:

  + Properties: This is information such as characteristics or attributes.
  + Methods: They are functionalities that the EO provides and can be called from other GeneXus objects. Methods can be used to perform specific operations, interact with the EO, or process data according to the needs of the application.
  + Events: These are actions or events that can trigger specific responses in the application. These events can be used to notify the application about state changes, errors, or any other type of activity.
  + Types: They are a characteristic that facilitates the definition of generic and adaptable data structures. This allows a dynamic adaptation to different data types without the need for case-specific definitions. This means that the same type can be used with different data types. For more information, read [External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997).

* #### [Using Wizard/Inspector:](#Using+Wizard%2FInspector%3A)

  To create an EO through Wizards/Inspectors, go to Toolbar>Tools>Application Integration and select one of the following options:

  + [.Net Assembly Import](https://wiki.genexus.com/commwiki/wiki?6177)
  + [Java Class Import](https://wiki.genexus.com/commwiki/wiki?6176)
  + [WSDL Import](https://wiki.genexus.com/commwiki/wiki?6181)

Depending on the type of EO, you will be able to define properties and/or choose certain Wizards that you can use to create EOs. The types of EOs are as follows:

* [Stored Procedure](https://wiki.genexus.com/commwiki/wiki?6138)
* [Native Object (assemblies and/or classes)](https://wiki.genexus.com/commwiki/wiki?6148)
* [WSDL (Web Service)](https://wiki.genexus.com/commwiki/wiki?6154)
* [Java Session Beans](https://wiki.genexus.com/commwiki/wiki?6197)

### [Use](#Use)

Once an EO has been defined based on the properties related to the external resource you wish to use, the EO will be available just like any other type of data in the Knowledge Base, and you can use it from any of the objects you have. This is done in the same way as with any [extended data type](https://wiki.genexus.com/commwiki/wiki?6560): by defining a variable of that type and then calling the methods and/or setting the properties you need.

### [**Notes**](#Notes)

External objects aren't intended for the following cases:

* To interact with external Data (data on tables maintained by other applications), use [Data Views](https://wiki.genexus.com/commwiki/wiki?1914). That is, create a Data View object or let the [Database Reverse Engineering Tool](https://wiki.genexus.com/commwiki/wiki?6634) do the work for you.
* To interact with external Javascript, take a look at [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064).

### [Availability](#Availability)

Types node is available as Beta since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Pages** |
| [.Net Assembly Import Wizard](https://wiki.genexus.com/commwiki/wiki?6177) | [Allow Collection property](https://wiki.genexus.com/commwiki/wiki?57845) | [Compression External Object](https://wiki.genexus.com/commwiki/wiki?60618) |
| [CompressionConfiguration External Object](https://wiki.genexus.com/commwiki/wiki?60619) | [Contacts External Object](https://wiki.genexus.com/commwiki/wiki?31276) | [Default Type property](https://wiki.genexus.com/commwiki/wiki?57846) |
| [Dictionary External Object](https://wiki.genexus.com/commwiki/wiki?58246) | [External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997) | [External Object: Java Session Bean](https://wiki.genexus.com/commwiki/wiki?6197) |
| [External Object: Stored Procedure](https://wiki.genexus.com/commwiki/wiki?6138) | [External Object: WSDL - Web Service](https://wiki.genexus.com/commwiki/wiki?6154) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) |
| [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) | [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58043) | [HowTo: Implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066) |
| [Java Class Import Wizard](https://wiki.genexus.com/commwiki/wiki?6176) | [Javascript External Name property](https://wiki.genexus.com/commwiki/wiki?56499) | [Javascript Module Name property](https://wiki.genexus.com/commwiki/wiki?56496) |
| [Javascript Module Path property](https://wiki.genexus.com/commwiki/wiki?56406) | [Javascript Module Path property in Methods](https://wiki.genexus.com/commwiki/wiki?56478) | [Javascript Module Reference property](https://wiki.genexus.com/commwiki/wiki?56493) |
| [Parameters Style property in External Object](https://wiki.genexus.com/commwiki/wiki?53486) | [Property Name property](https://wiki.genexus.com/commwiki/wiki?57843) | [Should Await For Completion property](https://wiki.genexus.com/commwiki/wiki?56479) |
| [Should Await For Completion property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57562) | [Span External Object](https://wiki.genexus.com/commwiki/wiki?57597) | [SpanContext External Object](https://wiki.genexus.com/commwiki/wiki?57603) |
| [TraceContext External Object](https://wiki.genexus.com/commwiki/wiki?57604) | [Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593) | [Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690) |
| [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) | [Valid Types property](https://wiki.genexus.com/commwiki/wiki?57844) | [WSDL Import Wizard](https://wiki.genexus.com/commwiki/wiki?6181) |

---
