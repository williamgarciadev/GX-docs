---
title: "Examples of Using Formulas"
source_id: 5882
source_url: https://wiki.genexus.com/commwiki/wiki?5882
genexus_version: "18"
---

# Examples of Using Formulas

**1)** The following image shows the "FlightInstance" transaction being edited with the GeneXus transaction editor, and the *PassengerAge* attribute being defined as a [global formula](https://wiki.genexus.com/commwiki/wiki?6440) using the GeneXus formula editor:

`[imagen omitida: wiki id 6758]`

As you can see, in this defined formula a function was used to obtain the desired calculation.

**2)** Given the following transactions:

```
 
```

**Flight Transaction**

**FlightId\*  
       FlightDescription**

**FlightInstance Transaction**

****FlightInstanceId\*  
       FlightId  
       FlightDescription  
       FlightInstanceDate  
       FlightInstancePrice****

Suppose that you have defined a [Data Selector](https://wiki.genexus.com/commwiki/wiki?5271) as follows:

`[imagen omitida: wiki id 6745]`

The following code shows an [inline formula defined outside a For Each command](https://wiki.genexus.com/commwiki/wiki?6442) that [references the above Data Selector with the USING clause](https://wiki.genexus.com/commwiki/wiki?5432):

```
 
```

***&FlightPriceTotal* = Sum(*FlightInstancePrice*, using OneFlight(), 0)**

The table navigated by this inline formula is: FLIGHTINSTANCE in order to summarize all the *FlightInstancePrices* that belong to the *FlightId*=1.

**3)** Taking into account the FlightInstance transaction proposed in the above examples, we will show two [For Each commands in which inline formulas are defined in their where clause](https://wiki.genexus.com/commwiki/wiki?6426):

```
 
```

**for each**

**where Average(FlightInstancePrice) > 450**

**--------------**

**endfor**

```
 
```

**for each**

**where Sum(FlightInstancePrice) / Count(FlightInstanceDate) > 100**

**-------------**

**endfor**

See also: [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864), [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868), [Compound Formulas](https://wiki.genexus.com/commwiki/wiki?5879), [Redundant Formulas](https://wiki.genexus.com/commwiki/wiki?5962), [Generating SQL statements](https://wiki.genexus.com/commwiki/wiki?3155)


|  |
| --- |
| **Backlinks** |
| [Toc:Formulas](https://wiki.genexus.com/commwiki/wiki?25327) |

---
