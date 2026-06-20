---
title: "Serialization of Business Components"
source_id: 20207
source_url: https://wiki.genexus.com/commwiki/wiki?20207
genexus_version: "18"
---

# Serialization of Business Components

Business components can be serialized to XML or JSON.

In both cases the state of the record is included in the serialization:

```
Personas.ToXml()

<Personas>
   <PersonaId>3</PersonaId>
   <PersonaId_z>3</PersonaId_z>
   <PersonaName>Juan</PersonaName>
   <PersonaName_z>Juan</PersonaName_z>
   <PersonaDate>2012-06-08</PersonaDate>
   <PersonaDate_z>2012-06-08</PersonaDate_z>
   <PersonaImage xmlns=''>
   </PersonaImage>
   <PersonaImage_GXI>
   </PersonaImage_GXI>
   <PersonaImage_GXI_z>
   </PersonaImage_GXI_z>
   <gx_mode>UPD</gx_mode>
   <initialized>0</initialized>
</Personas>
```

Sometimes it is desirable to serialize the record data only, and to avoid the auxiliar variables (like old values, mode, initialized flag, etc), so the generated code can interact easily with other applications. Something like:

```
Personas.ToXml(False, False)

<Personas>
   <PersonaId>3</PersonaId>
   <PersonaName>Juan</PersonaName>
   <PersonaDate>2012-06-08</PersonaDate>
   <PersonaImage >
   </PersonaImage>
</Personas>
```

You can do that with the *IncludeState*  boolean parameter. It is an optional one, and the default  value is *False*.

It applies both to .ToXML and .ToJson methods.

In the case of .ToJSon the return would be:

```
Personas.ToJson()

{ "PersonaId":3, "PersonaId_z":3, "PersonaName":"Juan", "PersonaName_z":"Juan", "PersonaDate":"2012-06-08", "PersonaDate_z":"2012-06-08", "PersonaImage":"","PersonaImage_z":"",

"PersonaImage_GXI":"", "PersonaImage_GXI_z":"", "gx_mode":"UPD", "initialized":0}
```

```
Personas.ToJson(False)

{ "PersonaId":3, "PersonaName":"Juan", "PersonaDate":"2012-06-08","PersonaImage":""}
```


|  |
| --- |
| **Backlinks** |
| [ToXml method - SDT](https://wiki.genexus.com/commwiki/wiki?8789) |

---
