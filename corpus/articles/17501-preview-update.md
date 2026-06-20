---
title: "Preview Update"
source_id: 17501
source_url: https://wiki.genexus.com/commwiki/wiki?17501
genexus_version: "18"
---

# Preview Update

When using the *Preview update* [Team Development Contextual Menu](https://wiki.genexus.com/commwiki/wiki?17493,,) on a list of objects, a Preview is triggered to get the list of selected objects from the GXserver repository:

```
========== Receive changes started ==========
Contacting GeneXus Server at 'http://....'... done!
Exporting Data Selector 'SampleObject'...
GeneXus Server: Partial update requested by GXTechnical\genexus
GeneXus Server: Processing file...
GeneXus Server: Checking Import References...... Finished
GeneXus Server: Reading import file objects...... Finished
GeneXus Server: Exporting Data Selector 'SampleObject'...
Processing file 'C:\Users\genexus\AppData\Local\Temp\tmp576D.tmp'...
Checking Import References...Finished
Reading import file objects...Finished
Receive changes Success
========== Preview Update started ==========
Preview Update Success
```

Then, the Team Development [update dialog](https://wiki.genexus.com/commwiki/wiki?10627) will be instantiated with the selected object list from the GXserver repository; the user can actually execute the update operation or cancel it.
