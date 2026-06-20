---
title: "GAM - External Authentication: version 1.0"
source_id: 21548
source_url: https://wiki.genexus.com/commwiki/wiki?21548
genexus_version: "18"
---

# GAM - External Authentication: version 1.0

[External Authentication Type with GAM](https://wiki.genexus.com/commwiki/wiki?21755) can be defined using a SOAP web service or an external program.

### [Web service (SOAP) requirements](#Web+service+%28SOAP%29+requirements)

In the case of using a Web service (SOAP) it must meet certain requirements in order to be used as [External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512):

* The exposed Namespace of the webservice, must be "GAM".
* If the web service is generated with GeneXus and the [KB](https://wiki.genexus.com/commwiki/wiki?2428) uses [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), check that the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) of the web service is set to None.
* It has to receive 2 parameters:

```
Type GAMWSLoginInSDT : in parameter
Type GAMWSLoginOutSDT: out parameter
```

In case of the [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751), the same data types should be used, except that in this case they are passed to the program as strings in json format.

### [External authentication program 1.0 data types](#External+authentication+program+1.0+data+types)

#### [Type GAMWSLoginInSDT](#Type+GAMWSLoginInSDT)

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Type** |
| GAMUsrLogin | User identification login | String |
| GAMUsrPwd | User Password | String |
| GAMUsrAddPar | Collection of additional parameters | GAMWSLoginInAddParSDT (Collection) |

#### [Type GAMWSLoginInAddParSDT](#Type+GAMWSLoginInAddParSDT)

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Type** |
| GAMAddParId | Additional parameter identifier | String |
| GAMAddParValue | Additional parameter value | String |

`[imagen omitida: wiki id 21568]`

### [Type GAMWSLoginOutSDT](#Type+GAMWSLoginOutSDT)

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Type** |
| WSVersion | web service version (1.0) | String |
| WSStatus | Response status:  1 = User and password ok  2 = Unknown user  3 = Invalid password  4 = User is not active | Short |
| WSMessage | Custom message when the user tries to authenticate | String |
| User | Information of the connected user | GAMWSLoginOutUserSDT |

**Note:** WSStatus can be any other value than 1 to 4. Numbers above 4 correspond to custom messages. In that case, the string value in WSMessage will be shown to the user when he tries to login.

#### [Type GAMWSLoginOutUserSDT](#Type+GAMWSLoginOutUserSDT)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Description** | **Type** | |
| Code | User identifier | String | |
| FirstName | User first name | String | |
| LastName | User last name | String | |
| Email | User email | String | |
| Roles | User roles list | Collection of RoleItem | RoleItem has RoleCode (String) child. |

#### 

**Note:** The Code (\*) of the user will be mapped to the [External ID property of GAMUser object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21734,,) when the user registers to the application.

### [Example of the HTTP response of the webservice 1.0:](#Example+of+the+HTTP+response+of+the+webservice+1.0%3A)

<GAMWSLoginOutSDT xmlns="GAM">  
  <WSVersion>1.0</WSVersion>  
  <WSStatus>1</WSStatus>  
  <WSMessage />  
  <User>  
              <Code>500</Code>  
              <FirstName>Juan</FirstName>  
              <LastName>Perez</LastName>  
              <EMail>jperez@gxportal.com</EMail>  
              <Roles>  
                          <GAMWSLoginOutUserSDT.RoleItem>  
                                      <RoleCode>4</RoleCode>  
                          </GAMWSLoginOutUserSDT.RoleItem>  
                          <GAMWSLoginOutUserSDT.RoleItem>  
                                      <RoleCode>10</RoleCode>  
                          </GAMWSLoginOutUserSDT.RoleItem>  
                          <GAMWSLoginOutUserSDT.RoleItem>  
                                      <RoleCode>15</RoleCode>  
                          </GAMWSLoginOutUserSDT.RoleItem>  
              </Roles>  
  </User>  
</GAMWSLoginOutSDT>

### [Download](#Download)

* xpz of the web service 1.0 sample [here](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16927,,)
* wsdl of the web service 1.0 sample [here](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21554,,)

### [See Also](#See+Also)

[GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555)


|  |
| --- |
| **Backlinks** |
| [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Authentication: version 2.0](https://wiki.genexus.com/commwiki/wiki?21555) | [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Manage Roles through external authentication programs](https://wiki.genexus.com/commwiki/wiki?16929) | [HowTo: Pass additional parameters to external authentication programs using GAM](https://wiki.genexus.com/commwiki/wiki?21752) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) |
| [HowTo: Use GAM and Windows Authentication](https://wiki.genexus.com/commwiki/wiki?24034) |

---
