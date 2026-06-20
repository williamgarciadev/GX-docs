---
title: "Previous function"
source_id: 8477
source_url: https://wiki.genexus.com/commwiki/wiki?8477
genexus_version: "18"
---

# Previous function

Returns the previously entered value of a given attribute.

### [Syntax](#Syntax)

**Previous**( [Attribute] )

**Type Returned:**  
Same as argument attribute

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

Returns the value of *attribute* used in the last insertion in the current program session. The value is not stored and it is lost after the user leaves the [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) program. If no attribute is specified, the attribute being assigned is assumed.

### [Samples](#Samples)

Transaction Rule:

```
Default(ClientState, Previous());
```

If, for instance, the user types in 'SUSP' as the ClientState value and completes the insertion for the Transaction, the next insert screen will display 'SUSP' as the default value for ClientState, which the user may change. In other words, the default value for ClientState will be the last value entered.


|  |
| --- |
| **Backlinks** |
| [Default rule](https://wiki.genexus.com/commwiki/wiki?6850) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
