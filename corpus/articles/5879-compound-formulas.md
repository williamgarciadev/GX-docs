---
title: "Compound Formulas"
source_id: 5879
source_url: https://wiki.genexus.com/commwiki/wiki?5879
genexus_version: "18"
---

# Compound Formulas

A Compound [Formula](https://wiki.genexus.com/commwiki/wiki?5861) is an expression whose definition includes several [Horizontal](https://wiki.genexus.com/commwiki/wiki?5864) and/or [Aggregate](https://wiki.genexus.com/commwiki/wiki?5868) formulas.

Look at the following example. Given these transactions:

```
Flight Transaction 
```

*FlightId\**

*FlightDescription*

*FlightPrice*

***FlightInstanceAveragePrice* = [Sum](https://wiki.genexus.com/commwiki/wiki?6500)(*FlightInstancePrice*) / [Count](https://wiki.genexus.com/commwiki/wiki?6500)(*FlightInstanceDate*)**

**FlightInstance** Transaction

*FlightInstanceNumber\**

*FlightId*

*FlightDescription*

*FlightPrice*

*FlightInstanceDate*

*FlightInstanceNumberOfPassengers*

*FlightInstancePrice* = *FlightPrice* if *FlightInstanceNumberOfPassengers* <= 100;

*FlightPrice* \* 0.9 if *FlightInstanceNumberOfPassengers* > 100 and *FlightInstanceNumberOfPassengers* < 200;

*FlightPrice* \* 0.8 otherwise;

*FlightInstanceAveragePrice* is a Compound Formula (defined in a [global](https://wiki.genexus.com/commwiki/wiki?6440) way).

The following image shows the "Flight" transaction being edited with the GeneXus transaction editor, and the *FlightInstanceAveragePrice*compound formula attribute being edited with the GeneXus formula editor:

`[imagen omitida: wiki id 5881]`

Note that *FlightInstancePrice* is an [horizontal formula](https://wiki.genexus.com/commwiki/wiki?5864)*.*


|  |
| --- |
| **Backlinks** |
| [Data Provider Element statement](https://wiki.genexus.com/commwiki/wiki?25103) | [Data Provider Variable statement](https://wiki.genexus.com/commwiki/wiki?25413) | [Examples of Using Formulas](https://wiki.genexus.com/commwiki/wiki?5882) |
| [Category:Formulas](https://wiki.genexus.com/commwiki/wiki?5861) | [Toc:Formulas](https://wiki.genexus.com/commwiki/wiki?25327) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) |

---
