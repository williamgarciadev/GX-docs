---
title: "New command"
source_id: 6714
source_url: https://wiki.genexus.com/commwiki/wiki?6714
genexus_version: "18"
---

# New command

Procedures include a command called New to insert records in a table. Using this command, you can assign values to the attributes of **one** physical table.

`[imagen omitida: wiki id 28559]`

It is a low-level command, used to insert a [New Record](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6739,,) in a table. Since the New record modifies the database, it is only suitable for the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), not even for the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), where the addition is performed differently.

**Note:** Reading the paper "[GeneXus and Relational Databases: the Essence](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6720,,)" by Breogán Gonda and Nicolás Jodal is highly recommended.

### [Example](#Example)

There is a “Product” Transaction for saving the information related to the products managed in a system, with its corresponding price list. The structure is as follows:

```
Product
{
   ProductId*
   ProductDescription
   ProductStock
   PriceList
   {
     ProductPriceListDate*
     ProductPriceListPrice
   }
}
```

Based on this, GeneXus creates two tables: PRODUCT and PRODUCTPRICELIST, each one corresponding to a level in the structure. The last one, PRODUCTPRICELIST, will have three attributes: ProductId, ProductPriceListDate and ProductPriceListPrice, with [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868) {ProductId, ProductPriceListDate}.

Suppose you want to implement a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) so that the product whose code is received as a parameter adds the new price (also received as a parameter) to its price list, for the date when the procedure is executed. Therefore, within its rules section, the Procedure will include the following:

**Parm( in: &ProductId, in:&price );**

In Source, type the following:

```
New
    ProductId = &ProductId
    ProductPriceListDate = &Today
    ProductPriceListPrice = &price
EndNew
```

Note that within the New command there are assignment commands, where each attribute in the table where the record is intended to be inserted is given a value. In this case, you want to add a record in the PRODUCTPRICELIST table.

