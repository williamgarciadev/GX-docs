---
title: "Using Data Providers in Other GX Objects"
source_id: 5310
source_url: https://wiki.genexus.com/commwiki/wiki?5310
genexus_version: "18"
---

# Using Data Providers in Other GX Objects

As you may already know, the [output of a Data Provider](https://wiki.genexus.com/commwiki/wiki?41037) is an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) or [BC](https://wiki.genexus.com/commwiki/wiki?5846) (that could be later -even immediately- converted to another format such as XML). The only output formats supported are SDT and BC. However, not only a simple SDT or BC can be returned, but also a collection of them.

Using a Data Provider in another [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) is similar to using a Procedure that returns an SDT or BC to the caller.

### [Example](#Example)

An easy way to implement an [RSS](https://wiki.genexus.com/commwiki/wiki?2337,,) feed is defining a Procedure that calls a Data Provider to populate the data and returns an XML with the RSS format:

```
&rss = rss() // RSS() is a DP that load the data
&response.addstring(&rss.toxml(true))
```

Notes:

* the proc must be defined as Main with Call Protocol HTTP.
* &rss is of type [RSS SDT](https://wiki.genexus.com/commwiki/wiki?6898,,).
* &response is of type HTTPResponse.

### [When the output is a Business Component](#When+the+output+is+a+Business+Component)

Usually, the Data Provider Output is an SDT, but some times it is very convenient to use a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) as the Output. For example for the following Data Provider 'CustomersProvider'  the Output is the 'Customer' BC, the 'Collection' property is set to 'True', and the 'Collection Name' property is set as 'customers' (exactly the name given to the root Group in the Source).

`[imagen omitida: wiki id 5974]`

Notes

* Given this DP will return more than one Customer, the 'Collection' property is set to 'True', and the 'Collection Name' property is set as 'customers' (exactly the name given to the root Group in the Source).

```
customers
{
  customer
  {
     CustomerId = 400
     CustomerName = 'Mike Hemingway'
  }
  customer
  {
     CustomerId = 401
     CustomerName = 'Jeniffer Faulkner'
  }
}
```

So, in a procedure, we could define a '&myCustomersBC' variable with 'Customer' BC data type and with the 'Collection' property set to True (see [Collection variables](https://wiki.genexus.com/commwiki/wiki?6352)):

`[imagen omitida: wiki id 5975]`  
  
Then, inside the object we could write:

```
&myCustomersBC = CustomersProvider()

For &customer in &myCustomersBC
    &customer.Save()
endfor
```

That is, the two-item collection returned by the 'CustomerProvider' Data Provider is scanned and each time, in the '&customer' variable (of the 'Customer' BC data type) each item is loaded and a Save is done, having a new record on the database customers table.

**Important**:  
The Data Provider only fills the associated structure of the BC, as would be done by hand in a Procedure, so that, the resulting BC mode is 'INSERT'. In other words, a Data Provider cannot make a 'LOAD' operation. That is to say, the[Save() method](https://wiki.genexus.com/commwiki/wiki?23229) applied to the BC returned by a Data Provider will attempt to create **new records** in the database.

It isn't necessary to define the '&myCustomersBC' variable, you just can write (see [For in command](https://wiki.genexus.com/commwiki/wiki?6359)):

```
For &customer in CustomersProvider()
       &customer.Save()​
​​​​​​endfor
```

### [Parameters](#Parameters)

The Data Provider also supports receiving parameters (all parameters are "IN" parameters).

Example:

```
&CustomerId = 1
&Tabs = Tabs(&CustomerId)
```

Suppose that you define a &Tabs variable of TABS type, which is an SDT associated with the [Output property](https://wiki.genexus.com/commwiki/wiki?41037) of the Data Provider named "Tabs".

### [How to work with the items of a collection returned by a Data Provider](#How+to+work+with+the+items+of+a+collection+returned+by+a+Data+Provider)

You just write the following:

```
For &Var in Dataprovider(parameters list)
    &Var.SomeElement
Endfor
```

This avoids having to define a [collection variable](https://wiki.genexus.com/commwiki/wiki?6352) and writing the following:

```
&Collection = Dataprovider(parameters list)

For &Var in &Collection
    &Var.SomeElement
Endfor
```

See also [For in command](https://wiki.genexus.com/commwiki/wiki?6359).

### [Example](#Example)

Another example could be to show a tree from a transaction structure through an SDT.

```
 TreeNodeCollection
{
TreeNode
  where CategoryParentId = &CategoryId when not &CategoryId.IsEmpty()   
  {
  Id = CategoryId.ToString()
  Name = CategoryName
  Nodes = CategoriesDP(CategoryId)
 }
 TreeNode
  where CategoryId = &CategoryId
  {
  Id = CategoryItemId.ToString()
  Name = CategoryItemName  
 }
}
```


|  |
| --- |
| **Backlinks** |
| [Collection property](https://wiki.genexus.com/commwiki/wiki?41179) | [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [Example: 'CustomersProvider' Data Provider](https://wiki.genexus.com/commwiki/wiki?6310) |
| [Output property](https://wiki.genexus.com/commwiki/wiki?41037) |

---
