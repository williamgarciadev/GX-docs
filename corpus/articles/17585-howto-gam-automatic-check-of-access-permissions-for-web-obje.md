---
title: "HowTo: GAM Automatic Check of Access Permissions for Web Objects"
source_id: 17585
source_url: https://wiki.genexus.com/commwiki/wiki?17585
genexus_version: "18"
---

# HowTo: GAM Automatic Check of Access Permissions for Web Objects

#### [Problem to solve](#Problem+to+solve)

Only some users will have access rights to the execution of a web page (web objects with URL access; that is, web panels, web transactions, web components with URL Access property set to Yes). It also includes Soap and REst web services.

#### [How to solve it](#How+to+solve+it)

1. [Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) must be set to "Authorization" value (at version level, or at object level). In the following example it's set at version level, and at object level the property is set to "Use Environment property value".

Define [Permission Prefix Property](https://wiki.genexus.com/commwiki/wiki?17571) for this web object.

`[imagen omitida: wiki id 17572]`

###### [Figure 1.](#Figure+1.)

2. Check that the permission (prefix\_execute) has been created for the WEB application (it´s available at applications permissions list in [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935))

`[imagen omitida: wiki id 17573]`

###### [Figure 2.](#Figure+2.)

3. Define a Role or edit an existing role and add the permission recently created. You need to select the application where the permission has been defined, and add this permission to the Role.

Note that the access type of this permission will be "Allow" for this Role.

`[imagen omitida: wiki id 17587]`

###### [Figure 3.](#Figure+3.)

4. The user needs to be associated to this Role.

`[imagen omitida: wiki id 17588]`

###### [Figure 4.](#Figure+4.)

Only users with this Role will have access rights to the "samplewebpanel" object.

Note:

When any object of the KB is configured with [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214) = Authorization, the property

"Require Access Permissions" is automatically checked for the [Application](https://wiki.genexus.com/commwiki/wiki?15910) that the object belongs to; see the following figure:

`[imagen omitida: wiki id 15911]`

###### [Figure 5. "Require Access Permissions" application property.](#Figure+5.+%22Require+Access+Permissions%22+application+property.)

This property needs to be set in order that the permissions are generated for the application.

#### [See Also](#See+Also)

[GAM Applications](https://wiki.genexus.com/commwiki/wiki?15910)  
[GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569)


|  |
| --- |
| **Backlinks** |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) |

---
