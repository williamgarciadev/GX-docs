---
title: "Users enabled or disabled in the GAM Repository"
source_id: 21042
source_url: https://wiki.genexus.com/commwiki/wiki?21042
genexus_version: "18"
---

# Users enabled or disabled in the GAM Repository

A [GAM](https://wiki.genexus.com/commwiki/wiki?24746) user can be enabled in more than one [Repository](https://wiki.genexus.com/commwiki/wiki?17568), and its purpose is to let the user connect to any of the repositories where he is enabled.

A User can connect to a repository only if he's enabled on it, and can connect to only one repository at a time. The [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521), [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) and [Roles](https://wiki.genexus.com/commwiki/wiki?17569) are taken from the [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) of the Repository he is connected to.

One possible scenario where a user is enabled on more than one repository is when a company has different branches, and the user connects to any of the branches using the same credentials (he may have different access levels in each company). See [Multiple Repository Scenario: A company with different branches](https://wiki.genexus.com/commwiki/wiki?18709,,) for details on this scenario.

### [How to enable a User in a GAM Repository](#How+to+enable+a+User+in+a+GAM+Repository)

The condition for a user to be enabled in a repository is that he has the same Namespace as the repository.

Users can only be created in a repository if the [GAM connection](https://wiki.genexus.com/commwiki/wiki?16150) is established in that repository. Then, the user's Namespace is always initialized with the [Repository's Namespace](https://wiki.genexus.com/commwiki/wiki?18678,,) where he is created.

By default, users are automatically enabled in the repository where they are created.

Additionally, a user can be enabled on any other repository as long as the repository has the same namespace as the user.

### [Example: Get the enabled / disabled users or all users of a repository](#Example%3A+Get+the+enabled+%2F+disabled+users+or+all+users+of+a+repository)

Take a look at the GAMExampleWWUsers object. There, the users are listed, regardless if they are enabled or not in the repository, and they are displayed with a different look and feel in each case.

If you want to list only the enabled users, only the disabled users, or all, use the *IsEnabledInRepository* property of the *GAMUserFilter* object, as shown in the following code:

```
&Filter_Name.IsEnabledInRepository = GAMBooleanFilter.False //Domain type whose values are TRUE, FALSE, ALL
&Users= GAMRepository.GetUsersOrderBy(&Filter_Name, GAMUserListOrder.None, &Errors)
```

### [Example: Enable or disable a user in a repository](#Example%3A+Enable+or+disable+a+user+in+a+repository)

The code to enable or disable a user in the current GAM Repository (where the GAM connection is established) is as follows:

```
&User.Load(&UserId)        
If &User.IsEnabledInRepository
    &isOK = &User.RepositoryDisable(&Errors)            
Else
    &isOK = &User.RepositoryEnable(&Errors)                
EndIf

If not &isOK
    For &Error in &Errors
        Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
    EndFor
EndIf
```

Note that the objective of the *IsEnabledRepository* property of the GAMUser object is to know whether or not a user is enabled on the GAM Repository. It returns a Boolean data type.

```
&User.Load(&UserId) //&UserId is GAMGUID data type
&IsEnabledInRepository = &User.IsEnabledInRepository
```

### [See Also](#See+Also)

[User Activation Method Repository property](https://wiki.genexus.com/commwiki/wiki?18932)


|  |
| --- |
| **Backlinks** |
| [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) |
| [User Activation Method Repository property](https://wiki.genexus.com/commwiki/wiki?18932) |

---
