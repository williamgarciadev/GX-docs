---
title: "KB Task Items"
source_id: 35636
source_url: https://wiki.genexus.com/commwiki/wiki?35636
genexus_version: "18"
---

# KB Task Items

A task item represents an entity associated to the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) for the GeneXus MSBuild tasks. You can use a list of KB task items as input or output parameters. Each item specification must detail the object type and the fully qualified object name; separated by ":". The syntax is detailed as follows:

```
<ListSpecification> ::= <ObjectsSpecification> [";" <ListSpecification>]
<ObjectsSpecification> ::= [<ObjectType> ":"] <ObjectName>
```

for example

```
Transaction:transaction1;Attribute:Id;Attribute:Description;
```

### [Notes](#Notes)

* The specification is case insensitive.
* When the type is not detailed; it will search for an object within the associated object namespace (Transaction, Procedure, WebPanel, and so on).
* For those KB entities not associated to an object namespace (Environment, Attributes, Domains); the type is mandatory.
* To set version properties; use "Version Properties:" or "Version Properties:Version Properties".


|  |
| --- |
| **Backlinks** |
| [Import MSBuild Task](https://wiki.genexus.com/commwiki/wiki?35599) |

---
