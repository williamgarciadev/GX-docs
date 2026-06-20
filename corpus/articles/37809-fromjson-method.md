---
title: "FromJson method"
source_id: 37809
source_url: https://wiki.genexus.com/commwiki/wiki?37809
genexus_version: "18"
---

# FromJson method

Loads a variable based on a [Structured Data Type (SDT)](https://wiki.genexus.com/commwiki/wiki?10021) or [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) from a JSON string received as a parameter.

### [Syntax](#Syntax)

[&Boolean =] &var**.FromJson(**AttOrVar[, &Messages]**)**

**Where:**  
*&var*  
    Variable based on an SDT or Business Component.

*AttOrVar*  
    [Attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) with the JSON content.

*&Messages*  
   Variable based on the GeneXus's Messages data type. In case of an error, it will contain the error information. This parameter is optional.

**Type returned:**  
Boolean  
   It returns False in case of having an error; otherwise, it returns True. The assignment of the return value is optional.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The FromJson method loads the &var structure from the CharacterAttOrVar content. The variable's JSON format (&String) must be compatible with the variable based on an SDT or Business Component structure (&var).

### [Samples](#Samples+)

Consider a Structured Data Type defined as follows:

SDT1  
{  
     NumericMember: Numeric  
     CharacterMember: Character  
     GeoPointMember: GeoPoint  
 }

Define the following code (for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) / [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Event):

```
 &VarBasedOnSDT1.FromJson('[{"NumericMember": 0,"CharacterMember":"ValueCharacter","GeoPointMember":"POINT(-56.10 -33.01)"}]')
```

The above code initializes the &VarBasedOnSDT1 variable.

Note that the GeoPointMember receives a value in WellKnowText Format (WKT). Another alternative, only available when generating for Android, is to pass a [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) format as parameter, as follows:

```
&VarBasedOnSDT1.FromJson('[{"NumericMember": 0,"CharacterMember":"VallueCharacter","GeoPointMember":"57.10, 68.9"}]')
```

### [Technical Details](#Technical+Details)

**Data Type Mapping**

The GeneXus basic data types are mapped to JSON data types in this way:

* Character, VarChar, LongVarChar → JSON string
* Boolean → JSON Boolean
* Numeric → JSON Number
* Collections → an ordered sequence of values, comma-separated and enclosed in square brackets

**Ignored SDT Properties**

The following properties are ignored in the process of serializing an SDT to JSON:

* [Xml Type](https://wiki.genexus.com/commwiki/wiki?7251)
* [XML Name](https://wiki.genexus.com/commwiki/wiki?7268)
* [XML Namespace](https://wiki.genexus.com/commwiki/wiki?7270)
* [SOAP](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10369,,) Type

### [References](#References)

* [JSON](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4794,,)
* [Wikipedia - JSON](http://en.wikipedia.org/wiki/JSON)
* [Introducing JSON](http://www.json.org/)

### [See Also](#See+Also)

[ToJson method](https://wiki.genexus.com/commwiki/wiki?37817)  
[Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Table of contents:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Consuming JSON with GeneXus Properties Data Type](https://wiki.genexus.com/commwiki/wiki?37750) |
| [Facebook Button control](https://wiki.genexus.com/commwiki/wiki?31841) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) | [ToJson method](https://wiki.genexus.com/commwiki/wiki?37817) |

---
