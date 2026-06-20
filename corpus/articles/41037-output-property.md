---
title: "Output property"
source_id: 41037
source_url: https://wiki.genexus.com/commwiki/wiki?41037
genexus_version: "18"
---

# Output property

Sets the name of the Structured Data Type or Business Component whose type is returned by the Data Provider.

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)

### [Description](#Description)

The output of a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) is a hierarchical structure. GeneXus represents this kind of data using a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) or a collection of SDTs. A [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) (BC) or a collection of BCs can also be returned.

This property is the only way to define the Data Provider's output (it is not possible to do it using the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)).

Completing this property is mandatory.

If you drag an SDT or a [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) configured as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) from the KB Explorer to a Data Provider's source, the **Output property** of the **Data Provider**​​​​​​is automatically set with the name of the SDT or BC.

#### [**Business Component as output**](#Business+Component+as+output)

The GeneXus Transaction object also provides a way to represent hierarchical data, but at the database level, through a user interface (the Form). The corresponding hierarchical structure resulting from keeping only the structure (and all the logic) but not the Form is called a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846). A Business Component involves an SDT, meaning it is also a hierarchical structure that can be used in the same scenarios where an SDT is applicable. For this reason, the output of a Data Provider can be not only an SDT (or a collection of SDTs) but also a BC (or a collection of BCs).

There is no difference if the output of the Data Provider is an SDT or a BC. The BC structure is filled within the Data Provider source, just like an SDT.

It is important to note that [the object calling the Data Provider](https://wiki.genexus.com/commwiki/wiki?5310) will have to work with the result returned by the Data Provider, and execute the [Insert method](https://wiki.genexus.com/commwiki/wiki?31695) or the [InsertOrUpdate method](https://wiki.genexus.com/commwiki/wiki?31697) to perform the insertion(s) into the database.

#### [**Properties related to this property**](#Properties+related+to+this+property+)

The following properties allow you to choose whether to return an instance, a collection, or a matrix of the type you set in the **Data Provider Output property**:

- [Collection property](https://wiki.genexus.com/commwiki/wiki?41179)  
- [Collection Name property](https://wiki.genexus.com/commwiki/wiki?41229)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.


|  |
| --- |
| **Backlinks** |
| [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) | [Collection Name property](https://wiki.genexus.com/commwiki/wiki?41229) | [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) |
| [Custom Chatbot Definition property](https://wiki.genexus.com/commwiki/wiki?45528) | [Table of contents:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) | [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292) |
| [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GXScheduler User Control](https://wiki.genexus.com/commwiki/wiki?11583) | [HowTo: Consume a Rest Data Provider](https://wiki.genexus.com/commwiki/wiki?30737) | [HowTo: Use the Infer Structure property of a Data Provider](https://wiki.genexus.com/commwiki/wiki?23651) |
| [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296) | [Infer Structure property](https://wiki.genexus.com/commwiki/wiki?23628) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Modules Distribution in GeneXus (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58151) |
| [Package Module with database access for Solutions extensibility scenarios](https://wiki.genexus.com/commwiki/wiki?42900) | [RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360) | [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310) |

---
