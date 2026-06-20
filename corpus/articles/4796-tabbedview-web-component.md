---
title: "TabbedView Web Component"
source_id: 4796
source_url: https://wiki.genexus.com/commwiki/wiki?4796
genexus_version: "18"
---

# TabbedView Web Component

Quite often, while developing a form you may need to organize its data into Tabs. For example, in the [Web Based Work With Pattern](https://wiki.genexus.com/commwiki/wiki?1837,,), the View panel (like this page itself) uses a Tabbed View. The problem is that until now it was necessary to have codes for handling tabs in every View panel, but in GeneXus all these codes can be encapsulated in a single Web Component. The GeneXus Work With Pattern already provides a web component named TabbedView that can be used in other objects.

### [How to use it](#How+to+use+it+)

Suppose you need to implement a tabbed view for the Customer transaction, with the following tabs:

* General. Shows just the general information, like Name and Address;
* Invoices. Shows the Customer's Invoices;
* Payments. Shows the Customer's Payments.

The first step is to create a Web Component for each Tab (in this case named: CustomerGeneral, CustomerInvoices and CustomerPayments). This is necessary because the tabbed view should only have one Tab loaded at a time in order to avoid very heavy pages.

The second step is to create the ViewCustomer Webpanel and drag into the WebForm the TabbedView web component (it comes with the Work With Pattern, so just generate one to have it in the KB). The TabbedView Web Component has two parameteres: an SDT representing available Tabs and an identifier telling you which of these tabs are active. The SDT is a collection of a structure as described below.

```
TabOptionsItem [IsCollection]  
{  
   Code  
   Description  
   Link  
   WebComponent  
}
```

The collection must be loaded with every available Tab, before calling the TabbedView. To load an item in the collection, members must have the following information:

* Code = a unique item identifier. It identifies the item among all the other items in the collection
* Description = a brief description of what the tab is intended for.
* Link = the URL of the object to be called if the tab is selected (usually obtained by using the Link method of a Web object)
* WebComponent = the URL of the Web Component that must be shown when the item is selected

For instance, in the ViewCustomer objects the SDT can be loaded with this information:

```
Rules:  
Parm(in:CustomerId, in:&TabCode);

Event Start  
   ...  
   &Tabs = new()  
   &TabsItem.Code         = 'General'  
   &TabsItem.Description  = 'General info'  
   &TabsItem.Link         = ViewCustomer.Link(CustomerId, 'General')  
   &TabsItem.WebComponent = CustomerGeneral.Link(CustomerId)  
   &Tabs.add(&TabsItem)  
    ...

TabWC.Object = TabbedView.Create(&Tabs, &TabCode)  
Endevent
```

Once the TabbedView is called, it builds the tabs (handles selected, unselected, drawings, etc. and, for the active tab, it uses the information in the WebComponent member to create the active Web Component.

(see [Data Provider Use Case: TabbedView usage](https://wiki.genexus.com/commwiki/wiki?4955) for a simpler code).

### [How does the TabbedView Web Component work?](#How+does+the+TabbedView+Web+Component+work%3F)

The TabbedView Web Component is, of course, a standard GeneXus Web Component that uses a GeneXus feature to encapsulate tab-handling codes. This GeneXus feature lets you create a [Web Component at runtime](https://wiki.genexus.com/commwiki/wiki?5404) based on a link to it, as follows:

```
&WebComponentUrl = &Tab.WebComponent  
Control.Object = CreateFromURL(&WebComponentUrl)
```


|  |
| --- |
| **Backlinks** |
| [CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509) | [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [Data Provider Use Case: TabbedView usage](https://wiki.genexus.com/commwiki/wiki?4955) |
| [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404) | [HistoryManager User Control](https://wiki.genexus.com/commwiki/wiki?22724) |

---
