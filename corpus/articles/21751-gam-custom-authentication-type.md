---
title: "GAM - Custom Authentication Type"
source_id: 21751
source_url: https://wiki.genexus.com/commwiki/wiki?21751
genexus_version: "18"
---

# GAM - Custom Authentication Type

Using a SOAP web service as an external identity provider is not useful when you need to store and persist data in a web session related to the login and read this data when desired from any other object of the application.

Suppose a .dll file has been implemented for authentication purposes, and it has one method for authenticating the user and another one for viewing his account balance. The login method saves a web session, which needs to be read when the "ViewUserBalanceAccount" is executed. As web sessions do not persist if saved in web services, a web service is not useful for this scenario.

In this scenario, instead of using [External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) you may use GAM Custom Authentication Type, where the external program is not a SOAP service, but a program of the same platform as the application which uses [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) (it can be a .dll, .rb, or .class developed using Genexus or not).

Using GAM Custom Authentication Type there are two possible versions of the external program supported, depending on the json format of the input   and output  parameters of the program, which are the following: [External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) and [External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555). In those links, you can download the XPZ containing the data types needed.

### [How to authenticate using GAM Custom Authentication Type](#How+to+authenticate+using+GAM+Custom+Authentication+Type)

#### [1. The external authentication program (.rb, .class., .dll) needs to meet some requirements.](#1.+The+external+authentication+program+%28.rb%2C+.class.%2C+.dll%29+needs+to+meet+some+requirements.)

* in parameter: string.  
  It has to be a string in json format, which structure has to be the same as the GAMWSLoginInSDT structured data type.
* out parameter: string.  
  It has to be a string in json format, which structure has to be the same as the GAMWSLoginOUTSDT structured data type, or void.

For information about the data types, see [External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) or [External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555).

#### [Example of external authentication program version 1.0](#Example+of+external+authentication+program+version+1.0)

Rules:

```
Parm(in:&StrInput, out:&StrOutput); //&StrInput and &StrOutput are varchar(256)
```

Source code:

```
&Key = '03E1E1AAA5BCA19FBA8C42058B4ABF28'
&GAMWSLoginIn.FromJson(&StrInput) // &GAMWSLoginIn is &GAMWSLoginInSDT data type
//Decrypt parameters
&UserLogin      = Decrypt64( &GAMWSLoginIn.GAMUsrLogin, &Key )
&UserPassword   = Decrypt64( &GAMWSLoginIn.GAMUsrPwd, &Key )
&GAMWSLoginOut             = New GAMWSLoginOutSDT() //&GAMWSLoginOut is &GAMWSLoginOutSDT data type
&GAMWSLoginOut.WSVersion   = GAMAutExtWebServiceVersions.GAM10
&GAMWSLoginOut.User        = New GAMWSLoginOutUserSDT()
Do 'ValidUser'
&StrOutput = &GAMWSLoginOut.ToJson()

Sub 'ValidUser'
    If &UserLogin = !"user"
       If &UserPassword = !"password"
          &GAMWSLoginOut.WSStatus = 1
          &GAMWSLoginOut.User.Code         = !"code"
          &GAMWSLoginOut.User.FirstName    = !"FirstName"
          &GAMWSLoginOut.User.LastName     = !"LastName"
          &GAMWSLoginOut.User.EMail        = !"name2@domain.com"    
          Do 'GetRoles' //optional
       Else
          &GAMWSLoginOut.WSStatus = 3
       EndIf
    Else
       &GAMWSLoginOut.WSStatus = 2
    EndIf
EndSub

Sub 'GetRoles' 
    &GAMWSLoginOutUserRol = New()
    &GAMWSLoginOutUserRol.RoleCode = "role_1"
    &GAMWSLoginOut.User.Roles.Add(&GAMWSLoginOutUserRol) 
    &GAMWSLoginOutUserRol = New()
    &GAMWSLoginOutUserRol.RoleCode = "role_2"
    &GAMWSLoginOut.User.Roles.Add(&GAMWSLoginOutUserRol
EndSub
```

