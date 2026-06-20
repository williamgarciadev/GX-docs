---
title: "Expose descriptive metadata property"
source_id: 45754
source_url: https://wiki.genexus.com/commwiki/wiki?45754
genexus_version: "18"
---

# Expose descriptive metadata property

Controls whether build information is exposed in the generated code files. It consists of metadata about the GeneXus environment used, such as version, database server, generation timestamp. It applies to JavaScript, server-side, and HTML files.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | No information is included (default value) |
| **Yes** | Build information is included |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

Configures if the generated source code will contain build-related information comments or metadata.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

When this property is set to **Yes**,it will generate comments specific to the GeneXus version, generator, and build time. For example, it will add the following comment to the gxgral.js:

```
/**@preserve GeneXus 16.0.10.140960*/
```

And a comment section like the following for source code (.java, .cs):

```
/*
               File: CommonsDummy
        Description: Commons Dummy
             Author: GeneXus C# Generator version 16_0_3-132778
       Generated on: 8/5/2019 16:20:27.64
       Program type: Main program
          Main DBMS: SQL Server
*/
```

It will also add this metadata on Panels HTML source code:

```
<meta name="generator" content="GeneXus C# 16_0_10-141114"/>
```

If the property is set to **No**,GeneXus will not generate any of those comments or metadata.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Compatibility](#Compatibility)

When this property is set to Yes, existing Knowledge Bases will be opened and will continue to generate comments and metadata, keeping backward compatibility,
When this property set to No, new Knowledge Bases will be created avoiding the creation of build-related comments and metadata on sources.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).
