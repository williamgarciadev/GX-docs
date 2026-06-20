---
title: "What are the differences between Procedures and Data Providers? Do DP replace Procedures?"
source_id: 5968
source_url: https://wiki.genexus.com/commwiki/wiki?5968
genexus_version: "18"
---

# What are the differences between Procedures and Data Providers? Do DP replace Procedures?

In some situations, Data Providers can be used instead of Procedures. We can say that a Data Provider solves a subset of problems created by Procedures. What are they? Those where the input is taken from the Database or an SDT, or fixed data, and the goal is to obtain a hierarchical output that could be represented by an SDT (or BC).

While in a procedure the focus is in the transformation language (that transforms the input into the output), in a Data Provider the focus is on the proper Output. For this reason, we say that it's an output-based language, mainly "declarative" (instead of "procedural").

What are the benefits? In addition to its ease of use, a declarative language is higher-level. In the future, the underlying implementation will be changed without having to change the declaration of what the DP does, that is, the DP code itself.
