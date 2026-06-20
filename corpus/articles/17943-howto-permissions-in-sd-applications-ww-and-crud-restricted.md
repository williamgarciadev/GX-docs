---
title: "HowTo: Permissions in SD Applications, WW and CRUD Restricted"
source_id: 17943
source_url: https://wiki.genexus.com/commwiki/wiki?17943
genexus_version: "18"
---

# HowTo: Permissions in SD Applications, WW and CRUD Restricted

#### [Problem description](#Problem+description)

Suppose you have a Smart Devices Application which allows users to see all the products a company distributes.  
Imagine that a security requirement is that for both, navigating the products catalog and updating the data, authorization is required.  
Besides, the authorization permissions for the former are not the same as for the latter.

Objects of the application:

* Product [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) ([Business Component](https://wiki.genexus.com/commwiki/wiki?5846))
* Dashboard1 ([Dasboard object up to GeneXus Evolution 3](https://wiki.genexus.com/commwiki/wiki?46149,,)) which has the following item:
  + WorkWithDevicesProduct ([WWSD](https://wiki.genexus.com/commwiki/wiki?15974) object which lists all the products). By selecting one item of this list you can view the detail of the product; and update, or delete the product if desired. There is also the possibility of adding a new product by using the menu of this object.

Only authorized users can execute the WorkWithDevicesProduct object (see the products list and products detail), and other users with different permissions, can execute insert, update, delete over the "products" Business Component.  
  
Note that the actions in WWSD panels (insert, update, delete) are related directly to the Business Component associated with the WWSD and not the WWSD itself. That means that, if you apply [Work With Pattern for Smart Devices](https://wiki.genexus.com/commwiki/wiki?9413,,) to a transaction ("Product"), the "Product" transaction is automatically saved as Business Component exposed as REST web service. In order to control permissions over the actions insert, update, delete, you need to declare permissions over the Business Component itself.

On the other hand, the permissions over the list and view of the item's list are managed in the WWSD object.

### [Solution](#Solution)

One possibility is to set [Default Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) to "Authentication" at version level, and configure [Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) to "Authorization" for "WorkWithDevicesProduct" object and "Product" transaction.

`[imagen omitida: wiki id 17947]`  
Figure 1.

`[imagen omitida: wiki id 17948]`  
Figure 2.

Otherwise, [Default Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) at version level can be set to "Authorization" and "WorkWithDevicesProduct" and "Product" transaction objects can take the property value from the environment.

Afterwards, you need to create two different roles, one of them (Role1) will enable users to execute the products list, see the products detail, and update the data also (insert, update and delete products).  
Another role (Role2) will enable users to execute the products list but deny the permissions over data update, insert, and delete.

See the following figures for the definition of the roles:

`[imagen omitida: wiki id 17949]`  
Figure 3. Role1 definition.

`[imagen omitida: wiki id 17950]`  
Figure 4. Role2 definition.

In order to give the user permissions to insert a new product, you need to grant "product\_services\_insert" permission, where "product" is the Permission Prefix Property value set in Product transaction (see figure 2).

The same idea with the update and delete permissions, "product\_services\_update" and "product\_services\_delete" permissions need to be defined.

These permissions ("product\_services\_insert", "product\_services\_update", and "product\_services\_delete") require "product\_services\_execute" permission (that is to say, if this permission is not allowed, none of the others can be).

"product\_services\_execute" is the permission to GET the Business Component data.

Note that [Permission Prefix Property](https://wiki.genexus.com/commwiki/wiki?17571) of WorkWithDevicesProduct is set by default to the "Product services" value (see Figure 1).

This means that if the "product\_services\_execute" permission is allowed (which implies that the user can GET the Business Component data), executing the WorkWithDevicesProduct *by default* will also be possible. That's why users with Role2 will be able to execute WorkWithDevicesProduct and navigate through the products list.

#### [Conclusion](#Conclusion)

As a consequence of the configuration shown, users with Role2 will not be allowed to update products, and users with Role1 will be able to do it (to be strict, if a user has any role where the permissions are denied, they will not be able to update data, see [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) for more details).

Users with Role1 as well as users with Role2 have the "product\_services\_execute" permission, so both will be able to execute the Product Business Component in order to GET data (read data). Both will be able to execute "WorkWithDevicesProduct" object because of the Permission Prefix property value of this object.

#### [**Important notes:**](#Important+notes%3A)

1. [Permission Prefix Property](https://wiki.genexus.com/commwiki/wiki?17571) of WorkWithDevicesProduct is set by default to the "Product\_services" value.

This is in order to make the administration of permissions easier. It's assumed that a user who will be able to GET (read) the Business Component data, will also be able to execute the WWSD related to this Business Component. But this is a default option and can be changed as Approach #2 explains at the bottom of this page.

2. The  "<BusinessComponentPermissionPrefix>\_services\_mode" permissions are defined because the transaction in case of SD applications is executed as a Business Component exposed as [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573). See [Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916) for more details.

#### [Approach # 2:](#Approach+%23+2%3A)

If you want to discriminate the permission to execute the Business Component and GET the data, from executing the WorkWithDevicesProduct object, you may do the following:

Assign a different [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) for WorkWithDevicesProduct object (other than "product\_services"). See the following figure where the permission prefix assigned is "wwdevicesproducts":

`[imagen omitida: wiki id 17952]`  
Figure 5.

Define a role where the "wwdevicesproducts\_execute" permission is denied and the "product\_services\_execute" is allowed. The users assigned to this role will be able to GET the Business Component data, but not to execute the WorkWithDevicesProduct object.

`[imagen omitida: wiki id 17953]`  
Figure 6.

### [See Also](#See+Also)

[Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916)  
[GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) | [HowTo: Permissions in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17925) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
