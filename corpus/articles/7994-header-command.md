---
title: "Header command"
source_id: 7994
source_url: https://wiki.genexus.com/commwiki/wiki?7994
genexus_version: "18"
---

# Header command

Defines the header lines to be printed at the top of each page.

### [Syntax](#Syntax)

**Header**  
       *code*  
**End**  
  
**Where:**  
  
*code*  
      Sequence of valid language commands.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual Basic (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The Header command can be included in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664). Its use is optional.

The most common use case is to declare it as the first statement (outside of [For Each commands](https://wiki.genexus.com/commwiki/wiki?24744)) in the Procedure Source. This implies that the data in the Header is printed at the top of each page.

The Header command can also be included inside a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) defined in the Source. For example, suppose that you have defined a Header command at the top of the Procedure Source (outside any For each) and after that, you define a For each command containing a Header command. In this case, the following will happen every time a page is ejected:

* What is included inside the main Header command (the one outside the For each command) will be printed.
* In addition, if the For each command is still being executed, what is included in the Header contained inside it will be printed too.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Client
{
   ClientId*
   ClientName
}
```

Suppose you want to define a Procedure to list all your clients. In the Procedure Source, you define a main Header command (it contains the [Print command](https://wiki.genexus.com/commwiki/wiki?5479) calling the [Printblock control](https://wiki.genexus.com/commwiki/wiki?1958) called "Header"). After that, you define a For each command that scans over the Client table. The For each command contains a Header command (with a [Print command](https://wiki.genexus.com/commwiki/wiki?5479) that calls the [Printblock control](https://wiki.genexus.com/commwiki/wiki?1958) called "TitleClient").

```
Header
   Print Header
End

For each 
   Header
      Print TitleClient
   End
   Print InfoClient
Endfor
```

The following image shows the Procedure Layout containing the three [Printblock controls](https://wiki.genexus.com/commwiki/wiki?1958) invoked with the [Print command](https://wiki.genexus.com/commwiki/wiki?5479) from the Source (two of them are inside Header commands to be repeated every time a page is ejected):

`[imagen omitida: wiki id 7997]`

### [See Also](#See+Also)

[Footer Command](https://wiki.genexus.com/commwiki/wiki?7967)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Footer command](https://wiki.genexus.com/commwiki/wiki?7967) | [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) |
| [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |

---