#### [2. Define a new ([Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508)) using [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).](#2.+Define+a+new+%28wiki%3F16508%2CGAM%2B-%2BAuthentication%2BTypes+Authentication+Type%29+using+wiki%3F15935%2CCategory%253AGAM%2B-%2BWeb%2BBackoffice+GAM+Backoffice.)

It has to be "Custom Authentication" Type.

##### Java Sample .Net sample

##### [Figure 1.](#Figure+1.)

As seen in Figure 1, you have to specify some data of the authentication external program.

Function: You have to specify if the external program will be used for authentication and authorization purposes also. In the case of specifying "Authentication and Roles", see [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929).

Json Version: Specify the external program version (1.0 or 2.0).

Private Encryption Key: The "Encryption Key" is useful in case of Genexus external authentication programs because the Encrypt64 function is used to encrypt the user name and password when passed to the program. Here, you have to configure the Encryption key used in the external program for decrypting the user and password received.

File Name: Specify the file name corresponding to the external program (dll/jar/class/rb). It's optional for Java.

Package: Here specify the same value of [Java Package Name Property](https://wiki.genexus.com/commwiki/wiki?9111,,) in case of Java models, the value of [.Net Application namespace property](https://wiki.genexus.com/commwiki/wiki?8947) in case of NET models and the Code Namespace in case of Ruby. This property is optional and depends on the external program if it has a package or not.

Class Name: This field is required. Here, specify the name of the class of the external program.

See the sample object GAMExampleEntryAuthenticationType which is part of the GAM Backoffice in order to get an example code for adding and updating any Authentication Type.

#### [3. Program "Custom Authentication" login in a Native Mobile application](#3.+Program+%22Custom+Authentication%22+login+in+a+Native+Mobile+application)

The LoginExternal method of [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) is used. In this case, the first parameter sent to the method must be "Custom".

```
Event 'ExternalLogin'
    Composite
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Custom, &User, &Password)
        Return
    EndComposite
EndEvent
```

#### [4. Program "Custom Authentication" login in the web application](#4.+Program+%22Custom+Authentication%22+login+in+the+web+application)

The following code is an example of executing the custom external login in web applications. In the case of a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) the Login method of GAMRepository object is used. You need to define a variable of GAMLoginAdditionalParameters in order to specify the AuthenticationType which is going to be used.

See the GAMExampleLogin Web Panel (which is part of the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993)), where this code is used as an example:

```
&AdditionalParameter.AuthenticationTypeName = &LogOnTo //&LogOnTo is a combo box where the user selects the authentication type he wants to use. 
                                                       // This is the name of the Authentication Type. Using the example shown in figure 1 it would be "custom1.0testjava".
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )//&Errors is collection of GAMError
```

#### [Note:](#Note%3A)

1. In case the external program was developed using Genexus, it will have a method named "execute".  
If the program was developed using another tool than Genexus it may have any method used for authentication. In this case, you have to declare the name of the method using the following line of code, when you define the Custom Authentication type:

```
&AuthenticationTypeCustom.Custom.Method = "myauthenticationmethod" //&AuthenticationTypeCustom is GAMAuthenticationTypeCustom data type.
```

See the sample object GAMExampleEntryAuthenticationType (which is part of the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993)) for the complete example code.

2. Only one "Custom" Authentication Type can be defined for each GAM Repository.

### [Download](#Download)

* XPZ Sample from [here](https://wiki.genexus.com/commwiki/wiki?54441,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) |
| [GAM - External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755) | [GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) | [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) |
| [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815) | [GAM - Two Factor Authentication (2FA)](https://wiki.genexus.com/commwiki/wiki?48254) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [HowTo: LDAP Authentication using GAM](https://wiki.genexus.com/commwiki/wiki?29474) | [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [HowTo: Use GAM and Windows Authentication](https://wiki.genexus.com/commwiki/wiki?24034) |
| [Managing Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) |

---
