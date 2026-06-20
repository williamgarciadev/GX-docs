---
title: "Error rule"
source_id: 6852
source_url: https://wiki.genexus.com/commwiki/wiki?6852
genexus_version: "18"
---

# Error rule

Displays an error announcement and does not allow continuing with the execution while the condition is complied with.

### [Syntax](#Syntax)

**Error(**'announcement' | &var | character\_expression [,ExceptionName]**)** [ IF condition ] [ON triggering event];

**Where:**

*'**announcement**'**(or &var or character\_expression)*  
         Is the phrase (string) you want to display when the condition is complied with.  
        When using a variable or character\_expression, GeneXus controls the resulting type is character (if not, it is adviced in the navigation report).

*ExceptionName*  
         If the transaction is configured as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), the ExceptionName parameter can be set as the ID of the error to solve [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)

*condition*  
         Is any valid logic condition

*triggering event*  
         Is one of the predefined events available in GeneXus for transaction rules, which allows you to define the precise time for executing a rule

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Samples](#Samples)

**Example 1**

Customer                    
{                                     
    CustomerId\*           
    CustomerName     
    CustomerLastName  
    CustomerAddress  
    CustomerPhone  
    CustomerBirthDate        
}

Customer rules:

```
error('Enter the customer name please') if CustomerName.isempty();
error('Enter the customer last name please') if CustomerLastName.isempty();
error('The customer must be 18 years old or older') if CustomerBirthDate.age()<18;
error('Customers can not be deleted') if delete;
```

**Example 2**

Suppose the Customer transaction is configured as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) and the transaction has the following rule defined:

```
error('The customer must be 18 years old or older', 'CustomerMustBe18YearsOld') if CustomerBirthDate.age()<18;
```

The value referenced in the ExceptionName parameter will be charged in the &Messages collection variable based on the Messages SDT (in the "ID" property) which you can load using the [GetMessages() method](https://wiki.genexus.com/commwiki/wiki?23475).

Example code:

```
&CustomerBc is a Customer variable

&CustomerBc.save()
If &CustomerBc.Fail()
   &Messages = &CutomerBc.GetMessages()
    If &Messages.Item(1).ID = 'CustomerMustBe18YearsOld'
        .......
```

The ExceptionName parameter is an identifier, so it does not accept neither spaces, special characters: / : ” | = < > | nor Functions.

If the syntax is not correct, GeneXus will display the following compilation error:

xxx.cs(yy,yy): error CS0103: the name 'pushError' does not exist in the actual context.

**Example 3**

Working with the same Customer transaction, the following rule can be defined:

```
Error(&ReturnedText) if ProcedureCheck(&ReturnedText);
```

The previous definition is valid, but you must take into account that the variable &ReturnedText is considered a procedure input parameter. So, the rule will only be triggered if the variable is assigned (for example, if it is an output variable in another rule).

**Note**: When deleting a record from a Transaction, the rules won't execute unless you specify the condition "if delete".

### [See Also](#See+Also)

[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)


|  |
| --- |
| **Backlinks** |
| [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems - First Rules definitions](https://wiki.genexus.com/commwiki/wiki?34181) | [GeneXus for SAP Systems First Rules definitions (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54700) | [Category:Language object](https://wiki.genexus.com/commwiki/wiki?7258) |
| [Msg rule](https://wiki.genexus.com/commwiki/wiki?6854) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
