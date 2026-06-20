---
title: "Structured Data Type editor"
source_id: 6365
source_url: https://wiki.genexus.com/commwiki/wiki?6365
genexus_version: "18"
---

# Structured Data Type editor

The Structured Data Type editor allows you to define the structure of a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021).

While creating a Structured Data Type (SDT) object, you may define a multilevel structure, similar to the Transaction's structure. Each level can have one or more members. These members may be classified into:

* Simple Elements
* Compound Elements (also composed of other elements).

### [Simple Elements](#Simple+Elements)

While defining a member in a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021), you must specify the following:

* **Name property:** Identifies the member. There cannot be two elements defined with the same name.
* **Data Type property:** You can select between GeneXus basic types (Numeric, Character, etc), Domains, or another already defined SDT.
* **Is Collection property:** Indicates whether the element has multiple instances (it can be repeated) or not. It has two possible values: True or False.

Look at the following image:

`[imagen omitida: wiki id 6452]`

#### [**XML Properties**](#XML+Properties)

While working with [SDTs](https://wiki.genexus.com/commwiki/wiki?10021) you can define some properties related to each kind of element, in order to have control over the SDT serialization to different formats, such as XML. When working with a simple element (a member), you will see the following XML properties:

* XmlType
* XML Namespace

These properties allow you to have control over the XML that will be generated.

`[imagen omitida: wiki id 6479]`

**XmlType Property**

This property may have one of the following values:

* **Element:** This is the default value. The element (member) will be serialized as an XML Element.
* **Attribute:** The member will appear as an XML attribute but in the last level of the parent element.
* **CData:** The member will be serialized as an element with a CDATA. It is usually used with values that contain XML.
* **Value:** The member will be the Value of the parent Element.

**XML Namespace property**

### [Compound Elements](#Compound+Elements)

They are those elements defining a new element group, a new collection, or a group of simple elements.

Different bullets, in the editor, identify the compound elements:

`[imagen omitida: wiki id 6453]` Identifies a member in a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)

`[imagen omitida: wiki id 6454]` Identifies a collection

`[imagen omitida: wiki id 6455]` Identifies a structure, a group of simple elements

Compound elements have the same properties as simple elements, but the Data Type property is not enabled.

In the following example you can see a Structured Data Type named Customers with some simple and compound elements:

`[imagen omitida: wiki id 6456]`

Now look at the corresponding Properties windows:

`[imagen omitida: wiki id 6457]` `[imagen omitida: wiki id 6458]` `[imagen omitida: wiki id 6459]`

When a substructure defines a collection, besides the data type created with the SDT name, there will be another data type created with Name.SubstructureName, and they will be selectable as data types in any variable definition. This means that the two data types will be created. Following the example, while defining variables in a procedure, you may see:

`[imagen omitida: wiki id 6461]`

Stop and take a look again at the image of the **Collection** properties window. Can you see the **Collection Serialization** property?

`[imagen omitida: wiki id 6480]`

The purpose of this property is to help solve the problem of how to serialize a collection. Its possible values are:

* **Wrapped:** Default value. Includes the collection start/end tag.
* **Sequence:** Will serialize as a plain sequence of collection elements.

### [Different Actions over each kind of Element](#Different+Actions+over+each+kind+of+Element)

As with any other editor, the SDT editor allows you to define actions over each kind of element by right-clicking on:

* Structured Data Type
* Collection
* Member

**Drag and drop:** You can select a Transaction from the Folder View and drop it into the SDT structure. The Transaction structure will be added to the SDT structure.

##### [Structured Data Type](#Structured+Data+Type)

By right-clicking on a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) you will see the following secondary menu:

`[imagen omitida: wiki id 6462]`

