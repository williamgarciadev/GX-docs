---
title: "HowTo: Implement GAM permissions in Transaction's Modes"
source_id: 18046
source_url: https://wiki.genexus.com/commwiki/wiki?18046
genexus_version: "18"
---

# HowTo: Implement GAM permissions in Transaction's Modes

The purpose of this article is to explain how to configure permissions over [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s modes so that only authorized users can view the data (by executing the Transaction in Display mode) or Insert, Update, or Delete data by executing the Transaction in the corresponding modes.

### [How to do it](#How+to+do+it)

[GAM](https://wiki.genexus.com/commwiki/wiki?24746) defines [automatic permissions](https://wiki.genexus.com/commwiki/wiki?17916) to execute the Transaction (in Display mode) and one permission for each mode: Insert, Update or Delete.

The names of the permissions are determined from the [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) value set at the Transaction level (see Figure 1).

In runtime, these permissions are checked automatically and the GeneXus user just needs to declare the [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) in the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

The process at execution time consists of validating if the user has the rights to execute the Transaction object. In this case, GAM checks that the user has a *<prefix>\_execute* permission (where prefix is the [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) defined for the Transaction). So, the *<prefix>\_execute* permission enables the user to display the data of the Transaction (Display mode).

If the user executes an action over the Transaction (Insert, Update or Delete) another permission will be required:

* *<prefix>\_Insert*
* *<prefix>\_Update*
* *<prefix>\_Delete*

In fact, there is a permission that "groups" the other permissions (see [Full Control Permissions](https://wiki.genexus.com/commwiki/wiki?17664) for more details):

```
<prefix>.FullControl
```

* *<prefix>\_Execute*
* *<prefix>\_Insert*
* *<prefix>\_Update*
* *<prefix>\_Delete*

### [Samples](#Samples)

Suppose you have a "Product" [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), where some users will have access rights to execute it, but not to insert, update, or delete data.

Just follow these steps:

#### [**Step 1**](#Step+1)

Check the following properties values:

* [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) = True (at the KB [version level](https://wiki.genexus.com/commwiki/wiki?7860))
* [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authorization (at the KB version level or at least for the Transaction)
* [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) at the Transaction level is set to any value (in this example it is set to "Product")

###### Figure 1.

#### **Step 2**

Define a role where the permissions mentioned above are specified with their corresponding [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603).

##### Figure 2.

#### **Step 3**

The users need to be associated with the role created.

##### Figure 3.

In this example, the WW pattern has been applied to the Product Transaction.

The user associated with the role previously defined, will be able to execute the WWPproduct Web Panel, and select products from the list in order to view the data.  
  
When the user tries to update or delete an existing product, or insert a new product, the [Not Authorized Object for Web](https://wiki.genexus.com/commwiki/wiki?17551,,) object will be called, as seen in the following figures (if the Transaction does not receive KEY and Mode as parameters, the permission error is shown using the Error Viewer).

###### Figure 4.

###### Figure 5.

###### Figure 6.

### [See Also](#See+Also)

[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664)  
[GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) |

---
