---
title: "Technical specifications of GeneXus"
source_id: 55715
source_url: https://wiki.genexus.com/commwiki/wiki?55715
genexus_version: "18"
---

# Technical specifications of GeneXus

This document describes the technical specifications of GeneXus; that is, the capacity limits and recommended values in different areas that help to plan the use of GeneXus.

### [Understanding the table](#Understanding+the+table)

* Measure: A specific area that may be reached.
* Range: Theoretical capacity limits.
* Reasonable Maximum: Based on heuristics, modularization techniques, modeling and programming practices, and experience with multiple KBs built by the GeneXus community.
* Comments: Additional comments that provide explanations or advice, links to additional resources.

|  |  |  |  |
| --- | --- | --- | --- |
| Measure | Range | Reasonable Maximum | Comments |
| **General Limits** |  |  |  |
| # of Knowledge Bases per GeneXus installation | 0- |  | There is no technical limit. Licenses may limit the # of Users (e.g.: some [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31337,,) plans limit it). |
| # of Users per GeneXus installation | 0- |  | There is no technical limit. Licenses may limit the # of Users (e.g.: some GeneXus Server plans limit it). |
| # of Knowledge Bases per GeneXus Server installation | 0-9999999999 |  | Licenses may limit the # of KBs (e.g.: some GeneXus Server plans limit it). |
| # of Users per GeneXus Server installation | 0-9999999999 |  | Open GXserver plans have tens of thousands of users. Licenses may limit the # of Users (e.g.: some GeneXus Server plans limit it). |
|  |  |  |  |
| **KB limits** |  |  |  |
| # of KB Versions | 0-maxint | 1000 | Production lines and frozen versions may grow indefinitely, especially in KBs hosted by GeneXus Server. The impact on build times is very low. |
| # of KB Environments | 0-maxint | 10000 | # of Environments grows with # Versions. The impact on build times of a particular environment is very low. |
| # of User Objects | 0-maxint | 10000 | Consider modularizing your system and building it from multiple KBs. |
| # of Transactions | 0-maxint | 3000 | Consider modularizing your system and building it from multiple KBs. |
| # of other objects | 0-maxint | 10000 | Consider modularizing your system and building it from multiple KBs. |
| # of Subtype groups | 0-maxint | ⅔ of # of Transactions | The more complex the system, the more the build performance may be affected. |
| **Limits inside Objects** |  |  |  |
| # of Rules in Transactions | 0-maxint | 1000 | Consider merging some validations in separate [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s. |
| # Fields in Transactions | 0-maxint | 200 | Consider modeling some fields in another subordinated N to N relation or in another [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) (parallel). |
| # of Formulas in Transactions | 0-maxint | ⅔ of # of Fields in Transaction | The more complex the system, the more the build performance may be affected. |
| # Lines in Procedures, Events, Data Providers | 0-maxint | 1000 | Consider modularizing better. |
| # lines Events in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s | 0-maxint | 2000 | Consider modularizing the object using web components/components and/or moving login to other objects (e.g. load using a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)). |
| # of conditions per Object or [Grid](https://wiki.genexus.com/commwiki/wiki?24817) | 0-maxint | 50 | The greater the number of conditions, the more complex the navigation and SQL statement will be, and the more performance will be affected. |
| # of conditional orders per navigation | 0-maxint | 5 | Consider selecting an appropriate set of possible orders for your query. |
| **Limits in Property values** |  |  |  |
| Max length of Long varchar | 33563648 | 2M | The larger the field, the more memory consumption. See [Maximum Size of LongVarChar Fields](https://wiki.genexus.com/commwiki/wiki?7767). |
| Max length of Numeric | 38 | 28 | Default max is 18 and can be configured. See [Maximum numeric length property](https://wiki.genexus.com/commwiki/wiki?6801). |
| Max Attribute Name Length | 128 | 30 | Length affects readability and can be configured. See [Significant attribute name length property](https://wiki.genexus.com/commwiki/wiki?7248). |
| **Inferred limits** |  |  |  |
| # of steps in closures | 0-maxint | 5 | In complex KBs (many tables with many relations, in general with many subtypes). The limit can be configured. |
| # of Tables | 0-maxint | 3000 | Limited by target DBMS, typically correlated with # of Transactions. |
| # of Attributes, Primary Key attributes, Indexes per table | Limited by target DBMS |  | Limited by DBMS. Limits vary depending on DBMS and version. |
|  |  |  |  |
| **Build options** |  |  |  |
| # of concurrent specifiers | 64 | # of processors | If specifiers and generators work concurrently, the recommended value is int(#CPUs / 2 + 1). See [Multiple Concurrent Generator and Specifier Instances](https://wiki.genexus.com/commwiki/wiki?25808). |
| # of concurrent generators | 64 | # of processors | Concurrent Generator Instances: max(1, int(#CPUs/2)). See [Multiple Concurrent Generator and Specifier Instances](https://wiki.genexus.com/commwiki/wiki?25808). |
