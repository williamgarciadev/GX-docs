---
title: "Enumerated Domains Methods"
source_id: 9918
source_url: https://wiki.genexus.com/commwiki/wiki?9918
genexus_version: "18"
---

# Enumerated Domains Methods

This document describes methods to work with [Enumerated Domains](https://wiki.genexus.com/commwiki/wiki?2207).

The samples below use the following Enumerated Domain definition:

```
Enumerated Domain Name: MaritalStatus
Data type             : Character(1)
Values                : Name        Description   Value
                        Single      Single        S
                        Married     Married       M
                        Widowed     Widowed       W
                        Divorced    Divorced      D
```

## [Methods](#Methods)

### [Convert()](#Convert%28%29)

Converts a **Value** into the corresponding Enumerated Domain **Name**. The result will be indeterminate if the given value (parameter) does not match any of the Enumerated Domain values.

#### [**Syntax**](#Syntax)

*AttVarOrSDTMember* *= EnumeratedDomain***.Convert(***expression**)***

***Where:***

*AttVarOrSDTMember*Is an attribute, variable, or [SDT](https://wiki.genexus.com/commwiki/wiki?10021) Member (based on a certain Enumerated Domain) to which you want to assign one of the available values of the Enumerated Domain.

**EnumeratedDomain** Is the name of an Enumerated Domain defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

**expression** Is a valid [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,). Its data type must match the Enumerated Domain data type.

#### [**Description**](#Description)

There are scenarios (for example, when reading an XML or CSV file, etc.) in which you have a value to be assigned to an attribute, variable, or SDT member. However, if the field is based on an Enumerated Domain, you cannot directly assign the value to it. Instead, you need to obtain the corresponding Enumerated Domain Name.

The Convert() method tries to convert a given value (by parameter) to the corresponding Enumerated Domain Name. It does not check if the parameter's value belongs to the Enumerated Domain; therefore, if you are not sure whether the value belongs to the Enumerated Domain, you should check it using the Elements() method first.

#### [**Samples**](#Samples)

&MaritalStatus is a variable based on the MaritalStatus [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207).

```
&MaritalStatus = "M"                          //This code will display a "type mismatch" error.
&MaritalStatus = MaritalStatus.Convert("M")   //This code is correct. It is analogous to: &MaritalStatus = MaritalStatus.Married (&MaritalStatus = "M").
```

```
&Value = &ExcelDocument.Cells(&i, 5).Text
if &Value in MaritalStatus.Elements()
    &MaritalStatus = MaritalStatus.Convert(&Value)
else
    msg('The value does not correspond to a marital status')
endif  
```

### *Elements()*

Returns a collection populated with all the values defined in the Enumerated Domain. The elements in the returned collection are sorted by Value. It can be used anywhere a collection can be used.

#### [**Syntax**](#Syntax)

*&ElementsCollection *= EnumeratedDomain***.*****Elements()**

***Where:***

**&ElementsCollection**  Is a collection variable based on the Enumerated Domain.

**EnumeratedDomain**Is the name of an Enumerated Domain defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

#### [**Samples**](#Samples)

**1)**The following code scans the MaritalStatus [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) values and inserts them into the MaritalStatus physical table:

```
For &x in MaritalStatus.Elements()  //&x is a variable based on the MaritalStatus Domain.
   new
      MaritalStatusId = &x
      MaritalStatusDescription = &x.EnumerationDescription()
   endnew
EndFor
```

**2)**The following code shows how the method can be used in the where clause:

```
For each
   where MaritalStatusId in MaritalStatus.Elements()
   ... //do something
Endfor
```

### [*EnumerationDescription()*](#EnumerationDescription%28%29)

Returns the descriptive text associated with the given Enumerated Domain value.

#### [**Syntax**](#Syntax)

*&Description* = *AttVarOrSDTMember***.EnumerationDescription()**

*****Where:*****

*&Description*Is a variable in which you want to obtain the descriptive text associated with the given value.

*AttVarOrSDTMember*Is an attribute, variable, or SDT member based on an Enumerated Domain.

#### [****Samples****](#Samples)

```
&MaritalStatus = MaritalStatus.Married
&MaritalStatusDescription = &MaritalStatus.EnumerationDescription()
```

* &MaritalStatus = "M"
* &MaritalStatusDescription = "Married"

```
&MaritalStatus = MaritalStatus.Divorced 
&MaritalStatusDescription = &MaritalStatus.EnumerationDescription()
```

* &MaritalStatus = "D"
* &MaritalStatusDescription = "Divorced"


|  |
| --- |
| **Backlinks** |
| [Enum Values property](https://wiki.genexus.com/commwiki/wiki?7379) | [HowTo: Use the Wheel Control](https://wiki.genexus.com/commwiki/wiki?16239) | [Timezones Domain](https://wiki.genexus.com/commwiki/wiki?21989) |

---
