---
title: "Best Practices for Manual Synchronization"
source_id: 22276
source_url: https://wiki.genexus.com/commwiki/wiki?22276
genexus_version: "18"
---

# Best Practices for Manual Synchronization

When choosing the first option of [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266), the developer has to code all the objects which manage the interaction with the server.

A sample code for manual synchronization can be seen here: [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543).

This document states best practices for programming these objects.

### [1. Clear after using the [SDT](https://wiki.genexus.com/commwiki/wiki?2427) [collections](https://wiki.genexus.com/commwiki/wiki?6296)](#1.+Clear+after+using+the+wiki%3F2427%2CSDT+SDT+wiki%3F6296%2CImplementing%2BSDT%2Bcollections+collections)

Using the clear function of the SDT at the end of the for-endfor block will free memory allocated for that collection. If this is not done, the OS will keep memory allocated for that collection even though the routine is not using it any more.

For example:

```
&httpclient.Execute(!'GET', !'GetAllDepartments?fmt=json')
&departmentslist.FromJson(&httpclient.ToString())
For &department in &departmentslist
new
  DepartmentId = &department.DepartmentId
  DepartmentName = &department.DepartmentName
endnew
&i+= 1
endFor
&departmentsList.Clear()
```

### [2. Different [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) for each Local Table](#2.+Different+wiki%3F6293%2CCategory%253AProcedure%2Bobject+Procedure+for+each+Local+Table)

To ensure that all the memory allocated for a table synchronization process is released, it is recomended to separete each table synch on a different Procedure. This will force the OS to release all the memory allocated used for one table before synchronizing the next one. This can be done because once you inserted the data on the local database it is unlikely that you are going to use the SDT collection and httpclient for that table again.

### [3. Use [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)](#3.+Use+wiki%3F5846%2CToc%253ABusiness%2BComponent+Business+Component)

Using Business Components instead of New - EndNew code blocks is better in order to have the [KB](https://wiki.genexus.com/commwiki/wiki?2428) ready to pass from Manual to Automatic Synchronization with less problems.

This best practice applies only for the [Events Tables](https://wiki.genexus.com/commwiki/wiki?22269), because all the data that are going to be inserted via [BC](https://wiki.genexus.com/commwiki/wiki?2416) (in Procedure or [WW](https://wiki.genexus.com/commwiki/wiki?20840)) is the one that in Automatic Synchronization is going to be replicated on the server. So, this best practice can be taken in consideration if your application is going to convert to [Automatic Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) at any time in the future.

### [4. Conceptually divide tables in Master and Event Tables](#4.+Conceptually+divide+tables+in+Master+and+Event+Tables)

Having this virtual division done will also help to be able to switch from one synchronization criteria back and forward. Remember that the data received from the server is usually the Master Tables and the ones added locally and sent to the server are the Event Tables.

This division is going to make your code more maintainable and is easier to see the flow of the information on your system.

### [5. Use Paging when synchronizing](#5.+Use+Paging+when+synchronizing)

To optimize the memory resources of the devices this is quite crucial. Using paging on the request of master Data can save lots of space on the local memory of the device's OS.

#### [How to do it?](#How+to+do+it%3F)

Note: This sample suposes that the variable based on [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) has already been initialized.

##### [Server side](#Server+side)

[Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270): with the total quantity of registers of the Product Table.

```
Product [NoOutput] Order ProductId
{
    &Total = &Total + 1
}
SDTTotal
{
    Total = &Total
}
```

Data Provider: which given a page and quantity returns a subset of registers.

```
SDTProduct [Count = &PageSize] [Skip = (&PageNumber - 1) * &PageSize]
{
ProductId
ProductName
ProductPrice = ProductPrice.ToString()
ProductStock
ProductImage = ProductImage.ImageURI
DepartmentId
}
```

##### [Client Side](#Client+Side)

Procedure: Code to Get the Products in pages.

```
&httpclient.Execute(!'GET', !'GetTotalProducts?fmt=json')
&SDTTotal.FromJson(&httpclient.ToString())

&TotalProducts = &SDTTotal.Total

&PageSize = 10
&TolalPages = (&TotalProducts / &PageSize)
If &TolalPages > &TolalPages.Truncate(0) 
&TolalPages = &TolalPages.Truncate(0)  + 1
Endif

For &PageId = 1 to &TolalPages.Truncate(0) step 1
    &httpclient.Execute(!'GET', !'GetAllProducts?Pagenumber='+ &PageId.ToString().Trim() + '&Pagesize=' + &PageSize.ToString().Trim() + '&fmt=json')
    &productslist.FromJson(&httpclient.ToString())
    For &product in &productslist
        new
            ProductId = &product.ProductId
            ProductName = &product.ProductName
            ProductPrice = &product.ProductPrice.ToNumeric()
            ProductStock = &product.ProductStock
            DepartmentId = &product.DepartmentId
        endnew
    endfor
endfor
commit
```


|  |
| --- |
| **Backlinks** |
| [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) | [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
