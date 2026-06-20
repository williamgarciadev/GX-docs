---
title: "Value range property"
source_id: 6797
source_url: https://wiki.genexus.com/commwiki/wiki?6797
genexus_version: "18"
---

# Value range property

Indicates a range of valid values for attributes, variables, domains, or SDT members to prevent end users from entering invalid values.

### [Scope](#Scope)

**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Domain](https://wiki.genexus.com/commwiki/wiki?7221), [SDT member](https://wiki.genexus.com/commwiki/wiki?10021), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

The verification of whether a value is within the established range is done at runtime when the value is entered through a form (when entering the value and leaving the field).

When an assignment is performed by code, the value is not validated against the specified range. It is taken into account when the value is to be saved in the database.

If the validation of an entered value fails, an error message is automatically generated, indicating "%1 is out of range" (%1 is replaced by the name of the attribute).

### [Considerations](#Considerations+)

1) This property is not available when the attribute is a formula, or when the attribute, variable, or SDT member is based on the Date data type.

2) Value Range Edition

In most cases, you can edit and change the default Value Range property, even if it is calculated automatically (inherited from a domain or subtype). In [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207)s, however, this value can't be modified even though the Value Range is also calculated automatically.

### [Syntax](#Syntax)

```
<ValueRange> ::= <Range> | <Value> [<ValueRange>]
<Range>      ::= <FromValue> ":" <ToValue>
             | <FromValue> ":" [<ToValue>]
             | [<FromValue>] ":" <ToValue>
<FromValue>  ::= <Value>
<ToValue>    ::= <Value>
<Value>      ::= <NumericConstant>
             | <StringConstant>
             | <DateConstant>
```

### [Samples](#Samples)

**1:20 30:** means the valid values are between 1 and 20 and greater than or equal to 30.  
**1 2 3 4:** means the valid value can be either 1, 2, 3 or 4.  
**'Y' 'N':** means the valid value can be either 'Y' or 'N'.  
**#1753-01-01****#****:****#****2010-03-07#:** means a date range.

### [Compatibility](#Compatibility)

Since GeneXus 17 Upgrade 4, this property also applies to SDT members.

### [See Also](#See+Also)

[Regular Expression property](https://wiki.genexus.com/commwiki/wiki?10484)  
[Validation Failed Message property](https://wiki.genexus.com/commwiki/wiki?10483)  
[Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802)


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) |
| [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371) | [Numeric data type](https://wiki.genexus.com/commwiki/wiki?6793) | [Regular Expression property](https://wiki.genexus.com/commwiki/wiki?10484) | [Supertype property](https://wiki.genexus.com/commwiki/wiki?7230) |
| [Validation Failed Message property](https://wiki.genexus.com/commwiki/wiki?10483) | [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

---
