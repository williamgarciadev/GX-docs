---
title: "GAM - How to revoke tokens from external IDPs"
source_id: 51085
source_url: https://wiki.genexus.com/commwiki/wiki?51085
genexus_version: "18"
---

# GAM - How to revoke tokens from external IDPs

When a user [is removed from a GAM application](https://wiki.genexus.com/commwiki/wiki?22082), the user's tokens should be revoked from external IDPs.

To achieve this requirement, the different Identity Providers have endpoints.

The following Procedures solve the need for some external IDPs. These Procedures and their invocations must be defined by the GeneXus developer.

It is necessary to pass the &UserGUID variable as input to the Procedures containing the user whose token should be revoked. This makes it possible to make the invocation for the same logged-in user or as an administrator passing the GUID of the user to be deleted.

### [Apple](#Apple)

```
&AuthenticationTypeName = "apple"
//Get the Apple tokens for the user and fetch the last one
&GAMSessionLogFilter.UserGUID = &UserGUID
&GAMSessionLogFilter.AuthenticationTypeName = &AuthenticationTypeName
&GAMSessionLogCollection = GAMRepository.GetSessionLogsOrderBy(&GAMSessionLogFilter, GAMSessionLogListOrder.Date_Desc, &Errors)
//Load of the authentication type is performed to obtain the client id and secret
&GAMAuthenticationTypeApple.Load(&AuthenticationTypeName)
For &GAMSessionLog in &GAMSessionLogCollection
    If not &GAMSessionLog.ExternalToken.IsEmpty()
        Do "AppleRevoke"
        Exit
    EndIf
EndFor

Sub "AppleRevoke"
    //DOC: https://developer.apple.com/documentation/sign_in_with_apple/revoke_tokens
    &HttpClient.Host = !"appleid.apple.com"
    &httpClient.Secure    = 1
    &httpClient.AddHeader(!"Content-Type", !"application/x-www-form-urlencoded")
    &HttpClient.AddVariable(!"client_id", &GAMAuthenticationTypeApple.Apple.ClientId.ToString())
    &HttpClient.AddVariable(!"client_secret", &GAMAuthenticationTypeApple.Apple.ClientSecret.ToString())
    &HttpClient.AddVariable(!"token",&GAMSessionLog.ExternalToken)
    &HttpClient.AddVariable(!"token_type_hint",!"access_token")
    &HttpClient.Execute(HttpMethod.Post, !"/auth/revoke")
    If &httpClient.StatusCode = 200
        //OK
    Else
        Msg(Format("Error when trying to revoke %1 token %2:%3 - %4 ", &AuthenticationTypeName, &httpClient.StatusCode, &httpClient.ErrDescription, &httpClient.ToString()), status)
    EndIf
EndSub
```

### [Google](#Google)

```
&AuthenticationTypeName = "google"
//Get the Google tokens for the user and fetch the last one
&GAMSessionLogFilter.UserGUID = &UserGUID
&GAMSessionLogFilter.AuthenticationTypeName = &AuthenticationTypeName
&GAMSessionLogCollection = GAMRepository.GetSessionLogsOrderBy(&GAMSessionLogFilter, GAMSessionLogListOrder.Date_Desc, &Errors)
For &GAMSessionLog in &GAMSessionLogCollection
    If not &GAMSessionLog.ExternalToken.IsEmpty()
        Do "GoogleRevoke"
        Exit
    EndIf
EndFor

Sub "GoogleRevoke"
    //DOC: https://developers.google.com/identity/protocols/oauth2/web-server#tokenrevoke
    &HttpClient.Host = !"oauth2.googleapis.com"
    &httpClient.Secure    = 1
    &httpClient.AddHeader(!"Content-Type", !"application/x-www-form-urlencoded")
    &HttpClient.Execute(HttpMethod.Post, !"/revoke?token=" + &GAMSessionLog.ExternalToken)
    If &httpClient.StatusCode = 200
        //OK
    Else
        Msg(Format("Error when trying to revoke %1 token %2:%3 - %4 ", &AuthenticationTypeName, &httpClient.StatusCode, &httpClient.ErrDescription, &httpClient.ToString()), status)
    EndIf
EndSub
```

### [Azure](#Azure)

```
&AuthenticationTypeName = "azure"
//Get the Azure tokens for the user and fetch the last one
&GAMSessionLogFilter.UserGUID = &UserGUID
&GAMSessionLogFilter.AuthenticationTypeName = &AuthenticationTypeName
&GAMSessionLogCollection = GAMRepository.GetSessionLogsOrderBy(&GAMSessionLogFilter, GAMSessionLogListOrder.Date_Desc, &Errors)
&GAMAuthenticationTypeOauth20.Load(&AuthenticationTypeName)
For &GAMSessionLog in &GAMSessionLogCollection
    If not &GAMSessionLog.ExternalToken.IsEmpty()
        Do "AzureRevoke"
        Exit
    EndIf
EndFor

Sub "AzureRevoke"
    //DOC: https://docs.microsoft.com/en-us/graph/api/user-revokesigninsessions?view=graph-rest-1.0&tabs=http
    &HttpClient.Host = !"graph.microsoft.com"
    &httpClient.Secure    = 1
    &httpClient.AddHeader(!"Content-Type", !"application/json")
    &httpClient.AddHeader(!"Authorization", &GAMSessionLog.ExternalToken)
    &GAMUser = GAMUser.GetByGUID(&UserGUID,&GAMErrorCollection)
    If not &GAMUser.GetExternalId().IsEmpty()
        &HttpClient.Execute(HttpMethod.Post, !"/v1.0/users/" + &GAMUser.GetExternalId() + !"/revokeSignInSessions")
        If &httpClient.StatusCode = 200
            //OK
        Else
            Msg(Format("Error when trying to revoke %1 token %2:%3 - %4 ", &AuthenticationTypeName, &httpClient.StatusCode, &httpClient.ErrDescription, &httpClient.ToString()), status)
        EndIf
    EndIf
EndSub
```

[Download the .xpz file that contains the Procedures](https://wiki.genexus.com/commwiki/wiki?51086,,)

### [IDPs Documentation](#IDPs+Documentation)

* **Apple:**<https://developer.apple.com/documentation/sign_in_with_apple/revoke_tokens>
* **Azure:** <https://docs.microsoft.com/en-us/graph/api/user-revokesigninsessions?view=graph-rest-1.0&tabs=http>
* **Google:**<https://developers.google.com/identity/protocols/oauth2/web-server#tokenrevoke>
* **Facebook:** (search invalidate a token) <https://developers.facebook.com/docs/pages/access-tokens/?locale=es_LA#get-a-short-lived-user-access-token>
* **Twitter:**<https://developer.twitter.com/en/docs/authentication/api-reference/invalidate_bearer_token>

### 

### [See Also](#See+Also)

[Users Deletions in GAM](https://wiki.genexus.com/commwiki/wiki?22082)


|  |
| --- |
| **Backlinks** |
| [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) |

---
