---
title: "After Action Triggering event"
source_id: 8284
source_url: https://wiki.genexus.com/commwiki/wiki?8284
genexus_version: "18"
---

# After Action Triggering event

Triggering a Rule after a specific action has been executed.

### Syntax

[AfterValidate](https://wiki.genexus.com/commwiki/wiki?8282)

It allows the execution of rules after certain level data has been confirmed. But before the insert, update or delete operations are performed in association with the mentioned level of the Transaction.

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213)  [ IF *condition* ][ **ON AfterValidate**];

**Wh​ere:**

*condition*  
     Is any valid logic condition

#### AfterInsert

It triggers immediately after doing the Insert action.

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213)  [ IF condition ][ **ON AfterInsert**];

**Where:**

*condition*  
      Is any valid logic condition

#### AfterUpdate

It triggers immediately after doing the Update action.

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213)  [ IF condition ][ **ON AfterUpdate**];

**Where:**

*condition*  
      Is any valid logic condition

#### AfterDelete

It triggers immediately after doing the Delete action.

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213)  [ IF condition ][ **ON AfterDelete**];

**Where:**

*condition*  
     Is any valid logic condition

[AfterComplete](https://wiki.genexus.com/commwiki/wiki?8160)

It triggers after the completion of a Logical Work Unit.

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213)  [ IF condition ][ **ON AfterComplete**];

#### Where:

*condition*  
      Is any valid logic condition

Type Returned: Boolean (True or False)

### Examples

The operation is triggered after updating or inserting the associated record.

```
A = B * C On AfterInsert, AfterUpdate;
```

Supposing we have a transaction that allows handling customer information, we want to print the customer's information after inserting a new customer or after an existing one has been modified. To do so, we must call a procedure that re-reads the Customer record from the database and then prints it.

Customers  
}  
    CustomerId\*  
    CustomerName  
    CustomerAccountBalance  
    CustomerAddress  
}

The following call is correct, because the operation (insert or update) over the database record has already been performed. So the called procedure will be able to read the information again.

```
PrintFile.Call(CustomerId) On AfterInsert, AfterUpdate;
```

The call takes place after the record has been inserted or updated.

In this example:

```
PrintFile.Call(CustId) On AfterComplete;
```

the call takes place after the LUW (Logical Unit of Work) has been completed. In this case, the insertion or update has been completed, and confirmed by the execution of the Commit (only works if transactional integrity is supported).

The following examples show a wrong way of specifying this:

```
PrintFile.Call(CustId); // Incorrect!!
```

For triggering the rule, the only thing necessary is to know the Customer Id. In a Microcomputer environment, because the operation is done field by field, the CALL will be performed after entering the Customer Id. This is incorrect, since the customer has not yet been inserted or modified.

In the iSeries environment, Java and Web interface, the CALL is triggered after pressing ENTER (even before requesting confirmation). This occurs because the dialog is performed by screen (instead of by field). Only after pressing ENTER the program takes control of all the data entered. Either way, the specification is not correct since the insert or update operation has not yet occurred.

```
PrintFile.Call(CustId) On AfterValidate; // Incorrect!!
```

The above rule is executed when there is an explicit change. AfterValidate means: "only after the operation on the table has been confirmed or validated". But "has been confirmed/validated" does not mean "has been performed", so the specification is incorrect for our purposes.

### Scope

**Objects** [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)

Compatibility

The After(Insert), After(Update) and After(Delete) functions are maintained for backward compatibility reasons. We highly recommend that you use the AfterInsert, AfterUpdate and AfterDelete events instead, For further information see [Triggering Events](https://wiki.genexus.com/commwiki/wiki?6840).

### See also

[After function](https://wiki.genexus.com/commwiki/wiki?8321)  
[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)

[Before Action Triggering events](https://wiki.genexus.com/commwiki/wiki?8283)  
[Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840)


|  |
| --- |
| **Backlinks** |
| [Before Action Triggering events](https://wiki.genexus.com/commwiki/wiki?8283) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Level clause for Transaction rules](https://wiki.genexus.com/commwiki/wiki?8438) |
| [Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868) | [Category:Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840) |

---
