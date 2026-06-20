---
title: "Subtype Group object"
source_id: 20206
source_url: https://wiki.genexus.com/commwiki/wiki?20206
genexus_version: "18"
---

# Subtype Group object

Defines a group of attributes as an alias of others.

### [Description](#Description)

An attribute can be a 'subtype' of another, meaning that the first attribute is just the second attribute with another name.

Subtypes must be defined in 'Groups'. For example, given the Airport [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Airport
{
    AirportId*
    AirportName
}
```

The subtypes of AirportId and AirportName must be defined in a group as follows:

|  |
| --- |
| **DepartureAirport Subtype Group** |
| DepartureAirportId is a subtype of AirportId |
| DepartureAirportName is a subtype of AirportName |

A Group can be viewed as a 'virtual' transaction in the sense that even if the Subtype Group definition doesn't indicate GeneXus by itself that a table must be created to store departure airports, it has all the other properties of a Transaction (a Group key, a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), etc.).

DepartureAirportId is a subtype attribute and AirportId is its supertype attribute. In the same way, the DepartureAirportName attribute is a subtype and AirportName is its supertype. A well-defined Subtype Group must contain a subtype attribute or a set of subtype attributes, whose corresponding supertype attributes make up the primary key of an existing physical table. In the above example, there is a physical table whose primary key is AirportId: the AIRPORT table (and that physical table is the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) of the Group).

The Subtype Group definition allows:

* Subtypes of supertypes that belong to the base table of the Group.
* Subtypes of supertypes that belong to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of the base table of the Group.
* Formula attributes can be used in the group definition, except formulas that use [Udp](https://wiki.genexus.com/commwiki/wiki?3964) calls.

### [**Note**](#Note)

To include inferred subtypes from the extended table of the base table of the Subtype Group in it, it is necessary to define in the Group a subtype of the foreign key through which they are inferred.

### [See also](#See+also)

[When to use Subtypes](https://wiki.genexus.com/commwiki/wiki?2213)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [What are Subtypes?](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/what-are-subtypes-v16?p=5358)
