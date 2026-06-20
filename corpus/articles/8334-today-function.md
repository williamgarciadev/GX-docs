---
title: "Today function"
source_id: 8334
source_url: https://wiki.genexus.com/commwiki/wiki?8334
genexus_version: "18"
---

# Today function

Returns the current date.

### [Syntax](#Syntax)

**Today()**

**Type Returned:**  
Date

### [Scope](#Scope)

**Object:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)

**Notes:**

* In the iSeries environment, this function returns the start date of the job and not the System Date. This allows running a job with a date different from the current one and using it in the program.
* To use the actual System Date, see the [Sysdate() function](https://wiki.genexus.com/commwiki/wiki?8493).
* In a PC environment, it returns the System Date so the Today and Sysdate functions are equivalent.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
   CustomerId*
   CustomerName
   CustomerPhone
   CustomerDateOfBirth
   CustomerAddedDate
}
```

**1)** In the Transaction Rules Tab, you can define the following rules:

```
Default(CustomerDateOfBirth, Today());
Error("The date of birth cannot be higher than today.") if CustomerDateOfBirth > Today();
```

The [Default rule](https://wiki.genexus.com/commwiki/wiki?6850) is only triggered when inserting a new record. So, the first rule initializes the CustomerDateOfBirth attribute with the current date as the default and the end user may change the value.  
The second rule validates whether the CustomerDateOfBirth is higher than today. If so, it displays an error text.

**2)** In addition, in the same Transaction Rules Tab you may define the following rules:

```
Default(CustomerAddedDate, Today());
Noaccept(CustomerAddedDate);
```

This Default rule initializes the CustomerAddedDate attribute with the current date as default. In turn, the [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) disables the edition of the CustomerAddedDate attribute. Therefore, the CustomerAddedDate attribute is set to the current date and that value can't be updated.

**3)**Now, consider a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that contains a &StartDate variable and a button in its [Web Layout](https://wiki.genexus.com/commwiki/wiki?8132). The end user must enter a date in the variable, and when clicking on the button, the associated event has to validate whether the &StartDate is empty or higher than the current date. If none of these things occur, all the customers inserted from the &StartDate value onwards must be navigated and some action must be performed.

The event associated with the button contains the following code:

```
Event 'Processes customers'
    If &DateFrom.IsEmpty()
        msg("The date must not be empty")
    Else
        If &DateFrom > Today()  
            msg("The date must not be higher than today")
        else
            For each Customer
              where CustomerAddedDate < &DateFrom
              //do something
            endfor  
        endif
    endif
Endevent
```

### [See Also](#See+Also)

[Sysdate function](https://wiki.genexus.com/commwiki/wiki?8493)  
[GxRemove variable](https://wiki.genexus.com/commwiki/wiki?8495)


|  |
| --- |
| **Backlinks** |
| [Age function](https://wiki.genexus.com/commwiki/wiki?8330) | [Age method](https://wiki.genexus.com/commwiki/wiki?12687) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Now function](https://wiki.genexus.com/commwiki/wiki?8335) | [ServerDate function](https://wiki.genexus.com/commwiki/wiki?8490) |
| [ServerNow function](https://wiki.genexus.com/commwiki/wiki?8491) | [Sysdate function](https://wiki.genexus.com/commwiki/wiki?8493) | [Today variable](https://wiki.genexus.com/commwiki/wiki?8873) |

---
