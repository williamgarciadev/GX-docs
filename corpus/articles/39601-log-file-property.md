---
title: "Log file property"
source_id: 39601
source_url: https://wiki.genexus.com/commwiki/wiki?39601
genexus_version: "18"
---

# Log file property

It defines the name of the Log Output file when the Log Output Property is set to File.

### [Description](#Description)

The default value for this property is client.log

In .NET, the file is generated in the current directory, that is

* for .Web, the folder where the web.config is (The folder where the Virtual directory points to)
* for command line procedures, the current (starting) directory

In Java web, the file is generated in the <webapp>/logs.

In all cases, an absolute path can be set too. (eg.: C:\MyLogGolder\client.log )

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Log output property](https://wiki.genexus.com/commwiki/wiki?39568)  
[Log level property](https://wiki.genexus.com/commwiki/wiki?36304)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [HowTo: Enable Log for GXflow runtime](https://wiki.genexus.com/commwiki/wiki?24568) |

---
