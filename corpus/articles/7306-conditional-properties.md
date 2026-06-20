---
title: "Conditional properties"
source_id: 7306
source_url: https://wiki.genexus.com/commwiki/wiki?7306
genexus_version: "18"
---

# Conditional properties

The are two ways of expressing conditions:

### 1. Using the condition editor

To do this double clic over the conditional edge. E.g.: MemberId = 0

`[imagen omitida: wiki id 7559]`

`[imagen omitida: wiki id 7517]`

* Type: It shows that the edge is conditional.
* Condition rule: It allows writing the condition or showing the condition write through the editor.
* Conditional code: Conditional code.

### 2. Assigning a procedure

`[imagen omitida: wiki id 7558]`

* Name: Conditional name.
* Procedure: Procedure asociated with condition.

### Considerations

The conditions editor does not support non ANSI character set. If you need to set conditions as the following:

```
testdata = "未承認"
```

...where "未承認" means "not approved"; use a Enumerated Domain.
