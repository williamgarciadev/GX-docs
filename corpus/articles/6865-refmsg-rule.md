---
title: "Refmsg rule"
source_id: 6865
source_url: https://wiki.genexus.com/commwiki/wiki?6865
genexus_version: "18"
---

# Refmsg rule

Replaces GeneXus default message whenever a referential integrity check fails.

### [Syntax](#Syntax)

**Refmsg(**'*Character-expression*' | &*var* | *att*, *att1*, ... , *attn* **);**  
  
**Where:**  
  
*Character-expression (or**&var or att**)*

Is the phrase (string) you want to display when the referential integrity check fails.  
  
*att1 , ... , attn*  
         Attributes that forms the foreign key (simple o compound by several attributes) for which the referential integrity check fails.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

This rule allows you to replace the GeneXus default message whenever a referential integrity check fails. There are two types of referential integrity messages:

* While inserting or updating:  " No matching ......"
* When deleting: " Invalid deletion....."

However, only the first type of message will be changed by defining this rule.

### [Samples](#Samples)

Given the following Transactions:

```
Airline
{
   AirlineId*
   AilineName
}

Flight
{
   FlightId*
   FlightDate
   FlightPrice
   AirlineId
   AilineName
}
```

The following rule is defined in the Flight Transaction:

```
Refmsg('Enter a valid Airline, please.', AirlineId);
```

**Note:**Since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,) the Refmsg rule offers the following features:

* You can include the [Format function](https://wiki.genexus.com/commwiki/wiki?8406) as the first argument containing any attribute that is present in the [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661) in the message to be shown.
* A warning [spc0158](https://wiki.genexus.com/commwiki/wiki?6774) is displayed when a Refmsg rule will be never triggered.
* A warning [spc0231](https://wiki.genexus.com/commwiki/wiki?6774) is displayed to warn if the Refmsg rule references secondary attributes that cannot be instantiated.

### [See Also](#See+Also)

[Refcall rule](https://wiki.genexus.com/commwiki/wiki?6864)  
[Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863)


|  |
| --- |
| **Backlinks** |
| [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) | [Refcall rule](https://wiki.genexus.com/commwiki/wiki?6864) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |
| [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
