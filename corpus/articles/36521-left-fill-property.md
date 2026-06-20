---
title: "Left fill property"
source_id: 36521
source_url: https://wiki.genexus.com/commwiki/wiki?36521
genexus_version: "18"
---

# Left fill property

It details how to display the non-significant zeros for a number (the zeros to the left of the number).

### [Values](#Values)

|  |  |
| --- | --- |
| **Blank** | Left zeros are not shown, but when the value is zero, it is shown. This is the default value. |
| **Blank when Zero** | Left zeros are not shown, also the zero value. |
| **Zero** | Left zeros are shown. |

### [Samples](#Samples)

|  |  |  |  |
| --- | --- | --- | --- |
|  | **INPUT** | **OUTPUT** | |
|  | *Numeric(7.2)* | *0* | *123.5* |
| **Blank** | ZZZ9.99 | 0.00 | 123.50 |
| **Blank when zero** | ZZZZ.ZZ |  | 123.50 |
| **Zero** | 9999.99 | 0000.00 | 0123.50 |

How to read this table?

The first column shows the possible values of the left fill picture: Blank, Blank when zero and Zero of this property.

The 'INPUT' column shows the numeric type used for the example - in this case, a variable of type N(7,2), - and for each left fill property value, shows the value that is generated AUTOMATICALLY in the 'Picture'.

The 'OUTPUT' column shows:

1) Examples of values that the Variable can take (i.e. 0 and 123.5 on left fill table)  
2) How GeneXus format that value, according to the value of the left fill property

For example, on left fill property, on a Numeric(7,2), when selected value is "Blank", on Picture property changes to ZZZ9.99 automatically, and when that variable is assigned "123.5", it shows on screen "123.50".


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) |

---
