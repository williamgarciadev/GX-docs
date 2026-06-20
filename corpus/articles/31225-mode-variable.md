---
title: "Mode variable"
source_id: 31225
source_url: https://wiki.genexus.com/commwiki/wiki?31225
genexus_version: "18"
---

# Mode variable

Indicates the mode in which a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) will work.

**Data type:**  
Character(3)

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974)

### [Values](#Values)

|  |  |
| --- | --- |
| **INS** | Insert. This is the default value. |
| **UPD** | Update. |
| **DLT** | Delete. |
| **DSP** | Display. |

**Note**: ***TrnMode*** domain is also available with those values.

### [Description](#Description)

The &Mode [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) defines the valid mode in which the Transaction can work in, during execution time.

The calling program passes a valid mode value as a parameter to the Transaction, which receives &Mode variable as a parameter.  
  
The received mode affects the first level of the Transaction, and it cannot be changed. Thus, a Transaction with two or more levels can receive the &Mode variable, with the values Insert ('INS'), Display (‘DSP’) or Update ('UPD'), as a parameter. The second level can use all three modes (Insert, Update, or Delete).

If the received mode is Delete ('DLT'), a [delete cascade](https://wiki.genexus.com/commwiki/wiki?20901) is performed.  
  
The Transaction that receives the *Display Mode* by parameter doesn't accept secondary attributes, nor does it update the database or lock information. Only the load of the record is executed (and rules, depending on the conditioning). The [Navigation Buttons](https://wiki.genexus.com/commwiki/wiki?22882,,) and the *Close* button are enabled. All other buttons are disabled. Enabling the key depends on the [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856), or if it is received as a parameter. The rest of the fields are disabled.

Like all other modes (Update, Delete and Insert) the Display mode can also be evaluated in the rules.

**Note**: Values are case sensitive.

### [Triggering actions](#Triggering+actions)

**Events:** Only Start and Exit events are triggered.

**Rules:** Only the rules that fulfill the following conditions are triggered:

* When appearing before the "Read" of the record in the navigation.
* When conditioned to the Update Mode.
* When depending only on the Transaction’s key.

### [[Panels](https://wiki.genexus.com/commwiki/wiki?24829)](#wiki%3F24829%2CCategory%253APanel%2Bobject+Panels)

The &Mode variable is available in Section and Detail nodes of [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15974). This approach is useful to decide in runtime what information you want to show when the end-user access to any of those Panels. The following table shows whether it is possible to use the &Mode variable.

|  |  |  |
| --- | --- | --- |
|  | Client | Server |
| **Detail** | YES | YES |
| **Section**   (View mode) | YES | YES |
| **Section**  (Edit mode) | YES | NO |

**Note**: The value of &Mode received by the Transaction cannot be changed, otherwise, the corresponding program will not be generated.

### [Samples](#Samples)

A [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) calls a Transaction to insert, update, delete or display purchase orders.

#### [Case 1](#Case+1)

**Rules:**

The Transaction receives &Mode and purchase order identifier as parameters:

```
Parm(&OrderNumber, &Mode);
OrderNumber = &OrderNumber If Update Or Delete;
Noaccept(OrderNumber) If Update Or Delete;
```

The record's key is assigned the value passed as a parameter when Update or Delete mode is activated. The key has no pre-set value when Insert mode is activated, so the user has to enter a valid key-value and several orders may be inserted.

#### [Case 2](#Case+2)

**Rules:**

```
Parm(OrderNumber, &Mode);
```

As OrderNumber is the key attribute and receives the value passed as a parameter, then the key will be fixed for all three modes. Only one record can be updated, deleted or inserted. If an insertion is to be performed, the user doesn’t have to enter the key of the new record, as this value has been received as a parameter. So, the key is passed to the Transaction even in Insert mode. In this case, when the action over the record is completed, the program automatically returns to the calling program.

#### [Case 3](#Case+3)

Suppose that you want to change the form caption depending on the mode that the end-user access to the Panel.  
In the following case, if the end-user enters the Panel in delete mode, then the header text asks if the end-user wants to delete it.

```
Event ClientStart
    if &Mode = TrnMode.Delete
        Form.Caption = format("Delete customer %1?", CustomerId)
    endif
EndEvent
```

### [See Also](#See+Also)

[Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386)


|  |
| --- |
| **Backlinks** |
| [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
