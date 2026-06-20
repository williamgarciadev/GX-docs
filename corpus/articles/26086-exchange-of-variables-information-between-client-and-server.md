---
title: "Exchange of variables information between client and server side in GeneXus"
source_id: 26086
source_url: https://wiki.genexus.com/commwiki/wiki?26086
genexus_version: "18"
---

# Exchange of variables information between client and server side in GeneXus

GeneXus automatically keeps the state of some variables when an web object is executed.

This means that some variables may be exchanged between the client and server side even if they are not present on the screen.

This behavior applies when a variable:

* is used on the Refresh event or any other user event
* is used as In or Inout parameter in a Call or UDP command.

In this case, the variable will be exchanged automatically by GeneXus in all communications between the server and client side.   
An internal variable called GXstate will keep track of the variable value during the client-server exchange.
