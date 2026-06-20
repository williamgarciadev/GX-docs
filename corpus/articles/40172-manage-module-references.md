---
title: "Manage Module References"
source_id: 40172
source_url: https://wiki.genexus.com/commwiki/wiki?40172
genexus_version: "18"
---

# Manage Module References

Manage Module References is another option (together with [Knowledge Manager Import](https://wiki.genexus.com/commwiki/wiki?3179)) for knowledge sharing among developers. You can install a module provided by other developers that have [packaged their funcionalities](https://wiki.genexus.com/commwiki/wiki?31376) for distribution.

The Manage Module References dialog allows you to:

1. Look for external modules on servers (including your local machine).
2. Install, Update, or Restore a module in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).
3. Get information about the module, including its version, author, description, license, platforms available, etc.

`[imagen omitida: wiki id 40175]`

The Install/Update process displays the relevant process status, warnings, and errors in the Output window. Make sure it is open to see the information.

### [Module Installation](#Module+Installation)

GeneXus uses the Maven repository for managing and downloading modules from its Global Matrix. However, when defining your own repository, you can choose between Maven and NuGet for module management and downloading. To do so, you must configure the repository as a [Module Server](https://wiki.genexus.com/commwiki/wiki?45933) and specify whether it is a Nexus - NuGet or Nexus - Maven repository. This way, GeneXus will use the selected repository to manage the modules and their dependencies.

#### [Maven](#Maven)

Maven is widely used and allows for dependency management, which simplifies the installation and update of modules in GeneXus.

To use Maven as a module server, you must have Maven installed. You can download it from the official [Maven site](https://maven.apache.org).

#### [NuGet](#NuGet)

NuGet is presented as a recommended alternative, as it automatically manages dependencies.

When using NuGet, if a module A depends on another module B, it is not necessary to have module B previously installed. GeneXus, in conjunction with NuGet, automatically installs the required dependencies before installing the main module. This approach significantly simplifies the process of installing and updating modules, especially when working with a considerable number of modules and their respective dependencies.

Make sure you have NuGet installed by looking for the "nuget.exe" file in %userprofile%\.gxmodules\.tools. If you cannot find it, you can download it from the official [NuGet site](https://www.nuget.org/downloads).

### [Troubleshooting](#Troubleshooting)

#### [**Symptom:** When Installing, "pmm0037: Maven installation not found."](#Symptom%3A+When+Installing%2C+%22pmm0037%3A+Maven+installation+not+found.%22)

```
error: Error downloading module '<module>' from 'Global Matrix' (internal error: 'pmm0037: Maven installation not found. Please, add Maven installation 'bin' path to environment variable 'PATH'.').
```

**Reason:** GeneXus requires Maven 3.6.1 or higher for installing modules from a Nexus [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933).

**Solution:** You must update Maven.

#### [**Symptom:** Error accessing Global Matrix through Maven.](#Symptom%3A+Error+accessing+Global+Matrix+through+Maven.)

```
error: Error downloading module '<module>' from 'Global Matrix' (internal error: 'Object reference not set to an instance of an object.').
```

In gxlogging.log you can see the following error:

**PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target**

**Reason:** The error occurs due to a change in the certificate of the Matrix site you are trying to access through Maven in GeneXus. The error message indicates that a valid certification path to the requested target could not be found, preventing the artifacts from being transferred correctly.

**Solution:** To solve the problem, it is necessary to update the JDK or manually update the certificate in the Java version of the development machine so that the new certificate used by the Matrix server is recognized. This will allow you to establish a secure connection and resolve the error. More information is available at [SAC #52914](https://www.genexus.com/en/developers/websac?data=52914;;).

### [See Also](#See+Also)

* [When and how is the GeneXus module updated in a KB?](https://wiki.genexus.com/commwiki/wiki?47842)
* [GeneXus behind corporate proxy](https://wiki.genexus.com/commwiki/wiki?55898)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [GeneXus FTPS Module](https://wiki.genexus.com/commwiki/wiki?45274) |
| [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [GeneXus SFTP Module](https://wiki.genexus.com/commwiki/wiki?44965) |
| [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [GeneXusReporting module](https://wiki.genexus.com/commwiki/wiki?51178) | [Category:Knowledge Manager Menu](https://wiki.genexus.com/commwiki/wiki?5679) |
| [Manage Module References (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55064) | [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [Module Version property](https://wiki.genexus.com/commwiki/wiki?46755) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |
| [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933) | [Modules Server (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55061) |
| [Sample: GeneXus Cognitive API Custom-Models proof of concept](https://wiki.genexus.com/commwiki/wiki?44217) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) | [SecurityAPICommons Module](https://wiki.genexus.com/commwiki/wiki?47252) | [Updating Unanimo](https://wiki.genexus.com/commwiki/wiki?52180) |

---
