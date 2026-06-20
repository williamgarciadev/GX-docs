---
title: "RestMethod annotation"
source_id: 50508
source_url: https://wiki.genexus.com/commwiki/wiki?50508
genexus_version: "18"
---

# RestMethod annotation

Specifies the method of a declared service in an [API object](https://wiki.genexus.com/commwiki/wiki?46151).

### [Syntax](#Syntax)

```
'['RestMethod(<Method>)']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*Method*  
         [HTTP method](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50500,,) indicating the operation to perform.

### [Description](#Description)

The method of a service is [GET](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50500,,) by default. If you don't want to use GET, you can use this annotation to specify the method that will provide the service.

### [Sample](#Sample)

Enter a new customer.  
Consider the following [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) defined as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

```
Customer
{
     CustomerId*     (Autonumber property = Yes)
     CustomerName
     CustomerLastName
}
```

Create a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) called InsertOneCustomer and define the following:

Variables:

```
&Customer                (Type: Customer)
&CustomerId              (Type:Attribute:CustomerId)
&CustomerName            (Type:Attribute:CustomerName)
&CustomerLastName        (Type:Attribute:CustomerLastName)
&Messages                (Type: Messages, GeneXus.Common)
```

Rules:

```
Parm(in:&CustomerId, in:&CustomerName, in:&CustomerLastName, out:&Messages);
```

Source:

```
&Customer.CustomerId = &CustomerId
&Customer.CustomerName = &CustomerName
&Customer.CustomerLastName = &CustomerLastName

if &Customer.Insert()
   commit
Else
   rollback
Endif
&Messages = &Customer.GetMessages()
```

Create an API Object called APICustomer and define the following:

Variables:

```
&CustomerId         (Type:Attribute:CustomerId)
&CustomerName       (Type:Attribute:CustomerName)
&CustomerLastName   (Type:Attribute:CustomerLastName)
&Messages           (Type: Messages, GeneXus.Common)
```

Service Source:

```
Customer
{
     [RestMethod(POST)]
     InsertCustomer(in:&CustomerId, in:&CustomerName, in:&CustomerLastName, out:&Messages) =>InsertOneCustomer(&CustomerId,&CustomerName, &CustomerLastName, &Messages);
}
```

Notes:

* The RestMethod annotation can be combined with the [RestPath](https://wiki.genexus.com/commwiki/wiki?50360) annotation; for example: [RestMethod(PUT),RestPath ("/Customer/{&CustomerId}/{&CustomerName}")].
* The RestMethod annotation must be written immediately before the service declaration.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,).


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) | [API object - Delete service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49781) | [API object - Delete service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60083) |
| [API object - Insert service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49778) | [API object - Insert service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60081) | [API object - Update service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49780) | [API object - Update service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60082) |
| [API object Syntax](https://wiki.genexus.com/commwiki/wiki?50879) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |
| [RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360) |

---
