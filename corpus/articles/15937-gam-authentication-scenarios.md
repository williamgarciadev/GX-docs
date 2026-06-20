---
title: "GAM - Authentication Scenarios"
source_id: 15937
source_url: https://wiki.genexus.com/commwiki/wiki?15937
genexus_version: "18"
---

# GAM - Authentication Scenarios

GeneXus Access Manager (GAM) provides robust authentication capabilities for applications, enabling secure access control through various scenarios.

All [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Authentication scenarios include the possibility of entering a username and password and validating this data against an existing Database.

Likewise, this Database, can be hosted in the application’s own Database or in standalone manner, according to the desired combination. Both options will depend on the selected way to use it or the company’s or client’s policies.

The modes to which the GAM can be applied to depend on the environment for which applications are developed or implemented. The options available are Web and Native Mobile.

### [Scenario 1 – Authentication in Web Applications](#Scenario+1+%E2%80%93+Authentication+in+Web+Applications)

In this scenario, users authenticate via a web screen using their username and password, validated against a designated database. This scenario supports the creation of new users and password management.

There are different possible scenarios, the following are some of them :

* #### [Applications where all their objects are private:](#Applications+where+all+their+objects+are+private%3A)

[GAM use Example: Private web application](https://wiki.genexus.com/commwiki/wiki?15923)

* #### [Public Applications with some private objects:](#Public+Applications+with+some+private+objects%3A)

[GAM Use Example: Public Application With Some Private Components](https://wiki.genexus.com/commwiki/wiki?15772)

### [Scenario 2 - Conversion from the traditional security mechanisms to GAM](#Scenario+2+-+Conversion+from+the+traditional+security+mechanisms+to+GAM)

If you already have your application which implements security in the traditional way, there are some tips to take into account in order to start using GAM. See [How to map Application users to GAM users in existing applications](https://wiki.genexus.com/commwiki/wiki?16552).

### [Scenario 3 - Authentication in Native Mobile Applications](#Scenario+3+-+Authentication+in+Native+Mobile+Applications)

At present, the importance of productive applications running on Native Mobile cannot be understated, given their explosive growth. However, even though developing applications with GeneXus for Native Mobile is relatively simple, you can't think of a productive, professional, and reliable application without any security features. One of the reasons why GeneXus includes GAM by default is the ability to quickly implement security for Native Mobile applications.

Like in Web Applications, in Native Mobile Applications one possible scenario is such that all of the Native Mobile objects are private. In another scenario, only some objects are private, and the other have public access.

See the following for details:

* [Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214)
* [Native Mobile Authentication](https://wiki.genexus.com/commwiki/wiki?15222)

### [Scenario 4 - Integrate with other applications, authenticate against the user’s repository of an external application.](#Scenario+4+-+Integrate+with+other+applications%2C+authenticate+against+the+user%E2%80%99s+repository+of+an+external+application.)

Authenticate users against external application repositories using GAM's External Authentication Type, ensuring integration across platforms.

For more information, see [GAM - External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755).

### [Scenario 5 - Interact with REST Web Services which are private](#Scenario+5+-+Interact+with+REST+Web+Services+which+are+private)

In addition to building Web applications and Native Mobile applications, GeneXus users can build [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) using [GeneXus X Evolution 2](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15152,,). Using GAM, these Web Services will be private, and only authorized users will be able to execute their methods.

See [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) for details.

### [Scenario 6 - More than one application connecting to the same GAM repository](#Scenario+6+-+More+than+one+application+connecting+to+the+same+GAM+repository)

In scenarios where multiple applications of the same company use the same repository, GAM allows for centralized user management and authentication.

See [HowTo: Use the same GAM Database by different applications](https://wiki.genexus.com/commwiki/wiki?16151).

### [Scenario 7 - GAM Multiple Repositories Scenarios](#Scenario+7+-+GAM+Multiple+Repositories+Scenarios)

Take as an example the scenario where a company has n branches, the same application runs in the different branches, but users have different privileges depending on the branch where the application runs.

In this case, the GAM database used will be only one, in order not to duplicate users information (and easy maintenance), but different roles have to be assigned to users depending on the branch where the application runs, so it's necessary to define multiple Repositories in GAM database.

See [GAM Multiple Repositories Scenarios](https://wiki.genexus.com/commwiki/wiki?18682) for details.

### [Scenario 8 - Using GAM as an Identity Provider (IDP)](#Scenario+8+-+Using+GAM+as+an+Identity+Provider+%28IDP%29)

There is the possibility to set a GeneXus Knowledge Base with GAM as an Identity Provider for other Knowledge Bases. This means that if you are already registered in for example KB "A "and want to access KB "B" without having to sign up in both of them, you can use the same user that is in “A” without having to register in “B”.

See [GAM remote authentication type](https://wiki.genexus.com/commwiki/wiki?25355) for details.

### [Scenario 9 - Using GAM as an Identity Provider (IDP) with other IDPs](#Scenario+9+-+Using+GAM+as+an+Identity+Provider+%28IDP%29+with+other+IDPs)

Also, users that use your KB as an IDP, will be able to authenticate themselves through the authentication types you have added to your KB.

For example, this means you have set a Google authentication to your web app “A”.   
Then, a user of web app “B” can select the Google authentication type of web app “A” to authenticate to “B”.  
When you are used as an IDP for the other KB, all users of the external KB will be able to authenticate to Google.

`[imagen omitida: wiki id 49306]`

See [GAM Authentication](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18456,,) to see all authentication types you can add to your web app.

### [See Also](#See+Also)

[GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
