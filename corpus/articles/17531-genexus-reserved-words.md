---
title: "GeneXus reserved words"
source_id: 17531
source_url: https://wiki.genexus.com/commwiki/wiki?17531
genexus_version: "18"
---

# GeneXus reserved words

Reserved words in GeneXus have a special meaning in the target languages, SQL statements, DBMS, or Windows environment. These words are essential for the underlying systems to work correctly, and therefore if you use them as object names, attribute names, table names, index names, module names, etc., you might encounter unexpected errors during code generation or at runtime.

GeneXus also has some keywords that cannot be used as object names, attribute names, table names, index names, variable names, etc. These keywords are specific to GeneXus and are used to define the structure and behavior of your applications.

The reserved words in GeneXus can be categorized as follows:

* Target Language Reserved Words: These words have a special meaning in the programming language you are targeting (e.g., .NET, .NET Framework, Java).
* DBMS Reserved Words: These words have a special meaning in the database management system (DBMS) you are using (e.g., SQL Server, MySQL, PostgreSQL, Oracle).
* Windows Reserved Words: These words have a special meaning in the Windows operating system, particularly when naming files or folders.

### [Patterns Considerations](#Patterns+Considerations)

Avoid using the following patterns:

* **GX:** Do not use "GX" at the beginning (prefix) of your object names, attribute names, table names, index names, etc. For example, you cannot name a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) "GXCustomer" or an attribute "gxCustomerId".
* **\_BC:** Do not use the suffix "\_BC" to name your objects, attributes, tables, or indexes.
* **Database:** Do not name a Transaction object "Database".
* **Event:** Do not name a Transaction "Event".
* **modified, calendar, gxgral, gxwebsocket, static:** Do not use these words to name your objects, attributes, tables, or indexes.
* **\_impl:** Do not use the suffix "\_impl" to name your [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) in Java.
* **GAM:** Do not use "GAM" as the name of your [Knowledge Base (KB)](https://wiki.genexus.com/commwiki/wiki?1836) when [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) is activated.

### [Prefixes Considerations](#Prefixes+Considerations)

Avoid Using the Following Prefixes:

* agxpl\_
* apwf
* awf
* wf

### [SDT and BC Considerations](#SDT+and+BC+Considerations)

You should be aware of reserved words when working with [Structured Data Types (SDT)](https://wiki.genexus.com/commwiki/wiki?10021) and [Business Components (BC)](https://wiki.genexus.com/commwiki/wiki?5846). For example:

* &SDT.Imageuri(or &BC).
* &SDT.Audiouri (or &BC).
* &SDT.Videouri (or &BC).
* &SDT.Fileuri (or &BC).

The words Imageuri, Audiouri, Videouri, and Fileuri are reserved. Their use as attribute names within an SDT or BC can cause problems when trying to assign a value to them.

### [JavaScript Considerations](#JavaScript+Considerations)

Avoid declaring objects (located inside the Root module) whose names:

* Are JavaScript reserved words.Refer to the [JavaScript reserved words](https://www.w3schools.com/JS/js_reserved.asp) for a complete list.
* Collide with [Window object](https://developer.mozilla.org/en-US/docs/Web/API/Window) properties. Avoid using names that conflict with properties of the Window object**.**
* Are not supported in the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model). Avoid using names that are not supported by the Document Object Model (DOM).

Take this into account also when developing [Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) or [User Control object](https://wiki.genexus.com/commwiki/wiki?39356)s.

### [User Control Considerations](#User+Control+Considerations)

* Do not use the "Scripts" value for property values on a User Control, as this is internally used to load Scripts dependencies.

### [Reserved Words by Category](#Reserved+Words+by+Category)

#### [Languages](#Languages)

* **C# reserved words:** Refer to the [C# language specification](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/) for a complete list.
* **Java reserved words:** Refer to the [Java language specification](https://docs.oracle.com/javase/specs/jls/se8/html/jls-3.html#jls-3.9) for a complete list.
* **Swift Lexical Structure:** Refer to the [Swift Lexical Structure](https://docs.swift.org/swift-book/ReferenceManual/LexicalStructure.html) for a complete list.

#### [DBMS (Valid for Table and Index Names)](#DBMS+%28Valid+for+Table+and+Index+Names%29)

* **SQL Server:** Refer to [SQL Server](https://docs.microsoft.com/en-us/sql/odbc/reference/appendixes/reserved-keywords) for a complete list.
* **MySQL:** Refer to [MySQL](https://dev.mysql.com/doc/refman/5.7/en/replication-features-reserved-words.html) for a complete list.
* **PostgreSQL:** Refer to [PostgreSQL](https://www.postgresql.org/docs/7.3/sql-keywords-appendix.html) for a complete list.
* **Oracle:** Refer to [Oracle](https://docs.oracle.com/cd/B19306_01/em.102/b40103/app_oracle_reserved_words.htm) for a complete list.

#### [Environment](#Environment)

* **Windows (reserved words for filenames):** Refer to [Windows](https://en.wikipedia.org/wiki/Filename#Reserved_characters_and_words) for a complete list.

### [Samples of Reserved Word Issues](#Samples+of+Reserved+Word+Issues)

* **Environment -** **Transaction Naming:** Avoid using "con" as a Transaction name. If you do, you will encounter a generation error. This error message might look something like: "Waiting for 1 generator to finish their work..."
* **Front End - Web Object Naming:** Do not use "Location" as the name of Web Objects. For more information, read [SAC #47209](https://www.genexus.com/developers/websac?es,,,47209).
* **IDE - Transaction Naming:**Do not use "Order" as the name of a Transaction. For more information, read [SAC #47215](https://www.genexus.com/developers/websac?es,,,47215).


|  |
| --- |
| **Backlinks** |
| [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) | [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626) |

---
