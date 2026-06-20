---
title: "HowTo: Connect to GAM Manager Repository"
source_id: 18625
source_url: https://wiki.genexus.com/commwiki/wiki?18625
genexus_version: "18"
---

# HowTo: Connect to GAM Manager Repository

GAM Manager Repository is a particular repository used to administer the rest of the repositories, and users of this repository are the only ones who can create new repositories and manage them.

This document explains how to connect to "GAM Manager Repository".

The [GAM Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) to "GAM Manager Repository" already exists in the GAM database.

### [How to connect to GAM Manager Repository using GAM Backend as it is](#How+to+connect+to+GAM+Manager+Repository+using+GAM+Backend+as+it+is)

**1.** Connect to [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) using "gamadmin".

You should create an entry in the SysConnectionConfig table (in the GAM database) with the GAM Repository Connection to "GAM Manager Repository". The way to do this is through the [GAMDeployTool](https://wiki.genexus.com/commwiki/wiki?18608). See [GAM Deploy Tool: Creating the connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610).

`[imagen omitida: wiki id 48663]`

###### [Figure 1. GAMDeployTool, create connection.gam file with a connection to GAM Manager Repository.](#Figure+1.+GAMDeployTool%2C+create+connection.gam+file+with+a+connection+to+GAM+Manager+Repository.)

After obtaining the connection.gam file, copy it to the virtual directory (or root of the web app for JAVA applications). Now you are able to connect to the "GAM Manager Repository".

**2.** If the only connection associated with the key contained in the connection.gam file is "GAM Manager Repository", you can log in using "gamadmin", and connect directly to "GAM Manager Repository".

`[imagen omitida: wiki id 48661]`

###### [Figure 2. Login using "gamadmin".](#Figure+2.+Login+using+%22gamadmin%22.)

If the connection key has more than one connection associated ("GAM Manager Repository" and another one), the application will connect to the default repository selected. By default, it is the master repository.

In that case, you can "Change working Repository" by going through this link in the GAM Backend.

`[imagen omitida: wiki id 48660]`

###### [Figure 3. Execute GAM Backend, go to "Change Working Repository" and select "GAM Manager Repository".](#Figure+3.+Execute+GAM+Backend%2C+go+to+%22Change+Working+Repository%22+and+select+%22GAM+Manager+Repository%22.)

```
If GeneXusSecurity.GAM.GetDefaultRepository(&RepositoryGUID)
     &isConnectionOK = GeneXusSecurity.GAM.SetConnectionByRepositoryGUID(&RepositoryGUID, &Errors)
Else
     &ConnectionInfoCollection = GeneXusSecurity.GAM.GetConnections()
     If &ConnectionInfoCollection.Count > 0
         //The first connection found is established by default
         &isConnectionOK = GeneXusSecurity.GAM.SetConnection(&ConnectionInfoCollection.Item(1).Name, &Errors)
     EndIf
Endif
```

The connection to the Repository is stored in the web session.

If the user is not enabled in the repository they are trying to connect to, an error is thrown: "User Unknown".

This error occurs at login:

```
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
```

So, after performing "Change Working Repository", the user who is logged in will be automatically logged out unless they are a user of GAM Manager Repository. When logged out, you can log in using "gamadmin" credentials, as shown in figure 2.

Now, you are working at "GAM Manager Repository". Once there you can add new administrator users, and perform all the tasks these users can (see: [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642)).

### [Some aspects to be considered](#Some+aspects+to+be+considered)

The [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935) uses the GAM API, so the objects distributed in GAM Library can be taken as examples of how to program the desired operations.

1. You can have the GAM backend published only to administrators of the GAM Manager Repository, so the connection key will need to associate only the connection to this Repository.

2. Otherwise, if the application installation is the same for all users (administrators, as well as non-administrator users) you need to associate the connection key with all the necessary connections. In the code, you need to set the connection to the corresponding [GAM Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) depending on the user who has signed in. See [HowTo: Get and Set GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?19245).

### [See Also](#See+Also)

[GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617)


|  |
| --- |
| **Backlinks** |
| [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) | [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) | [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) |

---
