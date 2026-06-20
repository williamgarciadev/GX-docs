---
title: "Serial rule"
source_id: 6866
source_url: https://wiki.genexus.com/commwiki/wiki?6866
genexus_version: "18"
---

# Serial rule

Numbers a Transaction object’s second, third, or another nested level, automatically.

### [Syntax](#Syntax)

**Serial(***att1* **,** *att2* **,** *step***)**;  
  
**Where:**  
  
*att1*  
     Is the attribute to be increased.  
  
*att2*  
     Marks the starting value for att1 and is always updated with the last value of att2. This attribute must be included in the structure level that is immediately above the attribute you wish to autonumber. You can delete att2 from the form, but the attribute att1 is required to be on the web form, otherwise the rule will not work on the client-side.

*step*  
     Is the value to add to each *att1.* In other words, is the serialization step or increment.

### [Description](#Description+)

You need to use this rule to automatically number a second, third, or another nested level, as the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) can only be applied to single primary keys.  
This rule requires defining an attribute in the first level of the Transaction, which will save the last value assigned to the lines of the second level.

### [Samples](#Samples)

`[imagen omitida: wiki id 22872]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
