---
title: "HowTo: Use MultiWheel Control"
source_id: 20171
source_url: https://wiki.genexus.com/commwiki/wiki?20171
genexus_version: "18"
---

# HowTo: Use MultiWheel Control

Multiwheel is a control that allows the end-user to set multiple values by swiping up and down.

This allows minimizing the number of tap gestures and group values corresponding to a single concept.

`[imagen omitida: wiki id 20192]`

This article explains a few concepts of the control. Do it yourself, follow the steps below, or check [this video](http://www.youtube.com/watch?v=dIKxQzErxv0).

### [Step 1](#Step+1)

In order to use the MultiWheel control, a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) with the following structure has to be created:

`[imagen omitida: wiki id 54089]`

### [Step 2](#Step+2)

Load the Structured Data Type with a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) adding the values that will appear in the Multiwheel.

#### [Load Example](#Load+Example)

`[imagen omitida: wiki id 20175]`

### [Step 3](#Step+3)

To show the control:

**1.** Create two variables:

* *&var1:*Based on  Wheel type (SDT) and with the property [Collection property (IsCollection checkbox)](https://wiki.genexus.com/commwiki/wiki?9761) = True.
* *&var2:*Based on Character.

**2.**  In the Layout section, add the variable *&var2* and set the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = "MultiWheel".

**3.**  In the Event section, add the following code:

```
&var1 = DataProviderWheel()
&var2 = &var1.ToJson()
```

### [How to load the Wheel SDT](#How+to+load+the+Wheel+SDT)

The field values of the SDT members must be:

* *"Name"* and *"Title"* have the name and title of the column.
* *"Type"* supports *"int"* for numeric ranges and "char" for strings.
* *"Value"* is where GeneXus reads and writes the current value of the field, always handled as a string.
* *"Range"* is a vector of strings with the range of values to show in the wheel, this value is always required.  
   For numeric type, the vector has the beginning and end of the range of numbers that will be shown on the picker.  
   For character type, it has each of the values you want to appear on the picker.
* "Unit" is the unit of the column (this is used to format the string shown in the field in the device after choosing a value).

### [Samples](#Samples)

**Blood pressure:**

Json:

```
    [
     { "Name":"Systolic", "Title":"Systolic", "Unit":"/", "Type":"int", "Range":["8","18"], "Value":"12"},
     { "Name":"Diastolic", "Title":"Diastolic", "Unit":"mmHg", "Type":"int", "Range":["4","14"], "Value":"8"}
    ]
```

`[imagen omitida: wiki id 20179]`

**Medicine dose:**

Json:

```
   [
    { "Name":"Dose", "Title":"Dose", "Type":"char", "Value":"1", "Unit":"",
            "Range":["1\/4","1\/2","1","2","3","4","5","10","15","20","3"]},
    { "Name":"Measure", "Title":"Measure", "Type":"char", "Value":"tablet", "Unit":"\/",
            "Range":["aplication","capsule","drops","injection","measure","ml","pill","spoon","tablet"]},
    { "Name":"Period", "Title":"Period", "Type":"string", "Value":"week", "Unit":"",
             "Range":["4 hours","6 hours","8 hours","12 hours","day"]}
   ]
```

`[imagen omitida: wiki id 20177]`

### [See Also](#See+Also)

[HowTo: Use the Wheel Control](https://wiki.genexus.com/commwiki/wiki?16239)  
[Collection property (IsCollection checkbox)](https://wiki.genexus.com/commwiki/wiki?9761)  
[Control Type property](https://wiki.genexus.com/commwiki/wiki?9550)


|  |
| --- |
| **Backlinks** |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Control Type property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57964) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) |
| [HowTo: Use the Wheel Control](https://wiki.genexus.com/commwiki/wiki?16239) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
