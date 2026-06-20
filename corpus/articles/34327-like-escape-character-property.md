---
title: "LIKE escape character property"
source_id: 34327
source_url: https://wiki.genexus.com/commwiki/wiki?34327
genexus_version: "18"
---

# LIKE escape character property

Indicates that an escape character is going to be used in the SQL sentences generated. This allows searching by special characters in SQL sentences like "\_" which in SQLServer is a wildcard indicating any character.

### [Scope](#Scope)

**Level:** Version

### [Description](#Description)

**Values**

* None: No escape character is specified in the sentence
* \ (backslash): Backslash is used as an escape character in the sentence.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.
