---
title: "Workstation Settings"
source_id: 42339
source_url: https://wiki.genexus.com/commwiki/wiki?42339
genexus_version: "18"
---

# Workstation Settings

Applications that use multiple languages must be generated with special care in order to work properly. For this, it is important to check the workstation configuration.

The Windows workstation that will be in charge of the generation must be explicitly configured to match the [default language](https://wiki.genexus.com/commwiki/wiki?42336) used in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). This is because the local system and language settings are used when generating the application.

You can ensure that the "Language version of non-Unicode programs" is correct by going to Control Panel > Regional and Language Options > Advanced.

Make sure that the following option is **not checked**:

```
Beta: Use Unicode UTF-8 for worldwide language support
```

### [Sample](#Sample)

If you have set the Japanese Language in your Knowledge Base,  you may set it as seen in the image below:

`[imagen omitida: wiki id 43573]`

### [Considerations](#Considerations)

This configuration is important when using [GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) for languages with different code pages.

For [Static Translation](https://wiki.genexus.com/commwiki/wiki?54437) the Windows configuration must match because the code must be generated and compiled on a machine in that Language; otherwise you will notice funny characters or question marks (??????) when running the objects.


|  |
| --- |
| **Backlinks** |
| [HowTo: Add RTL styles](https://wiki.genexus.com/commwiki/wiki?42319) | [HowTo: Add RTL styles (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54443) | [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) |
| [Translation types (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54444) |

---
