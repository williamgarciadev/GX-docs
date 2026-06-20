---
title: "Troubleshooting 'Execution failed' message when running a Web app"
source_id: 49557
source_url: https://wiki.genexus.com/commwiki/wiki?49557
genexus_version: "18"
---

# Troubleshooting 'Execution failed' message when running a Web app

This article guides you through the steps you should follow when you [run](https://wiki.genexus.com/commwiki/wiki?5692) a web app and the following error appears

```
Could not reach web server or something went wrong running your application at <URL> please try again.
The request was aborted: The operation has timed out..
```

The steps you should follow depend on the environment and feature you are using

### [[Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046)](#wiki%3F15046%2CCategory%253ACloud%2Bprototyping+Cloud+prototyping)

If it occurs in an environment that uses Cloud prototyping:

1. Check that you followed these steps: [Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250)
2. Apply the solutions provided in [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292)

If you're still in trouble:

* Contact gxtrial@genexus.com if you are using the GeneXus Trial edition
* Contact support at <http://genexus.com/issuetracking> if you are a GeneXus client

## [Local Prototyping (Java)](#Local+Prototyping+%28Java%29)

If it occurs in an environment that uses a local Tomcat installation, check the following

* Is Tomcat running? If not, start it
* Check if [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) corresponds to the version of your Tomcat installation

If you're still in trouble:

* Contact support at <http://genexus.com/issuetracking>

## [Local Prototyping (.NET)](#Local+Prototyping+%28.NET%29)

If it occurs in a .NET environment, check the following

* Check which Web Server you configured in the [Web Server property](https://wiki.genexus.com/commwiki/wiki?9017)
* If you use the Kestrel web server, close the corresponding window and run again. If the problem persists, check if the Kestrel window shows some error details.
* If [Protocol specification property](https://wiki.genexus.com/commwiki/wiki?8079) is set to HTTPS, check [How to configure Https when prototyping .NET applications](https://wiki.genexus.com/commwiki/wiki?48174,,)

If you're still in trouble:

* Contact your instructor if you are using GeneXus Trial (Learning Edition)
* Contact support at <http://genexus.com/issuetracking> if you are a GeneXus customer
