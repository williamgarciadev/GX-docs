---
title: "Nested Grids in Web Panels"
source_id: 6062
source_url: https://wiki.genexus.com/commwiki/wiki?6062
genexus_version: "18"
---

# Nested Grids in Web Panels

You can define Nested Grids in a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132).

To achieve this, inside a [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) you can add another [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) or a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817).

A [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) (standard grid) cannot have other grids nested within it.

For example, consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Category
{
  CategoryId*
  CategoryName
}

Company
{
  CompanyId*
  CompanyName
  CategoryId
  CategoryName
}
```

To display in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) each category and its associated companies, as shown:

|  |  |
| --- | --- |
| **Hotels** |  |
|  | Hilton |
|  | Hyatt |
|  | Marriot |
| **Airlines** |  |
|  | United |
|  | Air France |
| **...** |  |

You must first insert a Free Style Grid containing the CategoryName attribute. Then, within the Free Style Grid, insert another Grid (standard or Free Style) containing the CompanyName attribute.

Remember the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) (standard grid) cannot have other grids nested within it. So, if you need to have several levels of nested grids, only the last grid may be a standard grid.

### [Finding Base Tables](#Finding+Base+Tables)

Nested grids follow the same relationship rules as nested [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s. Therefore, GeneXus finds each grid's base table (they aren't completely independent: the main grid's base table will influence the finding of the nested grid's base table).

Next, based on these findings it defines the navigations it will make for each grid. The grids' logic will depend on the relationships found between said tables.

If there isn't a base table, the data should be loaded with the Load command.

### [Triggering Events](#Triggering+Events)

Each grid maintains its own [Load event](https://wiki.genexus.com/commwiki/wiki?8188) and [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,). Every time the Load command is executed in a grid with nested grids, a call is made to each child's Refresh and Load event.


|  |
| --- |
| **Backlinks** |
| [Determining the Base Table for each Grid in a Web Panel](https://wiki.genexus.com/commwiki/wiki?6105) | [Category:Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) |

---
