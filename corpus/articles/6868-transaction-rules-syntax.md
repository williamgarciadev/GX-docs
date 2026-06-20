---
title: "Transaction Rules Syntax"
source_id: 6868
source_url: https://wiki.genexus.com/commwiki/wiki?6868
genexus_version: "18"
---

# Transaction Rules Syntax

The purpose of this article is to describe the general syntax associated to the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)’s rules.

### [Syntax](#Syntax)

```
<RuleName> [if <condition>] [on <event1>,...,<eventN>] [level <Att1>,...,<AttN>] [dependencies <Att1>;...;<AttN>|<&var1>;...;<&varN>];
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**  
  
*RuleName*Specifies a [Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213).

*condition*   
       Is the boolean expression that details the conditions that must be fulfilled to trigger the rule. It can be composed of logic operators (and, or, not).

[*event1,...,**eventN*](https://wiki.genexus.com/commwiki/wiki?6840)  
Is the event or list of events separated by “,”. The possible values are [AfterInsert, AfterUpdate, AfterDelete](https://wiki.genexus.com/commwiki/wiki?8284), [AfterValidate](https://wiki.genexus.com/commwiki/wiki?8282), [AfterComplete](https://wiki.genexus.com/commwiki/wiki?8160), [AfterLevel](https://wiki.genexus.com/commwiki/wiki?8285), [BeforeValidate, BeforeInsert, BeforeUpdate, BeforeDelete and BeforeComplete.](https://wiki.genexus.com/commwiki/wiki?8283)

*Att1*,...,*AttN*  
         Is the attribute or list of attributes separated by “,” determining the **level** of the Transaction where the rule applies; the first level is assumed in case the section level is not specified.

*Att1*,...,*AttN*| **&***var1,...,***&***varN*Is an attribute (or variable), or a list of them separated by ";", that determines the rule will be triggered upon accepting those attributes (variables). This is because the **Dependencies clause** is used to indicate attributes and/or variables that once their values are obtained, the rule will be triggered.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

The syntax of the transaction rules can be logically divided into two sections: *condition* and *triggering event*. The *condition* section is used to specify an expression that must be evaluated to execute the rule. The *triggering event* details the events where the rule must be triggered, which are associated with the **on** and **level** sections.

### [Samples](#Samples)

Given the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Client
{
  ClientId*
  ClientName
  ClientType
  ClientBalance
  Phone
  { 
     ClientPhoneId*
     ClientPhoneNumber
     ClientPhoneDescription
  }
}
```

The following are some detailed examples using this syntax:

Assigning a value on the AfterValidate (same to BeforeInsert) event:

```
ClientType = 1 If Insert On AfterValidate;
ClientType = 1 On BeforeInsert;
```

Calling a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) on the AfterInsert or AfterUpdate event:

```
Proc(ClientId) On AfterInsert, AfterUpdate;
```

Executing the rule error if a maximum is reached:

```
Error('Maximum reached') If ClientBalance > &Max On AfterValidate;
```

Calling a log Procedure on the AfterInsert or AfterDelete event:

```
Proc1(ClientId, &Mode) On AfterInsert, AfterDelete;
```

Calling a Procedure after the level associated with the attribute ClientPhoneId:

```
Proc2(ClientId) On AfterLevel Level ClientPhoneId;
```

### [See Also](#See+Also)

[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)  
[Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840)


|  |
| --- |
| **Backlinks** |
| [After Attribute function](https://wiki.genexus.com/commwiki/wiki?8324) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
