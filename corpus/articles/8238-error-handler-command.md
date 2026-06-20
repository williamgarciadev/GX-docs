---
title: "Error_Handler command"
source_id: 8238
source_url: https://wiki.genexus.com/commwiki/wiki?8238
genexus_version: "18"
---

# Error_Handler command

# Error\_Handler command

Performs user-specific actions dynamically when a database-related error occurs at program execution time.

### [Syntax](#Syntax)

**Error\_Handler(***['subname']***)**  
  
**Where:**  
  
*subname*  
     Is the name of a subroutine defined in the object that contains this rule. This parameter is optional.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This command performs user-specific actions dynamically when a database-related error occurs at program execution time. Transactional and connection errors are detected and a user-defined routine is executed.

The error\_handler command is procedural and the subname parameter is optional. If specified, the subroutine becomes the new error\_handler until the program ends or a different error\_handler is executed (in the same program). When the subname parameter is not specified, the error handling routine is reset to the one specified by the error\_handler rule or, to the default error\_handler if no error\_handler rule exists.

More information at [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853)

### [See Also](#See+Also)

[Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) |
| [ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125) | [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |

---
