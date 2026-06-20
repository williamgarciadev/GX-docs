---
title: "How to configure an Oracle .Net Environment"
source_id: 28463
source_url: https://wiki.genexus.com/commwiki/wiki?28463
genexus_version: "18"
---

# How to configure an Oracle .Net Environment

This article describes the requirements and configurations required to run an application with the [GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892).

Suppose you have Oracle 11g installed on the computer named "Oracle11g," with a schema named "ARTF69456" and SID "test11g.artech.local."

The steps to follow are described below:

1. Install the ADO .NET provider or the Oracle client.

**Note**: ADO.NET support is not installed with the Instant Client. It is necessary to install the full client (which includes the Network folder with the Oracledataaccess.dll).

2. Edit **tnsnames.ora**, where you must describe the Oracle client you want to access from your application. This file is usually found below the Oracle client installation, for example: C:\oracle\product\10.2.0\client\_1\NETWORK\ADMIN.

```
<ServerName> =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = <host>)(PORT = <port>))
    )
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = <service name>)
    )
  )
```

**Where:**

*ServerName:*  
    Any name given by you to identify your Oracle client; for example, "Oracle11."

*host*  
    Name or IP of the computer where the Oracle client is installed; for example, "oracle11g."

*port*  
    Port where the Oracle client listens for ADO .NET connections; for example, "1521."

*service name*  
    SID, for example, "test11g.artec.local."

**Note**: This file can be edited with any text editor such as Notepad, or by using a utility that comes with the Oracle client when it is installed.

3. Configure the Data Store in the .Net Environment, as follows:

```
Server Name = Oracle11   //it must be the server name configured in the previous item
User id = ARTF69456
User password = ****
```

If you haven’t configured the [Environment](https://wiki.genexus.com/commwiki/wiki?7115) or the Oracle client, this error will be displayed:

```
ORA-12514: TNS:Listener does not currently know of service requested in connect descriptor
```

4. Compatibility of 32-bit and 64-bit Oracle clients

Installing 32-bit and 64-bit Oracle clients on the same machine is not recommended. Instead, you should select one of them depending on your needs. When using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), it is recommended to install the 32-bit client because the database reorganizations are generated with that client.
