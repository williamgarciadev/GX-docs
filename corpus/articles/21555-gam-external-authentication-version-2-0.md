---
title: "GAM - External Authentication: version 2.0"
source_id: 21555
source_url: https://wiki.genexus.com/commwiki/wiki?21555
genexus_version: "18"
---

# GAM - External Authentication: version 2.0

[External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755) may be defined using a SOAP web service or an external program.

When using [External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512), external services used for authentication compliant with specification 2.0 have a different signature from the [version 1.0 external services](https://wiki.genexus.com/commwiki/wiki?21548).

2.0 specification gives more flexibility because it allows us to receive custom parameters from the authentication service, and additional user information.

From here on, the consumer application will be referred to as the application which uses [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) and allows its users to authenticate using an external service, in order to integrate with an external application.

The External Web Service (SOAP) must meet the following requirements:

* The exposed Namespace of the webservice must be "GAM".
* If the web service is generated with GeneXus and the KB uses GAM, you must check that the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) of the web service is set to none.
* 2 parameters must be received:

```
Type GAMWSLoginInSDT : in parameter
```

```
Type GAMWSLoginOutSDT: out parameter
```

In case of [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751), the same data types should be used, except that in this case they are passed to the program as strings in json format.

### [External authentication program 2.0 data types](#External+authentication+program+2.0+data+types)

#### [GAMWSLoginInSDT Type](#GAMWSLoginInSDT+Type)

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Type** |
| Login | User identification | String |
| Password | User Password | String |
| CustomParameters | Collection of additional parameters | GAMWSLoginCusParSDT (Collection) |

#### [GAMWSLoginCusParSDT](#GAMWSLoginCusParSDT)

The purpose of this collection of SDTs is to send a list of the form property-value to the service. This list is not processed by GAM.

|  |  |
| --- | --- |
| **Name** | **Type** |
| Id | Char(60) |
| Token | Char(40) |
| Value | Char(400) |

`[imagen omitida: wiki id 52753]`

#### [GAMWSLoginOutSDT Type](#GAMWSLoginOutSDT+Type)

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Type** |
| WSVersion | web service version (2.0) | String |
| WSStatus | Response status:  1 = User and password ok  2 = Unknown user  3 = Invalid password  4 = User is not active | Short |
| WSMessage | Custom message when the user tries to authenticate | String |
| User | Information of the connected user | GAMWSLoginOutUserSDT |
| ApplicationData | Additional Information sent to the consumer | LongVarChar(64k) |

**Note:** WSStatus can be any value from 1 to 4. Numbers over 4 correspond to custom messages, in which case, the string value in WSMessage will be shown when the user tries to log in.

#### [GAMWSLoginOutUserSDT](#GAMWSLoginOutUserSDT)

|  |  |
| --- | --- |
| **Name** | **Type** |
| Code (\*) | Char |
| FirstName | Char |
| LastName | Char |
| Email | Char |
| Properties | GAMWSLoginOutUserPropSDT (collection) |
| Attributes | GAMWSLoginOutUserAttSDT  (collection) |
| Roles | Char (collection) |

`[imagen omitida: wiki id 52754]`

