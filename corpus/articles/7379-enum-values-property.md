---
title: "Enum Values property"
source_id: 7379
source_url: https://wiki.genexus.com/commwiki/wiki?7379
genexus_version: "18"
---

# Enum Values property

Enumerates the possible values that a domain-based attribute or variable can take.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Domain](https://wiki.genexus.com/commwiki/wiki?7221)

### [Description](#Description)

This property can be set for any domain defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). It opens a dialog ("Values Editor") to enumerate the possible values that an attribute or variable based on the domain can take.

For each possible value, you must specify:

* A **Name**, to be used to make reference to the value at programming time.
* A **Description**, which will be shown as a possible value to be selected for an attribute/value based on this domain.
* A **Value** that will be stored in the attribute/variable when selecting the corresponding **Description**.

`[imagen omitida: wiki id 22285]`

By default, the attribute/variable controls belonging to an enumerated domain are shown as a combo box, with the **Description**values.  
All the attributes/variables whose definition is based on an enumerated domain take these domain characteristics automatically.

### [Samples](#Samples)

It is not possible to assign a value to an enumerated variable or attribute directly:

```
&var = value
```

In the same example, this syntax is wrong and a “type mismatch” error will be shown in the navigation:

```
&var = "M"
```

The correct assignment must be made through the value name:

```
&var = Domain.Name
```

In the example, the syntax should be:

```
&var = Gender.Female
```

or

```
&var = Gender.Male
```

If **Name** does not exist among the defined names, an error will occur at runtime. The valid characters to define the **Name**are the same as for attribute names; i.e.: only letters, numbers, and underscore (\_) are valid, and it must start with a letter.

#### [Handling Nulls](#Handling+Nulls)

In some cases, you need to store a Null value and/or let the user select a value that isn't part of the domain. In that case, you don't need to add the Null or Empty value to the Domain. Just set the EmptyItem property to True and the Empty as null property to Yes.

### [See Also](#See+Also)

[Enumerated Domains Methods](https://wiki.genexus.com/commwiki/wiki?9918)


|  |
| --- |
| **Backlinks** |
| [Compare function](https://wiki.genexus.com/commwiki/wiki?45423) | [Domain definition](https://wiki.genexus.com/commwiki/wiki?7239) | [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) |
| [HowTo: Use Check Box for Smart Devices](https://wiki.genexus.com/commwiki/wiki?18482) | [HowTo: Use Combo Box in Panels](https://wiki.genexus.com/commwiki/wiki?18408) | [HowTo: Use Radio Button in Panels](https://wiki.genexus.com/commwiki/wiki?18434) |

---
