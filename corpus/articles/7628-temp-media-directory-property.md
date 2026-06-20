---
title: "Temp media directory property"
source_id: 7628
source_url: https://wiki.genexus.com/commwiki/wiki?7628
genexus_version: "18"
---

# Temp media directory property

This property is used to configure the path in the Web server where the files will be temporarily saved when loaded to the database. This happens when a Blob is added or changed; it is temporarily saved in this directory.

### [Description](#Description)

The default value is PrivateTempStorage. This directory should not be accesible from the web application for security reasons.

If the directory doesn't exist (even if it's absolute or relative to the virtual directory), it is created automatically in runtime.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Blob data type](https://wiki.genexus.com/commwiki/wiki?6704)  
[Blob local storage directory property](https://wiki.genexus.com/commwiki/wiki?6979)


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [A02:2021 - Cryptographic failures](https://wiki.genexus.com/commwiki/wiki?50182) | [A05:2021 - Security misconfiguration](https://wiki.genexus.com/commwiki/wiki?50185) |
| [Blob local storage directory property](https://wiki.genexus.com/commwiki/wiki?6979) |
| [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [File Upload control](https://wiki.genexus.com/commwiki/wiki?30574) | [Good practices for secure development using GAM](https://wiki.genexus.com/commwiki/wiki?47241) |

---
