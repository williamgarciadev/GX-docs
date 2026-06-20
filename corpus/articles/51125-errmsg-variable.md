---
title: "ErrMsg variable"
source_id: 51125
source_url: https://wiki.genexus.com/commwiki/wiki?51125
genexus_version: "18"
---

# ErrMsg variable

It is automatically loaded when using the [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853), [Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238), or [New command](https://wiki.genexus.com/commwiki/wiki?6714).

**Data Type:**  
Character(70)

### [Description](#Description)

Read the article about [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853) to check the values obtained by the variable depending on the error when using the Error\_Handler rule or command.

When using the [New command](https://wiki.genexus.com/commwiki/wiki?6714), if the primary key or any candidate key already exists, the &Err [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) could be created and set to code = 1. Also, the &ErrMsg [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) could be created; if so, it will contain the message associated with the corresponding error code contained in &Err.

### [See Also](#See+Also)

[Err variable](https://wiki.genexus.com/commwiki/wiki?51028)  
[Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853)  
[Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238)  
[New command](https://wiki.genexus.com/commwiki/wiki?6714)


|  |
| --- |
| **Backlinks** |
| [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) | [Error handling when Composite command is not used](https://wiki.genexus.com/commwiki/wiki?51603) | [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |

---
