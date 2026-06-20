---
title: "Default rule"
source_id: 6850
source_url: https://wiki.genexus.com/commwiki/wiki?6850
genexus_version: "18"
---

# Default rule

Assigns a default value to an attribute or variable.

### [Syntax](#Syntax)

Default(*att* | &*var*, *expression*);

**Where:**

*att*| *&var*  
    Is the attribute or variable to be assigned.

*expression*  
    Is any valid [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,). The result must match the attribute or variable data type.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)

### [Description](#Description)

This rule is mostly used to initialize an attribute with a certain value, which can be modified, in a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,). Here, the rule is triggered only when the Transaction is executed in Insert mode. When the Transaction is executed in other modes like Update, Delete or Display, the attribute already has a stored value, and the objective of this rule is not to rewrite it.

Although this rule can be used in other objects with the same objective, its use is unusual because depending on the object, the variables may be initialized in different sections, like an event, source, etc.

### [Samples](#Samples)

**Sample # 1**

```
Customer
{
  CustomerId*      
  CustomerName         
  CustomerAddress      
  CustomerPhone   
  CustomerAddedDate 
  CustomerState
}
```

**Customer Rule:**

```
Default(CustomerAddedDate,today());
```

When the Customer Transaction is executed in Insert mode, the CustomerAddedDate attribute is displayed initialized with today's date. The end user can modify the suggested date.   
If you don't want to allow it to be modified, you can add the following rule:

```
Noaccept(CustomerAddedDate);
```

**Sample # 2**

The following example shows a rule defined in the Customer Transaction that uses the [Previous function](https://wiki.genexus.com/commwiki/wiki?8477) to initialize the CustomerState attribute for a new customer that is being inserted (with the value of the previous customer).

```
Default(CustomerState,Previous());
```

In other GeneXus objects (like Procedures or Web panels), the Default rule can only be defined to initialize variables, and they will be triggered at the beginning of program execution. The expression in these cases only allows 'literals' between quotes, numbers, and the following functions: Today(), Date() and Sysdate(). An example is shown below:

```
Default(&FirstCustomerId, 1);
Default(&LastCustomerId, 999);
```


|  |
| --- |
| **Backlinks** |
| [Code Snippets](https://wiki.genexus.com/commwiki/wiki?10662) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Rules in Procedures](https://wiki.genexus.com/commwiki/wiki?8262) |
| [Rules in Transactions](https://wiki.genexus.com/commwiki/wiki?8213) | [Rules in Web Panels](https://wiki.genexus.com/commwiki/wiki?8288) | [Today function](https://wiki.genexus.com/commwiki/wiki?8334) |

---
