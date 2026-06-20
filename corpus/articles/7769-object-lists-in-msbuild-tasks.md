---
title: "Object lists in MSBuild tasks"
source_id: 7769
source_url: https://wiki.genexus.com/commwiki/wiki?7769
genexus_version: "18"
---

# Object lists in MSBuild tasks

Many of GeneXus MSBuild tasks can receive an object list specification parameter. The object list uses the following syntax:

```
<ListSpecification> ::= <SpecificationElement> [";" <ListSpecification>]

<SpecificationElement> ::= <ObjectsSpecification> | <FileSpecification>

<ObjectsSpecification> ::= [<ObjectType> ":"] <ObjectName> ["," <ObjectName>]

<FileSpecification> ::= "@" <filepathname>
```

In other words: an object list specification is a semicolon-separated list of elements, each of which can contain a comma-separated list of the same type of object names (optionally prefixed with a type name), or the pathname of an XML file containing a list of objects. When no type name is specified, the object name is assumed to be in the "objects" namespace, which is used by the most common types of GeneXus objects (eg: transaction, web panel, procedure, etc.). For other types, you need to specify the type name (eg: image, attribute, etc.)

e.g.:

```
Transaction:Invoice,Client,Product;MyObjectList.xml;@AnotherList.xml;Procedure:ListClients,PrintInvoices;WWItems,ManageClients,ViewInvoices
```

XML files containing a list of objects use the following format:

```
<Objects>

<Object guid="{object-guid}" />

<Object type="{type-guid}" >

<ObjName>name</ObjName>

</Object>

<Object>

<ObjName>name</ObjName>

</Object>

</Objects>
```

That is to say that an object can be identified by its GUID, in which case nothing else is needed, or by its name, optionally quallified with the type's GUID. When no type is specified, the name is assumed to be in the "objects" namespace.


|  |
| --- |
| **Backlinks** |
| [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) |
|

---
