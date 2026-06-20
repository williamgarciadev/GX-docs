---
title: "HowTo: Manage Roles through external authentication programs"
source_id: 16929
source_url: https://wiki.genexus.com/commwiki/wiki?16929
genexus_version: "18"
---

# HowTo: Manage Roles through external authentication programs

In order to solve the integration of applications regarding security issues, use [External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755).

Below you can see an example where [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) manages Authentication and Authorization issues using data received from the external authentication program.

### [Sample](#Sample)

From now on, suppose application A has to integrate to application B.

* Application A has GAM Integrated Security incorporated.
* Application B exposes a program that solves authentication and authorization (basically authenticates a user and returns his roles).

Assume that the external authentication program of application B complies with [External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) or [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751).

The roles returned by the web service or external program of application B need to have a corresponding role in the GAM database of application A so that GAM can manage Authorization.

So all the roles returned by the external authentication program need to have been previously defined in GAM and mapped to the external roles.

The way to map [roles](https://wiki.genexus.com/commwiki/wiki?17569) to the roles of application B is through the External ID property of GAMRole object (located in GAMLibrary).

### [See step by step](#See+step+by+step)

1. The population of roles in GAM is done using the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) or programmatically using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

The External ID property of the role can be set using GAM Web Backoffice (see Figure 1.), which has to be assigned to the role Identification in the application B database. This is the way to map application B roles to application A GAM roles in [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568).

`[imagen omitida: wiki id 57531]`

##### [Figure 1.](#Figure+1.)

2. Return roles in the external authentication program.

This depends on the external program version, which can be [External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548), or [External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555).

Suppose you are implementing External Authentication: version 1.0, so you have implemented a web service for authentication purposes, which complies with the 1.0 specification.

The code of the web service is such that, after the user has been validated, you load in an SDT variable (&GAMWSLoginOutUserRole, based on GAMWSLoginOutUserSDT.RoleItem) the roles of the user who has been authenticated.

The value assigned to the RoleCode property of this variable has to be the same as the one specified in the External ID property for the role defined in GAM (see Figure 1).

Afterwards you assign it to the collection of roles of &GAMWSLoginOut variable which is the out parameter of the web service.

```
&GAMWSLoginOutUserRole = New() //&GAMWSLoginOutUserRole is GAMWSLoginOutUserSDT.RoleItem data type.
&GAMWSLoginOutUserRole.RoleCode = "role_1"
&GAMWSLoginOut.User.Roles.Add(&GAMWSLoginOutUserRol) //&GAMWSLoginOut is GAMWSLoginOutSDT data type.
&GAMWSLoginOutUserRole = New()
&GAMWSLoginOutUserRole.RoleCode = "role_2" //assign RoleCode property with the External Id given to the role in GAM
&GAMWSLoginOut.User.Roles.Add(&GAMWSLoginOutUserRol)
```

So, after a user has logged in, GAM gets his roles from the webservice Response or the external authentication program output, and maps these roles to [GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569) using External ID property.

3. In application A configure [External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755), using GAM Web Backoffice or the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

Take into account that when defining the external Authentication Type, you need to specify the value Function = Authentication and Roles, as shown in Figure 2.

`[imagen omitida: wiki id 57532]`

##### [Figure 2.](#Figure+2.)

After the login has taken place, you can obtain the roles of the logged-in user by coding the following:

```
&session = GAMSession.get(&errors) // &session is GAMSession DataType, &errors is collection of GAMError
&user = GAMUser.get() // &user is GAMUser DataType.
&roles =  &Session.getroles(&errors) // &roles is collection of GAMRole
for &role in &roles
  //process Roles
endfor
for &error in &errors
 //process Errors
endfor
```

### [Note](#Note)

1. Each time the user logs in, the roles loaded in the out parameter of the external authentication program (&GAMWSLoginOut.User.Roles in the example above) are assigned to the user, and the relation to roles that he had been assigned previously is deleted.
2. The first role of the list of roles is taken as the main role for the user. See [GAM - Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) concept.


|  |
| --- |
| **Backlinks** |
| [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755) | [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) |
| [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: LDAP Authentication using GAM](https://wiki.genexus.com/commwiki/wiki?29474) |

---
