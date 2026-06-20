---
title: "Database performance from the GeneXus perspective"
source_id: 26285
source_url: https://wiki.genexus.com/commwiki/wiki?26285
genexus_version: "18"
---

# Database performance from the GeneXus perspective

When you are coding, you often find that a program can be coded in different ways to do the same job. So it is important to understand how to improve your GeneXus coding to get the most of it and make sure the generated code is optimized.

This guideline resumes some helpful tips to take into account in relation to the GeneXus language, associated coding and what to do next if you want to improve the database access for certain navigations.

### [Detailed navigation](#Detailed+navigation)

Enable a [detailed navigation](https://wiki.genexus.com/commwiki/wiki?7165,,) report.

### [Warning messages](#Warning+messages)

Carefully review all [warnings](https://wiki.genexus.com/commwiki/wiki?5933) detailed on the navigation detail.

### [For Each Optimizations](#For+Each+Optimizations)

Based on your code, check if you can apply any of the following optimizations.

* [optimizations](https://wiki.genexus.com/commwiki/wiki?26286)
* [Blocking Data Updates](https://wiki.genexus.com/commwiki/wiki?5572)

### [Index and Order](#Index+and+Order)

Check index and Order usage for filtering data. If needed, create new indexes but be careful; more indexes on a tables will slow the INSERT, UPDATE, DELETE operations.

See also

* [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100)
* [Conditional Orders and Filters](https://wiki.genexus.com/commwiki/wiki?12566)

### [Server Paging](#Server+Paging)

Use [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) whenever possible for grid navigation.

### [Enable management](#Enable+management)

Enable the [Enable Management property](https://wiki.genexus.com/commwiki/wiki?9244) and monitoring your application to analyze SQL usage, number of executions and related parameters to know on what statements to concentrate the tuning.

### [DBMS specific](#DBMS+specific)

To run the database economically and optimally you need to identify the long-duration queries, isolate them, examine the query execution plan, analyze the individual execution steps and change the steps as required to improve the performance of the system.

Each DBMS comes with a host of performance monitoring / tuning tools. If you need to go further to effectively optimize some queries, check you DBMS documentation and follow these steps:

* Identify the high load or top SQL statements that are inefficient and are responsible for a large share of the application workload and system resources.
* Verify that the execution plans produced by the query optimizer for these statements are performing satisfactorily.
* Implement corrective actions to generate better execution plans to rectify the poorly performing SQL statements.

### [Network I/O](#Network+I%2FO)

If you have long batch processes execution, take into account how your program will be deployed and where it will be executed.  
If your application runs in a different location from your database server; your performance may be decreased.

### [Dynamic Translation](#Dynamic+Translation)

Whenever possible use the bang character (!) to minimize the usage of the dynamic translation functions only when is needed.  
Another option is to use the Translation Type environment property with the "static" value.

### [See Also](#See+Also)

[What do we talk about when we talk about performance](https://wiki.genexus.com/commwiki/wiki?1812,,)  
[Performance problems diagnosis in Java applications](https://wiki.genexus.com/commwiki/wiki?10985,,)  
[Stress Test Tips](https://wiki.genexus.com/commwiki/wiki?9404,,)  
[Blocking clause in a 'For each' command](https://wiki.genexus.com/commwiki/wiki?4837)  
[Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100)  
[OptimizedUpdate](https://wiki.genexus.com/commwiki/wiki?2016,,)  
[Navigation Reports for Procedures, Web Panels and Data Providers](https://wiki.genexus.com/commwiki/wiki?7178)  
[Navigation Report for Transactions](https://wiki.genexus.com/commwiki/wiki?7177)
