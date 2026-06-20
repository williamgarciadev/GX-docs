---
title: "SMTP server (for mail functions) property"
source_id: 9113
source_url: https://wiki.genexus.com/commwiki/wiki?9113
genexus_version: "18"
---

# SMTP server (for mail functions) property

The SMTP protocol (MAPI is not supported) is used to send emails.

### [Description](#Description)

Kept for backwards compatibility with version 6.1 (and higher) of GeneXus.

You will need to indicate which SMTP server will be used. If you have not specified any server and you are executing the application as an applet, attempts are made to use the same server that performs web server functions.

With higher versions of GeneXus it is no longer necessary to complete this property, since emails are handled in another way.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(Java)
