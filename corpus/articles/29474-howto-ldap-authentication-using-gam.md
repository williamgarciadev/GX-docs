---
title: "HowTo: LDAP Authentication using GAM"
source_id: 29474
source_url: https://wiki.genexus.com/commwiki/wiki?29474
genexus_version: "18"
---

# HowTo: LDAP Authentication using GAM

**Warning**: This sample shows how to configure GAM to authenticate using LDAP. GeneXus does not support the configuration of these external systems. Samples, screenshots, parameters, and/or locations may change over time.

When you need your application to use [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) authentication, and you also need the advantages of [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), you can use an external program or web service to bridge the GAM application and your LDAP.

LDAP offers so many options in terms of vendors and solutions that there isn't an "LDAP GAM Authentication Type" because there should be one for each implementation. Anyway, you can authenticate using your LDAP as a third-party authenticator or identity provider while GAM is enabled in your KB.

Here you will find how to configure GAM to authenticate using LDAP.

The solution consists of using any of these authentication types:

* [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512)
* [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751)

When any of these authentication types is used, GeneXus Access Manager is not the owner of the user credentials; only the username and other information that depends on the external program output will be stored in [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568). Information on roles can also be incorporated into GAM Repository if the external program returns this information.

### [Example](#Example)

The following is an example where an [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) is used and works as an identity provider to authenticate the application users. The [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) was chosen to implement the solution.

Using GAM Custom Authentication Type, GAM delegates the authentication to an external program (which can be developed using GeneXus). In this example, the external program will make the communication to LDAP.

Remember that in most cases, sending some additional parameters to the external program is necessary (besides the obvious ones such as username and password). In addition, the external program that communicates with LDAP will return additional data, not only the user's basic data. That's the reason to use [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555).

**Warning**: This is an example. Each LDAP can be different and the code to log in and get data from it will be different.

### [1. Configure the Custom Authentication Type](#1.+Configure+the+Custom+Authentication+Type)

Following the steps explained in [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751), configure the external program that is going to communicate with LDAP.

In the example, the authentication is delegated to an external program called "gamwsloginLDAP".

`[imagen omitida: wiki id 52620]`

### [2. Implementing the external program "gamwsloginLDAP"](#2.+Implementing+the+external+program+%22gamwsloginLDAP%22)

The data types used in this program are explained in [External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555), and are basically: GAMWSLoginInSDT Type and GAMWSLoginOutSDT data type.  
The parameters are sent to the program as strings in JSON format (although the structure is based on the SDTs mentioned above).

##### #1 In parameters

##### #2 Out parameters

### [Definition of variables for the external program "gamwsloginLDAP"](#Definition+of+variables+for+the+external+program+%22gamwsloginLDAP%22)

|  |  |
| --- | --- |
| **Variable name** | **Data Type** |
| GAMWSLoginIn | GAMWSLoginInSDT |
| GAMWSLoginOut | GAMWSLoginOutSDT |

As explained before, when the Authentication Type is custom, the parameters have to be strings (in JSON format following the structure of the GAMWSLoginInSDT Type and GAMWSLoginOutSDT data type).

```
Parm(in:&StrInput, out:&StrOutput);
```

The Procedure that makes the communication to LDAP - "gamwsloginLDAP"- looks as follows:

```
//Private key to decrypt parametrers
&Key = 'DCA3132624CF204E0399DF5011AC91D2'

//////Get the &GAMWSLoginIn data fron the input///////////

&GAMWSLoginIn.FromJson(&StrInput)

//////Get the Login information entered by the end user/////

&UserLogin      = Decrypt64( &GAMWSLoginIn.Login, &Key ) 
&UserPassword   = Decrypt64( &GAMWSLoginIn.Password, &Key )

//////Build the output parameter/////////////////////////////////////

&GAMWSLoginOut = new()
&GAMWSLoginOut.WSVersion = GAMAutExtWebServiceVersions.GAM20

do "validate user"    
&StrOutput = &GAMWSLoginOut.ToJson()

sub "validate user"
       &Input_Parameters = &GAMWSLoginIn.CustomParameters
    For &ParameterIN in &Input_Parameters
        if &ParameterIN.Id = 'LDAPpath'    
            &strpath = &ParameterIN.Value
        else
            if &ParameterIN.Id = 'LDAPFilter'
                &filter = &ParameterIN.Value
            endif
        endif
    endfor
    &UserName =  GetUserName(&UserLogin) //Ex:  "CN=" + &UserLogin +",OU=Promotions,OU=Marketing,DC=sampledomain,DC=local"
    connectLDAP.Call(&strpath,&UserName,&UserPassword,&filter,&GAMLDAPParametersRet,&result)
    
    if &result = 0
        &GAMWSLoginOut.WSStatus            = 1
        &GAMWSLoginOut.User.Code        = &GAMLDAPParametersRet.UserCode
        &GAMWSLoginOut.User.FirstName    = &GAMLDAPParametersRet.FirstName
        &GAMWSLoginOut.User.LastName    = &GAMLDAPParametersRet.LastName
        &GAMWSLoginOut.User.EMail        = &GAMLDAPParametersRet.mail
        &GAMWSLoginOut.ApplicationData = &GAMLDAPParametersRet.ToJson()
  else
        if &result = 2
            &GAMWSLoginOut.WSStatus            = 5
            &GAMWSLoginOut.WSMessage = "Invalid user or password."
        else
            &GAMWSLoginOut.WSStatus            = 6
            &GAMWSLoginOut.WSMessage = "User unknown."
        endif
endif
endsub
```

