---
title: "Work With Pattern instance for Multi-level Transactions"
source_id: 16004
source_url: https://wiki.genexus.com/commwiki/wiki?16004
genexus_version: "18"
---

# Work With Pattern instance for Multi-level Transactions

When a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) has [more than one level](https://wiki.genexus.com/commwiki/wiki?42569), each subordinated level generates in the Work With Pattern instance:

* A Level node
* An additional [Section](https://wiki.genexus.com/commwiki/wiki?20624) under the [Detail node](https://wiki.genexus.com/commwiki/wiki?15985) corresponding to the superordinated level.

Consider the following two-level Transaction shown below:

```
Property
{
    PropertyId*
    PropertyName
    PropertyAddress
    Photo
    {
       PropertyPhotoId*
       PropertyPhoto
       PropertyPhotoDescription
    }
}
```

Upon [applying the Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975), several nodes and sections are created in the Work With instance:

`[imagen omitida: wiki id 52273]`

Note that for each Transaction level, a **Level** node is created:

  - Level(Property)  
  - Level(Photo)

Then, for the first **Level** node (Property), the following is created:

* A **List** node to show all records. (Read more at [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984))
* A **Detail** node to show detailed information about a record selected from the List. (Read more at [Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985))

For the rest of **Level** nodes, only the **Detail** node is created.

The Work With pattern analyzes the Transaction information, its base table and also all the subordinates (even if they are not levels of the Transaction) in which you are applying the pattern. Based on this analysis, it generates **Section** nodes under the Detail nodes.

Look at the Section(Photo) node under the Detail node:

`[imagen omitida: wiki id 52271]`

From the Section(Photo) node the necessary code will be generated to show the several Photos of the Property displayed in the Detail [Panel](https://wiki.genexus.com/commwiki/wiki?24829).

Read more at [Work With Section Node](https://wiki.genexus.com/commwiki/wiki?20624).

## [Limitations](#Limitations)

Insert method is not supported in multilevel Transactions.

## [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Container of sections in the Detail screen of the Work With](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/container-of-sections-in-the-detail-screen-of-the-work-with?p=3658)


|  |
| --- |
| **Backlinks** |
| [Category:Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |

---