* **Insert Member:** This allows you to insert a new member to the [SDT](https://wiki.genexus.com/commwiki/wiki?10021) structure.
* **References:** Displays which objects refer to the [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021).
* **History:** Displays all modifications that were done to the [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) (version, name, date, user).
* **Properties:** Displays the Properties window.
* **Locate in Folder View:** This shows you where the [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) is located within the Folder View / KB Explorer.

`[imagen omitida: wiki id 6463]` `[imagen omitida: wiki id 6464]`

**Note:** When you need to insert a new member in the structure, you may use the corresponding option in this secondary menu shown above, or you may also drag the attribute to the structure. Look at the following image:

`[imagen omitida: wiki id 6485]`

Another method for inserting members in the SDT structure is to use the Insert Menu from the GeneXus main toolbar.  
The available menu options are :

* Insert Attribute: inserts a member with the same name and with type based on the selected attribute
* Insert Domain: inserts a member with the same name and with type based on the selected domain
* Insert Object (only Transactions can be selected): inserts one member for each attribute in the Transaction structure, with the same name and type based on it. Note: If the description of an attribute of the Transaction changes, it also changes in the SDT structure (as since GeneXus 15 upgrade 3).

If the focus is on the SDT structure root, the new members added with the Insert menu will be placed on the end of the structure, if the focus is on one existing member, the new member will be added immediately after the selected one.

#### [Collection](#Collection)

By right-clicking on a Collection you will see the following secondary menu:

`[imagen omitida: wiki id 6465]`

* **Delete:** Deletes the Collection.
* **Move Items Up:** Moves the Collection up in the [SDT](https://wiki.genexus.com/commwiki/wiki?10021) structure.
* **Move Items Down:** Moves the Collection down in the [SDT](https://wiki.genexus.com/commwiki/wiki?10021) structure.
* **Indent:** Adds the selected collection under a new collection.
* **Unindent:** Takes the selected collection away from its container collection.
* **Insert Member:** This allows you to insert a new member to the collection.
* **Insert Sibling Substructure:** This allows you to define a substructure under the [SDT](https://wiki.genexus.com/commwiki/wiki?10021) structure (under Customers, in the example above).
* **Properties:** Displays the Properties window.

#### [Substructure](#Substructure)

By right-clicking on a Substructure you will see a secondary menu quite similar to the Collection menu:

`[imagen omitida: wiki id 6467]`

#### [Member](#Member)

By right-clicking on a Member you will see a secondary menu quite similar to the Collection menu:

`[imagen omitida: wiki id 6466]`

### [Examples of SDT Serialization to XML](#Examples+of+SDT+Serialization+to+XML)

1) Suppose that you have the following SDT:

`[imagen omitida: wiki id 6481]`

You want to generate the following XML:

```
Richard Smith
```

So, you will need to set the following values to the corresponding properties:

* XmlType property in Id member: attribute
* XmlType property in Name member: value

2) Suppose that you have now defined an SDT like the one below:

`[imagen omitida: wiki id 6483]`

The collection may be serialized as follows:

```
<Country>
       <Cities>
            <CityName>Montevideo</CityName>
            <CityName>Rocha</CityName>
            ...
        </Cities>
</Country>
```

In this case, the Collection Serialization property must be specified as Wrapped

Or as:

```
<Country>
    <CityName>Montevideo</CityName>
    <CityName>Rocha</CityName>
     ...
</Country>
```

In this case, the Collection Serialization property must be specified as Sequence

### [Defining a Collection Based on Any Data Type](#Defining+a+Collection+Based+on+Any+Data+Type)

By working with the SDT Editor, you may define collections as shown in the following image:

`[imagen omitida: wiki id 6488]`

However, you will not be able to define a collection based on any Data Type (Numeric, Character, another SDT data type, [BC](https://wiki.genexus.com/commwiki/wiki?5846), etc). In order to solve this situation, you must work with [Collection Domains](https://wiki.genexus.com/commwiki/wiki?6393), or you may even define a [Collection Variable](https://wiki.genexus.com/commwiki/wiki?6352) based on the corresponding Data Type, as shown below.

`[imagen omitida: wiki id 6530]`

### [See Also](#See+Also)

[Recursive SDTs](https://wiki.genexus.com/commwiki/wiki?4680)  
[Implementing SDT Collections](https://wiki.genexus.com/commwiki/wiki?6296)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Compound data types](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/compound-data-types-6098937?p=5262)  
`[imagen omitida: wiki id 20668]` [Loading Compound Data Types (SDT) using Data Providers](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/loading-compound-data-types-sdt-using-data-providers?p=5265)


|  |
| --- |
| **Backlinks** |
| [Collection property (IsCollection checkbox)](https://wiki.genexus.com/commwiki/wiki?9761) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296) |
| [Recursive SDTs](https://wiki.genexus.com/commwiki/wiki?4680) | [Category:Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) |

---
