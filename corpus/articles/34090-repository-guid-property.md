---
title: "Repository GUID property"
source_id: 34090
source_url: https://wiki.genexus.com/commwiki/wiki?34090
genexus_version: "18"
---

# Repository GUID property

It's a property of the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) which allows configuring the Repository GUID of any Repository of the GAM Ident  ity Provider in a multitenant architecture.

When the [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) is used in a multitenant scenario, in the client Application, you can configure which is the Identity Provider's Repository to connect to. This should be done in the GAMRemote Authentication Type configuration of the client application.

See [Howto: Multitenant applications using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?30482,,) for detailed information on this topic.

The property belongs to the GAMAuthenticationGAMRemote object.

`[imagen omitida: wiki id 34135]`

See how to use it programmatically in the GAMExampleAuthenticationTypeEntry object (which is part of the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)):

```
&AuthenticationTypeGAMRemote.GAMRemote.RemoteRepositoryGUID    = &GAMRRepositoryGUID
```
