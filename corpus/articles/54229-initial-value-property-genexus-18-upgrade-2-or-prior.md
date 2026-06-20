---
title: "Initial value property (GeneXus 18 Upgrade 2 or prior)"
source_id: 54229
source_url: https://wiki.genexus.com/commwiki/wiki?54229
genexus_version: "18"
---

# Initial value property (GeneXus 18 Upgrade 2 or prior)

Initializes attributes and variables based on domains in any object, with a constant value, formula or procedure, when a reorganization is necessary.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It initializes the value of attributes of any GeneXus object. It initializes variables based on attributes or domains, and performs initial value calling procedures, and loading SDTs, too. The values to be given to the property must correspond to the attribute's data type.

#### [Note](#Note)

This property is not available when the attribute is a formula.

### [Samples](#Samples)

To date: **#10-12-23#**  
To datetime: **#10-12-23 08:12:36#**  
To numeric integer: **4326**  
To numeric decimal: **4326.93**  
To character (take into account the quotes):**'Hello World'**  
To boolean:**TRUE/FALSE**
