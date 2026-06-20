---
title: "How are partially qualified object names resolved"
source_id: 22438
source_url: https://wiki.genexus.com/commwiki/wiki?22438
genexus_version: "18"
---

# How are partially qualified object names resolved

When writing code you may reference an object without fully qualifying it (i.e type its name but not the full [Module path](https://wiki.genexus.com/commwiki/wiki?22437) it is in). How references to partially qualified objects are resolved is called Automatic qualification rules.

## [Automatic qualification rules](#Automatic+qualification+rules)

Automatic qualification rules apply to partially qualified object names references in, for example, a referencing object source code. That is, the rules that GeneXus follows to identify, for example, what ObjectB (see picture below) you are talking about if you do not fully qualify it.

The basic concept behind automatic qualification is to free developers working in a Module from having to be aware of other Modules in a Knowledge Base unless they have to (i.e. they have to interact with other Modules).

To achieve the above objective, automatic qualification takes into account where the unqualified references are made, meaning that it does not solve in the same way a reference made to ObjectC from ModuleA.ObjectE and from ModuleB.ObjectB, for example (see picture below).

Modules are organized in a tree structure. Every Module has a “parent” Module (except the [Root module](https://wiki.genexus.com/commwiki/wiki?22439)) and may also have “children” Modules. A “Module branch” is the set of Modules comprised by any given Module and its ancestors. A “Module tree” is the set of Modules comprised by any given Module and its successors. It is important to remember these concepts as they are used to explain how automatic qualification works.

`[imagen omitida: wiki id 22436]`

Vertical lines are intended for helping you identify duplicated names.

Automatic qualification algorithm works as follows.

1. If the name of the object is unique in the Knowledge Base, the call is resolved to that object.
2. If the name of the object is not unique, the partially qualified object is searched in the caller's [Module object](https://wiki.genexus.com/commwiki/wiki?22411) and resolved to that object.
3. If no object is found, the search continues over the sub-modules of the caller's [Module object](https://wiki.genexus.com/commwiki/wiki?22411) and resolved to that object.1
4. If no object is found, the parent [Module object](https://wiki.genexus.com/commwiki/wiki?22411) of the caller's [Module object](https://wiki.genexus.com/commwiki/wiki?22411) is used to repeat steps 2 and 3.1  
   This process goes on until an object can be found.

**Note**1: if two objects are found and no other object with the same partially qualified name exists, the call is ambiguous and the algorithm stops displaying an error. Then the developer must qualify the object in order to break the ambiguity.

This can be explained using the following rules which are explained later:

* Referenced object name is unique in a referencing object container Module tree.
* Referenced object name exists in the referencing object container Module branch.
* Ambiguous call.

### [Referenced object name is unique in a referencing object container Module tree](#Referenced+object+name+is+unique+in+a+referencing+object+container+Module+tree)

The rule may sound pretty complex to read but, with a few examples, it is easy to understand.

#### [Example 1](#Example+1)

Say you are referencing ObjectA from any other object in any Module. As there is no other object named ObjectA in the Knowledge Base (the [root module](https://wiki.genexus.com/commwiki/wiki?22439)), the reference will be automatically qualified as ModuleA.ObjectA.

#### [Example 2](#Example+2)

Unqualified references to ObjectB from objects in ModuleA, ModuleC, ModuleD, ModuleE and ModuleF are automatically qualified as ModuleA.ObjectB. ObjectB is unique in ModuleA's Module tree that is a container module of any of the mentioned modules.

#### [Example 3](#Example+3)

There are two objects named ObjectC in ModuleA's Module tree but only one in either ModuleC, ModuleD and ModuleB. Unqualified references to ObjectC from objects in any of the last named Modules will be automatically qualified to ModuleC.ObjectC, ModuleD.ObjectC and ModuleB.ObjectC.

### [Referenced object name exists in the referencing object container Module branch](#Referenced+object+name+exists+in+the+referencing+object+container+Module+branch)

When the referenced object name is not unique in a referencing object container Module tree, but there is an object with the same name (the referenced object) in the referencing object container Module branch, the unqualified reference is resolved for that object. Let's take a look at a few examples that will make things clearer.

#### [Example 1](#Example+1)

Say you are referencing ObjectE from an object in Module ModuleC. The name ObjectE is \_not\_ unique in any of ModuleC's container Module trees. There is, however, one object named ObjectE in ModuleC branch. The reference is qualified as ModuleC.ObjectE.

### [Ambiguous calls](#Ambiguous+calls)

In some cases, the Automatic qualification rules cannot solve partially qualified object names references. In those cases the following error is displayed:

```
error: '{ObjectQualifiedName}' is ambiguous, there are more than one object with this name. Use the full qualified name to resolve the ambiguity.
Conflicting objects: {ObjectType_1} '{FullyQualifiedName_1}', {ObjectType_2} '{FullyQualifiedName_2}', ...[{ObjectType_N} '{FullyQualifiedName_N}']
```

Example 1

`[imagen omitida: wiki id 25680]`

If a call to ObjectH is made from ObjectG—see image above, the call cannot be resolved automatically and the following error will be diplayed:

```
error: 'ObjectH' is ambiguous, there are more than one object with this name. Use the full qualified name to resolve the ambiguity.
Conflicting objects: Web Panel 'ModuleG.ModuleH.ObjectH', Web Panel 'ModuleG.ModuleI.ObjectH' (ModuleG.ObjectG Events, Line: Y, Char: XXX)
```


|  |
| --- |
| **Backlinks** |
| [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Modules - Grammar](https://wiki.genexus.com/commwiki/wiki?25609) |
| [Modules - Object names](https://wiki.genexus.com/commwiki/wiki?22483) | [Which objects can be defined in a module?](https://wiki.genexus.com/commwiki/wiki?23850) | [Working with Modules](https://wiki.genexus.com/commwiki/wiki?25607) |

---
