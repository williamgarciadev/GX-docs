---
title: "Printing Commands Summary"
source_id: 5526
source_url: https://wiki.genexus.com/commwiki/wiki?5526
genexus_version: "18"
---

# Printing Commands Summary

GeneXus provides developers with a solid set of printing commands to generate reports easily and comfortably. This set of commands, which is listed in the table below, is used in [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) to control and send printing jobs.

A description of each command is provided in the table below, to help you understand what they do:

`[imagen omitida: wiki id 5527]`

|  |  |
| --- | --- |
| **CP** | Defines whether to continue printing on the same page or jump to the next one, depending on the lines remaining in the printable area (text-mode only). |
| **Eject** | Sets a page break. |
| **Footer** | Sets the footer lines to be printed at the bottom of each page. |
| **Header** | Defines what is going to be printed as the header of each page. |
| **Lineno** | Defines the line number where the following line will be printed. If the number is less than the current line, a page break is made. |
| **MB** | Defines the number of lines that will make up the bottom margin of the report. |
| **MT** | Defines the number of lines that will make up the upper margin of the report. |
| **NoSkip** | Avoids skipping a line. |
| **PL** | Sets the maximum number of lines per page (text-mode only). |
| **Print** | Sends a complete print block to the report's output media. |

The Measurement unit used is the User Space Units. This User space unit is approximately the same as the unit used in the printing industry which is the Point (pt) unit.  
1 inch = 25.4 mm = 72 user units

### [Example](#Example)

This example explains how to obtain a statistical report of all the crew members of an airline whose ages are in a given range, and whose ranks (Commander, Copilot, etc.) also match a given grade. These values are received by parameters through previously requested variables.

Since the process of accessing the database and selecting the data is carried out as follows:

```
For each order CrewLastName
       where CrewAge >= &AgeFrom
       where CrewAge <= &AgeTo
       where CrewRank = &Rank
       ...
EndFor
```

...and it is used in many places (reports, processes, etc.) in the project, a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) has been programmed as a navigation object that can be reused from other objects. This Data Selector, called CrewPerAgeRanks, has the following structure:

`[imagen omitida: wiki id 5528]`

The following group of print blocks has been designed within the Procedure object called AgesAndRanks:

`[imagen omitida: wiki id 5529]`

The following rules have been applied to the procedure:

`[imagen omitida: wiki id 5530]`

Lastly, the following source code has been programmed:

`[imagen omitida: wiki id 5531]`

The first group of lines sets the margins and length of the page, in lines. Next is the Header group, which is accessed by GeneXus only when a start page is detected. The body made up by only one line, prints the Header print block. The same happens with the Footer group, which is accessed when a page change is detected.

Note that the [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) is used in the relevant For Each group. Whenever valid information is found, it will be printed in the body of the For Each.

### [Basic Considerations](#Basic+Considerations)

To obtain the output report, remember that:

* The **Main program** property must be "True".
* The **Call** **protocol** property must be "HTTP".
* You need write the rule "Output\_File('reportname','PDF');".

When using a Graphic format such as PDF is not supported by the PL command. To get a custom report, modify the Paper Width and Paper Height Procedure's layout properties and use MT and MB commands when needed.


|  |
| --- |
| **Backlinks** |
| [Code Blocks](https://wiki.genexus.com/commwiki/wiki?7922) | [Footer command](https://wiki.genexus.com/commwiki/wiki?7967) | [Footer on last page property](https://wiki.genexus.com/commwiki/wiki?7992) |
| [Line variable](https://wiki.genexus.com/commwiki/wiki?8099) | [MB](https://wiki.genexus.com/commwiki/wiki?8631) | [MT](https://wiki.genexus.com/commwiki/wiki?8864) | [PL](https://wiki.genexus.com/commwiki/wiki?8635) |
| [Print Blocks](https://wiki.genexus.com/commwiki/wiki?7938) | [Print command](https://wiki.genexus.com/commwiki/wiki?5479) | [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) | [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |

---
