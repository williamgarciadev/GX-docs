---
title: "Unit Testing"
source_id: 38334
source_url: https://wiki.genexus.com/commwiki/wiki?38334
genexus_version: "18"
---

# Unit Testing

**Unit Tests** are the most effective way to test business logic in GeneXus in an isolated, fast and repeatable way. GeneXus Procedures are the way to encapsulate business logic code and reutilize it on different panels.

You may want to test GeneXus [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) when:

* Given some input parameters, you want to test Procedure output by comparing expected results (using [Assertions](https://wiki.genexus.com/commwiki/wiki?38336)) with process results (output variables, files or database records).
* Given no input parameters but based on database parameters and configurations, you expect the Procedure to return some expected output (variables or database records).
* A mix of both.

This means that any GeneXus Procedure could be tested to verify that it works as expected in the product specification. Additionally, to Procedures, you can add a Unit test to DataProviders and Business Transactions also.

The main benefits of adding a Unit test are:

* Detect bugs in GX code before even creating a test environment and deploying the solution
* Provides Immediate feedback to Developers, even before they commit a buggy change.
* Unit tests can run very fast, and they are shared across all the Knowledge Base if you are using GeneXus Server.
* Developers can run their tests on Genexus IDE without using or installing other tools
* Developers can test their Procedures, without creating a special “Test Procedure WebPanel” for that purpose.

The next sections will guide you on [Unit Testing capabilities](https://wiki.genexus.com/commwiki/wiki?38337) inside GeneXus.   
If you want to test different WebPanels behavior, please visit [UI Testing](https://wiki.genexus.com/commwiki/wiki?38353).

## [Compatibility](#Compatibility)

GXtest supports Unit Testing capabilities over GeneXus 15 and higher versions over Java and .NET Web environments.

Also, NET Core support is provided under GeneXus 16.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [Test Target property](https://wiki.genexus.com/commwiki/wiki?42595) | [Testing Automation Pyramid](https://wiki.genexus.com/commwiki/wiki?38333) | [Category:Unit Test object](https://wiki.genexus.com/commwiki/wiki?38401) |

---
