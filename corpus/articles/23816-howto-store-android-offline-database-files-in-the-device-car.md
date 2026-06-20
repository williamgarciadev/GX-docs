---
title: "HowTo: Store Android offline database files in the device card"
source_id: 23816
source_url: https://wiki.genexus.com/commwiki/wiki?23816
genexus_version: "18"
---

# HowTo: Store Android offline database files in the device card

Before the generation of an offline
[Android](https://wiki.genexus.com/commwiki/wiki?14453) application with GeneXus, it is possible to specify whether the offline database files are going to be stored in the device local storage, or in the device card storage.

The way to do that is by changing the value of a property in the *MainApplication.java file*. This file is located at *C:\<GeneXus installation directory>\Android\Templates\ApplicationProject\src\main\java\com\genexus\namespace\*  
Once you have found the file, and if you want to store the offline database files in the device card, change the following line:

```
application.setUseInternalStorageForDatabase(true);
```

for this line:

```
application.setUseInternalStorageForDatabase(false);
```

The next time you are building your application, the offline database will be created in the device card storage.

### [Considerations](#Considerations)

If the offline database was created in the internal storage at the beginning, once you perform the changes mentioned above, the offline database will **not** be copied to the device card, it will be created from scratch instead.

### [See Also](#See+Also)

[HowTo: Look for offline database files](https://wiki.genexus.com/commwiki/wiki?23815)  
[HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298)


|  |
| --- |
| **Backlinks** |
| [HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298) | [HowTo: Look for offline database files](https://wiki.genexus.com/commwiki/wiki?23815) |

---
