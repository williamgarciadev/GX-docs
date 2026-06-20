---
title: "Name property"
source_id: 6985
source_url: https://wiki.genexus.com/commwiki/wiki?6985
genexus_version: "18"
---

# Name property

Identifies an Object (in a Module) or a Theme-class (in a Theme object). In a Data View object, it is the name of the external physical file (or logical file in iSeries), or the name of the external index file.

### [Description](#Description)

Its value must begin with an alphabetic character and may be followed by alphanumeric characters and/or the underscore sign ("\_") for a maximum length of 256 characters. The number of significant characters (the number of characters used for identification purposes) is controlled by the following properties:

* [Significant object name length property](https://wiki.genexus.com/commwiki/wiki?7250)
* [Significant attribute name length property](https://wiki.genexus.com/commwiki/wiki?7248)

As mentioned, in [Data View objects](https://wiki.genexus.com/commwiki/wiki?1914) this property is used to set the name of the external physical (or logical in the iSeries) file you want to access. In particular, each [Data View object](https://wiki.genexus.com/commwiki/wiki?1914), has a **Name Property** associated with the object and you can also find the **Name property** in the Data View Structure under the Data Stores node, for each DBMS you define. GeneXus always uses the name you set under the Data Stores node for the corresponding DBMS, unless it is empty; in that case, GeneXus uses the **Name property** associated with the Data View object. Besides, each Data View contains the Indexes tab, where for each index you define, the **Name property** is available to complete the name of the external index file.

Moreover, the **Name property** of a [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246), identifies it in the [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) or [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) (i.e. if a new Theme Class is created in one Theme object, it will be replicated to every Theme object of the same nature).

#### [Notes](#Notes)

* You should avoid starting object names with "GX". This prefix is reserved for GeneXus internal use.
* The name cannot contain blank spaces.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.

### [See Also](#See+Also)

[Module object](https://wiki.genexus.com/commwiki/wiki?22411)  
[Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802)  
[Domain definition](https://wiki.genexus.com/commwiki/wiki?7239)  
[Variable definition](https://wiki.genexus.com/commwiki/wiki?7375)


|  |
| --- |
| **Backlinks** |
| [Address property](https://wiki.genexus.com/commwiki/wiki?6984) | [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Attribute theme-class](https://wiki.genexus.com/commwiki/wiki?37646) |
| [BPD Subprocesses Embedded Properties](https://wiki.genexus.com/commwiki/wiki?17582) | [BPD Subprocesses Reusable Properties](https://wiki.genexus.com/commwiki/wiki?17580) | [Business Process Diagram Properties](https://wiki.genexus.com/commwiki/wiki?20896) | [Button theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37647) |
| [Calling objects from Menu Events](https://wiki.genexus.com/commwiki/wiki?17392) | [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) | [Domain definition](https://wiki.genexus.com/commwiki/wiki?7239) | [Event Gateway](https://wiki.genexus.com/commwiki/wiki?17504) |
| [Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17505) | [Category:File object](https://wiki.genexus.com/commwiki/wiki?5852) | [Form theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37648) | [Grid Theme class](https://wiki.genexus.com/commwiki/wiki?37657) |
| [HowTo: Convert a Folder into a Module](https://wiki.genexus.com/commwiki/wiki?25231) | [HowTo: Convert a Module into a Folder](https://wiki.genexus.com/commwiki/wiki?35373) | [HowTo: Merge two or more Knowledge Bases into one using Modules](https://wiki.genexus.com/commwiki/wiki?25613) | [Inclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17506) |
| [Index Properties](https://wiki.genexus.com/commwiki/wiki?7131) | [LocalName Property](https://wiki.genexus.com/commwiki/wiki?7034) | [MailRecipient Data Type](https://wiki.genexus.com/commwiki/wiki?6926) | [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) |
| [Menu theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37667) | [Category:Module object](https://wiki.genexus.com/commwiki/wiki?22411) | [Modules - Grammar](https://wiki.genexus.com/commwiki/wiki?25609) | [Modules - Known Limitations](https://wiki.genexus.com/commwiki/wiki?22492) |
| [Modules - Object names](https://wiki.genexus.com/commwiki/wiki?22483) | [Modules vs. Folders](https://wiki.genexus.com/commwiki/wiki?22470) | [Parallel Gateway](https://wiki.genexus.com/commwiki/wiki?17507) |
| [Progress theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37765) | [Qualified Name property](https://wiki.genexus.com/commwiki/wiki?22477) |
| [Query Object Properties](https://wiki.genexus.com/commwiki/wiki?18471) | [Reusable Properties](https://wiki.genexus.com/commwiki/wiki?12867) | [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [Slider Theme class](https://wiki.genexus.com/commwiki/wiki?42294) |
| [Structured Data Type Properties](https://wiki.genexus.com/commwiki/wiki?8081) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) | [Validation Failed Message property](https://wiki.genexus.com/commwiki/wiki?10483) |
| [Variable definition](https://wiki.genexus.com/commwiki/wiki?7375) |

---
