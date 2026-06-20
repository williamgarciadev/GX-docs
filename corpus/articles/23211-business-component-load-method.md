---
title: "Business Component Load method"
source_id: 23211
source_url: https://wiki.genexus.com/commwiki/wiki?23211
genexus_version: "18"
---

# Business Component Load method

Executes something equivalent to what happens when you type an identifier value in a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) Form and exit the field. All the data corresponding to that identifier are loaded into memory (in this case in a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)).

### [Syntax](#Syntax)

**&***VarBasedOnBC*.**Load**(*PKAttri1, ..., PKAttriN*)

**Where:**  
*&VarBasedOnBC*  
      Is a variable defined in a GeneXus object, based on a Business Component.

*PKAttri1, ..., PKAttriN*   
      Are the values that make up the [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868) of a Transaction first [level](https://wiki.genexus.com/commwiki/wiki?42569).  
      It must be a valid value for the Primary Key of the Transaction set as a Business Component and the *&VbleBasedOnBC*variable was defined based on it.

### Samples

```
  &Customer.Load(10)
  &Customer.CustomerEmail = 'jsmith@gmail.com'
  &Customer.save()
  commit
```

The above code loads in memory a Customer by applying the Load method to the variable based on the Customer Business Component data type. Then, the next line of code modifies the Customer email by assigning a certain value to the &Customer.CustomerEmail [property](https://wiki.genexus.com/commwiki/wiki?2276). The third line of code updates physically the record (by applying the [Save method](https://wiki.genexus.com/commwiki/wiki?23229) to the variable). Finally, the [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) is executed (which is indispensable).

### See Also

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Business Component Delete method](https://wiki.genexus.com/commwiki/wiki?23238) |
| [Business Component Fail method](https://wiki.genexus.com/commwiki/wiki?23402) | [Business Component GetByKey method](https://wiki.genexus.com/commwiki/wiki?31846) | [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Business Component Mode method](https://wiki.genexus.com/commwiki/wiki?23790) |
| [Business Component RemoveByKey method](https://wiki.genexus.com/commwiki/wiki?31847) | [Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229) | [Business Component Success method](https://wiki.genexus.com/commwiki/wiki?23404) | [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) |
| [Business Components - Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) | [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) | [RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360) |

---
