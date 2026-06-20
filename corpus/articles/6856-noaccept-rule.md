---
title: "NoAccept rule"
source_id: 6856
source_url: https://wiki.genexus.com/commwiki/wiki?6856
genexus_version: "18"
---

# NoAccept rule

Prevents the value of a field from being changed by end-user interaction. In most environments, this means the field is disabled (no end-user input is allowed) when the condition (if any) applies.

If user input cannot be disabled ([Business Component](https://wiki.genexus.com/commwiki/wiki?5846), iSeries, for example), the input value is ignored.

### [Syntax](#Syntax)

**NoAccept(***att* | **&***var***)** [ **IF** *condition* ][ **ON** *triggering event*] **;**

**Where:**

*att* | ***&**var*In [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s only variables are editable. So, in those objects, this rule can be used for variables. In [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, attributes are editable. So, mostly this rule is used for attributes. Variables are accepted in Transaction if you define [Accept rule](https://wiki.genexus.com/commwiki/wiki?6844)s.

*condition*  
   Is the condition that must be met to trigger the rule.

*triggering event*  
   See [Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840).

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Visual FoxPro (up to GeneXus X Evolution 3), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The NoAccept rule doesn´t allow the end-user to change the value of a field. In most [Environments](https://wiki.genexus.com/commwiki/wiki?7115), this means that the field is disabled (no end-user input is allowed) when the condition (if any) applies. If user input cannot be disabled ([Business Component](https://wiki.genexus.com/commwiki/wiki?5846), iSeries, for example), then that input value is ignored.

GeneXus evaluates which Attributes/Variables are used for input/output. However, there are times when you do not want the end-user to enter data for what GeneXus considers to be an input Attribute/Variable. This rule enables you to define which will not be used as input fields. The rule may also be used in combination with conditions.

All variables that appear in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) are always by default input variables (i.e. they accept input) unless a NoAccept rule has been defined for it. Hence, this rule indicates that the variable must not be accepted.

When you declare this rule, you will be able to assign a value for the attribute or variable with another rule.

### [Samples](#Samples)

```
NoAccept(ProductDescription);                             // Unconditional NoAccept
NoAccept(CustomerCreditLimit) if CustomerCategoryId = 1;  // Conditional NoAccept
```

**Notes:**

* **&var**could be an [SDT](https://wiki.genexus.com/commwiki/wiki?2427) variable and in this case just writing *NoAccept(&var)* is enough to disable all the SDT elements.
* *Conditional Noaccept*: You **must** be able to evaluate the condition before the attribute/variable in the NoAccept rule is entered. That is, the attributes/variables involved in the condition must have a value before the rule is triggered. Conditional NoAccept is only valid for Transactions.
* NoAccept rule over Primary Keys does not apply to Business Components methods (Load, Insert, Update, InsertOrUpdate).
* The NoAccept rule is expanded at specification time as **{att|&var}.E*nabled = 0* assignment for the No Accept condition and **{att|&var}.E*nabled = 1* for the otherwise section.
* If you take the conditional rule of the previous example, you will see in the following code the Navigation view of the object:

*One condition:*

Rule:

```
NoAccept(CustomerCreditLimit) if CustomerCategoryId = 1;
```

Navigation View:

```
CustomerCreditLimit.Enabled = 0 If CustomerCategoryId = 1; 1 OTHERWISE;
```

This means that the rule will disable the CustomerCreditLimit attribute only if the value of the attribute CustomerCategoryId is 1. Otherwise, it will remain enabled.

*More than one condition:*

Rule:

```
NoAccept(CustomerDiscount) if CustomerDate > Today() and CustomerActive = false and CustomerAmount = 0;
```

Navigation View:

```
CustomerDiscount. Enabled = 0 IF CustomerDate > today() and CustomerActive = FALSE and CustomerAmount = 0; 1 OTHERWISE;
```

This means that the rule will disable the CustomerDiscount attribute only if the value of the attribute CustomerDate is < Today() and the value of the attribute CustomerActive = false and the value of the attribute CustomerAmount = 0, otherwise it will remain enabled.

* If you have different conditionals NoAccept, you must be careful with the conditions defined in each one, as they can cause conflicts between them.

### [See Also](#See+Also)

[Enabled property](https://wiki.genexus.com/commwiki/wiki?8765)


|  |
| --- |
| **Backlinks** |
| [Enabled property](https://wiki.genexus.com/commwiki/wiki?8765) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) |
| [How to define Variables and Arrays](https://wiki.genexus.com/commwiki/wiki?7385) | [Mode variable](https://wiki.genexus.com/commwiki/wiki?31225) | [ReadOnly property](https://wiki.genexus.com/commwiki/wiki?8826) | [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506) |
| [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) | [Update rule](https://wiki.genexus.com/commwiki/wiki?21430) | [Web Panel rules](https://wiki.genexus.com/commwiki/wiki?8288) |

---
