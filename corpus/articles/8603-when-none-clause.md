---
title: "When None Clause"
source_id: 8603
source_url: https://wiki.genexus.com/commwiki/wiki?8603
genexus_version: "18"
---

# When None Clause

Specifies the code to be executed when a For Each command or Xfor Each does not filter any record.

#### [Syntax](#Syntax)

**When None***<CodeWhenNone>*

#### [Description](#Description)

It is often necessary to execute a certain code when a For Each or Xfor Each does not filter any record.

To simplify the logic of the For Each and to provide more programming clarity, the command When None can be used.

##### [Note:](#Note%3A)

It is important to clarify that if *For Each*s are included within a When None, neither joins nor any type of filter will be inferred with respect to the For Each that includes the *When None* command.

#### [Example](#Example)

Use of this clause is in the numbering procedure

```
For each
    where NumCode = &code
           &LastNum = LastNum + 1
           LastNum = &LastNum
    when none
           &LastNum = 1
           New 
                  NumCode = &code
                  LastNum = &LastNum
           EndNew
EndFor
```

In this example, you update the last number for the document specified by &code, If the record does not exist, you insert it in the table.

#### [Scope](#Scope)

Commands: For each command ([XEv2](https://wiki.genexus.com/commwiki/wiki?20195,,), [XEv3](https://wiki.genexus.com/commwiki/wiki?24744)), [XFor Each](https://wiki.genexus.com/commwiki/wiki?8596), [XFor First](https://wiki.genexus.com/commwiki/wiki?8601)

#### [See Also](#See+Also)

[For Each command](https://wiki.genexus.com/commwiki/wiki?20195,,) - [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) (XEv3)  
[XFor Each Command](https://wiki.genexus.com/commwiki/wiki?8596)  
[XFor First Command](https://wiki.genexus.com/commwiki/wiki?8601)


|  |
| --- |
| **Backlinks** |
| [Default clause](https://wiki.genexus.com/commwiki/wiki?25407) | [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596) | [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601) |

---
