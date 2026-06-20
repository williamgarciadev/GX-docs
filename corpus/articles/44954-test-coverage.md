---
title: "Test Coverage"
source_id: 44954
source_url: https://wiki.genexus.com/commwiki/wiki?44954
genexus_version: "18"
---

# Test Coverage

This feature is useful to see what coverage a test does of its called objects for a particular test execution.

### [Set up](#Set+up)

To use it, the first thing to do is [enable Code Coverage for your environment](https://wiki.genexus.com/commwiki/wiki?44369).

Once it's enabled, the test objects may need to be rebuilt. To achieve that, you can perform a "Rebuild All Tests" operation under the "Test" menu.

### [Test Coverage information](#Test+Coverage+information)

Finally, when a test execution is finished, the coverage is displayed in the [Tests Results window](https://wiki.genexus.com/commwiki/wiki?47576).

The coverage percentage displayed is calculated as follows:

Given a test, coverage information about all its called objects (Procedures and Data Providers) is summarized and calculated taking into account only direct relative objects (the ones called directly by the test).

When a test doesn't call any other testable object, a hyphen is shown (e.g. test AssertXMLs in the previous image).

### [Example 1](#Example+1)

There is a test X that calls to procedure A and data provider B.

If during the execution of test X, 8 of 10 lines of object A and 2 of 10 lines of object B were executed, the coverage for that test for that execution will be 50% ( ((8 + 2) /(10 + 10)) \* 100); regardless of any other object that could be called by objects A or B.

Note: In case you want to view even more details about coverage, you can always open [Code Coverage window](https://wiki.genexus.com/commwiki/wiki?44369) and load the file from the file system. Note that the path of the generated code coverage file by GXtest is logged in the GeneXus IDE log.

### [Example 2](#Example+2)

There are 2 tests (test1 and test2) that call a procedure with an if / else sentence. The test1 covers 50% of the procedure and test2 covers the other 50%.

If both tests are executed together the total coverage for the procedure will be 100%. This is, coverage for each unit test will be displayed as 100%. On the other hand, if you run a single test of them, the displayed coverage will be displayed as 50%.

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369) |
| [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [Test Results window](https://wiki.genexus.com/commwiki/wiki?47576) |

---
