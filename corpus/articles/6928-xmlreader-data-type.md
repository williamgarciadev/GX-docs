---
title: "XMLReader Data Type"
source_id: 6928
source_url: https://wiki.genexus.com/commwiki/wiki?6928
genexus_version: "18"
---

# XMLReader Data Type

It allows XML files or XML strings to be read.

### [Description](#Description)

A variable of a data type called XMLReader must be defined in order to read the content of an XML file or XML string from a GeneXus object. The methods and properties needed to obtain the information concerning the nodes that make it up must then be invoked.

The basic idea is that there is a Read() method that behaves like a cursor moving forward through the file, one node at a time. Using some properties such as Name and Value, it is possible to obtain the data for a node, in this case, its name and value. Thus, the Read() method is used to “navigate” through the document in a sequential way, obtaining the information on the different nodes.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [AttributeCount](https://wiki.genexus.com/commwiki/wiki?6927) | [Nodetype](https://wiki.genexus.com/commwiki/wiki?6997) |
| [EOF](https://wiki.genexus.com/commwiki/wiki?6975) | [Prefix](https://wiki.genexus.com/commwiki/wiki?7039) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) | [ReadExternalEntities](https://wiki.genexus.com/commwiki/wiki?6967) |
| [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) | [RemoveWhiteNodes](https://wiki.genexus.com/commwiki/wiki?7000) |
| [ErrLineNumber ErrLinePos](https://wiki.genexus.com/commwiki/wiki?7104) | [RemoveWhiteSpaces](https://wiki.genexus.com/commwiki/wiki?6960) |
| [IsSimple](https://wiki.genexus.com/commwiki/wiki?7044) | [SimpleElements](https://wiki.genexus.com/commwiki/wiki?6989) |
| [LocalName](https://wiki.genexus.com/commwiki/wiki?7034) | [ValidationType](https://wiki.genexus.com/commwiki/wiki?6969) |
| [Name](https://wiki.genexus.com/commwiki/wiki?19417) | [Value](https://wiki.genexus.com/commwiki/wiki?6950,,) |
| [NameSpaceURI](https://wiki.genexus.com/commwiki/wiki?7031) |  |

### [Methods](#Methods)

|  |  |
| --- | --- |
| [AddSchema](https://wiki.genexus.com/commwiki/wiki?7073) | [GetAttributePrefix](https://wiki.genexus.com/commwiki/wiki?2712) |
| [Close](https://wiki.genexus.com/commwiki/wiki?7093) | [GetAttributeURI](https://wiki.genexus.com/commwiki/wiki?2712) |
| [ExistsAttribute](https://wiki.genexus.com/commwiki/wiki?7062) | [Open](https://wiki.genexus.com/commwiki/wiki?6992) |
| [GetAttEntityNotationByIndex](https://wiki.genexus.com/commwiki/wiki?7105) | [OpenFromString](https://wiki.genexus.com/commwiki/wiki?7050) |
| [GetAttEntityNotationByName](https://wiki.genexus.com/commwiki/wiki?7105) | [Read](https://wiki.genexus.com/commwiki/wiki?7049) |
| [GetAttEntityValueByIndex](https://wiki.genexus.com/commwiki/wiki?7105) | [ReadRawXML](https://wiki.genexus.com/commwiki/wiki?7099) |
| [GetAttEntityValueByName](https://wiki.genexus.com/commwiki/wiki?7105) | [ReadType](https://wiki.genexus.com/commwiki/wiki?7048) |
| [GetAttributeByIndex](https://wiki.genexus.com/commwiki/wiki?7081) | [Skip](https://wiki.genexus.com/commwiki/wiki?7085) |
| [GetAttributeByName](https://wiki.genexus.com/commwiki/wiki?7082) | [SetDocEncoding](https://wiki.genexus.com/commwiki/wiki?7054) |
| [GetAttributeLocalName](https://wiki.genexus.com/commwiki/wiki?2712) | [SetNodeEncoding](https://wiki.genexus.com/commwiki/wiki?7055) |
| [GetAttributeName](https://wiki.genexus.com/commwiki/wiki?2712) |  |

Say we have the following XML document, called Meeting.xml:  
  
<?xml version="1.0" encoding="ISO-8859-1" ?>  
<MEETING Date="**06/03/01**">  
  <DATE>**06/03/01**</DATE>  
   <!—Meeting description-->  
<! [ CDATA [ Meeting of the application development team.  
The meeting was held on Friday, 9.30 a.m. ] ] >  
<MEMBERS>  
  <MEMBER>**Peter**</MEMBER>  
  <MEMBER>**Laura**</MEMBER>  
  <MEMBER>**John**</MEMBER>  
  <MEMBER>**Diana**</MEMBER>  
  </MEMBERS>  
<TASKS>  
<TASK>  
  <PERSON\_IN\_CHARGE>**Peter**</PERSON\_IN\_CHARGE>  
   <! [ CDATA [ Write the application’s documentation ] ] >  
  </TASK>  
<TASK>  
  < PERSON\_IN\_CHARGE >**Diana**</ PERSON\_IN\_CHARGE >  
   <! [ CDATA [ Meet with clients ] ] >  
  </TASK>  
<TASK>  
  < PERSON\_IN\_CHARGE >**Laura**</ PERSON\_IN\_CHARGE >  
   <! [ CDATA [ Write user’s manual ] ] >  
  </TASK>  
<TASK>  
  < PERSON\_IN\_CHARGE >**John**</ PERSON\_IN\_CHARGE >  
   <! [ CDATA [ Document the specifications ] ] >  
  </TASK>  
  </TASKS>  
  </MEETING>  
  
The following GeneXus procedure reads the file and obtains the members attending the meeting:

```
&XMLReader.Open('Meeting.xml')     
&XMLReader.ReadType(1, 'MEMBERS')
&XMLReader.Read()
    Do While &XMLReader.Name <> 'MEMBERS'
       &MEMBER = &XMLReader.Value
       &XMLReader.Read()                                                             
    Enddo
&XMLReader.Close()
```

The following GeneXus procedure reads the file and obtains the tasks of a member attending the meeting:

```
&XMLReader.Open('Meeting.xml') 
&success = &XMLReader.ReadType(1,'PERSON_IN_CHARGE') 
Do While &XMLReader.Value <> &MEMBER 
   &success = &XMLReader.ReadType(1,'PERSON_IN_CHARGE')
   If &success = 0
      Exit
   Endif
Enddo

If &success <> 0
   &XMLReader.Read()
   &tasks = &XMLReader.Value
Else
   &tasks = Nullvalue(&tasks)
Endif
&XMLReader.Close()
```

## [Security tips](#Security+tips)

When a property or method is used to assign a file's path (or URL) do not use user's inputs concatenations or sanitize the user's entries to avoid path traversal or path manipulation vulnerability risks.

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[XMLWriter](https://wiki.genexus.com/commwiki/wiki?6938)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A05:2021 - Security misconfiguration](https://wiki.genexus.com/commwiki/wiki?50185) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [AddSchema method](https://wiki.genexus.com/commwiki/wiki?7073) |
| [AttributeCount Property](https://wiki.genexus.com/commwiki/wiki?6927) | [Close method](https://wiki.genexus.com/commwiki/wiki?7093) | [Data Types for Http Handling](https://wiki.genexus.com/commwiki/wiki?10150) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [EOF Property](https://wiki.genexus.com/commwiki/wiki?6975) | [EOF Property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55641) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) |
| [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [ErrLineNumber and ErrLinePos Properties](https://wiki.genexus.com/commwiki/wiki?7104) | [ExistsAttribute method](https://wiki.genexus.com/commwiki/wiki?7062) | [External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) |
| [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) | [GetAttributeByIndex method](https://wiki.genexus.com/commwiki/wiki?7081) |
| [GetAttributeByName method](https://wiki.genexus.com/commwiki/wiki?7082) | [GetAttributeName, GetAttributePrefix, GetAttributeLocalName,GetAttributeURI Methods](https://wiki.genexus.com/commwiki/wiki?2712) | [IsSimple Property](https://wiki.genexus.com/commwiki/wiki?7044) | [LocalName Property](https://wiki.genexus.com/commwiki/wiki?7034) |
| [Name Property (for XMLReader Data Type)](https://wiki.genexus.com/commwiki/wiki?19417) | [NameSpaceURI Property](https://wiki.genexus.com/commwiki/wiki?7031) | [NodeType Property](https://wiki.genexus.com/commwiki/wiki?6997) |
| [Open method](https://wiki.genexus.com/commwiki/wiki?6992) | [OpenFromString method](https://wiki.genexus.com/commwiki/wiki?7050) | [OpenRequest method](https://wiki.genexus.com/commwiki/wiki?7692) | [OpenResponse method](https://wiki.genexus.com/commwiki/wiki?7694) |
| [Read method](https://wiki.genexus.com/commwiki/wiki?7049) | [ReadExternalEntities Property](https://wiki.genexus.com/commwiki/wiki?6967) | [ReadRawXML method](https://wiki.genexus.com/commwiki/wiki?7099) | [ReadType method](https://wiki.genexus.com/commwiki/wiki?7048) |
| [RemoveWhiteNodes Property](https://wiki.genexus.com/commwiki/wiki?7000) | [RemoveWhiteSpaces Property](https://wiki.genexus.com/commwiki/wiki?6960) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [SetDocEncoding method](https://wiki.genexus.com/commwiki/wiki?7054) | [SetNodeEncoding method](https://wiki.genexus.com/commwiki/wiki?7055) | [SimpleElements Property](https://wiki.genexus.com/commwiki/wiki?6989) |
| [Skip method](https://wiki.genexus.com/commwiki/wiki?7085) | [ValidationType property](https://wiki.genexus.com/commwiki/wiki?6969) | [XMLReader Attribute Methods](https://wiki.genexus.com/commwiki/wiki?7105) |
| [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
