---
title: "HowTo: Permissions in SD Applications, CRUD Restricted"
source_id: 17935
source_url: https://wiki.genexus.com/commwiki/wiki?17935
genexus_version: "18"
---

# HowTo: Permissions in SD Applications, CRUD Restricted

Suppose you have a Smart Devices Application which allows users to see all the products a company distributes.

The application will be used by employees of the company (who have authorization to add, update, or delete products, and change their prices), and will be used by users who are interested in buying those products and are authorized just to navigate through the products list.

Objects of the application:

* Dashboard1 ([Menu object](https://wiki.genexus.com/commwiki/wiki?16321)) which has the following item:
  + WorkWithDevicesProduct ([WW](https://wiki.genexus.com/commwiki/wiki?20840) object which lists all the products). By selecting one item of this list you can view the detail of the product; and update, or delete the product if desired. There is also the possibility of adding a new product by using the menu of this object.
* Product [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) ([Business Component](https://wiki.genexus.com/commwiki/wiki?5846)).

### [Problem Description](#Problem+Description)

The application as a whole requires [authentication](https://wiki.genexus.com/commwiki/wiki?18456,,), so only authenticated users can access the WorkWithDevicesProduct item of the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321). When clicking on this option, authentication is required. As a consequence, any authenticated user can display the products list and see the product detail by clicking on any item of the list. That is to say that no special permission is required to execute "WorkWithDevicesProduct", because authorization is not going to be checked.

But in order to add a new product, update or delete an existing product, authorization is required.

So only authorized users can execute actions (add, update, delete) over the "Products" Business Component.

### [Solution](#Solution)

The [Default Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) value at version level can be set to "Authentication", if only specific objects need authorization, and are the minority.

The property [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214) of the WorkWithDevicesProduct object is set to "Use Environment property value" = Authentication.

`[imagen omitida: wiki id 17927]`  
Figure 1.

But you need to set Integrated Security Level Property of "Product" Transaction to Authorization value.

`[imagen omitida: wiki id 17928]`  
Figure 2.

Define a role, named "Role1" in the example, with the following permissions:

`[imagen omitida: wiki id 17929]`  
Figure 3.

Look at figure 3 to see the permissions defined. The goal is to define permissions in order to allow / deny users the privilege to execute the Product Business Component modes (insert, update, delete), regarding that this Business Component is executed through a SD application (not a web application).

In order to give the user permissions to insert a new product, you need to grant product\_services\_insert permission, where "product" is the [Permission Prefix Property](https://wiki.genexus.com/commwiki/wiki?17571) value set in Product transaction (see figure 4).

See [How to: Add a permission to a role](https://wiki.genexus.com/commwiki/wiki?17963) for information on how to add permissions to roles.

`[imagen omitida: wiki id 17931]`  
Figure 4.

The same idea with update and delete permissions, "product\_services\_update" and "product\_services\_delete" permissions need to be defined.

These permissions ("product\_services\_insert", "product\_services\_update", and "product\_services\_delete") requiere "product\_services\_execute" permission (that is to say, if this permission is not allowed, none of the others can be).

"product\_services\_execute" is the permission to GET the Business Component data.

Take into account the Default [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) at application level, as shown in figure 5.

`[imagen omitida: wiki id 17934]`  
Figure 5.

### [Conclusion](#Conclusion)

As a consequence of this configuration, only authenticated users can access the WorkWithDevicesProduct, but no particular authorization is needed to execute it. So, any authenticated user can display the list of products and select an item to view the detail.

Nevertheless, only users with "Role1" role can update, delete, or add new products. If another user tries to execute any of these actions, the following message appears in
[Android](https://wiki.genexus.com/commwiki/wiki?14453) applications:

`[imagen omitida: wiki id 17933]`  
Figure 6.

To be strict, as these permissions are restricted at application level (see figure 5), only users who are assigned to roles where these permissions are allowed, will have rights to execute the different modes of the Business Component; unless they have any role where any of these permissions is denied (see [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) for more details).

**Note**: The "<BusinessComponentPermissionPrefix>\_services\_mode" permissions are defined because the transaction, in case of SD applications, is executed as a Business Component exposed as REST web service. See [Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916) for more details.

### [See Also](#See+Also)

[GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) | [HowTo: Permissions in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17925) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
