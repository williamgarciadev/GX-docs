---
title: "Data Provider Use Case: TabbedView usage"
source_id: 4955
source_url: https://wiki.genexus.com/commwiki/wiki?4955
genexus_version: "18"
---

# Data Provider Use Case: TabbedView usage

The [procedural](https://wiki.genexus.com/commwiki/wiki?6293) way of loading an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) (like the one needed in the [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796)) is:

```
Event Start
    ...
    &Tabs = new()
    &TabsItem = new()
    &TabsItem.Code = 'General'
    &TabsItem.Description = 'General info'
    &TabsItem.Link = link(ViewCustomer, CustomerId, 'General'
    &TabsItem.WebComponent = create(CustomerGeneral, CustomerId)
    &Tabs.add(&TabsItem)
    &TabsItem = new()
    &TabsItem.Code = 'Invoices'
    &TabsItem.Description = 'Invoices'
    &TabsItem.Link = link(ViewCustomer, CustomerId, 'Invoices'
    &TabsItem.WebComponent = create(CustomerInvoices, CustomerId)
    &Tabs.add(&TabsItem)
    ...
    TabWC.Object = Create(TabbedView, &Tabs)
EndEvent
```

Using [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270), the declarative way is:

```
LoadCustomerTabs
Tabs
{ 
   TabOptionsItem
   {
      Code           = 'General'
      Description    = 'General info'
      Link           = link(ViewCustomer, CustomerId, 'General'
      WebComponent   = create(CustomerGeneral, CustomerId)
   } 
   TabOptionsItem
   {
      Code           = 'Invoices'
      Description    = 'Invoices'
      Link           = link(ViewCustomer, CustomerId, 'Invoices'
      WebComponent   = create(CustomerInvoices, CustomerId)
   }
}
```

So the Event Start becomes:

```
Event Start
   &Tabs = LoadCustomerTabs()
   TabWC.Object = Create(TabbedView, &Tabs)
Endevent
```


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796) |

---
