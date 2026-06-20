---
title: "GAM - Authorization Scenarios"
source_id: 17583
source_url: https://wiki.genexus.com/commwiki/wiki?17583
genexus_version: "18"
---

# GAM - Authorization Scenarios

In the first stage you can solve it automatically:

* Permission to execution
* Permission on modes of Transactions

### [Web Applications](#Web+Applications)

#### [Scenario 1: Access to a Web object ([Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) and Web Components with [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) = Yes)](#Scenario+1%3A+Access+to+a+Web+object+%28wiki%3F6916%2CCategory%253AWeb%2BPanel%2Bobject+Web+Panel+and+Web+Components+with+wiki%3F7868%2CURL%2Baccess%2Bproperty+URL+access+property+%3D+Yes%29)

Validates if the user has permission to execute the object. He should not see any data of the form if he has no rights to execute the object (in case of web objects event Start is not executed actually).  
  
In this case [GAM](https://wiki.genexus.com/commwiki/wiki?14960) checks that the user has <prefix>\_Execute permission, where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the object.

In case a permission error is detected, an automatic redirect will be done to the [Not Authorized Object for Web Object](https://wiki.genexus.com/commwiki/wiki?17551,,) in case of web applications.

See the following: [HowTo: GAM Automatic Check of Access Permissions for Web Objects](https://wiki.genexus.com/commwiki/wiki?17585).

#### [Scenario 2: Access to a Main Proc with call protocol HTTP (example PDF reports which display on the browser)](#Scenario+2%3A+Access+to+a+Main+Proc+with+call+protocol+HTTP+%28example+PDF+reports+which+display+on+the+browser%29)

Validates if the user has permission to execute this object.  
In this case, GAM checks that the user has <prefix>\_Execute permission, where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the object.

In case of an error, permission is detected, 401 HTTP error (thrown by application server) will be displayed (it should be captured by the programmer).

In case of a PDF report, [Not Authorized Object for Web Object](https://wiki.genexus.com/commwiki/wiki?17551,,) is considered.

#### [Scenario 3: Access to a web Transaction with or without mode](#Scenario+3%3A+Access+to+a+web+Transaction+with+or+without+mode)

First validates if the user has permission to execute this object. In this case, GAM checks that the user has <prefix>\_Execute permission (where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the Transaction).

The <prefix>\_Execute permission enables the user to display the data of the trn (display mode).

If the user executes an action over the trn (Confirm or Delete) another permission will be required :

```
<prefix>_Insert
<prefix>_Update
<prefix>_Delete
```

In fact there is a permission which "groups" the other permissions (see [Full Control Permissions](https://wiki.genexus.com/commwiki/wiki?17664)):

```
<prefix>.FullControl

    <prefix>_Execute
    <prefix>_Insert
    <prefix>_Update
    <prefix>_Delete
```

In case of an error, a standard error message of GeneXus will be displayed if the Transaction does not receive KEY and mode as parameters (in case it receives that information, a permission error redirects to [Not Authorized Object for Web Object](https://wiki.genexus.com/commwiki/wiki?17551,,)).

See: [How to implement permissions on modes of a web Transation](https://wiki.genexus.com/commwiki/wiki?18046).

#### [Scenario 4: Restricted access to a group of WEB pages](#Scenario+4%3A+Restricted+access+to+a+group+of+WEB+pages)

See [GAM: How to give restricted access to a group of web objects](https://wiki.genexus.com/commwiki/wiki?18510).

### [SD Applications](#SD+Applications)

#### [Scenario 5: Permissions to view a list, grid, or detail of a [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) and execute a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) (SD Applications).](#Scenario+5%3A+Permissions+to+view+a+list%2C+grid%2C+or+detail+of+a+wiki%3F15974%2CCategory%253AWork%2BWith%2Bpattern%2Band%2BWork%2BWith%2Bobject+Work+With+pattern+and+Work+With+object+and+execute+a+wiki%3F24829%2CCategory%253APanel%2Bobject+Panel+object+%28SD+Applications%29.)

Validates if the user has rights to execute the object, very similar to scenario #1.

It validates permissions for displaying the list and viewing the detail (view mode) of a WWSD panel.

In case of SD panels, GAM checks if the user has the permission to execute it.

In this case, GAM checks that the user has <prefix>\_Execute permission, where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the object.

In case a permission error is detected, the error is displayed on the screen or redirected to the object specified in [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018).

See [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064).

**Note**:

1. In case of WWSD and SD panels, the business logic of these objects is solved using [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573). When you generate a WWSD or SD panel object, Data Providers exposed as REST web services are generated.

These REST web services became private when you declare security over the corresponding objects (WWSD and SD panels).

From the perspective of the GeneXus user, he doesn´t need to worry about that, because it´s transparent to the developer.

2. Note that the actions in WWSD Panels (insert, update, delete) are related directly to the Business Component associated with the WWSD and not the WWSD itself. That means that, if you apply [Work With Pattern for Smart Devices](https://wiki.genexus.com/commwiki/wiki?9413,,) to a Transaction ("Product"), the "Product" Transaction is automatically saved as Business Component exposed as REST web service. In order to control permissions over the actions insert, update, delete, you need to declare permissions over the Business Component itself (see scenario #5).

#### [Scenario 6: Access to actions of a WWSD object (insert, update, delete)](#Scenario+6%3A+Access+to+actions+of+a+WWSD+object+%28insert%2C+update%2C+delete%29)

If you apply [Work With Pattern for Smart Devices](https://wiki.genexus.com/commwiki/wiki?9413,,) to a Transaction (ie. "Product"), the "Product" Transaction is automatically saved as Business Component exposed as [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573).

In order to control permissions over the actions insert, update, delete, you need to declare permissions over the Business Component itself.

The idea is to validate if the user has rights to execute this object depending on the method with which the call is issued.  
  
GET method requires <prefix>\_Services\_Execute permission (where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the Business Component), and this is the minimum permission required.

The rest of the permissions are:

```
<prefix>_Services_Insert
<prefix>_Services_Update
<prefix>_Services_Delete
```

Finally, there is a permission which "groups" the other permissions:

```
<prefix>_Services.FullControl

    <prefix>_Services_Execute
    <prefix>_Services_Insert
    <prefix>_Services_Update
    <prefix>_Services_Delete
```

The check of permissions is done through OAuth in this case. In case of a permission error, 401 HTTP error is received, which is captured by the SD application and an error is shown on the screen.

See: [HowTo: Permissions in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17925).

Note: The services of a Transaction (Business Component) is independent of the WWSD itself. You can give permissions over the WWSD and not over the BC, and viceversa.  
The services are independent, and as they are REST services, they can be called from any other application, as any REST web service (see scenario #7).

#### [Scenario 7: Access to user actions of a SD object](#Scenario+7%3A+Access+to+user+actions+of+a+SD+object)

See [Permissions over a user action in SDpanels](https://wiki.genexus.com/commwiki/wiki?18173).

### [REST web services](#REST+web+services)

#### [Scenario 8: Access to a Business Component exposed as Rest web service](#Scenario+8%3A+Access+to+a+Business+Component+exposed+as+Rest+web+service)

This kind of Rest services can be called using GET (read), POST (update), PUT (create), DELETE (delete) HTTP methods. See [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) for more details.

These methods are directly related to execute, update, insert, delete modes over the Business Component.

The idea is to validate if the user has rights to execute the BC exposed as REST web service, depending on the method with which the call is issued.

GET method requires <prefix>\_Services\_Execute permission (where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the Business Component), and this is the minimum permission required.

The rest of the permissions are:

```
<prefix>_Services_Insert
<prefix>_Services_Update
<prefix>_Services_Delete
```

Finally, there is a permission which "groups" the other permissions:

```
<prefix>_Services.FullControl

    <prefix>_Services_Execute
    <prefix>_Services_Insert
    <prefix>_Services_Update
    <prefix>_Services_Delete
```

The check of permissions is done through OAuth in this case. In case of a permission error, 401 HTTP error is received.

#### [Scenario 9: Access to a Data Provider exposed as Rest web service](#Scenario+9%3A+Access+to+a+Data+Provider+exposed+as+Rest+web+service)

These kinds of Rest services are only read services (always accessed via GET HTTP method). In this case, GAM checks that the user has <prefix>\_Services\_Execute permission (where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the Data Provider). The check of permissions is done through OAuth in this case (the same mechanism used for SD applications security checks).

In case of a permission error, 401 HTTP error is received.

#### [Scenario 10: Access to a procedure exposed as REST service](#Scenario+10%3A+Access+to+a+procedure+exposed+as+REST+service)

These kinds of services are only read services (always accessed via POST HTTP method).  
In this case, GAM checks that the user has <prefix>\_Services\_Execute permission (where prefix is the [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) defined for the procedure).  
The check of permissions is done through OAuth in this case (the same mechanism used for SD applications security checks).

### [See Also](#See+Also)

[GAM - Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916)  
[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[GAM - Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664)  
[GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910)  
[GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [Category:GAM - Authorization](https://wiki.genexus.com/commwiki/wiki?17918) | [GAM - Automatic Permissions generated by GeneXus](https://wiki.genexus.com/commwiki/wiki?17916) |
| [GAM - Automatic Permissions generated by GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53950) | [GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Give Restricted Access to a Group of Web Objects](https://wiki.genexus.com/commwiki/wiki?18510) |
| [HowTo: Implement GAM permissions in Transaction's Modes](https://wiki.genexus.com/commwiki/wiki?18046) | [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) | [HowTo: Permissions in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17925) | [HowTo: Permissions in SD Applications, CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17935) |
| [HowTo: Permissions in SD Applications, WW and CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17943) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) | [Permission Prefix property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53928) |
| [Permission Prefix property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55357) | [Permissions Over a User Action in SD Objects](https://wiki.genexus.com/commwiki/wiki?18173) | [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512) |

---
