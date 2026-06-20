---
title: "Text For Null Values property"
source_id: 55234
source_url: https://wiki.genexus.com/commwiki/wiki?55234
genexus_version: "18"
---

# Text For Null Values property

Displays a text where the value is null.

### [Scope](#Scope)

**Objects:** [Query](https://wiki.genexus.com/commwiki/wiki?9026)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The Text For Null Values property helps to display a text where the return values from the query are null.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

For example, the following query displays the information of all Countries:

`[imagen omitida: wiki id 55241]`

The default result is shown below. There is information where a null value is being displayed.

`[imagen omitida: wiki id 55242]`

To show a text instead of a null value, the Text For Null Values property can be set with a message on the query properties.

`[imagen omitida: wiki id 55243]`

The new result is as follows:

`[imagen omitida: wiki id 55244]`

Note: this property can only be used for NULL values, not empty values.
