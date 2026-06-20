---
title: "SAP BTP as IdP"
source_id: 52787
source_url: https://wiki.genexus.com/commwiki/wiki?52787
genexus_version: "18"
---

# SAP BTP as IdP

The Identity Provider service provided by SAP BTP can be used to authenticate from a GeneXus application that uses GAM.

In order for the GAM to authenticate against the Cloud Foundry services in SAP BTP and thus obtain the access token, the following steps must be followed:

In a KB with GAM , add a new authentication type that is OAuth 2.0 (GAM BackEnd: Settings/Authentication Types)

In the general tab, enter client id, client secret (this data can be obtained from the xsuaa data Json associated with the app in CF) and uncheck the Redirect to authenticate checkbox. (This is to avoid having to Login in the SAP Login screen, in other words avoid redirecting to the Login in SAP window).

`[imagen omitida: wiki id 52834]`

In the Token tab, in Url, enter the url value of the json of the xsuaa service associated with the app in CF and add /oauth/token. Tick  
Include Authentication header and add the realm of the service (in this case authentication.eu10.hana.ondemand.com)  
and change the value of grant type to password.

`[imagen omitida: wiki id 52835]`

In the Response remove the scope value and in the user id add jti.

`[imagen omitida: wiki id 52836]`

Finally, in the UserInfo tab, since SAP OAuth does not have a service that returns user information, what must be configured is an HTTP procedure that returns the Json with the user data. This method can be called with either GET or POST, it varies depending on how the procedure is configured. In the example we provide below it is set to GET, (but we include the POST lines commented out).

`[imagen omitida: wiki id 52837]`

`[imagen omitida: wiki id 52838]`

### [For mobile applications](#For+mobile+applications)

In order for the authentication token to be sent in SD in the calls, what they have to do is add a record (manually) in the GAM RepositoryProp table with the following info:

RepId = 2  
RepPropId = "UseExternalTokenInMobileApps"  
RepPropToken = "\*"  
RepPropValue = "true"

(this is so that the token loaded in the proc -FalsoUser- is considered instead of taking the token from the GAM)

After saving the record, restart the webapp. (In case of CF it would be enough to re-upload the application, cf push)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) | [GeneXus for SAP Systems 18 Release Notes](https://wiki.genexus.com/commwiki/wiki?51078) |

---
