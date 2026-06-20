---
title: "Flexible client version property"
source_id: 55856
source_url: https://wiki.genexus.com/commwiki/wiki?55856
genexus_version: "18"
---

# Flexible client version property

Specifies the version of the flexible client to compile with.

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** Generator

### [Description](#Description)

The default value of this property corresponds to the running GeneXus version.

Leaving this property blank indicates that the latest released version should be used.

The value must follow the [Semantic Versioning 2.0.0](https://semver.org/) specification, which consists of three main parts: MAJOR.MINOR.PATCH. In addition, the format also supports including the pre-release version.

To view the available versions, browse the [GeneXus-SwiftPackages](https://github.com/GeneXus-SwiftPackages/GXUIApplication/tags) repository.

Note that changing the default value may lead to compilation errors, so proceed with caution.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

For pre-release versions, the format should follow this example: 1.0.0.0-beta+20230217024255. In this format, "beta" is the pre-release tag, and "20230217024255" is an optional, version-specific release identifier.

For release versions, the format should be 1.0.0, without release tags or specific version identifiers.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,).

### [See Also](#See+Also)

[Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890)  
[Distribution of Apple's Flexible Client through Swift Packages](https://wiki.genexus.com/commwiki/wiki?55960)

[Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259)


|  |
| --- |
| **Backlinks** |
| [Distribution of Apple's Flexible Client through Swift Packages](https://wiki.genexus.com/commwiki/wiki?55960) | [Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890) | [Flexible client update policy property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60310) |
| [Flexible client version property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60725) | [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?59630) | [GeneXus Super App Render](https://wiki.genexus.com/commwiki/wiki?58435) | [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259) |

---
