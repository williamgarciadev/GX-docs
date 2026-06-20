---
title: "API object Syntax"
source_id: 50879
source_url: https://wiki.genexus.com/commwiki/wiki?50879
genexus_version: "18"
---

# API object Syntax

Below is a description of the syntax used in the Service Source tab of the [API object](https://wiki.genexus.com/commwiki/wiki?46151).

### [Syntax](#Syntax)

```
 <APIName>'{'
     ['['Annotation1']']
     ['['Annotation2']']
     <ServiceName1>(in:&var1, [in:&var2, inout:&var3,] out:&var4)=>
     <Implementation1>(&var1, [&var2, &var3,] &var4);
        ...
     ['['AnnotationN']']
     <ServiceNameN>(in:&var5, [inout:&var6,] out:&var7)=>
     <ImplementationN>(&var5, [&var6,] &var7);
     '}'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626).

**Where:**

*APIName*  
It’s the name used to describe the API in the code.

*Annotation1, …, AnnotationN*  
They are optional annotations that must be written between square brackets and before the declaration of the ServiceName to which they apply. Some of the possible annotations are [RestMethod](https://wiki.genexus.com/commwiki/wiki?50508) and ​​[RestPath](https://wiki.genexus.com/commwiki/wiki?50360).

*ServiceName1, …, ServiceNameN*  
External name (exposed as a service).

***&**var1, ..., **&**varN*  
These are variables defined in the API object that must be parameters in the service.

*Implementation1, …, ImplementationN*  
Name of GeneXus object implemented in the KB.

### [Description](#Description)

For each service declared in the API object, the following must be specified:

1. The name of the service exposed (with its parameters and the type of operator of each of them).
2. The name of the GeneXus object defined in the KB that implements the service functionality (with its parameters, and the possibility of indicating the type of operator for each one of them).

Each service is defined by the mapping between the external name and the implementation of the service functionality.

The basic mapping of the parameters, between the service and the implementation, is done by the variable names. That is, it doesn't matter if the order between the service parameters and the implementation varies.

The last parameters of the service are the return parameters (what the service returns), although they may not be the last ones in the implementation.

In the service declaration, you can omit parameters that are defined in the implementation with de [IN operator](https://wiki.genexus.com/commwiki/wiki?8220). In that case, they can be initialized in the [BEFORE event](https://wiki.genexus.com/commwiki/wiki?46151) of the service.

At the same time, in the service declaration, you can define parameters with the OUT operator that are not mentioned in the implementation. In this case, they can be initialized in the [AFTER event](https://wiki.genexus.com/commwiki/wiki?46151) of the service.

In addition, constants are supported in the implementation part if the parameters have the IN operator in those objects.

### [Samples](#Samples)

Consider the following [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) defined as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846):

```
Account
{
AccountId* 
AccountOwner
AccountPassword
AccountStatus        (Type:Boolean)
}
```

#### Sample #1

Suppose you want to know the status of an account and the account owner by entering the account number and password.

Create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) called QueryAccount and define the following:

Variables:

```
Account             (Type:Account)
AccountId           (Type:Attribute:AccountId)
AccountOwner        (Type:Attribute:AccountOwner)
AccountPassword     (Type:Attribute:AccountPassword)
AccountStatus       (Type:Attribute:AccountStatus)
```

Rules:

```
Parm(in:&AccountId, in:&AccountPassword, out:&AccountOwner, out:&AccountStatus);
```

Source:

```
&Account.Load(&AccountId)
&AccountOwner = &Account.AccountOwner
&AccountStatus = &Account.AccountStatus
```

Create the API object called APIAccount and define the following:

Variables:

```
AccountId           (Type:Attribute:AccountId)
AccountOwner        (Type:Attribute:AccountOwner)
AccountPassword     (Type:Attribute:AccountPassword)
AccountStatus       (Type:Attribute:AccountStatus)
```

Service Source:

```
Account{
        AccountInfo(in:&AccountId, in:&AccountPassword, out:&AccountStatus, out:&AccountOwner)
        =>QueryAccount(&AccountId,  &AccountPassword, &AccountOwner, &AccountStatus);
       }
```

AccountInfo is the name exposed as a service. The input parameters are &Account and &Password. The output parameters are &Status and &AccountOwner.

QueryAccount is the Procedure defined in the KB. The variables &AccountId, &AccountPassword are defined in the Procedure as input parameters. The variables &AccountStatus and &AccountOwner are defined as output parameters in the Procedure.

In addition, the order of &AccountStatus and &AccountOwner does not affect the performance of the service or the Procedure.

#### [Sample #2](#Sample+%232)

A slight variation from the previous example is to return only the account status.

```
Account{
       AccountInfo(in:&AccountId, in:&AccountPassword, out:&AccountStatus)
       =>QueryAccount(&AccountId, &AccountPassword, &AccountOwner, &AccountStatus);
       }
```

In this case, the variable &AccountOwner is only defined in the GeneXus object that solves the implementation.

There are two ways to deal with this type of variables:

* Initialize them in the Object API events. That is, define the value taken by the &AccountOwner variable in the BEFORE event of AccountInfo.
* Define them as inout in the Procedure; for example:

```
parm(in:&AccountId, in:&AccountPassword, inout:&AccountOwner, out:&AccountStatus);
```

#### [Sample #3](#Sample+%233)

Another option for sample 2 is to add a constant, as shown below:

```
Account{
       AccountInfo(in:&AccountId, in:&AccountPassword, out:&AccountStatus)
       =>QueryAccount(&AccountId,  &AccountPassword, "Tomas Huck", &AccountStatus);
      }
```

The &AccountOwnwer variable must be defined with the in operator in the implementation.


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) | [Description annotation](https://wiki.genexus.com/commwiki/wiki?56430) |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |

---
