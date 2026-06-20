---
title: "GAM - OAuth 2.0 Authentication Type"
source_id: 39484
source_url: https://wiki.genexus.com/commwiki/wiki?39484
genexus_version: "18"
---

# GAM - OAuth 2.0 Authentication Type

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) allows you to authenticate using any OAuth 2.0 provider by following the steps below.

The definition of this [GAM Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508) is the same as any other type of authentication already existing in GAM, only that this type of authentication requires a detailed configuration of the protocol used by the Provider.  
Therefore, to configure the OAuth 2.0 Authentication Type in GAM, you need to follow the documentation of the Identity Provider to which you want to connect.

At runtime, the operation is similar to that for [Facebook](https://wiki.genexus.com/commwiki/wiki?29007) / [Google Authentication](https://wiki.genexus.com/commwiki/wiki?29013), for example. When you select this type of authentication, the login is redirected to the Identity Provider configured.   
The Login is displayed by the Provider; there, users enter their credentials and are redirected back to the application.

In addition, GAM session renewal when the Access token of the Provider is refreshed is automatically solved. This behavior is optional. Otherwise, the GAM session expires at the same time as the Token provided. See below for more information **(1)**.

Some Providers are as follows:

* Azure Active Directory
* Facebook
* Google
* Instagram
* LinkedIn
* Mercado Libre
* Office 365
* WeChat

## [Configuration](#Configuration)

The configuration of this type of authentication is divided into Tabs.

`[imagen omitida: wiki id 60959]`

### [General tab](#General+tab)

Basic information identifying the application in OAuth 2.0 (Client ID, Client Secret, and Redirect URL).  
The Client ID and Client Secret are obtained from the Identity Provider.  
If "Custom Redirect URL?" is selected, GAM will not modify the URL. Therefore, the developer must correctly handle the response received.  
Clearing the option "Redirect to authenticate?" allows authentication with OAuth 2.0 using REST without redirection to the Identity Provider.

### [Authorization tab](#Authorization+tab)

Here, configure the URL for users to enter their credentials.

Some parameters are needed to call this URL and should be specified in this section. The same happens with the response parameters.  
Once the user is authenticated, the Identity Provider returns the Access Code. With the Access Code received, GAM requests the Access Token.

#### [**Important**](#Important)

In case your external Identity Provider requires [**PKCE**](https://datatracker.ietf.org/doc/html/rfc7636) to authenticate against it, ensure to enable "Enable PKCE?" property. Using GAM API the code will be the following:

```
&GAMAuthenticationOAuth20.Authorize.PKCEAuthentication.Enable = True
```

Also, you can add additional parameters when you use OAuth 2.0 to send to the IDP.

#### [Example:](#Example%3A)

```
&CustomGAMProperty = new()
&CustomGAMProperty.Id = "language"
&CustomGAMProperty.Value = "en"
&AdditionalParameter.Properties.Add(&CustomGAMProperty)
&CustomGAMProperty = new()
&CustomGAMProperty.Id = "DeviceId"
&CustomGAMProperty.Value = "AZ-Prueba"
&AdditionalParameter.Properties.Add(&CustomGAMProperty)
&CustomGAMProperty = new()
&CustomGAMProperty.Id = "CustomerId"
&CustomGAMProperty.Value = "123456"
&AdditionalParameter.Properties.Add(&CustomGAMProperty)

&AdditionalParameter.AuthenticationTypeName = &NameAuthType
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors)
```

After that, you just configure your authentication type in Authorization Tab:

Additional Parameters: DevId=$DeviceId&CusId=$CustomerId.

**Important:**The additional parameters shown above are based on the code example above, and are completely optional.

**Note**: The code shown in the previous example should be added to the events tab in your Login [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) in the [Login event](https://wiki.genexus.com/commwiki/wiki?19269).

### [Token tab](#Token+tab)

Configure the URL**(\*)** of the service to request the Token; this call is in the background and tries to obtain an Access Token.  
The response to this call is configured in the Response section.

Include Authorization header with Basic value: When performing an OAuth 2.0 authentication with a provider, it regularly requests only the Content-Type header to obtain the Token. However, some OAuth 2.0 providers (for example, Oracle Access Management - OAM) requests the Authorization header. This checkbox is for adding the Authorization header in base 64 (ClientId:ClientSecret in base 64).  
  
**(1)**Optionally, you can set GAM to validate the expiration of the Identity Provider's Access Token. In that case, when the Access token is refreshed, GAM renews the session automatically and the user doesn't need to log in again. This is done through the "Validate ExternalToken" checkbox.  
When the Provider returns a Refresh Token, you can configure the URL for this action (Refresh Token URL). If you don't configure a Refresh Token URL, the same URL**(\*)** configured above is used to request a Token.

`[imagen omitida: wiki id 39487]`

Additional Parameters: Lng=$language  
  
**Important:**The additional parameters shown above are based on the code example above, and are completely optional.  
  
If the Token is renewed, you can access it using the *GAMSession.ExternalToken* method. If the Token expires and doesn't refresh, the application logs out the user (the GAM Session ends).

### [User Information tab](#User+Information+tab)

Configure the service URL to obtain the authenticated user's data. This service is essential to be able to complete the application's authentication.  
The response is a JSON in which the user's data is obtained.

In some cases, the Provider fields need to be mapped to the GAM fields. For example, Gender Values: a string that maps the user's gender to the GAM conventions.

In GAM, M=male and F=female.

#### [Custom User Attributes](#Custom+User+Attributes)

For those attributes that cannot be mapped to any of the fields included in the User Information form, you can add a pair (Attribute Name, Attribute Tag). These attributes will be saved as [extended attributes](https://wiki.genexus.com/commwiki/wiki?19634) of the GAM user.

* Attribute Name: ID of the GAM extended user attribute, to be saved in the GAM database (you can retrieve the information using that ID).
* Attribute Tag: JSON service response tag that returns the user information corresponding to the attribute to be retrieved.

For example, the pair (Attribute Name = Amount, Attribute Tag = salaryAmount), means that the tag "salaryAmount" will be extracted from the response of the IDP, and that information will be saved as an extended attribute of the user using the "Amount" ID in the GAM table. This information can be retrieved using the [GAM User object extended attribute methods](https://wiki.genexus.com/commwiki/wiki?19634).

### [Roles and Signout Configuration](#Roles+and+Signout+Configuration)

To obtain roles from the external Identity Provider or to configure Single Logout, click **More Options**, and then **Additional Configuration**, as shown in the image below.

  
`[imagen omitida: wiki id 60960]`  
  
Once there, the TABS Roles and Signout will be available.  

### [Roles TAB](#Roles+TAB)

Configure the service URL to obtain the authenticated user's roles.   
  
`[imagen omitida: wiki id 60961]`

The properties listed under the “Include when calling the endpoint” category, if set to true, will be sent in the body of the request, except for those that specifically state that they will be sent in the URL or in the Header.  
  

**Note**: If it is necessary to send dynamic parameters in the service URL, this can be specified with “$”, for example: https://<idp\_domain>/api/$UserID/roles, and check the **Include user ID in the URL**  property .

It is also possible to obtain custom properties associated with the user's role:  
  
`[imagen omitida: wiki id 60964]`

Using GAM API, the code will be the following:

```
// Property Roles
&GAMPropertySimple = new()
&GAMPropertySimple.Id         = !"<Att_Name>"
&GAMPropertySimple.Value      = !"<Att_TAG>"    
GAMAuthenticationExternalUserRoles.SetProperty(&GAMAuthenticationTypeOAuth20.Name, &GAMPropertySimple, &GAMErrorCollection)
&GAMPropertySimple = new()
&GAMPropertySimple.Id         = !"<Att_Name2>"
&GAMPropertySimple.Value      = !"<Att_TAG2>"    
GAMAuthenticationExternalUserRoles.SetProperty(&GAMAuthenticationTypeOAuth20.Name, &GAMPropertySimple, &GAMErrorCollection)
```

### [Signout TAB](#Signout+TAB)

Configure the service URL to trigger the Signout against the external Identity Provider.  
  
`[imagen omitida: wiki id 60966]`  
  
In this service, you can configure whether to send the token from the external IDP in the header or in the body. You can also specify the redirect URL that the IDP will call when the sign-out process is completed.

### Configuration by provider

[Azure Active Directory](https://wiki.genexus.com/commwiki/wiki?48906)

[Facebook Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54310,,)

[Google Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54309,,)

[Instagram Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54307,,)

[LinkedIn Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54308,,)

[Mercado Libre Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54306,,)

[Office 365 Configuration](https://wiki.genexus.com/commwiki/wiki?39166)

[WeChat Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?54311,,)

### [See Also](#See+Also)

[HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493)  
[External ID property of GAMUser object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21734,,)


|  |
| --- |
| **Backlinks** |
| [Application Registration in Azure Active Directory](https://wiki.genexus.com/commwiki/wiki?42055) | [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) |
| [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59831) | [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60769) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Authenticate to Azure Active Directory using GAM (GeneXus 18 Upgrade 2 or pior)](https://wiki.genexus.com/commwiki/wiki?54393) | [HowTo: Authenticate to Azure Active Directory using GAM (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55881) | [HowTo: Authenticate to Azure AD using OpenID Connect with GAM](https://wiki.genexus.com/commwiki/wiki?55121) |
| [HowTo: Authenticate to Azure AD using OpenID Connect with GAM (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?60566) | [HowTo: Authenticate to Microsoft Entra ID using GAM](https://wiki.genexus.com/commwiki/wiki?48906) | [HowTo: Authenticate to Office 365 using GAM](https://wiki.genexus.com/commwiki/wiki?39166) | [HowTo: Configure OAuth 2.0 authentication with Azure AD (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55882) |
| [HowTo: Configure OAuth 2.0 authentication with Microsoft Entra ID](https://wiki.genexus.com/commwiki/wiki?54371) | [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) | [OAuthAccessCodeExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58098) | [OAuthRefreshTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58097) |
| [Security Client ID property](https://wiki.genexus.com/commwiki/wiki?21484) |

---
