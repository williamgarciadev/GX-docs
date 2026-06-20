---
title: "AfterLevel Event"
source_id: 8285
source_url: https://wiki.genexus.com/commwiki/wiki?8285
genexus_version: "18"
---

# AfterLevel Event

To indicate the completion of a specific Transaction level.

### [Syntax](#Syntax)

**AfterLevel**[**level** *att*…];

#### [Type Returned:](#Type+Returned%3A)

Boolean (True or False)

### [Description](#Description)

The evaluation of the AfterLevel event returns a Boolean value (TRUE or FALSE).

The AfterLevel level att… event is used to trigger a rule after a level is related to certain attributes. If the section level is not used, it applies to the first level of the transaction.

#### [Note:](#Note%3A)

In Java, .Net Win environments, or web interfaces, the rule will always be executed after validating the whole transaction.

#### [Compatibility:](#Compatibility%3A)

The After(Level(att) function is maintained for backward compatibility reasons. We highly recommend that you use the AfterLevel event instead. For further information see Triggering Events.

### [Example](#Example)

Supposing we receive supplier invoices and we want to verify that invoice total amount was calculated correctly:

Transaction Invoice Supplier

```
SupId*
InvNbr*
 ...

InvTot
  (PrdId*
   ...
   InvAmtLin)
...
InvTotCalc=SUM(InvAmtLin)
```

InvTot will be the value the supplier calculated as the invoice total.

InvTotCalc is the value calculated adding amounts of all lines entered.

To prevent differences between these two values, we define the following rule:

```
Error('Invoice Total does not match Calculated Total') If InvTot <> InvTotCalc;
```

InvTotCalc is calculated adding the line amounts (InvAmtLin), so that every time a line amount value changes we obtain a new value for InvTotCalc.

Every time an attribute changes, everything that depends on its value will have to be re-calculated. If InvAmtLin changes, InvTotCalc is re-calculated and the Error Rule must then be triggered for each line entered, if the condition becomes true. This will be true until ALL lines are entered. So, we will have an error as soon as InvTot is entered, and for every line in the grid (actually, we won't be able to advance the focus to the first line in the grid because the error rule will keep the focus on InvTot).

We must then change the MOMENT at which the error rule is evaluated, awaiting for all lines to be entered; that is: at the time of exiting the Lines level.

```
Error('Invoice Total does not match Calculated Total') If InvTotCalc <> InvTot On AfterLevel level InvAmtLin;
```

### [Scope](#Scope)

**Objects:** [Transactions](https://wiki.genexus.com/commwiki/wiki?1908)  
**Languages:** .NET, Ruby (up to GeneXus X Evolution 3), Java, RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol

### [See Also](#See+Also)

[After function](https://wiki.genexus.com/commwiki/wiki?8321)  
[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)  
[Rule Triggering Events](https://wiki.genexus.com/commwiki/wiki?6840)


|  |
| --- |
| **Backlinks** |
| [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868) |
| [Category:Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840) |

---
