---
title: "SQL command"
source_id: 8623
source_url: https://wiki.genexus.com/commwiki/wiki?8623
genexus_version: "18"
---

# SQL command

Executes SQL statements from GeneXus Client/Server applications.

### [Syntax](#Syntax)

**SQL** *[ Sql statement ]*  
  
**Where:**  
  
*[ SQL statement ]*  
       Statement to be executed. Character.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The sentence after the **SQL** constant will be executed.  
A comment will appear in the generated code, indicating that a user SQL statement is being executed.

### [Samples](#Samples)

You can use just a literal:

```
SQL DELETE FROM CLIENTES
```

Or you can use variables. These should be between “ **[ !**” and “**! ]** ”:

```
&Table= "CLIENTES"
SQL DELETE FROM [!&Table!]
```

**Notes:**

* When using variables, make sure you use basic datatypes (*Character*, *Number*, etc), [SDTs](https://wiki.genexus.com/commwiki/wiki?10021) references are not allowed.
* SQL commands are always executed in the default data store [SAC 23118](https://www.genexus.com/es/developers/websac?data=23118).
* SQL command does not need to specify a semicolon at the end of the command.
* The statement executed cannot return any value, it cannot be processed from the GeneXus side.

###


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) |
| [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
