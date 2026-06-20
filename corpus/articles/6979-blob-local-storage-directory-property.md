---
title: "Blob local storage directory property"
source_id: 6979
source_url: https://wiki.genexus.com/commwiki/wiki?6979
genexus_version: "18"
---

# Blob local storage directory property

When getting Blob data from the database, a temporary file is saved locally or in the server disc, depending on the architecture of the application. This generator property indicates the location where the temporary files are saved.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

#### [Web environment](#Web+environment)

In web environment, this property is used to set the web server path where files are temporarily saved when retrieved from the database. That is to say, when you Get data, a temporary file is saved in the Blob Local Storage Directory.

#### [Notes:](#Notes%3A)

1. The Blob Local Storage Directory must be accessible from the virtual directory, and there must be read permissions for the user who runs the web application (IIS user, for example) in that directory.  
  
2. If the property is not set up, the temporary files will be saved in the PublicTempStorage (default value) directory.

3. The value of this property has to point to a relative directory under the web directory. For this reason, the default value is PublicTempStorage, which is relative and is created at runtime as a folder under the web directory.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [See Also](#See+Also)

[Blob data type](https://wiki.genexus.com/commwiki/wiki?6704)  
[Temp media directory property](https://wiki.genexus.com/commwiki/wiki?7628)  
[Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719)


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [A05:2021 - Security misconfiguration](https://wiki.genexus.com/commwiki/wiki?50185) |
| [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [Good practices for secure development using GAM](https://wiki.genexus.com/commwiki/wiki?47241) |
| [PathToURL function](https://wiki.genexus.com/commwiki/wiki?9563) | [Temp media directory property](https://wiki.genexus.com/commwiki/wiki?7628) |

---
