---
title: "Web sessions also work outside the web environment"
source_id: 29896
source_url: https://wiki.genexus.com/commwiki/wiki?29896
genexus_version: "18"
---

# Web sessions also work outside the web environment

Web sessions ([WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321)) are used to store data about the context in which the application runs. This allows objects to set and get information from the context instead of using parameters in calls.

In a web environment (when a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is executed, for example), these web sessions rely on the web server's session, the use of cookies, etc.

But what happens if the application does not run in that environment?

For example, if instead of being a Web object running on IIS, it is a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) running from the command line.

In this case, the web session is still valid and retains the same functionality. Instead of being implemented on the web server/cookies, it is implemented in a memory structure, but the functional result is the same. Values can be set and retrieved: you can set and get the values.

This way, an object that retrieves session values can be executed both when called from a Web Panel and from a command line Procedure, without altering its logic or duplicating it depending on the environment in which it is invoked.

In this XPZ, you can see a simplified usage example: [Web session sample using command line procedure](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29900,,).
