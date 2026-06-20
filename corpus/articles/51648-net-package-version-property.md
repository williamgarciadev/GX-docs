---
title: ".NET Package Version property"
source_id: 51648
source_url: https://wiki.genexus.com/commwiki/wiki?51648
genexus_version: "18"
---

# .NET Package Version property

Determines the version of the .NET Package ID that implements the External Object.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

It is a specific version number in the form Major.Minor.Patch[-Suffix]

If the version is not specified, the Generator Standard Classes Version is used.

The Generator Standard Classes Version that is being used is the value of the [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259).

Values must follow the [package versioning specification](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning).

See sections [Version ranges](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges) and [Floating version resolutions](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning#floating-version-resolutions) for interval notations.

### [Samples](#Samples)

1.0 means the package with the smallest version >= 1.0 found at the repository (i.e. NuGet) will be referenced.  
[1.0] means the package with the exact version 1.0 will be referenced.  
1.\* means that the package with the highest existing version with major 1 will be used.

### [See Also](#See+Also)

[.NET Package ID property](https://wiki.genexus.com/commwiki/wiki?51647)


|  |
| --- |
| **Backlinks** |
| [.NET Package ID property](https://wiki.genexus.com/commwiki/wiki?51647) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |

---
