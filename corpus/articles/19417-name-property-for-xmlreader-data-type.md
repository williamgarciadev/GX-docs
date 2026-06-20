---
title: "Name Property (for XMLReader Data Type)"
source_id: 19417
source_url: https://wiki.genexus.com/commwiki/wiki?19417
genexus_version: "18"
---

# Name Property (for XMLReader Data Type)

The Name property returns the tag name of the selected element.

### [Syntax](#Syntax)

*&DataType***.Name**

#### [Type Returned](#Type+Returned)

Character

### [Example](#Example)

#### [XML file](#XML+file)

<?xml version="1.0" encoding="ISO-8859-1" ?>  
<MEETING Date="08/28/12">  
     <DATE>08/28/12</DATE>  
     <!—Meeting description-->  
     <MEMBERS>  
          <MEMBER>Peter</MEMBER>  
          <MEMBER>Laura</MEMBER>  
          <MEMBER>John</MEMBER>  
          <MEMBER>Diana</MEMBER>  
     </MEMBERS>  
</MEETING>

#### [A possible process could be:](#A+possible+process+could+be%3A)

```
Event 'ReadXML'
    &xmlreader.Open('file.xml')
    &xmlreader.ReadType(1, 'MEMBERS')
    &xmlreader.read()
    do while &xmlreader.name <> 'MEMBERS'
       &character = &xmlreader.value + " - " + &character
       &xmlreader.read()
    enddo
    &xmlreader.close()
    msg(&xmlreader.ErrDescription)
EndEvent
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Extended Data Types:** | [XMLReader](https://wiki.genexus.com/commwiki/wiki?6928) |
| **Languages:** | .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3) |

### See Also

[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
