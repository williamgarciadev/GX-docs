---
title: "SecurityPermission annotation"
source_id: 55422
source_url: https://wiki.genexus.com/commwiki/wiki?55422
genexus_version: "18"
---

# SecurityPermission annotation

Associates specific permissions to methods within an API object. These permissions control access and determine which users or roles are authorized to execute the methods.

### [Syntax](#Syntax)

```
'['SecurityPermission(<Permission_Name>)']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*Permission\_Name*  
         Permission name used to identify which users or roles are authorized to execute the methods that are associated with that specific permission.

### [Description](#Description)

In an API object, there may be different methods that perform different tasks or actions. Some of these actions may require the user making the request to have specific permissions to access them.

For example, in a user management system, there may be methods that allow reading user information, creating new users, or modifying existing information.  
  
This is where the concept of "specific permissions associated with methods" comes in with the SecurityPermission attribute.  
  
When you use SecurityPermission for a particular method, you are setting a security requirement that must be met in order to execute that method. In other words, only those users or roles that have the specific permission associated with the method will be able to access and execute it. If a user does not have the required permission, the system will deny access to that particular method.

### [Sample](#Sample)

Suppose that you have followed steps 1 and 2 listed in [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840).

In the CustomerInfo method of the APICustomer object, which allows you to get the information of a specific customer, you want to define a permission called "ViewCustomerInfo".

To do this, follow the first step mentioned in [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854). Clicking on the name of your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) will open a screen as shown below:

`[imagen omitida: wiki id 55445]`

Then click on MORE OPTIONS>Permissions>ADD and fill Name with ViewCustomerInfo.

When you click on confirm, the following information will appear under Permissions:

`[imagen omitida: wiki id 55446]`

Next, you must assign the permission to the desired role, as shown in [HowTo: Add a Permission to a Role using GAM](https://wiki.genexus.com/commwiki/wiki?17963).

You must then go back to the Service Source of the API object and define the SecurityPermission annotation as shown below:

```
Customer{
    [SecurityPermission("ViewCustomerInfo")]
    CustomerInfo(in:&CustomerId, in:&AccountId, in:&AccountPassword, out:&AccountBalance, out:&AccountStatus)
      => ShowCustomerInfo(&CustomerId, &AccountId, &AccountPassword, &AccountBalance, &AccountStatus);
    }
```

**Notes:**

* In the sample, the value Authorization has been selected for the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) in the API object.
* It is unnecessary to set the Integrated Security Level property to Authorization. The annotation can also be used when the value Authentication is set.
* The SecurityPermission annotation can be combined with the other API object notations.
* The SecurityPermission annotation affects the method directly below it.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).

### [See Also](#See+Also)

[GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723)


|  |
| --- |
| **Backlinks** |
| [API object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?55436) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) |
| [Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |

---
