---
title: ".NET Package ID property"
source_id: 51647
source_url: https://wiki.genexus.com/commwiki/wiki?51647
genexus_version: "18"
---

# .NET Package ID property

Sets the ID of the .NET Package associated with the External Object.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

This property can be used instead of or in addition to the .NET Assembly Name property. If both are specified, both will be considered.

The package identifier is case-insensitive, limited to 128 characters, does not contain spaces or characters that are not valid for a URL, and generally follows the .NET namespace rule. The package must be hosted on [Nuget.org](https://www.nuget.org/) or another package gallery.

See more details at [package identifiers](https://learn.microsoft.com/en-us/nuget/create-packages/creating-a-package#choose-a-unique-package-identifier-and-setting-the-version-number).

### [Samples](#Samples)

[GeneXus.Azure.Core](https://www.nuget.org/packages/GeneXus.Azure.Core)

[GeneXus.Classes.Core](https://www.nuget.org/packages/GeneXus.Classes.Core)

[MySqlConnector](https://www.nuget.org/packages/MySqlConnector/)

[Oracle.ManagedDataAccess.Core](https://www.nuget.org/packages/Oracle.ManagedDataAccess.Core)

[MailKit](https://www.nuget.org/packages/MailKit)

### [See Also](#See+Also)

[.NET Package Version property](https://wiki.genexus.com/commwiki/wiki?51648)


|  |
| --- |
| **Backlinks** |
| [.NET Package Version property](https://wiki.genexus.com/commwiki/wiki?51648) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [External Object: Native Object](https://wiki.genexus.com/commwiki/wiki?6148) |
| [External Object: Native Object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) |

---
