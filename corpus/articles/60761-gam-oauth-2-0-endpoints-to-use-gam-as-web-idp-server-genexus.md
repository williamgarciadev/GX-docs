---
title: "GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 13 or prior)"
source_id: 60761
source_url: https://wiki.genexus.com/commwiki/wiki?60761
genexus_version: "18"
---

# GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 13 or prior)

This article describes the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Endpoints in order to explain authentication with GAM as IDP using the [OAuth 2.0 protocol](https://datatracker.ietf.org/doc/html/rfc6749).

**Requirements:**

Define a GAM Application that will be the client that you want to connect to the IDP Server. Get the Client ID and the Client Secret credentials from this application.

`[imagen omitida: wiki id 55647]`

When creating the application, you must assign it a name, enable the Allow Authentication property within the WEB Identity Provider. Configure the URL of the Login Object and in the Callback URL property configure the address of the application to integrate. When confirming, the ClientID and Client Secret will be generated.

### [OAuth2.0 protocol flow with GAM Endpoints as IDP (Identity Provider)](#OAuth2.0+protocol+flow+with+GAM+Endpoints+as+IDP+%28Identity+Provider%29+)

### 

**Endpoints:**

* [1. Signin](https://wiki.genexus.com/commwiki/wiki?49817)
* [2. Access Token](https://wiki.genexus.com/commwiki/wiki?49817)
* [3. User Info](https://wiki.genexus.com/commwiki/wiki?49817)
* [4. Refresh Token](https://wiki.genexus.com/commwiki/wiki?49817)

### [**1. Signin**](#1.+Signin)

The endpoint is: https://gamidentityprovider.com/virtual\_dir**/oauth/gam/signin**.

**Parms:**  
  
**response\_type=code**: It's required, but in case it is not received, it's required "**oauth=auth**".  
**scope:** Scope of the user account you wish to access. It's only required when "&GAMApplication.ClientAuthenticationRequestMustIncludeUserScopes" it's True.  
**client\_id:** Client ID of the application, required.  
**redirect\_uri:** Callback URL (it must match the one configured in the application). https://<your\_server>/<virtual\_directory>**/oauth/callback**, required.  
**state:** Random string that stores the status before the request, required.

If your application does not contain that Friendly URL (/oauth/callback), you can specify another Custom URL. For example if your application have https://<your\_server>/<virtual\_directory>**/oauth/return** you must configure this URL in the IDP Server and check Custom Callback URL property**.**

Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)

**Redirect to:**

https://gamidentityprovider.com/virtual\_dir**/oauth/gam/signin?****response\_type=**code**&scope**=gam\_user\_data**&client\_id=**<Client\_ID>**&redirect\_uri=**https://<your\_server>/<virtual\_directory>/oauth/callback**&state=**<random\_alphanumeric>

After authenticate you will be automatically redirected to redirect\_uri, including the following parameters:**code** and **state,**this state is the same as the received.

For example: https://<your\_server>/<virtual\_directory>**/oauth/callback****?state=**<random\_alphanumeric>**&code=**e8279ad27bfd4e6ca717191cfc74fe4d413494378b53da98ca954924ac6791eb0ab56c06

The developer must validate that the value of the state is the same as the one sent to the IDP Server.

### [**2. Access Token**](#2.+Access+Token)

The endpoint is: https://gamidentityprovider.com/virtual\_dir**/oauth/gam/access\_token**.

**POST  
Headers:**

Content-Type: Type of content that will be returned. Use application/x-www-form-urlencoded

**Body:**

**grant\_type=authorization\_code:**It's required.  
**code:** Code obtained in the Step 1, required.  
**client\_id:** Client ID of the application, required.  
**client\_secret:** Client Secret of the application, required.  
**redirect\_uri:** Callback URL (it must match the one configured in the application). https://<your\_server>/<virtual\_directory>**/oauth/callback**, required.

**POSTMAN Example:**

`[imagen omitida: wiki id 51038]`  
`[imagen omitida: wiki id 51043]`

**Response:**

In response, you will receive a JSON with the following format:

```
{
    "access_token": "7032f1fd-e7a9-48bc-b9db-88a35b121b09!3964ab5e6ab7d771c6c5744122eaac8da2363a041fbfa96828441cd4a2b4c19d1319bb0dc775aa@SSORT!7032f1fd-e7a9-48bc-b9db-88a35b121b09!0c6fe15b76f14f5b8a0805c1b6c20appA",
    "token_type": "Bearer",
    "expires_in": 1800,
    "refresh_token": "00167b653abbc064b5982a1fd15e0f974b5",
    "scope": "gam_user_data",
    "user_guid": "139f4332-3f40-47b0-8fb4-ee7b3dbddc4f"
}
```

#### [**Note**](#Note)

To receive a refresh token, you must change the default value of the property [Maximum OAuth token renewals](https://wiki.genexus.com/commwiki/wiki?19324) in [GAM Security Policies](https://wiki.genexus.com/commwiki/wiki?18521).

### [**3. User Info**](#3.+User+Info)

The endpoint is: https://gamidentityprovider.com/virtual\_dir**/oauth/gam/userinfo**.

**GET  
Headers:**

**Content-Type:** Type of content that will be returned. Use application/x-www-form-urlencoded, required.  
**Authorization:** access\_token obtained in the Step 2, required.

**POSTMAN Example:**

`[imagen omitida: wiki id 51040]`

**Response:**

In response, you will receive a JSON with the following format:

```
{
   "guid":"139f4332-3f40-47b0-8fb4-ee7b3dbddc4f",
   "username":"user",
   "email":"user@example.com",
   "verified_email":true,
   "first_name":"user",
   "last_name":"User",
   "external_id":"",
   "birthday":"2000-01-01",
   "gender":"N",
   "url_image":"https://",
   "url_profile":"",
   "phone":"+598",
   "address":".",
   "city":".",
   "state":".",
   "post_code":".",
   "language":"Eng",
   "timezone":".",
   "CustomInfo":""
}
```

### [**4. Refresh Token**](#4.+Refresh+Token)

The endpoint is: https://gamidentityprovider.com/virtual\_dir**/oauth/gam/access\_token**.

**POST  
Headers:**

**Content-Type:** Type of content that will be returned. Use application/x-www-form-urlencoded

**Body:**

**client\_id:** Client ID of the application, required.  
**client\_secret:** Client Secret of the application, required.  
**grant\_type:** must be "refresh\_token.", required.  
**refresh\_token:** refresh\_token received when requesting the access\_token obtained in Step 2, required.

**POSTMAN Example:**

`[imagen omitida: wiki id 51041]`

`[imagen omitida: wiki id 51042]`

**Response:**

In response, you will receive a JSON with the following format:

```
{
    "access_token": "85a3006c-0606-41d2-980e-223f88463ec2!b1b3e778247c870560d49d17ffd514a2a8467747208b1cf4a641780a267466bc65fba8034c9bbc",
    "token_type": "Bearer",
    "expires_in": 180,
    "refresh_token": "002b9ec850f78b845d883779fa52c91a01",
    "scope": "gam_user_data",
    "user_guid": "139f4332-3f40-47b0-8fb4-ee7b3dbddc4f"
}
```

**When to call the Refresh Token**

When a Rest service is called and the access token has expired, 401 and Error 103 are returned. If this happens and there is a [Refresh Token](https://wiki.genexus.com/commwiki/wiki?49817) saved, it can be used as detailed above; otherwise, a new [Access Token](https://wiki.genexus.com/commwiki/wiki?49817) must be requested.

**POSTMAN Example:**

`[imagen omitida: wiki id 50293]`

**Response:**

In response, you will receive a JSON with the following format:

```
{
    "error": {
        "code": "103",
        "message": "Token expired, log in again."
    }
}
```
