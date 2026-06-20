---
title: "Replace Method for Extended Data Types"
source_id: 7067
source_url: https://wiki.genexus.com/commwiki/wiki?7067
genexus_version: "18"
---

# Replace Method for Extended Data Types

Allows replacing all the events of a text with another one.

### [Syntax](#Syntax)

**&***WordDocument***.Replace(***OldText***, NewText** [ **,** *MatchCase* [ **,** *MatchWholeWord* ] ] **)**  
  
**Type Returned:**   
Numeric  
  
**Where:**  
*OldText*  
   Indicates the text to be replaced.  
  
*NewText*  
   Indicates what the next text of the document will be.  
  
*MatchCase*  
   If the value is 1, only the events with equal upper and lowercase configuration will be replaced. If the value is 0 all events are replaced. This parameter is optional and the default behavior is as if the value were 0.  
  
*MatchWholeWord*  
   If the value is 1, only the events that are not part of another word will be replaced. If the value is 0, all events are replaced. This parameter is optional and the default behavior is as if the value were 0.  
  
**Note:**

This method returns an error code, so it is possible to call it as a function (**&**Err **=** **&**WordDocument**.Replace(…..)**).

### [Scope](#Scope)

#### **Extended Data Types:** [WordDocument](https://wiki.genexus.com/commwiki/wiki?2478,,) **Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,,)
