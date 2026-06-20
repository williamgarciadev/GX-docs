---
title: "HowTo: Filter data by user using the GAM API"
source_id: 15387
source_url: https://wiki.genexus.com/commwiki/wiki?15387
genexus_version: "18"
---

# HowTo: Filter data by user using the GAM API

This article shows you a basic example of [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) use.

Imagine a scenario where distributors of a company enter purchase orders through their devices.  
  
As there's only one "Purchase Orders" table in the system, the company wants to identify the salesman who entered the order. So the User Identification (*UserId* attribute) of the salesman is also stored in the "Purchase Orders" table.

The security information (Users, User information, [GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569), [GAM Security Policies](https://wiki.genexus.com/commwiki/wiki?18521), etc) is stored in the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568).

A system requirement is that when the users navigate within the "Work With Purchase Orders", they have to access only the information entered by them and not the information entered by others. So you need to get the data of a specific user (the user who is logged in).

### [How to solve it:](#How+to+solve+it%3A)

**1.** Set in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) = True

**2.** Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) for this example:

```
PurchaseOrder
{
  PurchaseOrderId*
  PurchaseOrderDate
  PurchaseOrderDescription
  UserId
}
```

The attribute named *UserId*is based on the GAMUserLogin domain. This attribute is going to store the identification of the user who enters the purchase order into the system. There are several ways to reference the user's id in the GAM database. Read [HowTo: Reference GAM users using the GAM API](https://wiki.genexus.com/commwiki/wiki?16534).

In this example, the GETLogin method of the GAMUser external object is used.

In order to go on with the example, apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) to the
[Transaction](https://wiki.genexus.com/commwiki/wiki?1908). Aftr that, create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and add the Work With Purchase Orders as an element of it.

**3.** The salesmen are requested for their credentials when they enter the application on their devices. Check in the Menu object that [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authentication.

**4.** The user credentials have to be captured automatically when the user enters the "Purchase Order" data, so the User Identification can be saved. This is solved by programming the **Equal rule** in the **PurchaseOrder** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908):

```
Equal(UserId, GetUser());
```

**GetUser** is a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293). Its definition is as follows:

Source:

```
&login=GAMUser.GetLogin()
&errors=GAMRepository.GetLastErrors()
      for &error in &errors
      endfor
```

Rules:

```
parm(out:&login);
```

Variables:  
`[imagen omitida: wiki id 15657]`​

**Notes:**

* As "GAMUser" is a "static variable" that instantiates the current user information, you can use static methods to obtain the desired information (GetLogin, GetName, GetEmail, GetId, etc.).
* GetLogin method returns a string of the form <namespace>\<Authentication method>\<username>, e.g: testgam.testgam2\local\admin

After following the previous steps, the User current information will be retrieved and saved in the table when the user confirms the PurchaseOrder Transaction.

**5.**  When the users navigate within the "Work With Purchase Orders", they have to see their own information only. In order to achieve this behavior, one solution is to:

a. Create a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) with the following code (note that "GetUser" is the procedure defined above):

`[imagen omitida: wiki id 15391]`

b. Edit WorkWithDevicesPurchaseOrders object and configure the Data Selector filter, editing the grid Data Selector property in the section detail:

`[imagen omitida: wiki id 15649]`

### [See Also](#See+Also)

[MyCowBook KB](https://wiki.genexus.com/commwiki/wiki?15265,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552) | [HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) |
|

---
