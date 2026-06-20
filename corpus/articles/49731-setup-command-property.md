---
title: "Setup Command property"
source_id: 49731
source_url: https://wiki.genexus.com/commwiki/wiki?49731
genexus_version: "18"
---

# Setup Command property

Sets that for each main object an install script must be run once.

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** Generator

### [Description](#Description)

The default value for this property is "npm install -f." When a main object is executed, it checks if this command has not been run before and runs it. It will install all the dependencies required to run properly.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).
