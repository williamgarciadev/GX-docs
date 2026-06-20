---
title: "Properties data type"
source_id: 31606
source_url: https://wiki.genexus.com/commwiki/wiki?31606
genexus_version: "18"
---

# Properties data type

This type represents a key-value list and it can be used for many purposes. For example, it can be used as a filter in the **GetAttribute** method of [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886). It can also be used with the Queue data type.

### [Properties](#Properties)

Count

Counts the number of items in the collection of properties.  
It is available as of [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,).

**Type Returned:** Numeric

### [Methods](#Methods+)

#### [Set](#Set)

Adds an attribute to be used as a filter. [Learn more](https://wiki.genexus.com/commwiki/wiki?6810)

**Type Returned:** None  
**Parameters:**  id:Character(20), value:Character(50)

#### [Clear](#Clear)

Clears all the key-value pairs added. [Learn more](https://wiki.genexus.com/commwiki/wiki?7084)

**Type Returned:**None  
**Parameters:**None

#### [Get](#Get)

Returns the value of a given key. [Learn more](https://wiki.genexus.com/commwiki/wiki?6812)

**Type Returned:**value:Character  
**Parameters:**id:Character

Remove

Removes the specified key. [Learn more](https://wiki.genexus.com/commwiki/wiki?6811)

**Type Returned:**None  
**Parameters:**id:Character

#### [ToJson](#ToJson)

It returns a string in JSON format.

**Type Returned:**json:Character  
**Parameters:**None

#### [FromJson](#FromJson)

It receives a string with JSON format and loads the variable with its content.

**Type Returned:**Boolean  
**Parameters:**source:Character

### Iterating properties

The following code reads all the properties stored in a variable based on the Properties data type.

Sample

```
for &property in &myProperties 
    msg(&property.Key)
    msg(&property.Value)
endfor
```

&myProperties is a variable based on the Properties data type.  
&property is a variable based on the [Property data type](https://wiki.genexus.com/commwiki/wiki?6888).

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [See also](#See+also)

[Consuming JSON with GeneXus Properties Data Type](https://wiki.genexus.com/commwiki/wiki?37750)


|  |
| --- |
| **Backlinks** |
| [Clear method for variables based on Extended data types](https://wiki.genexus.com/commwiki/wiki?7084) | [Configuration.ExternalStorage External Object](https://wiki.genexus.com/commwiki/wiki?45913) | [Consuming JSON with GeneXus Properties Data Type](https://wiki.genexus.com/commwiki/wiki?37750) |
| [Dictionary External Object](https://wiki.genexus.com/commwiki/wiki?58246) | [Property Data Type](https://wiki.genexus.com/commwiki/wiki?6888) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |

---
