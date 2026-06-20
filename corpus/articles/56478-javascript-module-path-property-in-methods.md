---
title: "Javascript Module Path property in Methods"
source_id: 56478
source_url: https://wiki.genexus.com/commwiki/wiki?56478
genexus_version: "18"
---

# Javascript Module Path property in Methods

Specifies the relative or absolute string that provides the location of the implementation of the module being imported.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The Javascript Module Path property is located at the method level of External objects of [Native Object](https://wiki.genexus.com/commwiki/wiki?6148) type and is part of the Javascript Module Information section.

`[imagen omitida: wiki id 56477]`

When importing a function library, this property indicates the path to the function, either to select specific functions ('cherry picking') or to the index.js where the function to be invoked is resolved.

By setting this property, the External Object method is considered as an import of a static function.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).
