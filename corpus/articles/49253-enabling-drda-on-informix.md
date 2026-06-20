---
title: "Enabling DRDA on Informix"
source_id: 49253
source_url: https://wiki.genexus.com/commwiki/wiki?49253
genexus_version: "18"
---

# Enabling DRDA on Informix

Since version 11.x, Informix supports the DRDA protocol. If you plan to connect to Informix using [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) you must enable DRDA support as described in [IBM Informix Developer's Handbook](https://www.redbooks.ibm.com/redbooks/pdfs/sg247884.pdf).

Here is an example for Linux:

**1.**Edit the sqlhosts file specified in the $INFORMIXSQLHOSTS (or  $SQLHOSTS) environment variable, for example **/opt/informix/etc/sqlhosts**, and add a line for DRDA (drsoctcp):

```
#dbservername    nettype       hostname      servicename      options
informixfullgx   onsoctcp   172.16.0.205   informix
informix_drda    drsoctcp   172.16.0.205   informix_drda
```

**2.** Edit the Informix Server configuration file located in the etc directory to include the new database definition as an alias. You can use the environment variable $ONCONFIG to access this file, e.i. $INFORMIXDIR/etc/$ONCONFIG  for example **/opt/informix/etc/onconfig**:

```
DBSERVERNAME    informixfullgx
DBSERVERALIASES informix_drda
```

**3.** Edit **/etc/services** and specify the port:

```
informix        9088/tcp # Informix server
informix_drda   9094/tcp # Informix server drda
```

**4.** Restart Informix Server for these changes to take effect. And set [Server TCP/IP Port](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9382,,) property in DataStore with the value 9094.

**Note: If the application throws the error**

**ERROR 08001 IBM SQL30081N A communication error has been detected. Communication protocol being used: "TCP/IP". Communication API being used: "SOCKETS". Location where the error was detected: "172.16.0.205". Communication function detecting the error: "connect". Protocol specific error code(s): "10060", "\*", "\*". SQLSTATE=08001**

Make sure the firewall on Linux allows the port used by DRDA. In the example 9094.

Example of configuring the firewall to allow port 9094:

```
root@fullgxinformix12 # firewall-cmd --list-ports
9088/tcp
root@fullgxinformix12 # firewall-cmd --add-port 9094/tcp
success
root@fullgxinformix12 # firewall-cmd --list-ports
9088/tcp 9094/tcp
root@fullgxinformix12 # firewall-cmd --permanent --add-port 9088/tcp
Warning: ALREADY_ENABLED: 9088:tcp
success
root@fullgxinformix12 # systemctl stop firewalld
root@fullgxinformix12 # systemctl start firewalld
root@fullgxinformix12 # firewall-cmd --list-ports
9088/tcp 9094/tcp
```


|  |
| --- |
| **Backlinks** |
| [.NET Generator Requirements](https://wiki.genexus.com/commwiki/wiki?38605) | [.NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55956) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?58946) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55768) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |

---
