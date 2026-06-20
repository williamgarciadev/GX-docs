---
title: "Xnew command"
source_id: 8640
source_url: https://wiki.genexus.com/commwiki/wiki?8640
genexus_version: "18"
---

# Xnew command

Inserts a record in an external file (Base Table). The insertion is performed when the Xendnew is found.

### [Syntax](#Syntax)

```
<Xnew>::= Xnew <filename> 
            {<Att> = <expression>}
             …
          Xendnew
```

View[Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**  
  
*filename*   
   The name of the [Data View object](https://wiki.genexus.com/commwiki/wiki?1914) defined to access the external file.

*Att*  
   The attribute to be assigned.

*expression*  
   The expression assigned can be either an Attribute, a Variable, a Constant, a Function or an Arithmetic Expression (Date and Numeric types only).

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)

### [Samples](#Samples)

Given the following Data View with no Associated Table:

Name: *CustomerExt*  
Composition:   
                        *CustomerId  
                        CustomerName*  
Indexes: *Name*: ICustomerExt (Unique)  
Composition: *CustomerId*  
  
The following example shows a Procedure definition that inserts a new Customer:

```
Xnew 'CustomerExt'
    CustomerId = 1
    CustomerName = 'Ulrich Karnbatz'
Xendnew

If &Err = 1
    Print Error
Endif
```

If the Customer number already exists, the message 'Record already exists' will be displayed. Duplicate keys will be checked because the index was defined as unique.

**Notes:**

* **Customer/Server:** Duplicate keys are checked only for Data Views where the index has been defined as unique.
* **iSeries:** External logical file keys must be defined as unique and uniqueness is automatically verified by the operating system.

### [See Also](#See+Also)

[New command](https://wiki.genexus.com/commwiki/wiki?6714)  
[Xfor Each command](https://wiki.genexus.com/commwiki/wiki?8596)
