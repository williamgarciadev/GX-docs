---
title: "HowTo: Permissions in Native Mobile Applications"
source_id: 17925
source_url: https://wiki.genexus.com/commwiki/wiki?17925
genexus_version: "18"
---

# HowTo: Permissions in Native Mobile Applications

Suppose you have a very simple Native Mobile Application which allows users to see all the products a company distributes.

One possible requirement is that the same application is used by employees of the company (who have the authorization to add, update, or delete products, and change their prices), and will also be used by users who are interested in buying those products and are allowed just to navigate through the products list. Authorization is needed to update products, but not to navigate the product's catalog.

Another different requirement may be that authorization is needed for both cases, and the authorization for each action (navigate the products catalog and update the data) has different permissions related to it.

### [Steps](#Steps)

The following steps show you how to achieve this, regarding permissions in the application, and how to solve it using [GAM](https://wiki.genexus.com/commwiki/wiki?14960).

Objects of the application:

* Product [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) ([Business Component](https://wiki.genexus.com/commwiki/wiki?5846))
* [Dashboard1](https://wiki.genexus.com/commwiki/wiki?36769) which has the following item:
  + WorkWithProduct ([Work With object](https://wiki.genexus.com/commwiki/wiki?15974) which lists all the products). By selecting one item of this list you can view the detail of the product; and update, or delete the product if desired. There is also the possibility of adding a new product by using the menu of this object.

#### **Case 1.** Insert, Update, Delete are restricted actions, but the list of products does not require authorization to execute

See [How to: Permissions in SD applications, CRUD restricted](https://wiki.genexus.com/commwiki/wiki?17935)

#### [**Case 2.** Insert, Update, Delete are restricted actions as well as the navigation of the products list](#Case+2.+Insert%2C+Update%2C+Delete+are+restricted+actions+as+well+as+the+navigation+of+the+products+list)

See [How to: Permissions in SD applications, WW and CRUD restricted](https://wiki.genexus.com/commwiki/wiki?17943)

### [See Also](#See+Also)

[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664)  
[GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
