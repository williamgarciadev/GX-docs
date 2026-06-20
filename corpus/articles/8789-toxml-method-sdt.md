---
title: "ToXml method - SDT"
source_id: 8789
source_url: https://wiki.genexus.com/commwiki/wiki?8789
genexus_version: "18"
---

# ToXml method - SDT

Returns a string with the XML format of the SDT variable data.

### [Syntax](#Syntax)

*CharacterAttOrVar = **&****VarBasedOnSDT**.******ToXml(***  [*boolean IncludeHeader*] *,*[*boolean IncludeState*]***)***

**Where:**

*CharacterAttOrVar*  
    Attribute or variable based on Character data type

*&VarBasedOnSDT*  
    Variable based on an [SDT](https://wiki.genexus.com/commwiki/wiki?10021)

*boolean IncludeHeader*  
    Optional parameter: If true, then the returned string contains this header tag: "<?xml version = "1.0" encoding = "UTF-8"?>". The default value is false.

*boolean IncludeState*  
    Optional parameter: It only applies to Business Components variables. If true, then the returned string contains the auxiliary variables (old values, mode, initialized flag). Otherwise, it only contains the record data. The default value is true.

**Type Returned:**   
Character

### [Scope](#Scope)

**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

It is the opposite of FromXML. It returns an XML string with the data of the SDT.

**Note**: The ToXML method applied to SDTs which have a blob data type item results in an XML in which the blob is represented as a base64 string ([SAC #30011](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,S,0,,30011;S;0;A;0;0;;;;;;;;;;;;;;;;;A;%20%20/%20%20/%20%20;;0;9;;30011;;99;;0;1;%200;N;N;S;B;B))

### [Samples](#Samples)

One of the possible contents of the resulting string would be the following:

```
<SDTName xmlns = “name_Kb”>
   <Name>Uruguay</Name>
   <Language>Spanish</Language>
   <Cordinating>
        <Latitude>30</Latitude>
        <Longitude>35</Longitude>
   </Cordinating >
   <Cities>
        <Item>Montevideo</Item>
        <Item>Paysandú</Item>
  </Cities>
```

### [Availability](#Availability)

Available since [GeneXus X Evolution 2](https://wiki.genexus.com/commwiki/wiki?15152,,) Upgrade 2.

### [See Also](#See+Also)

[FromXml Method](https://wiki.genexus.com/commwiki/wiki?8788)  
[Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)  
[Serialization of Business Components](https://wiki.genexus.com/commwiki/wiki?20207)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [FromXml method - SDT](https://wiki.genexus.com/commwiki/wiki?8788) | [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
