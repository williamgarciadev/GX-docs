---
title: "Msg rule"
source_id: 6854
source_url: https://wiki.genexus.com/commwiki/wiki?6854
genexus_version: "18"
---

# Msg rule

Displays a message as a notice or warning, but it doesn't prevent you from continuing working.

### [Syntax](#Syntax)

**Msg(**'*message*' | &*var* | character\_expression [,*ExceptionName*]**)** [ IF *condition* ] [ON triggering event]**;**

**Where:**

*'**message**'**(or &var or character\_expression)*  
         Is the phrase (string) you want to display when the condition is complied with.  
         When using a variable or character\_expression, GeneXus controls the resulting type is character (if not, it is adviced in the navigation report).

*ExceptionName*  
         If the transaction is configured as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), the ExceptionName parameter can be set as the ID of the message to solve [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)

*condition*  
         Is any valid logic condition

*triggering event*  
         Is one of the predefined events available in GeneXus for transaction rules, which allows you to define the precise time for executing a rule

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

This rule is used to display a message as a notice or warning, with the possibility to continue working if the condition is complied with. In other words, it does not stop the process as it happens with the [Error rule](https://wiki.genexus.com/commwiki/wiki?6852).

### [Samples](#Samples)

**Example 1**

```
Customer                    
{                                     
    CustomerId*           
    CustomerName     
    CustomerLastName 
    CustomerAddress
    CustomerPhone        
}
```

Customer Rules:

```
msg('The address is empty') if CustomerAddress.isempty();
msg('The phone is empty') if CustomerPhone.isempty();
error('Enter the customer name please') if CustomerName.isempty();
error('Enter the customer last name please') if CustomerLastName.isempty();
```

**Example 2**

Suppose the Customer transaction is set as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) and the transaction has the following rule defined:

```
msg('The phone is empty',CustomerPhoneIsEmpty) if CustomerPhone.isempty();
```

The value referenced in the ExceptionName parameter will be charged in the &Messages collection variable based on the Messages SDT (in the "ID" property) which you can load using the GetMessages() method.

Example code:

```
&CustomerBc is a Customer variable

&CustomerBc.save()
If &CustomerBc.Fail()
   &Messages = &CutomerBc.GetMessages()
    If &Messages.Item(1).ID = CustomerPhoneIsEmpty
       .......
```

The ExceptionName parameter is an identifier, so it does not accept neither spaces, special characters: / : ” | = < > | nor Functions.

If the syntax is not correct, GeneXus will show the following compilation error:

xxx.cs(yy,yy): error CS0103: the name 'pushError' does not exist in the actual context.

### [See Also](#See+Also)

[Message command](https://wiki.genexus.com/commwiki/wiki?8241,,)  
[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)


|  |
| --- |
| **Backlinks** |
| [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems - First Rules definitions](https://wiki.genexus.com/commwiki/wiki?34181) | [Category:Language object](https://wiki.genexus.com/commwiki/wiki?7258) |
| [Msg function](https://wiki.genexus.com/commwiki/wiki?31635) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
