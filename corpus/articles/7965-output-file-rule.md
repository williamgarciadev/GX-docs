---
title: "Output_File rule"
source_id: 7965
source_url: https://wiki.genexus.com/commwiki/wiki?7965
genexus_version: "18"
---

# Output_File rule

# Output\_File rule

Determines the name of the reports and procedures’ output.

### [Syntax](#Syntax)

**Output\_File(**{ *name* | *att* | &*var* }**,** *format***);**  
  
**Where:**  
  
*name*|*att*| **&***var*  
      Is the output name. In the case of output to a file, it is possible to indicate the path of the file to be generated, which must exist. It can also be a variable or an attribute, in which case it must be of Character type.  
  
*format*  
      Is the output file format. Possible values are ‘GXR’, ‘RTF’, ‘XML’ ‘PDF’ or ‘TXT’ (the last one only for reports in text mode). It is ignored in the case of output through screen or printer.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293)

### [Description](#Description)

This rule allows you to determine the name of reports and procedures’ output, on the screen, printer or to a file. In the case of output on screen, it allows assigning a name to the document in the Report Viewer’s dialog. In the case of output through the printer, it allows assigning the printing job’s name in the queue. And in case the output is to a file, it allows indicating its name and format.

### [Samples](#Samples)

```
Output_file('TicketReservation','PDF');
```

### [See Also](#See+Also)

[Report output property](https://wiki.genexus.com/commwiki/wiki?7943)


|  |
| --- |
| **Backlinks** |
| [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) | [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) |
| [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) | [Procedure rules](https://wiki.genexus.com/commwiki/wiki?8262) | [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) |
| [Web printing on client printer (without an applet)](https://wiki.genexus.com/commwiki/wiki?33912) |

---
