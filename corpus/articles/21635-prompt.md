---
title: "Prompt"
source_id: 21635
source_url: https://wiki.genexus.com/commwiki/wiki?21635
genexus_version: "18"
---

# Prompt

Prompt (or [Selection List](https://wiki.genexus.com/commwiki/wiki?23894)) is a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) automatically created for each Transaction's primary key and foreign keys to provide end users with the possibility of querying the data existent in a specific database table and selecting a certain record, returning its identifier.

**Note**: A Prompt created for a Transaction's primary key is also called Autoprompt. This is just a terminology difference since they are the same objects reused as Prompt or Autoprompt, depending on whether we invoke them, respectively, for a foreign or a primary key.

A Prompt created and maintained by GeneXus is also called System Prompt; once it is saved by the user it is called User Prompt.

When the generated application is running, the Autoprompt is called using the Select Button and the Prompt is called by a button or icon automatically placed aside the foreign key corresponding attribute.

The object corresponding to a Prompt is displayed and available at the [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) and it is automatically maintained by GeneXus when the data model is changed. You can change the object corresponding to a Prompt, but after saving the changes, GeneXus will not maintain it anymore and the user will be responsible for maintaining the object. Objects corresponding to Prompts changed by developers can be maintained by GeneXus again by deleting them and executing a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

Criteria for generating prompt grids: Attributes, according to their order in the correlative table, are being included (in the same order) while not exceeding the maximum width.

1. In Native Mobile or Angular applications, the maximum grid width is 68 characters.
2. Only the attributes up to <= grid width long are considered.
3. [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371) attributes are not considered.

About **Filters**: no more than 6 filters are generated.

### [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android platform](https://wiki.genexus.com/commwiki/wiki?14453), [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [See also](#See+also)

[Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863)


|  |
| --- |
| **Backlinks** |
| [Equal rule](https://wiki.genexus.com/commwiki/wiki?6855) | [How are prompts invoked?](https://wiki.genexus.com/commwiki/wiki?23901) |
| [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) | [Prompts Master Page property](https://wiki.genexus.com/commwiki/wiki?51714) |
| [Select Record from Prompt](https://wiki.genexus.com/commwiki/wiki?13576) | [Selection List](https://wiki.genexus.com/commwiki/wiki?23894) |

---
