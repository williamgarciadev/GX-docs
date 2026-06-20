---
title: "ToJson method"
source_id: 37817
source_url: https://wiki.genexus.com/commwiki/wiki?37817
genexus_version: "18"
---

# ToJson method

Returns a string with the JSON representation for the [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) or [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) variable.

### [Syntax](#Syntax)

AttOrVar = &var.**ToJson(**[&Boolean]**)**

**Where:**  
*AttOrVar*  
    [Attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the Character data type.

*&var*  
    Variable based on an SDT or Business Component.

*&Boolean*  
     Optional parameter. It only applies to Business Component variables. If True, the returned string contains the auxiliary variables (old values, mode, initialized flag). Otherwise, it only contains the record data. The default value is True.

### [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Samples](#Samples)

**1)** Given the following SDT:

`[imagen omitida: wiki id 10671]`

Define a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) (for example, named DPOneCountry). Drag the Country SDT from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to the Data Provider Source and fill in the data as shown below:

```
Country
{
    Name = "Uruguay"
    Language = "Spanish"
    Coordinates
    {
        Latitude = 30
        Longitude = 35
    }
    Cities
    {
        Item
        {
            Item = "Montevideo"
        }
        Item
        {
            Item = "Paysandu"
        }
    }
}
```

In a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), define a variable named &Country based on the Country SDT.

The purpose of the Web Panel is to convert data from a variable based on an SDT to a Json format. To achieve this, when the end user presses a button, the Event associated with it will load into memory (in the &Country variable) data of one country using the DPOneCountry Data Provider. After that, the Json method will be applied to the &Country variable to convert the data to a Json format. Finally, it will be displayed in the Web Panel Web Layout.

Design the Web Panel Web Layout as shown below:

`[imagen omitida: wiki id 51053]`

Define the following code associated with the Web Panel button:

```
Event 'ToJson'
   &SDTCountry = DPOneCountry()
   &Json=&SDTCountry.ToJson()
Endevent
```

The variables involved are as follows:

```
&Json                  Type: Character(200)
&Country               Type: Country
```

At runtime, when the end user presses the button, the country data is loaded in the &Country variable and converted to Json format. The &Json variable will contain and show the following:

{"Name":"Uruguay","Language":"Spanish","Coordinates":{"Latitude":30,"Longitude":35},"Cities":{{"Item":"Montevideo"},{"Item":"Paysandu"}}}

**Note**: When using Android platform, numbers do not contain quotes ("). But, when using this method in a user event or in an object whose [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) = Offline, all values returned contain quotes ("). [SAC #52162](https://www.genexus.com/es/developers/websac?data=52162) .

**2)** It is possible to apply the ToJson method to a variable based on an SDT that contains a member based on the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?32408) and it will be represented as plain text (serialized) using the Well KnownText standard (WKT).

Consider a Structured Data Type defined as follows:

SDT1  
{  
     CharacterMember: Character  
     GeoPointMember: GeoPoint  
 }

Initialize a variable based on the Structured Data Type and, after that, define the following code (for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) / [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Event):

```
 &VarBasedOnSDT1.ToJson()
```

The result will be something as follows:

```
 [{"CharacterMember":"","GeoPointMember":"POINT(-56.10 -33.01)"}]
```

### See Also

[FromJson method](https://wiki.genexus.com/commwiki/wiki?37809)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [Table of contents:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) |

---
