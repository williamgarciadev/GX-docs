---
title: "Refcall rule"
source_id: 6864
source_url: https://wiki.genexus.com/commwiki/wiki?6864
genexus_version: "18"
---

# Refcall rule

Calls a program whenever a referential integrity check fails.

### [Syntax](#Syntax)

**Refcall(*'****PgmName***',** *par1* **,** ... **,** *parN***);**  
  
**Where:**  
  
*PgmName*Is the name of the program to be called when [referential integrity](https://wiki.genexus.com/commwiki/wiki?42576) check fails.  
  
*par1* **,** ... **,** *parN* It is a list of attributes or variables. The attributes form the foreign key (simple o compound by several attributes) for which the referential integrity check fails. Variables are used to give additional information to the program.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

You can define this rule in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to call a program when a referential integrity check fails. All attribute parameters are used, maintaining the order given by the parameter list, to form the foreign key. So, when the referential integrity check fails for that foreign key, the object indicated by you is called.

**Notes:**

* The called program must receive the same parameter list specified by the Refcall rule.
* In Transactions, the Refcall cannot call an object with form ([Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) or [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)).
* This rule implicitly reads the referenced table twice: the first time to verify that the reference was incorrect and the second time to control that the values returned by the called program are a valid reference.

### [See Also](#See+Also)

[Refmsg rule](https://wiki.genexus.com/commwiki/wiki?6865)  
[Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863)


|  |
| --- |
| **Backlinks** |
| [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) | [Refmsg rule](https://wiki.genexus.com/commwiki/wiki?6865) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
