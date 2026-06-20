---
title: "HowTo: Configure OAuth 2.0 authentication with Azure AD (GeneXus 18 Upgrade 5 or prior)"
source_id: 55882
source_url: https://wiki.genexus.com/commwiki/wiki?55882
genexus_version: "18"
---

# HowTo: Configure OAuth 2.0 authentication with Azure AD (GeneXus 18 Upgrade 5 or prior)

**Note**: As of July 2023, Microsoft changed the name of its Azure Active Directory product to Microsoft Entra ID.

**Warning**: This sample shows how to use GAM with Microsoft Entra ID as an external OAuth 2.0 provider. GeneXus does not support the configuration of this external system. Samples, screenshots, parameters, and/or locations may change over time.

This article explains how to configure [OAuth 2.0 authentication](https://wiki.genexus.com/commwiki/wiki?39484) with Azure AD. In the OAuth 2.0 authentication type, you can find a new option called IDP that lets you switch from default to Azure. If you select Azure, all the fields will be filled automatically and you will only have to configure the following properties:

`[imagen omitida: wiki id 54372]`

```
Client ID:     client_id         Value: <clientid>
Client Secret: client_secret     Value: <clientsecret>
Redirect URL:  redirect_uri      Value: https://<server>/webapp
```

**Note**: To learn where you can find these parameters, please read the [Azure AD article](https://wiki.genexus.com/commwiki/wiki?48906).

### [Authorization Tab](#Authorization+Tab)

`[imagen omitida: wiki id 54373]`

In the link https://login.microsoftonline.com/**{tenat}**/oauth2/v2.0/authorize you must change **{tenat}** with your tenat.

See yours in the following panel.

`[imagen omitida: wiki id 48915]`

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).

## [See Also](#See+Also)

[HowTo: Authenticate to Microsoft Entra ID using GAM](https://wiki.genexus.com/commwiki/wiki?48906)
