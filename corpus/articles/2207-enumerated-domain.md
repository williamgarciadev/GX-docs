---
title: "Enumerated Domain"
source_id: 2207
source_url: https://wiki.genexus.com/commwiki/wiki?2207
genexus_version: "18"
---

# Enumerated Domain

It's a [Domain](https://wiki.genexus.com/commwiki/wiki?7221) with a finite number of values.

Each value has a Code, a Name, and a Value.

#### [**Example**](#Example)

```
"CardType" Domain
Code: Credit, Name: Credit, Value: 0
Code: Debit, Name: Debit, Value: 1
```

If an [Attribute or Variable](https://wiki.genexus.com/commwiki/wiki?6911) is based on an Enumerated Domain, it will be displayed in the Form as a combo box.  
  
It's a good practice to use an enumerator instead of using the value, as shown below:

```
&Var = 1              //BAD
&Var = CardType.Debit //GOOD
```

You can define the specific values for a Domain through its [Enum Values property](https://wiki.genexus.com/commwiki/wiki?7379).


|  |
| --- |
| **Backlinks** |
| [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) | [Compare function](https://wiki.genexus.com/commwiki/wiki?45423) | [Domain definition](https://wiki.genexus.com/commwiki/wiki?7239) |
| [Enumerated Domains Methods](https://wiki.genexus.com/commwiki/wiki?9918) | [GeneXus Application Localization - Programming considerations](https://wiki.genexus.com/commwiki/wiki?54440) | [Category:GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221) | [HowTo: Use CalculateDirections method from Maps external object](https://wiki.genexus.com/commwiki/wiki?46643) |
| [HowTo: Use the Wheel Control](https://wiki.genexus.com/commwiki/wiki?16239) | [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) | [OData Support in GeneXus](https://wiki.genexus.com/commwiki/wiki?40713) | [Rows per page property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52700) |
| [UITestSD external object](https://wiki.genexus.com/commwiki/wiki?44873) | [User Control Object - Definition of properties](https://wiki.genexus.com/commwiki/wiki?39541) | [User Control Object - Definition of properties (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53689) | [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) |

---