Also, read a detailed [explanation of the concepts behind the example](https://wiki.genexus.com/commwiki/wiki?6742).

### [Syntax](#Syntax)

```
New
   [Defined by attributeList]
   [Blocking NumericExpression]
             BodyCode
[When duplicate
   { AnotherCode |
       For each
         {att = exp}
         …
       Endfor
     | AnotherCode } ]
 EndNew
```

**Where:**

*attributeList*  
A list of attributes (comma or space-separated) used to determine (together with the attributes on the left in an assignment inside the *BodyCode*) the table where the record will be added.

*NumericExpression*  
The 'blocking factor.' Its presence activates the [Block (Batch) insertion mechanism](https://wiki.genexus.com/commwiki/wiki?4538) and controls the number of records to be added per block.

*BodyCode*  
A sequence of commands, most of which, if not all, will be the form assignment:  
*att* **=** *exp*

**where:**  
*att*  
Attribute to assign (for the record to be added).  
  
e*xp*  
The expression assigned can be an Attribute, Variable, Constant, Function, or Arithmetic Expression (Date and Numeric type only).

#### [**When duplicate**](#When+duplicate)

It specifies the code to be executed when a duplicate record is detected (when a record with the same [primary key](https://wiki.genexus.com/commwiki/wiki?1868) or [candidate key](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2199,,) already exists in the table). Most times, some attributes of that existing record need to be updated. In these cases, a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) must be used, and the attributes to be updated are assigned within it. Even though it's not so common, other commands can be executed as well (*AnotherCode*).

**Note**: If there is a Blocking clause, When Duplicate commands are executed **after** an attempt to insert the entire block and a duplicate record is found. In this case, an insertion attempt is made for each record in the block; all the records may be successfully inserted, or 'When duplicate' commands may have to be used. See an in-depth explanation of [Block (Batch) insertion mechanism](https://wiki.genexus.com/commwiki/wiki?4538).

### [Description](#Description)

The [extended table](https://wiki.genexus.com/commwiki/wiki?6029) concept is not used here – the command works by adding a single record in a single physical table, determined by the attributes in the *BodyCode* together with those in the 'Defined by' clause, if applicable. Duplicate keys are checked in [primary](https://wiki.genexus.com/commwiki/wiki?1868) and [candidate](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2199,,) keys. Even if the command has the [**Blocking clause**](https://wiki.genexus.com/commwiki/wiki?4538), it adds a single record in a single table. The blocking clause only improves performance when the New command is inside a repetitive structure, not in a loop.

If an assignment to an attribute that doesn't belong to the **base table** is detected within a New command, an error is shown in the Specification report, and the program is not generated.

The New command can be included in other iterative structures, such as Do while, [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), For to step, which allow for batch insertions (here, the Blocking clause improves performance). Many New commands can be concatenated one after the other as another way to insert multiple records. Also, New commands can be nested.

#### [How does GeneXus determine 'the table' of the New command?](#How+does+GeneXus+determine+%27the+table%27+of+the+New+command%3F)

Every time GeneXus finds a “new” command, it must identify the table where the records will be inserted. This table is identified based on the attributes in the *BodyCode* block of the “new” command (not the When Duplicate clause), on the **left in an assignment**, together with the attributes included in the 'Defined by' clause, if it exists, and it’s referred to as the **base table** of the "new" command. GeneXus will look for a **physical table** that contains all these attributes. If this table doesn't exist, an error message describing the issue will be displayed in the navigation report after the procedure specification, and the object will not be generated.

#### [Do all attributes of the base table have to be assigned inside the New command?](#Do+all+attributes+of+the+base+table+have+to+be+assigned+inside+the+New+command%3F)

Not necessarily. What happens to a record to be added depends on the context, when the table attributes are not explicitly assigned inside the *BodyCode* of the New command.

* If the attribute is not instantiated: it will be empty (or null, depending on the corresponding property of the attribute) for the record to be added.
* If the attribute is instantiated: the attribute, in the record to be added, will take the value of that attribute in the context, at the moment the addition is made.

What does context mean?

* If an attribute is received as a parameter, its scope is the entire code. It keeps its value everywhere it is mentioned or needed.
* If a command (such as New) is inside another (that is, in the scope of the latter), all the attributes 'instantiated' in the latter are in the 'context' of the former. For example, if a New command is inside a For Each command, all the attributes of the For Each command's [extended table](https://wiki.genexus.com/commwiki/wiki?6029) are in the context of the New command. What does it mean? For example, suppose a For Each command is iterating the Customers table and, after some calculations, a New command is added to its code, trying to insert for the current customer a record in a summarizing customer table. If the New command doesn't have an explicit assignment for the CustomerId attribute, its value will be taken from the For Each command (its context).

#### [What happens if the primary key or any candidate key already exist?](#What+happens+if+the+primary+key+or+any+candidate+key+already+exist%3F)

* The commands specified within the *BodyCode* block of the New command are not executed for that record.
* The When duplicate command can be used to specify the action to be executed when duplicates are detected. All commands, between When duplicate and Endnew are executed when a Duplicate Key is detected during insertion.
* A GeneXus variable: &ERR, could be created and if so, is set to code = 1.
* A GeneXus variable: &ERRMSG could be created, and if so, is set to a message.
* If the record to be inserted already exists and you want to update data in this record, a For Each command must be specified within the 'When duplicate' clause.
* See the above note about the 'Blocking' clause.

#### [When is the insertion performed?](#When+is+the+insertion+performed%3F)

It depends on the presence of the '[Blocking clause](https://wiki.genexus.com/commwiki/wiki?4538)'. If it doesn't exist, the insertion will be performed at the end of the command (when the Endnew is reached). Otherwise, the actual insertion will be performed at the end of the block. Suppose the New command has a blocking factor N and is inside a repetitive structure (such as a For Each command). Every time the For Each command body is executed (and the New command inside it), the record of the New is not actually inserted, but is added into a memory block (a buffer) of size N. Afterwards, if the buffer is filled, a special insert (of many rows) is sent to the database, in order to insert the entire block. Then, if some of the N records to be added are found duplicated, the special insertion fails, and a one-by-one insertion is done, running through the N block, using the simple insert command.

#### [Calling other programs within a New command](#Calling+other+programs+within+a+New+command)

If you call another program within a New command (whether you use [Call](https://wiki.genexus.com/commwiki/wiki?16224)] or [Udp](https://wiki.genexus.com/commwiki/wiki?3964)), the call is always executed, even if the key already existed.

Example

```
New
    A = 1
    B = 1
    Calculation.call()  //The call method can be omitted. You can write: Calculation()
When Duplicate
    For each
         B = 2
     Endfor
EndNew
```

The “Calculation” Procedure is always called even if the key of the record to be inserted already existed in the table and the call is placed before the When duplicate clause. This behavior occurs because the Call command can be used to fetch some values to assign to the attributes.

### [Notes](#Notes)

* **Referential Integrity** is **NOT** checked during insertion.
* Redundancy will **NOT** be automatically maintained during insertion in Procedures. This maintenance is the programmer's responsibility. That is, if redundancy has been defined for an attribute in the table you are inserting, GeneXus will not search or calculate data to store in that attribute. In case of a Formula Redundancy, the Formula will not be available and the value must be calculated explicitly and assigned to the associated attribute.

### [Scope](#Scope)

**Objects** [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)

### [See also](#See+also)

[When duplicate clause](https://wiki.genexus.com/commwiki/wiki?24843)  
[Update the database directly with commands VERSUS using Business Components](https://wiki.genexus.com/commwiki/wiki?2216)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Updating with procedure-specific commands. Introduction](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/updating-with-procedure-specific-commands-introduction-6104731)


|  |
| --- |
| **Backlinks** |
| [Blocking Clause in 'New' Command](https://wiki.genexus.com/commwiki/wiki?4538) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Category:Database update through procedures](https://wiki.genexus.com/commwiki/wiki?6826) |
| [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) | [ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |
| [Update the database directly with commands VERSUS using Business Components](https://wiki.genexus.com/commwiki/wiki?2216) | [What is a subroutine?](https://wiki.genexus.com/commwiki/wiki?24767) | [When duplicate clause](https://wiki.genexus.com/commwiki/wiki?24843) | [Xnew command](https://wiki.genexus.com/commwiki/wiki?8640) |

---
