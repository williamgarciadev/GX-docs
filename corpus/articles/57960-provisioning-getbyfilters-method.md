---
title: "Provisioning.GetByFilters method"
source_id: 57960
source_url: https://wiki.genexus.com/commwiki/wiki?57960
genexus_version: "18"
---

# Provisioning.GetByFilters method

Allows searching for Mini Apps in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) based on certain filter criteria. This method is offered by the [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959) through its Provisioning External Object.

When registering a Super App in the Mini App Center, several attributes can be declared and then instantiated when reviewing a Mini App Version. This method looks for exact matches for the given filters.

### [Syntax](#Syntax)

```
GetByFilters(&filters, &start, &count): collectionOf(MiniAppInformation)
```

Parameters:

●    &Filters: collectionOf(MiniAppFilter) -The filters to search for.  
●    &Start: Integer -0-based index from which elements will be returned.  
●    &Count: Integer - maximum number of returned elements (0 means all).

### [GeneXusSuperApps.MiniAppFilter: SDT](#GeneXusSuperApps.MiniAppFilter%3A+SDT)

●    **Field:** VarChar (40). Allows configuring the field by which records will be filtered.  
●    **Operator:** GeneXusSuperApps.MiniAppFilterOperator. Allows configuring the type of condition to apply in the filter.  
●    **Values:** Collection<VarChar (200). Allows specifying the values for which the filter will be applied.

`[imagen omitida: wiki id 57959]`

### [GeneXusSuperApps.MiniAppFilterOperator: Domain](#GeneXusSuperApps.MiniAppFilterOperator%3A+Domain)

Values:  
●    Equals  
●    Not Equals  
●    Greater  
●    Greater or Equals  
●    Less  
●    Less o Equals  
●    Contains  
●    In

### [Sample](#Sample)

In the example below, you want to retrieve Mini Apps whose name contains the word "Coffee" and whose country is Uruguay or Argentina.

```
&MiniAppFilter = new()
&MiniAppFilter.Field = !'name'
&MiniAppFilter.Operator = MiniAppFilterOperator.Contains
&MiniAppFilter.Values.Add(!'Coffee')
&MiniAppFilters.Add(&MiniAppFilter)

&MiniAppFilter = new()
&MiniAppFilter.Field = !'Country'
&MiniAppFilter.Operator = MiniAppFilterOperator.In
&MiniAppFilter.Values.Add(!'Uruguay')
&MiniAppFilter.Values.Add(!'Argentina')
&MiniAppFilters.Add(&MiniAppFilter)
&MiniApps = GeneXusSuperApps.Provisioning.GetByFilters(&MiniAppFilters,&start,&count)
```

Learn [how to configure attributes in Super Apps](https://wiki.genexus.com/commwiki/wiki?53316) and [instantiate attribute values at the Mini App Version level](https://wiki.genexus.com/commwiki/wiki?53318).

### [Considerations](#Considerations)

●    Two filters cannot be combined with OR. Every filter included in a call will be considered as AND regarding the previous one.  
●    Some field names are standard and accept only certain operators:

|  |  |  |
| --- | --- | --- |
| **Filter** | **Apply** | **Valid Operators** |
| id | ID | Equals, Not Equals, Contains |
| text | Name and/or Description | Equals, Not Equals, Contains |
| tag | Keywords | Equals, Not Equals, Contains |
| name | Name | Equals, Not Equals, Contains |
| description | Description | Equals, Not Equals, Contains |
| highlighted | Highlighted | Equals, Not Equals |
| center | Location | Equals |
| radius | Location | Equals |
| organization | Mini App Organization Name | Equals, Not Equals, Contains |
| type | Type | Equals, Not Equals, Contains |

### [Availability](#Availability)

This method is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [Highlighted Mini Apps](https://wiki.genexus.com/commwiki/wiki?56095) |
| [Provisioning external object in GeneXusSuperApps module](https://wiki.genexus.com/commwiki/wiki?58519) |

---
