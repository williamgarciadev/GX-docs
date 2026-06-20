---
title: "TargetPath property"
source_id: 9612
source_url: https://wiki.genexus.com/commwiki/wiki?9612
genexus_version: "18"
---

# TargetPath property

Indicates the directory name where the Environment's programs are created.

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

The default value of this property depends on the generator selected when the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is created. For example, it is set to "CSharpModel" for [.NET](https://wiki.genexus.com/commwiki/wiki?38604), to "JavaModel" for [Java](https://wiki.genexus.com/commwiki/wiki?12258), and so on.

When creating a new Environment, it is set to "DataXXX" —where XXX is a number corresponding to an internal Environment identifier.

The directory name you specify will be created as a subdirectory under the Knowledge Base path. This means that if the Knowledge Base is moved to a different directory, drive, or location, the target path will automatically adjust accordingly.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [.NET Framework Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39502) | [.NET Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39510) | [Android Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39506) |
| [Extract for .NET Framework Generator property](https://wiki.genexus.com/commwiki/wiki?39501) | [Extract for .NET Generator property](https://wiki.genexus.com/commwiki/wiki?39509) | [Extract for Android Generator property](https://wiki.genexus.com/commwiki/wiki?39505) | [Extract for iOS Generator property](https://wiki.genexus.com/commwiki/wiki?39503) |
| [Extract for Java Generator property](https://wiki.genexus.com/commwiki/wiki?39499) | [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) | [iOS Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39504) | [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500) |

---
