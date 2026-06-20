---
title: "After Attribute function"
source_id: 8324
source_url: https://wiki.genexus.com/commwiki/wiki?8324
genexus_version: "18"
---

# After Attribute function

**Deprecated**: Since GeneXus 8.0 . Replaced by the [Dependencies clause](https://wiki.genexus.com/commwiki/wiki?6868).

Allows mentioning an attribute to indicate that we want a transaction rule to be executed after that attribute's value has been entered by the user.

### [Syntax](#Syntax)

**Rule**  [ IF after(attribute) ];

**Where:**  
*attribute*  
    It's the attribute for whose value we want to wait in order to execute the rule.

**Type Returned:**  
Boolean (True or False)  
    The evaluation of the After(attribute) function returns a Boolean value (TRUE or FALSE).  
    The After(attribute) function becomes TRUE after the specified Attribute is entered by the user.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Samples](#Samples)

```
A                 
{                                  
  A1*        
  A2
  A3
  A4
  A5
}

Rule:
A2 = A3 *A4 if After(A5);
```

The rule is executed after the A5 attribute value has been entered by the user, or after level in the iSeries environment, or after confirm in the Java environment or Web interface.

It is not necessary to define rules like the following:

```
A2 = A3 *A4 if After(A3);
A2 = A3 *A4 if After(A4);
```

GeneXus already knows that to trigger these rules, it has to wait until the user has entered both A3 and A4. However, if you want to change the triggering moment and set it to happen after having the value of a certain attribute that is not included in the rule, this function can be used.

**Notes:**

* The After(attribute) condition works just like the Level(attribute) condition in the iSeries environment and works just like the After(confirm) condition in the Java environment or Web interface.
* Only input attributes can be specified as parameters; otherwise, the Rule will not be triggered.

### [See Also](#See+Also)

[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)


|  |
| --- |
| **Backlinks** |
| [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
