---
title: "Automatic paging in Grid control"
source_id: 6086
source_url: https://wiki.genexus.com/commwiki/wiki?6086
genexus_version: "18"
---

# Automatic paging in Grid control

Automatic paging implies that [paging](https://wiki.genexus.com/commwiki/wiki?31280) is implemented in the generated code without the need to program anything.

*For Web applications*, when the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) for a Grid is different than zero, GeneXus will perform automatic paging. That is, the paging buttons (FirstPage, PreviousPage, NextPage, and LastPage) are automatically added to the Grid footer and they will behave as expected.

`[imagen omitida: wiki id 31290]`

However, if any of those events are included explicitly in your object code, automatic paging will not be available. See [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) for details about programming paging manually.

### [Styles for paging buttons in Web applications](#Styles+for+paging+buttons+in+Web+applications)

In the [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) you are using, under the Image class, the following classes are offered:

`[imagen omitida: wiki id 31279]`

For those child classes, you can configure the appearance of the automatic paging buttons.

### [**Notes**](#Notes+)

* Automatic paging is supported in Grids with and without [Base Table](https://wiki.genexus.com/commwiki/wiki?6347).
* For those cases in which the Grid does not have a base table or the filters cannot be evaluated on the server side, the [LastPage](https://wiki.genexus.com/commwiki/wiki?8771) button doesn't work. The [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772), [RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757) aren't implemented either in that case.
* *In Native Mobile apps*, when the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) is set to a value different than zero, Grid paging behaves as [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231).

### [Scope](#Scope)

**Controls**:[Grid control](https://wiki.genexus.com/commwiki/wiki?24817)  
**Generators**: [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [See Also](#See+Also)

[Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231)


|  |
| --- |
| **Backlinks** |
| [Fixed Grid header with vertical scroll](https://wiki.genexus.com/commwiki/wiki?36036) | [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) | [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) |
| [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) |

---
