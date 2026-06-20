---
title: "Javascript debug mode property"
source_id: 17384
source_url: https://wiki.genexus.com/commwiki/wiki?17384
genexus_version: "18"
---

# Javascript debug mode property

All standard generated JScripts and CSS are compressed (obfuscated) by default to obtain better performance in the transfer of static files from the server to the client.
For debugging purposes, it may be necessary to not compress static files and, in such case, you should enable this property.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | JScripts and CSS are compressed. This is the default value. |
| **Yes** | Static files are not compressed (for debugging purposes). |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

#### [Note:](#Note%3A)

In production time, it is recommended to set Javascript Debug Mode property = No, for performance and security issues.

#### [Considerations:](#Considerations%3A)

For Smooth models, as since GeneXus X Evolution 3 upgrade 9 this property does not have relation with the On Session Timeout property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [A05:2021 - Security misconfiguration](https://wiki.genexus.com/commwiki/wiki?50185) | [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) |
|
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
|

---
