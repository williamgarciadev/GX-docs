---
title: "No triggered actions"
source_id: 17062
source_url: https://wiki.genexus.com/commwiki/wiki?17062
genexus_version: "18"
---

# No triggered actions

This document is a brief description of the concept of "no triggered actions" or "rules not included" during the specification phase. The "No Triggered Actions" section is detailed on the [Specification Report](https://wiki.genexus.com/commwiki/wiki?7171,,) when [enabled](https://wiki.genexus.com/commwiki/wiki?12885,,).

Every action has an entry list of dependencies. An action is a reading of a table, a business rule (eg: error rule, msg rule), the calculation of a formula, the calculation of Dynamic Combo box, Suggests, Input Type Descriptions features. A dependency is a variable or attribute that must be known to trigger the action.

An action can be triggered only when all input variables and attributes related with that action are known. Once the action is triggered, the attributes and variables computed with the action associated are now also considered to be known, so other attributes or variables depending on the previous ones are able to be evaluated too.

The "No Triggered Actions" or "Rules not included" sections, detail the set of actions that are not generated on the program because one of its dependencies never becomes instantiated (known in the context of the object.).

As a general term, the "No triggered actions" section will detail the transaction level where the problem occurs while the "Rules not included" section is more general and will only detail the rule that will not be included.

This means that the program will not behave as desired; the developer needs to check the transaction structure and rules and solve the problem.

### [Examples](#Examples)

#### [Inferred Attributes](#Inferred+Attributes)

Let's assume a Bill Transaction with a Customer Foreign Key. On the Bill transaction it is detailed the CustomerCode and CustomerName attributes.  
An action is generated to get CustomerName once the user inserts the desired CustomerCode attribute. The action generates a reading action on the Customer table to get the name, and this action is dependent on the CustomerCode attribute. Once this attribute is known the CustomerName is known and other actions depending on CustomerName can be triggered.

If you get a No "Triggered Action" message on CustomerName it means that the generated program will not resolve this attribute and dependencies on this attribute will not be resolved either.

#### [Formula calculation](#Formula+calculation)

Suppose you have the following "No Triggered Actions" section with the following formulas:

```
No Triggered Actions
t04f01 = t04int1 + t04int2
t04int2 = t05int1
```

and the following transaction structure

```
T04
{
t04id*
t04int1
t04f01
}
```

You need to check all the dependencies for those formulas; for the example the problem is related to the following not included attributes on the transaction structure: *t04Id*, *t05int1* and *t04int2* as these are needed dependencies to calculate t04f01. Once these attributes are included on the Transaction Structure all the dependencies will be resolved and the specification report will correctly detail:

```
READ t04 
WHERE t04. t04id = t04id
  INTO  t04int1 t05id
READ  t05 
WHERE t05. t05id = t04. t05id
  INTO  t05int1
  t04int2 = t05int1
  t04f01 = t04int1 + t04int2
```

### [See also](#See+also)

[Options - Build](https://wiki.genexus.com/commwiki/wiki?12885,,)  
[spc0208](https://wiki.genexus.com/commwiki/wiki?6774)
