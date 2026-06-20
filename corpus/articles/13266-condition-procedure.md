---
title: "Condition Procedure"
source_id: 13266
source_url: https://wiki.genexus.com/commwiki/wiki?13266
genexus_version: "18"
---

# Condition Procedure

#### [Scope](#Scope)

**Business Process Diagram Symbols:** [Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17505)  [Inclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17506) [Sequence Flow Connectors (Conditional)](https://wiki.genexus.com/commwiki/wiki?17494,,)

#### [Purpose](#Purpose)

It defines which paths are to be followed using a procedure. It is necessary to define the value of each edge and based on what the procedure returns; the process will follow one or more conditional routes.

#### [Structure](#Structure)

The procedure associated to a conditional must have the following parm rule:

```
parm( in:&WorkflowProcessDefinition, in:&WorkflowProcessInstance, in:&WorkflowWorkitem, out:&conditionCode)
```

Where:

*&WorkflowProcessDefinition* is a WorkflowProcessDefinition data type variable

*&WorkflowProcessInstance* is a WorkflowProcessInstance data type variable

*&WorkflowWorkitem* is a WorkflowWorkitem data type variable

*&conditionCode*Numeric(4) variable. If the conditional procedure is assigned to a Conditional Sequence Flow Connector, this value is restricted to 0 or 1 (False or True).

#### [Example](#Example)

Given a car rental process, it is specified which car brand you want to rent. Then it is evaluated by a procedure, if the mark is AUDI or CHEVROLET and the process corresponding to each brand will continue the execution.

`[imagen omitida: wiki id 13267]`

`[imagen omitida: wiki id 13268]`


|  |
| --- |
| **Backlinks** |
| [My first BPM Native Mobile application](https://wiki.genexus.com/commwiki/wiki?50516) |

---
