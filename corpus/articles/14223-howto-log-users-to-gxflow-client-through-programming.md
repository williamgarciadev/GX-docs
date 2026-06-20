---
title: "HowTo: Log users to GXflow Client through programming"
source_id: 14223
source_url: https://wiki.genexus.com/commwiki/wiki?14223
genexus_version: "18"
---

# HowTo: Log users to GXflow Client through programming

This article shows you the code lines to log into GXflow Client application by programming, thus avoiding logging in through the Client login dialog.

```
&Session.Set('WorkflowUser','WFADMINISTRATOR')

&Session.Set('WorkflowPassword','WFADMINISTRATOR')

//Java
Link('com.gxflow.wfautosignin')

//Net
Link('wfautosignin.aspx')

commit
```

**Where:**

*&Session*  
      Is of WebSession data type
