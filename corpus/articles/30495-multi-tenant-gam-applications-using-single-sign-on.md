---
title: "Multi-tenant GAM applications using Single Sign On"
source_id: 30495
source_url: https://wiki.genexus.com/commwiki/wiki?30495
genexus_version: "18"
---

# Multi-tenant GAM applications using Single Sign On

Multi-tenancy is an architecture in which a single instance of a software application serves multiple customers.

If you combine it with GAM Single Sign On (SSO); you will have a multi-tenant solution with a centralized and isolated way to authenticate users. SSO is supported for Web applications only.

Note that the GAM can be used as an identity provider regardless it implements a SSO or not. The GAM remote authentication type is supported for both, Web and SD apps. See [GAM Remote Authentication type for Smart Devices](https://wiki.genexus.com/commwiki/wiki?29672).

## [How Multi-tenancy and SSO works](#How+Multi-tenancy+and+SSO+works)

To solve this scenario (SSO + multi-tenancy) you need to combine two GAM features:

* [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385)
* [Howto: Multitenant applications using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?30482,,)

The GAM Identity Provider will need to configure n repositories to keep track of each tenant.

Read the configuration details [here](https://wiki.genexus.com/commwiki/wiki?30482,,).

### [See Also](#See+Also)

(1) [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355)  
(2) [GAM SSO flow of execution](https://wiki.genexus.com/commwiki/wiki?28106,,)  
(3) [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385)  
(4) [Howto: Multitenant applications using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?30482,,)
