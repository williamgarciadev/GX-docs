---
title: "Data Provider object"
source_id: 5270
source_url: https://wiki.genexus.com/commwiki/wiki?5270
genexus_version: "18"
---

# Data Provider object

Loads data in a hierarchical structure (from databases, services, fixed values, etc.).

### [Description](#Description)

Applications increasingly need to interact by exchanging data. From an application in a travel agency, ticket requests have to be sent to an airline containing the passengers' information; from another application, a Google service has to be used or merely exchange structured data within the application itself.

In this scenario, handling structured data becomes essential. The format used to represent them is not and will not be homogeneous. While XML is the most widely used format today, other formats are emerging, such as JSON to lighten the transfer, and we don't know what the future holds.

A Data Provider is a 'declarative procedure' used to obtain data in a hierarchical structure, with maximum clarity and minimum effort. How? By making the intention clear, that is to say, the output. Then, by simply indicating the desired format of the output.

`[imagen omitida: wiki id 5973]`

Anything that can be done with a **Data Provider** can also be done with a **[Procedure](https://wiki.genexus.com/commwiki/wiki?6293)**. Both can be seen as processes where there is an Input, a Transformation, and an Output. The difference between them is that in a regular Procedure the focus is on the Transformation language. Meanwhile, in a Data Provider, **the focus is on the Output language**.  
  
For example, if the process consists of reading all customers (Input) and writing an XML file with them (Output), the Procedure is as follows:

```
&XmlWriter.Open(...)
&XmlWriter.WriteStartElement('Clients')
For Each
   &XmlWriter.WriteStartElement('Client')
      &XmlWriter.WriteElement('Code', CustomerId.ToString())
      &XmlWriter.WriteElement('Name', CustomerName)
   &XmlWrite.EndElement()
Endfor
&XmlWriter.EndElement()
&XmlWriter.Close()
```

&XmlWriter is a variable of the GeneXus [XMLWriter](https://wiki.genexus.com/commwiki/wiki?5967,,) data type.

Here is not so easy to quickly 'see' the procedure output. Indeed, it is confusingly embedded inside the code written to obtain it.

Instead, the Data Provider shows clearly the intention:

```
Clients
{
     Client
     {
          Code = CustomerId
          Name = CustomerName
     }
}
```

Then, through the ToXML method, the output could be easily converted into the equivalent XML format:

```
<Clients>
   <Client>
      <Code>1</Code>
      <Name>John Smith</Name>
   </Client>
   <Client>
      <Code>2</Code>
      <Name>Jennifer Lopez</Name>
   </Client>
   ...
</Clients>
```

`[imagen omitida: wiki id 6020]`  
  
The way GeneXus implements hierarchical structures is the [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021). You can see this [example fully implemented](https://wiki.genexus.com/commwiki/wiki?6310).

As you can see, a Data Provider is easier to write and understand, so some tasks will be easier to do with Data Providers than with regular Procedures. Which are they? Those that return structured data. For example:

* Writing XML files, like [Web Services](http://en.wikipedia.org/wiki/Web_service) and [RSS feeds](https://wiki.genexus.com/commwiki/wiki?2337,,).
* Filling SDTs, like the one used to bind with [User Controls](https://wiki.genexus.com/commwiki/wiki?5273), [GXchart](https://wiki.genexus.com/commwiki/wiki?4890) or [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796).
* Filling the structure of BCs, that can be returned in a collection variable and then, going through it, saving in the Database.

### [Examples](#Examples)

Before going into a more formal definition, it can be helpful to present some samples:

#### [Sample 1: Listing today's Invoices ordered by the amount](#Sample+1%3A+Listing+today%27s+Invoices+ordered+by+the+amount)

```
Invoices
{
  Date = today()
  Invoice Order InvoiceAmount
  Where InvoiceDate = today()
  { 
    Id = InvoiceId 
    CustomerId = CustomerId
    CustomerName = CustomerName
    Amount = InvoiceAmount
    Product
    { 
      Id = ProductId
      DetailQuantity = InvoiceDetailQuantity 
      DetailAmount = InvoiceDetailAmount 
    } 
  }
}
```

The output will be an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) with today's date and a collection of items representing those invoices with InvoiceDate = today().

#### [Sample 2: System Constants](#Sample+2%3A+System+Constants)

```
ChartConstants
{
  ChartServer = 'http://www.gxchart.com/drawchart.asp'
  ChartParameters = '...'
}
```

Another example in the same area is loading the Tabs [SDT](https://wiki.genexus.com/commwiki/wiki?10021) needed by the [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796):

```
LoadTabs parm(&CustomerId)
Tabs
{
  Tab
  {
    Code = 'General'
    WebComponent = link(WCustomerGeneral, &CustomerId)
  }
  Tab
  {
    Code = 'Invoices'
    WebComponent = link(WCustomerInvoices, &CustomerId)
  }
}
```

(see [here](https://wiki.genexus.com/commwiki/wiki?4955) for more details).

#### [Sample 3: [RSS feed](https://wiki.genexus.com/commwiki/wiki?2337,,) with today's Invoices](#Sample+3%3A+wiki%3F2337%2CRSS+RSS+feed+with+today%27s+Invoices)

```
rss
{
  version = "2.0"
  channel
  {
    title = "Today's Invoices"
    link = link(ViewTodayInvoices)
    item where InvoiceDate = today()
    {
      title = format('Invoice %1', InvoiceId)
      link = link(ViewInvoice, InvoiceId)
      description = format('Invoice %1 for customer %2, amount %3', InvoiceId, CustomerName, InvoiceAmount)
      author = 'system'
      pubDate = today()
    }
  }
}
```

Now that you understand the spirit of Data Providers, take a look at:

* [Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309)
* [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292)
* [Data Provider: Output](https://wiki.genexus.com/commwiki/wiki?41037)
* [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310)
* [Expose a Data Provider as Web Service](https://wiki.genexus.com/commwiki/wiki?11231)
* [Recursive Data Providers](https://wiki.genexus.com/commwiki/wiki?4891)

And at the following examples and use cases:

* [Example: step by step 'CustomersProvider' Data Provider](https://wiki.genexus.com/commwiki/wiki?6310)
* [Data Provider Use Case: TabbedView usage](https://wiki.genexus.com/commwiki/wiki?4955)
* [Data Provider Use Case: sales invoice into accounting](https://wiki.genexus.com/commwiki/wiki?6342)
* [Example: Data Provider Break](https://wiki.genexus.com/commwiki/wiki?6043)

Data Providers go a step further in 'declaring' instead of 'programming'. The big advantage: the underlying implementation can be changed, and the Data Provider will remain valid. [More on Data Providers philosophy](https://wiki.genexus.com/commwiki/wiki?6259).

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Compound data types](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/compound-data-types-6098937?p=5262)  
`[imagen omitida: wiki id 20668]` [Loading Structured Data Types (SDTs) using Data Providers](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/loading-structured-data-types-sdts-using-data-providers-6104733)


|  |
| --- |
| **Pages** |
| [Collection Name property](https://wiki.genexus.com/commwiki/wiki?41229) | [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) | [Data Provider Element](https://wiki.genexus.com/commwiki/wiki?25096) |
| [Data Provider Element statement](https://wiki.genexus.com/commwiki/wiki?25103) | [Data Provider Subgroup statement](https://wiki.genexus.com/commwiki/wiki?25412) | [Data Provider Use Case: sales invoice into accounting](https://wiki.genexus.com/commwiki/wiki?6342) |
| [Data Provider Use Case: TabbedView usage](https://wiki.genexus.com/commwiki/wiki?4955) | [Data Provider Variable statement](https://wiki.genexus.com/commwiki/wiki?25413) | [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292) |
| [Data Providers philosophy](https://wiki.genexus.com/commwiki/wiki?6259) | [Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501) | [Default clause](https://wiki.genexus.com/commwiki/wiki?25407) |
| [Defining a Data Provider](https://wiki.genexus.com/commwiki/wiki?23658) | [Example: 'CustomersProvider' Data Provider](https://wiki.genexus.com/commwiki/wiki?6310) | [Example: Data Provider Break](https://wiki.genexus.com/commwiki/wiki?6043) |
| [Expose a Data Provider as Web Service](https://wiki.genexus.com/commwiki/wiki?11231) | [HowTo: Use the Infer Structure property of a Data Provider](https://wiki.genexus.com/commwiki/wiki?23651) | [Infer Structure property](https://wiki.genexus.com/commwiki/wiki?23628) |
| [Input clause](https://wiki.genexus.com/commwiki/wiki?25406) | [NoOutput clause](https://wiki.genexus.com/commwiki/wiki?25408) | [One clause in Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25411) |
| [Output property](https://wiki.genexus.com/commwiki/wiki?41037) | [OutputIfDetail clause](https://wiki.genexus.com/commwiki/wiki?25409) | [Paging clauses in Data Provider Group Statement](https://wiki.genexus.com/commwiki/wiki?25410) |
| [Recursive Data Providers](https://wiki.genexus.com/commwiki/wiki?4891) | [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310) |

---
