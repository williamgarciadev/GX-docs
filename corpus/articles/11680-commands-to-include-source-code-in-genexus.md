---
title: "Commands to include source code in GeneXus"
source_id: 11680
source_url: https://wiki.genexus.com/commwiki/wiki?11680
genexus_version: "18"
---

# Commands to include source code in GeneXus

The DBASE, CSHARP and JAVA commands are to include source code in GeneXus.  This may be useful to use commands of the languages for which they’re generated and don’t exist on GeneXus natively. 

By the following commands it’s allowed to include in GeneXus lines of source code from the languages for which GeneXus generates.

* DBASE: It applies for Xbase, FoxPro for Windows and Visual FoxPro generators.
* JAVA: It applies for Java generator.
* CSHARP: It applies for .NET and .NET Framework generators.

These commands may be included in events as well as in procedures and reports.

### [**Syntax**](#Syntax)

         <DBASE|JAVA|CSHARP>        ..... [!&variable!] ...[!Attribute!]

 All that is written on this line after one of these commands will be generated identically to the source code, taking into account the following exceptions:

* text delimited by "[! !]" will be converted to the associated GeneXus reference.
* one line [GeneXus comments](https://wiki.genexus.com/commwiki/wiki?21111) will be ignored.
* do not use multi-line [comments](https://wiki.genexus.com/commwiki/wiki?21111) otherwise a compile error may occur.

### [Examples](#Examples)

1) If we wish that a Visual FoxPro application searched the tables in another directory we may write the following at the Start event from the main work panel:

```
 DBASE SET PATH TO D:\directoryDBFs
```

If that directory varies actually, we may write the following:

```
DBASE SET PATH TO &[!&way!]
```

Where &way contains the access route to the DBFs.

 2) On .NET, to send a message with some function defined:

```
&msg = 'Prueba' 
 CSHARP GeneXus.Programs.class.function([!&msg!]);
```

3) On .NET to detect if it is running on .NET Framework or .NET:

```
csharp [!&IsNETFramework!] = System.Environment.Version.Major <= 4;
```

4) On Java, generate an own log from the JDBC driver, in which we obtain information about the sentences executed by the driver classes used to access to the DBMS and its results.

 To activate it:

```
java try{ 
java.sql.DriverManager.setLogStream(new 
java.io.PrintStream(new 
java.io.FileOutputStream("jdbc.log"))); } 
catch (java.io.IOException e){}
```

This sentence should be specified before performing the connection; for example in a work panel (that does nothing) and calls another that makes the connection, or on the first line of the procedure.
