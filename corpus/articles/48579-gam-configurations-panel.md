---
title: "GAM Configurations panel"
source_id: 48579
source_url: https://wiki.genexus.com/commwiki/wiki?48579
genexus_version: "18"
---

# GAM Configurations panel

This screen displays general information about the GAM, such as the schema version of the knowledge base database, and the GAM API version with which the binaries were compiled.  
In addition, there is an option to enable/disable the general GAM trace.

To access the GAM Configuration panel, go to *Settings > GAM Configurations*, to obtain (at first) the following view of the panel:  
`[imagen omitida: wiki id 48580]`  
This menu view corresponds to a knowledge base that has only one repository; that is, it isn’t multitenant.

If you authenticate to the GAM backend, to the GAMManager repository, or if the repository has the property [Enable working as GAMManager repository](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44937,,) enabled, additional options will be enabled which are shown below:

`[imagen omitida: wiki id 48581]`

* **Database version:** Indicates the GAM database version.
* **API version:** Indicates the application programming interface version.
* **Default repository:** Indicates the repository that is used by default, which can be changed by the developer.
* **Custom email regular expression:** Allows developers to enter their own regular expressions to validate user emails. If left empty, GAM validation is used.
* **Enable tracing:** Allows you to enable/disable the GAM trace that provides more information than the trace located in the menu options *Settings > Repository Configuration*.

**Note**: Note that the regular expression you use must validate that what is received is an email. It cannot be an expression such as “.\*” for example. .
