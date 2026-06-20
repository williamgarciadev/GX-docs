---
title: "HowTo: Use an environment variable to establish repository connections in GAM"
source_id: 59028
source_url: https://wiki.genexus.com/commwiki/wiki?59028
genexus_version: "18"
---

# HowTo: Use an environment variable to establish repository connections in GAM

This article explains how to use an environment variable to establish [repository connections](https://wiki.genexus.com/commwiki/wiki?16150) in [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

## [Description](#Description)

By default, GAM tries to connect with the repository using an environment variable. If it is not defined, it will use the connection.gam file.

In some scenarios, storing the connection key (the information needed to connect to the repository) in an environment variable is useful. For this, GAM provides the environment variable called GX\_GAMCONNECTIONKEY, in which you can assign the value contained in the KEY tag found in the connection.gam file.

## [How to get the connection key](#How+to+get+the+connection+key)

The connection key to the repository can be obtained in two ways:

#### [**1. Get the connection key from the connection.gam file.**](#1.+Get+the+connection+key+from+the+connection.gam+file.+)

First, locate the connection.gam file (under the KB 'web' folder). Open this file with a text editor and copy the value contained in the KEY tag.

```
<?xml version="1.0" encoding="UTF-8"?>
<Connection xmlns="">
         <key>cb831888-bd6e-4ddf-8a37-cdecaf7cbaf7</key>
</Connection>
```

Sample of how to set environment variables in Docker:

```
docker run -e GX_GAMCONNECTIONKEY="cb831888-bd6e-4ddf-8a37-cdecaf7cbaf7".
```

This allows you, for example, when deploying to Docker, to configure the connection key to be used for that instance of the container.

#### [**2. From the database**](#2.+From+the+database)

The repository connection information is stored in the SysConnectionConfig table. Therefore, if you want to obtain the connection key, the query should be as follows:

```
SELECT SysConnCfgKey FROM [gam].[SysConnectionConfig].
```

**Note**: The scheme is not used by all DBMSs. This is a general example.

## [Availability](#Availability)

Since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [GAM Deploy Tool command line (Windows and Unix-like operating systems)](https://wiki.genexus.com/commwiki/wiki?37764) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
