---
title: "Thousand separator property"
source_id: 8911
source_url: https://wiki.genexus.com/commwiki/wiki?8911
genexus_version: "18"
---

# Thousand separator property

It determines whether to include a separator for thousands or not.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

Default value: True

Notice the [IDE](https://wiki.genexus.com/commwiki/wiki?5587,,) uses the "," (comma) character to represent it in the Picture property. Later, during the generation phase, the programs will use the [Decimal separator property](https://wiki.genexus.com/commwiki/wiki?7670).

### [Samples](#Samples)

|  |  |  |  |
| --- | --- | --- | --- |
|  | **INPUT** | **OUTPUT** | |
|  | *Numeric(7.2)* | *456* | *1123.5* |
| **True** | Z,ZZ9.99 | 456.00 | 1,123.50 |
| **False** | ZZZ9.99 | 456.00 | 1123.50 |


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) |

---
