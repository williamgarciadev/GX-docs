---
title: "Output variable"
source_id: 8101
source_url: https://wiki.genexus.com/commwiki/wiki?8101
genexus_version: "18"
---

# Output variable

Specifies the output device.

**Data type:**  
Character(3)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)

### [Values](#Values)

|  |  |
| --- | --- |
| **SCR** | Screen. This is the default value. |
| **PRN** | Printer. |

### [Description](#Description)

Different [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468)s are produced, depending on whether the output is a screen or a printer.

The &Output [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) may be used to print lines or headers of different widths depending on the output device.

### [Samples](#Samples)

```
If &Output = 'PRN'
   // Call to Procedure that prints lines with more than 78 characters-width
Else
   // Call to Procedure that prints lines with not more than 78 characters-width
EndIf
```

### [See Also](#See+Also)

[Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386)


|  |
| --- |
| **Backlinks** |
| [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |

---
