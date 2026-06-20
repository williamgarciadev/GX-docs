---
title: "Transaction Rules in Native Mobile Applications"
source_id: 16843
source_url: https://wiki.genexus.com/commwiki/wiki?16843
genexus_version: "18"
---

# Transaction Rules in Native Mobile Applications

Rules provide a generic language to enforce controls in [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s. These rules can be applied in [Work With](https://wiki.genexus.com/commwiki/wiki?16847)s as well (remember Transactions will be executed as web services [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)s).

### [Behavior](#Behavior)

When the insert, update or delete actions are executed from the [WWSD Detail](https://wiki.genexus.com/commwiki/wiki?15985), is the Transaction as Business Component what is called. So, those Transaction rules not involving the Web Form will be executed, getting messages into the [Messages SDT](https://wiki.genexus.com/commwiki/wiki?2279), that are later processed by the Work With in order to show the corresponding information into the Native Mobile application. For instance:

### [Error](#Error)

This rule is triggered when the user taps "Save" on the Transaction. If the condition of the error Rule is true, then a pop-up message like the following will appear.

`[imagen omitida: wiki id 16844]`

### [NoAccept](#NoAccept)

Disables you to enter a value attribute field, as shown in the image.

`[imagen omitida: wiki id 16846]`

This rule assigns values or formulas/expressions to an attribute, for example:

`[imagen omitida: wiki id 16852]`

`[imagen omitida: wiki id 16849]``[imagen omitida: wiki id 16850]`

### [Default](#Default)

Assigns a default value to an attribute or variable at Insert time.

`[imagen omitida: wiki id 16867]`

As shown in the image below, fields are filled upon executing the insert operation.

`[imagen omitida: wiki id 16866]`

### [**Add**](#Add)

Adds two attributes if the condition evaluates to True. In the next example below, you have the following rule: "Add(Numeric1,Numeric2);" and, as pictured, numeric2 is disabled.

After tapping on "Save", the rule is executed and adds the value from "Numeric1" to "Numeric2".

`[imagen omitida: wiki id 16868]` `[imagen omitida: wiki id 16869]`

### [**Subtract**](#Subtract)

Subtracts the value of an attribute from another attribute, depending on a condition. In the example below, you have the rule "Subtract(Numeric1,Numeric2);" and, as pictured, numeric2 is disabled.

After tapping "Save" the rule is executed and subtracts the value from "Numeric1" from "Numeric2".

`[imagen omitida: wiki id 16872]` `[imagen omitida: wiki id 16873]`

### [**Call**](#Call)

Calls a GeneXus object, passing attributes/variables as parameters. Parameters may be attributes, variables or constant values.


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
