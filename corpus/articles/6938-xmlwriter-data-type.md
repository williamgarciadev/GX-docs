---
title: "XMLWriter Data Type"
source_id: 6938
source_url: https://wiki.genexus.com/commwiki/wiki?6938
genexus_version: "18"
---

# XMLWriter Data Type

The aim of this data type is to provide the possibility of recording XML files or strings.

### [Description](#Description)

In order to be able to create an XML file or string from a GeneXus object you must define an XMLWriter data type variable and then invoke the methods needed to create the nodes that compose it.

### [Properties](#Properties)

|  |
| --- |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) |
| [Indentation](https://wiki.genexus.com/commwiki/wiki?7012) |
| [IndentChar](https://wiki.genexus.com/commwiki/wiki?6998) |
| [ResultingString](https://wiki.genexus.com/commwiki/wiki?6959) |

### [Methods](#Methods)

|  |  |
| --- | --- |
| [Close](https://wiki.genexus.com/commwiki/wiki?7093) | [WriteDocType](https://wiki.genexus.com/commwiki/wiki?7095) |
| [Open](https://wiki.genexus.com/commwiki/wiki?6992) | [WriteDocTypePublic](https://wiki.genexus.com/commwiki/wiki?7094) |
| [OpenToString](https://wiki.genexus.com/commwiki/wiki?7077) | [WriteDocTypeSystem](https://wiki.genexus.com/commwiki/wiki?7096) |
| [OpenRequest](https://wiki.genexus.com/commwiki/wiki?7692) | [WriteNSElement](https://wiki.genexus.com/commwiki/wiki?7059) |
| [OpenResponse](https://wiki.genexus.com/commwiki/wiki?7694) | [WriteNSStartElement](https://wiki.genexus.com/commwiki/wiki?7060) |
| [WriteAttribute](https://wiki.genexus.com/commwiki/wiki?7068) | [WriteProcessingInstruction](https://wiki.genexus.com/commwiki/wiki?7076) |
| [WriteCData](https://wiki.genexus.com/commwiki/wiki?7052) | [WriteRawText](https://wiki.genexus.com/commwiki/wiki?7075) |
| [WriteComment](https://wiki.genexus.com/commwiki/wiki?7051) | [WriteStartElement](https://wiki.genexus.com/commwiki/wiki?7069) |
| [WriteElement](https://wiki.genexus.com/commwiki/wiki?7070) | [WriteStartDocument](https://wiki.genexus.com/commwiki/wiki?7083) |
| [WriteEndElement](https://wiki.genexus.com/commwiki/wiki?7072) | [WriteText](https://wiki.genexus.com/commwiki/wiki?7074) |
| [WriteEntityReference](https://wiki.genexus.com/commwiki/wiki?7071) |  |

### [Example](#Example)

The following procedure generates a file called MEETING.xml that contains the data for a meeting, indicating the people who participated in it and their corresponding tasks.

```
	For Each
    &XMLWriter.Open('MEETING.xml')
    &XMLWriter.WriteStartDocument()
    &XMLWriter.WriteStartElement('MEETING')
    &XMLWriter.WriteAttribute('Date', DToC(ReuFch))
    &XMLWriter.WriteElement('DATE', DToC(ReuFch))
    &XMLWriter.WriteComment('Meeting Description')    
    &XMLWriter.WriteCData(ReuDsc)
    &XMLWriter.WriteStartElement('MEMBERS')
    For Each
        &XMLWriter.WriteElement('MEMBER',ReuPerNom)
    Endfor
    &XMLWriter.WriteEndElement()   
    &XMLWriter.WriteStartElement('TASKS')
    For Each
        &XMLWriter.WriteStartElement('TASK')
        &XMLWriter.WriteElement('PERSON_IN_CHARGE',ReuTarPerNom)
        &XMLWriter.WriteCData(ReuTarDsc)
        &XMLWriter.WriteEndElement()
    EndFor
    &XMLWriter.WriteEndElement() 
    &XMLWriter.WriteEndElement()    
    &XMLWriter.Close()
Endfor
```

The MEETING.xml file contains:  
  
<?xml version="1.0" encoding="ISO-8859-1" ?>  
<MEETING Date="**06/03/01**">  
  <DATE>**06/03/01**</DATE>  
   <!—Meeting’s description-->  
<! [ CDATA [ Application development team’s meeting.  
The meting took place on Friday at 9:30. ] ] >  
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
  <PERSON\_IN\_CHARGE>**Diana**</PERSON\_IN\_CHARGE>  
   <! [ CDATA [ Meet with clients ] ] >  
  </TASK>  
<TASK>  
  <PERSON\_IN\_CHARGE>**Laura**</PERSON\_IN\_CHARGE>  
   <! [ CDATA [ Write user’s manual ] ] >  
  </TASK>  
<TASK>  
  <PERSON\_IN\_CHARGE>**John**</PERSON\_IN\_CHARGE>  
   <! [ CDATA [ Document the specifications ] ] >  
  </TASK>  
  </TASKS>  
  </MEETING>

## [Security tips](#Security+tips)

When a property or method is used to assign a file's path (or URL) do not use user's inputs concatenations or sanitize the user's entries to avoid path traversal or path manipulation vulnerability risks.

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[XMLReader](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [Close method](https://wiki.genexus.com/commwiki/wiki?7093) | [Data Types for Http Handling](https://wiki.genexus.com/commwiki/wiki?10150) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) |
| [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) | [Indentation Property](https://wiki.genexus.com/commwiki/wiki?7012) |
| [Indentchar Property](https://wiki.genexus.com/commwiki/wiki?6998) | [Open method](https://wiki.genexus.com/commwiki/wiki?6992) | [OpenRequest method](https://wiki.genexus.com/commwiki/wiki?7692) |
| [OpenResponse method](https://wiki.genexus.com/commwiki/wiki?7694) | [OpenToString method](https://wiki.genexus.com/commwiki/wiki?7077) | [ResultingString Property](https://wiki.genexus.com/commwiki/wiki?6959) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) |
| [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) | [WriteAttribute method](https://wiki.genexus.com/commwiki/wiki?7068) | [WriteCData method](https://wiki.genexus.com/commwiki/wiki?7052) |
| [WriteComment method](https://wiki.genexus.com/commwiki/wiki?7051) | [WriteDocType method](https://wiki.genexus.com/commwiki/wiki?7095) | [WriteDocTypePublic method](https://wiki.genexus.com/commwiki/wiki?7094) | [WriteDocTypeSystem method](https://wiki.genexus.com/commwiki/wiki?7096) |
| [WriteElement method](https://wiki.genexus.com/commwiki/wiki?7070) | [WriteEndElement method](https://wiki.genexus.com/commwiki/wiki?7072) | [WriteEntityReference method](https://wiki.genexus.com/commwiki/wiki?7071) | [WriteNSElement method](https://wiki.genexus.com/commwiki/wiki?7059) |
| [WriteNSStartElement method](https://wiki.genexus.com/commwiki/wiki?7060) | [WriteProcessingInstruction method](https://wiki.genexus.com/commwiki/wiki?7076) | [WriteRawText method](https://wiki.genexus.com/commwiki/wiki?7075) | [WriteStartDocument method](https://wiki.genexus.com/commwiki/wiki?7083) |
| [WriteStartElement method](https://wiki.genexus.com/commwiki/wiki?7069) | [WriteText method](https://wiki.genexus.com/commwiki/wiki?7074) | [XML Information Properties (SDT)](https://wiki.genexus.com/commwiki/wiki?7272) | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