**Note:** The user Code (\*) will be mapped to the [External ID property of GAMUser object](https://wiki.genexus.com/commwiki/wiki?21734,,) when the user is registered in the application.

#### [GAMWSLoginOutUserPropSDT Type](#GAMWSLoginOutUserPropSDT+Type)

|  |  |
| --- | --- |
| **Name** | **Type** |
| Id | Char(60) |
| Value | Char(400) |

#### [GAMWSLoginOutUserAttSDT Type](#GAMWSLoginOutUserAttSDT+Type)

|  |  |
| --- | --- |
| **Name** | **Type** |
| Id | Char |
| IsMultivalue | Boolean |
| Value | Char |
| Multivalues | GAMWSLoginOutUserAttMVSDT (Collection) |

#### [GAMWSLoginOutUserAttMVSDT](#GAMWSLoginOutUserAttMVSDT)

|  |  |
| --- | --- |
| Name | Type |
| Id | Char(60) |
| Value | Char(400) |

`[imagen omitida: wiki id 52755]`

### [Information that can be sent to the consumer application using WS 2.0 specification](#Information+that+can+be+sent+to+the+consumer+application+using+WS+2.0+specification)

Web service 2.0 enables us to send additional information on the user authenticated, to the consumer application. The information you may send is:

1. Static attributes of User which may be mapped to the GAMUser external object Through this functionality, the external application authenticating the user may determine the value of some attributes of the GAMUser object to be defined in the consumer application that uses GAM. Such information will be saved in the GAM Database for the corresponding user.

#### [Example 1](#Example+1)

The following is part of the web service code where information on the logged In user is loaded in an SDT variable, in order to pass it to the GAM application.  
The GAM application will save this data in the GAM Database for the corresponding user.

```
&Property = new()  //&property is GAMWSLoginOutUserPropSDT data type.
&Property.Id  = !"Phone"
&Property.Value  = !"1234567890"
&GAMWSLoginOut.User.Properties.Add(&Property)//&GAMWSLoginOut is based on GAMWSLoginOutSDT
 
&Property = new()
&Property.Id  = !"Address"
&Property.Value  = !"Millan 5768"
&GAMWSLoginOut.User.Properties.Add(&Property)
```

The ID of the GAMWSLoginOutUserPropSDT data type must be exactly the same as the properties of the GAMUser external object (part of the GAM Library).  
Only some of the properties of GAMUser object can be used and they are listed below.

```
name
Birthday
Gender
URLImage
URLProfile
Phone
Address
Address2
City
State
PostCode
Language : ISO639 3 characters
Timezone
DontReceiveInformation
IsBlocked
CannotChangePassword
MustChangePassword
PasswordNeverExpires
SecurityPolicyId
```

Specifically, and depending on the value of the [User Identification](https://wiki.genexus.com/commwiki/wiki?21030) Repository property, after logging in, the user may enter his email or name. If this property is set to "name or email", after the log in, and if it is considered valid by the external authentication program, then the string entered is checked to verify if it is an email (with a regular expression). If it is an email, and no name is returned by the external program (through the method explained above), then the email entered is assigned to the user name in the GAM User table.

The login entered by the user will always have priority over the information passed by the external authentication program. This means that the email and name entered by the user in the login have priority over the information returned by the program.

**Note:** The DefaultRoleId property of GAMUser object cannot be used like the other properties shown in the example, so the way to set a [Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) after authenticating, is to add the role as the first one on the roles list sent to the GAM application. See Example 3.

### [2. Dynamic attributes of user which may be passed to the consumer application](#2.+Dynamic+attributes+of+user+which+may+be+passed+to+the+consumer+application)

Additional information on the user, which is not part of the structure of GAMUser object (for example his "company"), may also be passed to the consumer application. In this case, the attributes will be considered as extended attributes of the user, and saved in the GAM database in the same way as [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634) is managed. These attributes can be queried from the GAM database as any extended user attribute.

#### [Example 2](#Example+2)

```
&Attribute = new() //&Attribute is GAMWSLoginOutUserAttSDT data type
&Attribute.Id   = !"Company"
&Attribute.IsMultiValue = False
&Attribute.Value  = !"ABC"
&GAMWSLoginOut.User.Attributes.Add(&Attribute)//&GAMWSLoginOut is based on GAMWSLoginOutSDT
 
&Attribute = new()
&Attribute.Id   = !"Phones"
&Attribute.IsMultiValue = True
&Attribute.Value  = !"Phones"
&Item.Id = !"HomeNumber" //&Item is GAMWSLoginOutUserAttMVSDT data type
&Item.Value = !"27896543"
&Attribute.MultiValues.Add(&Item)
 
&Item= new()
&Item.Id = !"JobNumber"
&Item.Value = !"23456234"
&Attribute.MultiValues.Add(&Item)
&GAMWSLoginOut.User.Attributes.Add(&Attribute)
```

### [3. User roles passed to the application that uses GAM](#3.+User+roles+passed+to+the+application+that+uses+GAM)

Roles of the external application may be mapped to the roles of the application that uses GAM, so that the user authenticated by the external web service may be incorporated in GAM Database with the [GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569) mapped to the external roles. The mapping is done through the externalId property of the GAM roles. See [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) for more information.

This is valid for [External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) as well. In case of GAM External Authentication version 2.0, the web service code that loads the roles of a user is shown in the following example.

#### [Example 3](#Example+3)

```
&GAMWSLoginOut.User.Roles.Add(!"role_1") //&GAMWSLoginOut is based on GAMWSLoginOutSDT
&GAMWSLoginOut.User.Roles.Add(!"role_2")
```

**Note:** The DefaultRoleId property of GAMUser object ([Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643)) is considered to be the first one in the list of roles given in GAMWSLoginOut.User.Roles collection.

### [4. Additional information that may be passed to the consumer application](#4.+Additional+information+that+may+be+passed+to+the+consumer+application+)

Other additional information, different than the previous information relating directly to the user, may be passed to the application. You can do this by using the ApplicationData item of the GAMWSLoginOutSDT data type, which accepts any string value. In particular, you may assign it a string in json format, so that the consumer application can easily read the information using the  function. In the following example it will be shown a part of the code of the web service 2.0 where additional information is loaded in the ApplicationData item of a variable based on GAMWSLoginOutSDT data type:

#### [Example 4](#Example+4)

```
&GAMExampleSDTApplicationData.Application = !"Sales" //&GAMExampleSDTApplicationData is GAMExampleSDTApplicationData. See figure below.
&GAMExampleSDTApplicationData.Operation  = !"ZETA"
&GAMExampleSDTApplicationData.Other   = 4
&GAMWSLoginOut.ApplicationData = &GAMExampleSDTApplicationData.ToJson()
```

Take into account that it is possible to define any structure for converting it to json format and load it in the GAMWSLoginOutSDT parameter afterward. For example, the structure could be as follows: `[imagen omitida: wiki id 52756]`

From the side of the consumer application, the following is a sample code that will get the additional information received from the authentication web service after the user has successfully logged in. Note that, in this case, you use the [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575).

```
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
If &LoginOK
  //Get my custom application data in json format //
  &ApplicationData = GAMSession.GetApplicationData() //&ApplicationData is LongVarChar(64Kb)

  If not &ApplicationData.IsEmpty()
   &GAMExampleSDTApplicationData.FromJson(&ApplicationData)
   msg("Application " + &GAMExampleSDTApplicationData.Application.ToString(), status)
   msg("Operation " + &GAMExampleSDTApplicationData.Operation.ToString(), status)
   msg("Other " + &GAMExampleSDTApplicationData.Other.ToString(), status)
  Endif
Endif
```

### [Download](#Download)

* XPZ Sample from [here](https://wiki.genexus.com/commwiki/wiki?21601,,)
* XPZ SDTApplicationData from [here](https://wiki.genexus.com/commwiki/wiki?45362,,)
* WSDL sample from [here](https://wiki.genexus.com/commwiki/wiki?21602,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) | [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575) | [HowTo: LDAP Authentication using GAM](https://wiki.genexus.com/commwiki/wiki?29474) | [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752) |
| [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) | [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) |

---
