---
title: "Servers available for Cloud prototyping (GeneXus 18 Upgrade 13 or prior)"
source_id: 60513
source_url: https://wiki.genexus.com/commwiki/wiki?60513
genexus_version: "18"
---

# Servers available for Cloud prototyping (GeneXus 18 Upgrade 13 or prior)

Below is a list of servers available for [Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046).

The possible values for the [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042) vary depending on the generator and the GeneXus version you are using.

| Servers | Generators | Available DBMSes | Web Server | GeneXus Versions | Region | Server  Health | IaaS Provider |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sandbox5.genexus.com | .NET | MySQL, SQL Server | IIS 8 | GeneXus 18 Upgrade 10 onwards (Default) | US East (Northern Virginia) Region | [Check](https://sandbox5.genexus.com/gxcloud/status) | AWS |
| trialapps3.genexus.com | .NET | SQL Server | IIS 8 | GeneXus X Evolution 3 Trial onwards (Default) | US East (Northern Virginia) Region | [Check](https://trialapps3.genexus.com/gxcloud/status) | AWS |
| sandbox6.genexus.com | JDK8 | MySQL 5.7 | Apache Tomcat 8.0 | GeneXus 18 Upgrade 10 onwards (Default) | USA | [Check](https://sandbox6.genexus.com/gxcloud/status) | AWS |

**Note**: All servers include SSL support. For more information, see [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042).

Angular frontend applications are deployed to a dedicated cloud server for prototyping purposes, independently of the backend cloud server. This server is "https://sandbox-angular.genexus.com".