ConnectLDAP is a Procedure that tries to connect to LDAP given some parameters. The parameters in this example are &username, &userpassword, &strpath of the LDAP (eg: LDAP://server1.sampledomain.local/ou=promotions, ou=marketing,dc=sampledomain,dc=local), and a &filter (eg: sn=Smith). The additional parameters &strpath and &filter are received through the CustomParameters of the GAMWSLoginInSDT data type (See #1 above).  
  
Depending on the parameters required to perform the authentication, you will need to vary the code shown in the example above.  
  
The Procedure ConnectLDAP returns the user information in the *&GAMLDAPParametersRet* out parameter. The information returned depends on the application's needs.

In this particular example, it returned the following: First Name, Last Name, Email, User Code, and UserAccountControl.

`[imagen omitida: wiki id 52619]`

##### [#3 Parameters returned by the ConnectLDAP Procedure](#%233+Parameters+returned+by+the+ConnectLDAP+Procedure)

### [3. Implement the login Web Panel](#3.+Implement+the+login+Web+Panel)

In the GAMExampleLogin Web Panel, you need to set the input parameters of the external program that performs the authentication.

### [Definition of variables](#Definition+of+variables+)

|  |  |
| --- | --- |
| **Variable name** | **Data Type** |
| &CustomProperty | GAMProperty (predefined data type) |
| &GAMLDAPParametersRet | GAMLDAPParametersRet SDT Data Type (see #3) |

The login code is as follows:

```
/////////////Load the input data to pass to the external authentication program/////////
CustomProperty = new()

&CustomProperty.Id    = "LDAPpath"

&CustomProperty.Token    = "LDAPpath"

&CustomProperty.Value    = "LDAP://server1.sampledomain.local/ou=promotions, ou=marketing,dc=sampledomain,dc=local"

&AdditionalParameter.Properties.Add(&CustomProperty)

&CustomProperty = new()

&CustomProperty.Id    = "LDAPFilter"

&CustomProperty.Token    = "LDAPFilter"

&CustomProperty.Value    = "sn=" + &surname

&AdditionalParameter.Properties.Add(&CustomProperty)

&AdditionalParameter.AuthenticationTypeName = &LogOnTo

/////////////////////////////////////////////Login User //////////////////////////////////////////////////////////////

 &LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )

 If &LoginOK

///////////////////////////Get my custom application data in json format ////////////
    
       &ApplicationData = GAMSession.GetApplicationData()
            If not &ApplicationData.IsEmpty()
                 &GAMLDAPParametersRet.FromJson(&ApplicationData)
                  &UserAccountControl = &GAMLDAPParametersRet.useraccountcontrol
            Endif
else
  //Process Errors
Endif
```

The external program gamwsloginLDAP is automatically called when the login is invoked, and the parameters are automatically sent.

Note that the UserAccountControl —which is an additional parameter returned— is retrieved using the [GetApplicationData and SetApplicationData method of GAMSession object](https://wiki.genexus.com/commwiki/wiki?21575).

Consider that this is an example adapted to one scenario (an Active Directory). The code will vary depending on the LDAP used (the parameters required for login and the desired parameters to get from the LDAP).

### [See Also](#See+Also)

[HowTo: Manage Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929)

### [Download Sample](#Download+Sample+)

[LDAPAuthSample Active Directory](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29485,,)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [LDAP](https://wiki.genexus.com/commwiki/wiki?6887) |

---
