---
title: "Accept rule"
source_id: 6844
source_url: https://wiki.genexus.com/commwiki/wiki?6844
genexus_version: "18"
---

# Accept rule

Modifies the default read-only behavior of variables in Transaction objects, allowing the user to enter a value for that variable.

### [Syntax](#Syntax)

**Accept(***&var* [ **,***att* ] **)**;

**Where:**

*&var*  
    Is the variable defined in the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) and included in the screen to accept a value. It could be an [SDT](https://wiki.genexus.com/commwiki/wiki?2427) variable and in this case just writing Accept(&var) is enough to enable all the SDT elements.

*att*  
    Is an optional attribute that you can mention, to help to determine in which [Transaction level](https://wiki.genexus.com/commwiki/wiki?42569) the variable must be considered. If att is not specified, then the first level is assumed.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This server rule allows you to accept a variable at the Transaction level where the Attribute *att* is found. The order in which data is entered for a certain level depends on the order in which the variables and attributes have been positioned on the screen. If *att* is not specified then the first level is assumed.

### [Samples](#Samples)

```
Customer
{
  CustomerId*
  CustomerName
  CustomerAddress
  CustomerPhone
  CustomerPassportNum
}
```

Customer rules:

```
Accept(&Print);
PrintTicket(CustomerPassportNum) if &Print='Y';
```


|  |
| --- |
| **Backlinks** |
| [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) | [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) | [Rules in Transactions](https://wiki.genexus.com/commwiki/wiki?8213) |
| [Transaction rules when executed as Business Component](https://wiki.genexus.com/commwiki/wiki?2280) |

---
