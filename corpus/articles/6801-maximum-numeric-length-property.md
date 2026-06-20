---
title: "Maximum numeric length property"
source_id: 6801
source_url: https://wiki.genexus.com/commwiki/wiki?6801
genexus_version: "18"
---

# Maximum numeric length property

Specifies the maximum numeric length.
Values: The value of the maximum numeric length and the default value is 18, but it can be changed to any value between 4 and 30.

### [Scope](#Scope)

**Level:** [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)

### [Description](#Description)

Specifies the maximum numeric length.

By default, GeneXus controls the most restrictive set limits so that the different platforms work in the same fashion, but it is possible to change these controls.

**Notes**

* The maximum supported value in C# is 79228162514264337593543950335 (ref.: [decimal data type](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types)), so, although that are 29 digits, the maximum recommended to not get overflows in GeneXus N(28).
* Java / Oracle supports N(38).
* Attributes and variables are not checked when this value is changed to a value lower than 18, so it is recommended that you verify that the new value is correct.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.

### [See Also](#See+Also)

[Significant attribute name length property](https://wiki.genexus.com/commwiki/wiki?7248)  
[Significant Table Name Length Property](https://wiki.genexus.com/commwiki/wiki?7249,,)  
[Significant object name length property](https://wiki.genexus.com/commwiki/wiki?7250)


|  |
| --- |
| **Backlinks** |
| [Length property](https://wiki.genexus.com/commwiki/wiki?6794) | [Numeric data type](https://wiki.genexus.com/commwiki/wiki?6793) |
| [Technical specifications of GeneXus](https://wiki.genexus.com/commwiki/wiki?55715) |

---
