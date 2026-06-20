---
title: "GAM - Security Policies"
source_id: 18521
source_url: https://wiki.genexus.com/commwiki/wiki?18521
genexus_version: "18"
---

# GAM - Security Policies

GAM Security Policies define access control rules for [Users](https://wiki.genexus.com/commwiki/wiki?22082) and [Roles](https://wiki.genexus.com/commwiki/wiki?17569) to ensure secure interaction with Applications. These policies govern sessions, tokens, and password requirements.

GAM security policies can be configured in two ways:

* Through the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)
* Programmatically via the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

When using the GAM Web Backoffice, you can add or update a Security Policy. For detailed steps, see [GAM Web Backoffice - Security Policies section](https://wiki.genexus.com/commwiki/wiki?61029).

At runtime, the applicable security policy for a user is determined according to the following precedence:

## [How GAM determines which Security Policy applies to a User](#How+GAM+determines+which+Security+Policy+applies+to+a+User+)

#### **1. Security policy assigned to the user.**

Each GAM user can have one security policy assigned to them or none at all.

To assign or update a user's security policy in the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), go to the [Users section](https://wiki.genexus.com/commwiki/wiki?60983) and edit the user properties (as shown in Figure 2).

`[imagen omitida: wiki id 58093]`

###### [Figure 2.](#Figure+2.)

Programmatically, you can retrieve a user's security policy with the SecurityPolicyId property of the GAMUser object.

```
&User.Load(&UserId) //&User is GAMUser object, &UserId is GAMGUID data type
&SecurityPolicyId   = &User.SecurityPolicyId //&SecurityPolicyId is GAMKeyNumShort data type.
```

**2. If the user has no associated Security Policy, the one assigned to their Main Role is used.**

If the user doesn't have a security policy assigned, the policy applied at runtime will be the one associated with their Main Role. See [GAM Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) for more information.

To check or update this in the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), go to the [Users section](https://wiki.genexus.com/commwiki/wiki?60983), select the user, and review their main role (only one role can be set as Main Role at a time).

`[imagen omitida: wiki id 52491]`

###### [Figure 3. Main Role of the User, in this example it's "Role1".](#Figure+3.+Main+Role+of+the+User%2C+in+this+example+it%27s+%22Role1%22.+)

By editing the role's properties, you can see the security policy of the role (which can be "none").

`[imagen omitida: wiki id 52492]`

###### [Figure 4. Security Policy assigned to a role](#Figure+4.+Security+Policy+assigned+to+a+role)

You can also retrieve the Security Policy of the role with the SecurityPolicyId property of the GAMRole object.

```
&Role.Load(&Id)//&Role is GAMRole, &Id is GAMKeyNumLong
&SecPolId = &Role.SecurityPolicyId //&SecPolId is GAMKeyNumShort data type
```

**3. If none of the above, but the user has other roles assigned, GAM applies the Security Policy of the Default Repository Role.**

`[imagen omitida: wiki id 58099]`

#### **4. If none of the above, the default Security Policy of the Repository is used.**

If the user has no security policy assigned, the security policy applied is the Default Security Policy of the Repository.

###### Figure 5. Default Security Policy of the Repository

The DefaultSecurityPolicyId property of the GAMRepository object indicates the default security policy of the repository.

```
&Repository.Load(&Id) //&Repository is GAMRepository, &Id is GAMKeyNumLong data type
&DefaultSecurityPolicyId  = &Repository.DefaultSecurityPolicyId //&DefaultSecurityPolicyId is GAMKeyNumShort data type
```

**Note:** When setting a value higher than 0 for the property MinimumSpecialCharactersPassword, the following regular expression is used:

```
&UserPassword.Matches(!"[^\d\w]")
```

Which means:

\w [a-zA-Z0-9\_] (literal or digit or underscore)  
\d [0-9] (digit)  
^ not

So, the regular expression means all that is NOT \d\w

### [See Also](#See+Also)

[GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569)  
[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338)  
[GAM Web Backoffice - Security Policies section](https://wiki.genexus.com/commwiki/wiki?61029)


|  |
| --- |
| **Backlinks** |
| [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013) | [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) | [GAM - Main Role of a user](https://wiki.genexus.com/commwiki/wiki?21643) |
| [GAM - Multiple Repositories Scenarios](https://wiki.genexus.com/commwiki/wiki?18682) | [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817) | [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60761) | [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56244) |
| [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) | [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) | [GAM architecture for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?14978) |
| [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GAM Web Backoffice - Security Policies section](https://wiki.genexus.com/commwiki/wiki?61029) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218) |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [HowTo: Filter data by user using the GAM API](https://wiki.genexus.com/commwiki/wiki?15387) | [OAuth Token expire (minutes) GAM Security Policy property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58155) |
| [OAuthRefreshTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58097) | [Users enabled or disabled in the GAM Repository](https://wiki.genexus.com/commwiki/wiki?21042) |

---
