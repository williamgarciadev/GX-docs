---
title: "HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)"
source_id: 55404
source_url: https://wiki.genexus.com/commwiki/wiki?55404
genexus_version: "18"
---

# HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)

This article shows you the steps to define an [API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52550). To do so, follow the steps below:

### [Step 1. API object definition](#Step+1.+API+object+definition)

Consider the following two-level [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) configured as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

```
Customer
{
    CustomerId*      (Autonumber property = Yes)
    CustomerName
    CustomerLastName
    CustomerPhone
    CustomerEmail
    CustomerLastAccountId
    Account
    {
       AccountId*
       AccountPassword
       AccountBalance
       AccountStatus    (Type:Boolean)
    }
}
```

The Transaction has the following rule defined:

```
Serial(AccountId,CustomerLastAccountId,1);
```

Suppose you want to see if a Customer has a certain active account and the Balance of that account. To do this, create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) called ShowCustomerInfo with the following sections:

**Variables:**

```
Account          (Type:Customer.Account)
AccountBalance   (Type:Attribute:AccountBalance)
AccountId        (Type:Attribute:AccountId)
AccountPassword  (Type:Attribute:AccountPassword)
AccountStatus    (Type:Attribute:AccountStatus)
Customer         (Type:Customer)
CustomerId       (Type:Attribute:CustomerId)
```

**Rules:**

```
Parm(in:&CustomerId, in:&AccountId, in:&AccountPassword, out:&AccountBalance, out:&AccountStatus);
```

**Source:**

```
&Customer.Load(&CustomerId)
&Account = &Customer.Account.GetByKey(&AccountId)
&AccountBalance = &Account.AccountBalance
&AccountStatus = &Account.AccountStatus
```

Create an [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomer and define the following:

**Variables:**

```
AccountBalance       (Type:Attribute:AccountBalance)
AccountId            (Type:Attribute:AccountId)
AccountPassword      (Type:Attribute:AccountPassword)
AccountStatus        (Type:Attribute:AccountStatus)
CustomerId           (Type:Attribute:CustomerId)
```

**Service Source:**

```
Customer{
      CustomerInfo(in:&CustomerId, in:&AccountId, in:&AccountPassword, out:&AccountBalance, out:&AccountStatus)
      => ShowCustomerInfo(&CustomerId, &AccountId, &AccountPassword, &AccountBalance, &AccountStatus);
    }
```

### [Step 2. Defining the security scheme](#Step+2.+Defining+the+security+scheme)

To enable [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), set the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True at [version level](https://wiki.genexus.com/commwiki/wiki?7860). Next, select the Authentication or Authorization value for the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) in the API object. Then, perform a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

If you select the Authorization value, you must define the role and the permissions for the role. In addition, you have to associate it with each user. To this end, you can modify the [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) to easily identify the permission when assigning it to a user.

The permission that is generated in this case is APICustomer, and you can execute any method of the API object with it.

### [See Also](#See+Also)

[HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854)  
[HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864)
