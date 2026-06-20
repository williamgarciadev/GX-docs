---
title: "Print command"
source_id: 5479
source_url: https://wiki.genexus.com/commwiki/wiki?5479
genexus_version: "18"
---

# Print command

Sends a printblock to the report's output media.

### [Syntax](#Syntax)

**Print***printblock-name*

### [Description](#Description)

The Print command used in the [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) of a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) is the only command that causes a printblock to be sent to the report's output media. Printblocks are containers used to design an output format, and they can be made up of attributes, variables, images, and so on.

### [Samples](#Samples)

In the following figure, two printblocks are defined:

`[imagen omitida: wiki id 5474]`

The first one, called Pb\_Header, contains information about the report's header while the second, called Pb\_Body, contains the relevant information.

The code to access the table and print it is as follows:

```
Header
   Print Pb_Header
End

For each order AirlineName
    Print Pb_Body
EndFor
```

Note that the header is printed in a group labeled "Header", which is executed by GeneXus every time there is a page top. The Print of the report's body is executed within the command's body [For Each command](https://wiki.genexus.com/commwiki/wiki?20195,,) that accesses the database.

### [See Also](#See+Also)

[Print If Detail Command](https://wiki.genexus.com/commwiki/wiki?5467)  
[Printing Commands Summary](https://wiki.genexus.com/commwiki/wiki?5526)


|  |
| --- |
| **Backlinks** |
| [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Print Blocks](https://wiki.genexus.com/commwiki/wiki?7938) | [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) |
| [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) |

---
