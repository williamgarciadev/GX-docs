---
title: "HowTo: Use API Key to request services from an application"
source_id: 56104
source_url: https://wiki.genexus.com/commwiki/wiki?56104
genexus_version: "18"
---

# HowTo: Use API Key to request services from an application

As of [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240), it is possible to request an access\_token using an API Key. In previous versions, an access\_token could only be obtained with User/Password to then use the Token obtained in the Header Authorization of the request.

### [How to create an API Key Authentication Type](#How+to+create+an+API+Key+Authentication+Type)

First, create an "API Key" (&GAMAuthenticationTypeAPIKey) Authentication Type that will be used by the user to authenticate against the application. A user must be created and provided with an API key to make the request to this application.

To do this, follow these steps:

1. Go to "Authentication Types" at the sidebar of the GAM Backoffice.

2. Click on "ADD", and select "API Key".

`[imagen omitida: wiki id 56237]`

Define the API Key authentication type as needed.

`[imagen omitida: wiki id 56108]`

### [Enabling an application to use API Key Authentication](#Enabling+an+application+to+use+API+Key+Authentication)

First, make sure that the application that will use API Key is already defined; if it is not, follow the steps below:

1. Go to "Applications" at the sidebar panel.
2. Click on "ADD".
3. Fill in all fields of the General Tab.
4. Finally, click on the "CONFIRM" button.

**Note**: An application must be defined for each client you want to connect; this allows you to have control over what is accessed by that application, including what user data, how many times it is authenticated, and several other functionalities.

If you already have a defined application that will use an API Key, see the configuration detailed below.

In the API Key tab of the application you defined above, configure everything related to the API Key.

`[imagen omitida: wiki id 56105]`

From there, it is possible to configure everything related to the API Key properties, such as its expiration, and the type of authentication for which it is enabled. It even allows you to use Custom Scopes to decide which Scopes are shared at Login with an API Key.

The "Enable work with API keys" property (&GAMApplication.APIKeyEnable: Boolean) allows enabling/disabling the API Key for that application (Remote REST Authentication must be enabled to use an API Key).

The property "API Key timeout (In hours)" (&GAMApplication.APIKeyTimeout: Numeric) configures how long the generated API Key will be valid; if its value is set to 0, it will never expire.

In addition, the API Key can be configured only for one type of API Key Authentication or for any type of Authentication in the property"Allow only this authentication type name" (&GAMApplication.APIKeyAllowOnlyAuthenticationTypeName: VarChar).

Finally, if the property "API Key Allow Scope Customization" (&GAMApplication.APIKeyAllowScopeCustomization: Boolean) is set to True, the user will be able to customize the scopes when generating the API Key.

`[imagen omitida: wiki id 56115]`

Follow the next link to view the possible [Scopes](https://wiki.genexus.com/commwiki/wiki?55603).

### [How to enable API Key for a User](#How+to+enable+API+Key+for+a+User)

At the user level in the GAM Backoffice, the property "Application API KEY" lists the Applications for which API Keys can be generated to access them. You can generate a different API Key for each application.

`[imagen omitida: wiki id 56109]`

For this, you can use the "GENERATE" (&isOK = &GAMUser.GenerateApplicationAPIkey(&ApplicationClientID, &DetailScope, &APIkey, &Expires, &GAMErrorCollection)) button, for the method *&GAMUser. GenerateApplicationAPIKey.*

`[imagen omitida: wiki id 56110]`

You will need the Client ID of the Application (&ApplicationClientID) for which you want to enable API Key for that user, and the Scopes that are going to be shared with that application (&DetailedScope). An example of these scopes can be: &DetailScope = !"user\_email+user\_first\_name+user\_external\_id".

When you click on the "GENERATE" button, the following pop-up window will appear:

`[imagen omitida: wiki id 56111]`

This pop-up will show a "GENERATE" button that will generate an API Key that will be used later to request the service.

**Important Note**: When generating an API Key, the scopes used in the application or customized by the user are associated with it. If the application stops publishing scopes that used an API Key at the moment of its creation, the API Key is invalidated, and a new one must be generated.

### [How to make a request to an Application Service using API Key](#How+to+make+a+request+to+an+Application+Service+using+API+Key)

**POSTMAN Example**

#### [1. Access Token](#1.+Access+Token)

**POST**

Endpoint: http://<domain>/<virtual\_directory>**/oauth/gam/v2.0/access\_token**

Header:

Content-Type: application/x-www-form-urlencoded

Body:

client\_id: Application ClientID  
client\_secret: Application Client Secret  
grant\_type: password  
api\_key: APIKey generated previously.  
authentication\_type\_name: apikey  
username: Username

`[imagen omitida: wiki id 56112]`

Response:

```
{
    "access_token": "ae47229f-e133-42d1-87e0-c5ac59e51edf!zuogvrYqVdJsoaq4nZohgqHfmfthCwBbd1ORZWoyGiHrBw9iIuNlLeRH3L9zPBuRG6hfsenvAUyhNu",
    "token_type": "Bearer",
    "expires_in": 0,
    "refresh_token": "",
    "scope": "user_first_name+user_external_id+user_email"
    "user_guid": "748cbb14-b408-4c04-a984-43f50df5f32f"
}
```

#### [2. User Info](#2.+User+Info)

GET

Endpoint: http://<domain>/<virtual\_directory>**/oauth/gam/v2.0/userinfo**

Headers:

Content-Type: application/x-www-form-urlencoded  
Authorization: access\_token

`[imagen omitida: wiki id 56113]`

Response:

```
{
    "email": "userapikey@mail.com"
    "verified_email": true,
    "first_name": "user",
    "external_id": "12a938b7123zg98",
}
```

### [See Also](#See+Also)

[HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server](https://wiki.genexus.com/commwiki/wiki?55623)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
