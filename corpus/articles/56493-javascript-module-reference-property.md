---
title: "Javascript Module Reference property"
source_id: 56493
source_url: https://wiki.genexus.com/commwiki/wiki?56493
genexus_version: "18"
---

# Javascript Module Reference property

Indicates the package or file that contains the library distribution being imported.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The Javascript Module Reference property is found at the level of external objects of [Native Object](https://wiki.genexus.com/commwiki/wiki?6148) type and is part of the Javascript Module Information section.

`[imagen omitida: wiki id 56492]`

This property allows setting an npm package with the following syntax:

```
packageName$version
```

It can also be a local path.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you want to add the library "web-standard-functions" in version 1.3.5. To do so, set the Javascript Module Reference as follows:

@genexus/web-standard-functions$1.3.5

It indicates the reference to the npm package with the specific version of the library.

To use a local file named "myfile.js", configure the property as shown below:

local/path/to/myfile.js

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).
