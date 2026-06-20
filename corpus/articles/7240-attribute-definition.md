---
title: "Attribute definition"
source_id: 7240
source_url: https://wiki.genexus.com/commwiki/wiki?7240
genexus_version: "18"
---

# Attribute definition

For every [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), you have to define the **attributes** or fields that describe that object of reality.

Suppose you were asked to record, for each customer, his/her name, last name, address, phone, and email. Therefore, the data that must be recorded for each customer matches the attributes that have to be created for the Customer Transaction.

* [GeneXus](#tabs1-1)
* [GeneXus Next](#tabs1-2)

After creating the Customer Transaction, its [Structure](https://wiki.genexus.com/commwiki/wiki?7661) is shown with the first line created to enter the first attribute:

`[imagen omitida: wiki id 22461]`

If you press the “dot” key on the keyboard, GeneXus automatically shows the Transaction name as a prefix in the attribute name:

`[imagen omitida: wiki id 22462]`

You only have to type "Id" after the "Customer" prefix to complete the first attribute name. Next, you press the Tab key and choose the data type that will be stored for this attribute:

`[imagen omitida: wiki id 22468]`

The data type combo box displays the data types available in GeneXus. For this attribute you can leave the default data type, that is to say: Numeric of 4 digits (with no decimals).

Pressing Enter opens a new line for you to start creating the second attribute.

It is strongly recommended to press the “dot” key on the keyboard when creating a new attribute to obtain automatically the Transaction name as a prefix in the attribute name. This helps to avoid typing errors and to name attributes correctly.

Note that an icon key is associated with the first line. The reason is that in every Transaction, an attribute – or set of attributes – must be set with an identifier or key role.

After creating the Customer [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), you have two alternatives to define its attributes:

1. Through the **Source** editor
2. Through the **Structure** editor

The attribute definitions you make through one editor or the other will be reflected in both. You can choose to use the **Source** editor or the **Structure** editor depending on which editor you like to work with.

Below you can see the brand new Customer Transaction (recently created), ready for you to define its attributes. By default, the Source editor is open. You can select the Structure editor (by clicking on the Structure selector). You can also use both editors alternating between them.

`[imagen omitida: wiki id 58259]`

Continuing with the example that for each customer it is necessary to register his/her name, last name, address, phone, and email, below is the Customer Transaction Structure (the definition was made through this editor):

`[imagen omitida: wiki id 58295]`

The Source editor was automatically completed with the same definitions:

`[imagen omitida: wiki id 58296]`

**Notes:**

* When using the Source editor, not only can you type the data type, but you can also use the [Properties Editor](https://wiki.genexus.com/commwiki/wiki?3160).
* Note the icons/symbols in both editors. Their interpretation is usually intuitive. Some particular symbols in the Source editor are:
  + **!** represents the [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154).
  + **?**represents a foreign key with its Nullable value = Yes.

### [See also](#See+also)

[Insert Attribute/Variable Dialog](https://wiki.genexus.com/commwiki/wiki?5985)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [First Transaction design](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/first-transaction-design-v16?p=5331)


|  |
| --- |
| **Backlinks** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Attributes and Domains Help and Documentation edition](https://wiki.genexus.com/commwiki/wiki?12509) |
| [Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892) | [Autonumber for replication property](https://wiki.genexus.com/commwiki/wiki?7225) | [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) | [Autonumber start property](https://wiki.genexus.com/commwiki/wiki?7223) |
| [Autonumber step property](https://wiki.genexus.com/commwiki/wiki?7224) | [Based on property](https://wiki.genexus.com/commwiki/wiki?7782) | [Beep on each read property](https://wiki.genexus.com/commwiki/wiki?48530) |
| [Case property](https://wiki.genexus.com/commwiki/wiki?39416) | [Column title property](https://wiki.genexus.com/commwiki/wiki?7235) | [Compare function](https://wiki.genexus.com/commwiki/wiki?45423) | [Data Provider property in Attributes/Variables](https://wiki.genexus.com/commwiki/wiki?56081) |
| [Date format property (for Date/DateTime attributes/variables)](https://wiki.genexus.com/commwiki/wiki?39441) | [Description property](https://wiki.genexus.com/commwiki/wiki?7446) | [Display mode property](https://wiki.genexus.com/commwiki/wiki?48528) | [Download content in Offline applications property](https://wiki.genexus.com/commwiki/wiki?40907) |
| [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154) | [FileURI property](https://wiki.genexus.com/commwiki/wiki?39979) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems - Working with Attributes and Domains](https://wiki.genexus.com/commwiki/wiki?34180) |
| [GIK Naming Convention](https://wiki.genexus.com/commwiki/wiki?9020) | [Hour format property](https://wiki.genexus.com/commwiki/wiki?39440) | [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) | [Image data type](https://wiki.genexus.com/commwiki/wiki?15204) |
| [ImageURI property](https://wiki.genexus.com/commwiki/wiki?15205) | [IN Operator](https://wiki.genexus.com/commwiki/wiki?11688) | [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) | [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) |
| [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) | [Length property](https://wiki.genexus.com/commwiki/wiki?6794) | [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) | [Map Type property in attributes/variables based on Geography data types](https://wiki.genexus.com/commwiki/wiki?41338) |
| [Null function](https://wiki.genexus.com/commwiki/wiki?8421) | [Operation mode property](https://wiki.genexus.com/commwiki/wiki?48529) | [Picture property](https://wiki.genexus.com/commwiki/wiki?36522) | [Picture property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58071) |
| [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) | [Regular Expression property](https://wiki.genexus.com/commwiki/wiki?10484) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [Signed property](https://wiki.genexus.com/commwiki/wiki?6796) | [Significant attribute name length property](https://wiki.genexus.com/commwiki/wiki?7248) | [Supertype property](https://wiki.genexus.com/commwiki/wiki?7230) |
| [TDiff function](https://wiki.genexus.com/commwiki/wiki?8513) | [Trace Color property](https://wiki.genexus.com/commwiki/wiki?45382) | [Trace Thickness property](https://wiki.genexus.com/commwiki/wiki?45381) | [Category:Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) |
| [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661) | [Val function](https://wiki.genexus.com/commwiki/wiki?8528) | [Validation Failed Message property](https://wiki.genexus.com/commwiki/wiki?10483) |
| [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) | [Category:Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) | [What is error 403?](https://wiki.genexus.com/commwiki/wiki?45483) |

---
