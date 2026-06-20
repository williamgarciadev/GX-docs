---
title: "Maximum cached cursors per connection property"
source_id: 9023
source_url: https://wiki.genexus.com/commwiki/wiki?9023
genexus_version: "18"
---

# Maximum cached cursors per connection property

Avoids infinite memory consumption and reduces this memory consumption.

### [Description](#Description)

When the maximum is reached, the application tries to close some open cursor. If this is possible, the application closes the cursor and opens a new one (and caches it). If not, it writes a warning to the log (if trace is enabled) telling that the cache is being expanded and continues the execution.

The objective is to avoid infinite memory consumption/reduce memory consumption. Changing the value specified in this property may affect the application's performance. The best value depends on the application and the environment.

#### [Values](#Values)

Numeric only.

**Default value** = 100

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)
