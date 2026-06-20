---
title: "Manage Module References (GeneXus 18 Upgrade 3 or prior)"
source_id: 55064
source_url: https://wiki.genexus.com/commwiki/wiki?55064
genexus_version: "18"
---

# Manage Module References (GeneXus 18 Upgrade 3 or prior)

The Manage Module Reference option is another intended (along with [Knowledge Manager Import](https://wiki.genexus.com/commwiki/wiki?3179)) for knowledge-sharing among developers. You can install a module provided by other developers that have [packaged their funcionalities](https://wiki.genexus.com/commwiki/wiki?31376) for distribution.

The Manage Module Reference dialog allows you to:

1. Look for external modules on servers (including your local machine).
2. Install, Update, or Restore a module to the KB
3. Get information about the module, such as its version, author, description, license, platforms available, etc.

`[imagen omitida: wiki id 40175]`

The Install/Update process updates the Output window with relevant process status, warnings, and errors. Make sure it is open to see the information.

### Troubleshooting

#### [**Symptom:** When Installing, "pmm0037: Maven installation not found."](#Symptom%3A+When+Installing%2C+%22pmm0037%3A+Maven+installation+not+found.%22)

```
error: Error downloading module '<module>' from 'Global Matrix' (internal error: 'pmm0037: Maven installation not found. Please, add Maven installation 'bin' path to environment variable 'PATH'.').
```

**Reason:** GeneXus requires Maven 3.6.1 or higher for installing modules from a Nexus [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933).

**Solution:**You must update Maven. 

#### [**Symptom:** Error accessing Global Matrix through Maven.](#Symptom%3A+Error+accessing+Global+Matrix+through+Maven.)

```
error: Error downloading module '<module>' from 'Global Matrix' (internal error: 'Object reference not set to an instance of an object.').
```

In gxlogging.log you can see the following error:

**PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested**

**Reason:** The error occurs due to a change in the certificate of the Matrix site you are trying to access through Maven in GeneXus. The error message indicates that a valid certification path to the requested target could not be found, preventing the artifacts from being transferred correctly.

**Solution:**To solve the problem, it is necessary to update the JDK or manually update the certificate in the Java version of the development machine, so that the new certificate used by the Matrix server is recognized. This will allow to establish a secure connection and resolve the error. More information is available at [SAC #52914](https://www.genexus.com/en/developers/websac?data=52914;;).

### [See Also](#See+Also)

[When and how is the GeneXus module updated in a KB?](https://wiki.genexus.com/commwiki/wiki?47842)
