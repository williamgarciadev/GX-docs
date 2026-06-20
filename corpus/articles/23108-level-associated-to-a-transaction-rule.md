---
title: "Level associated to a Transaction rule"
source_id: 23108
source_url: https://wiki.genexus.com/commwiki/wiki?23108
genexus_version: "18"
---

# Level associated to a Transaction rule

GeneXus always determines that a transaction rule is triggered at the first possible opportunity, that is, when all the data involved in the rule definition is available.

The attributes involved in a rule "tell" GeneXus the triggering level. For example, if a rule only references attributes of the first level of a transaction (either in the rule itself or in the triggering condition), then GeneXus will understand that the rule is associated with the tansaction's first level (and it will be triggered as soon as there are values for all data referenced in the rule).

Likewise, when a rule only references attributes in the second level of the transaction (either in the rule itself or in the triggering condition), then GeneXus will understand that the rule is associated with the transaction's second level. This means that the rule will be executed for each line in the second level (as soon as there are values for all data referenced in the rule).

If a rule references attributes from different levels, GeneXus understands that the rule is associated with the last nested level, the only location where all referenced attributes have values. The rule will be executed for each instance in the last level.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Samples](#Samples)

`[imagen omitida: wiki id 23109]`

**Example 1**

If the following rule is defined in the above transaction:

```
Default(CustomerAddedDate, &today);
```

...since the only attribute mentioned in the rule is CustomerAddedDate, which is an attribute from the transaction's first level, then GeneXus will determine that this rule is associated with the first level.

**Example 2**

If the following rule is also defined in the above transaction:

```
Add(CustomerTripMiles,CustomerTotalMiles);
```

...since the two attributes mentioned in this rule are in the transaction's second level, then GeneXus will determine that this rule is associated with the second level. So this [Add rule](https://wiki.genexus.com/commwiki/wiki?6845) will be executed for each line in the second level.

If no attributes are involved in a rule, then the triggering level associated by default with that rule will be the first level.

For example, the rule below, defined in the above transaction:

```
Error(‘Customers cannot be deleted’) if delete;
```

...involves no attributes, so, by default, the first level will be associated with the rule. This means that when the end-user tries deleting a customer, the condition turns to True, and the error text will be displayed, and the customer will not be deleted. Note that the rule will not be triggered if the end-user tries to delete a line with a trip, and this is because the rule is asociated with the first level.

### [See Also](#See+Also)

[Level clause for Transaction rules](https://wiki.genexus.com/commwiki/wiki?8438)


|  |
| --- |
| **Backlinks** |
| [AfterValidate Triggering event](https://wiki.genexus.com/commwiki/wiki?8282) |

---
