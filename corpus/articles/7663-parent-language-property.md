---
title: "Parent language property"
source_id: 7663
source_url: https://wiki.genexus.com/commwiki/wiki?7663
genexus_version: "18"
---

# Parent language property

To associate a parent language with the language.

### [Description](#Description)

A language may be a “specialization” of another one. This is useful for defining regional specific terms for a specific language without having to translate every term. Only those terms that are different must be translated into the child language.

#### [Values](#Values)

**(None):** Indicates that the object has no parent language associated with it.  
**(Language Object name):** Any language object name that doesn't produce circular references (e.g. German language is parent of German1 and German1 is parent of German).

### [Scope](#Scope)

**Objects:** Language
