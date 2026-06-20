---
title: "Javascript Module Name property"
source_id: 56496
source_url: https://wiki.genexus.com/commwiki/wiki?56496
genexus_version: "18"
---

# Javascript Module Name property

Specifies the name of the JavaScript export to be instantiated to access the desired functionality within the imported module.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The Javascript Module Name property is found at the level of External objects of [Native Object](https://wiki.genexus.com/commwiki/wiki?6148) type and is part of the Javascript Module Information section.

`[imagen omitida: wiki id 56494]`

When a module imports a class or function that needs to be instantiated for its use, the Javascript Module Name property becomes an essential element. It allows defining the name of the class or function that acts as an access point to use the functionalities provided by the external module.

If the external library exports a set of static functions, it is not necessary to define this property. In this case, the imported functions are directly accessed as methods of the External object without the need to instantiate a particular class.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you want to implement an external library called **GeneXusClientSocket** in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). In this case, you must configure the **Javascript Module Name property** as shown in the image:

`[imagen omitida: wiki id 56495]`

In the example, **GeneXusClientSocket** would be the name of the class that you would instantiate to access the specific socket manipulation functions.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).
