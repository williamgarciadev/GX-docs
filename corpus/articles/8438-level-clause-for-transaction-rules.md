---
title: "Level clause for Transaction rules"
source_id: 8438
source_url: https://wiki.genexus.com/commwiki/wiki?8438
genexus_version: "18"
---

# Level clause for Transaction rules

Modifies the default level for triggering a rule, changing it to a lower level.

### [Syntax](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213) [ IF condition ] [ON triggering event] [**Level Att…**] ;

#### [**Where:**](#Where%3A)

*condition*  
         Is any valid logic condition

*triggering event*  
         Is one of the predefined events available in GeneXus for transaction rules, which allows you to define the precise time for executing a rule

*Att*  
         Specifies an attribute or list of attributes separated by semi-colon

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

In transaction rules, most of the time it is not necessary to specify in the transaction rules the level at which we want them to be triggered because the attributes involved in them are sufficient for GeneXus to determine their associated level.

However, this optional clause allows you to modify the default level for triggering a rule, changing it to a lower level.

### [Samples](#Samples)

`[imagen omitida: wiki id 23109]`

If you don't want to allow the user to delete lines, you should define the following rule:

```
Error(‘Trips cannot be deleted’) if delete level TripDate;
```

If you don't include the Level clause followed by a second level attribute in the rule, the first level will be associated to the rule by default. In other words, the error text will be displayed if the end-user tries to delete a customer.

If you want to prevent the end user from deleting lines with trips and you don't need to evaluate a second level attribute in the rule as a condition or send a second level attribute as a parameter, the Level clause helps you to mention a second level attribute, so that GeneXus knows that the trigger level associated with the rule is the second and not the first one.

### [Compatibility](#Compatibility)

The Level(att) function is maintained for backward compatibility reasons. We highly recommend the use of the Level clause instead. For furhter information see [Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840).

### [See Also](#See+Also)

[Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840)  
[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)  
[After Action Triggering event](https://wiki.genexus.com/commwiki/wiki?8284)


|  |
| --- |
| **Backlinks** |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Level associated to a Transaction rule](https://wiki.genexus.com/commwiki/wiki?23108) |

---
