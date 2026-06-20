---
title: "Running Unit tests"
source_id: 38345
source_url: https://wiki.genexus.com/commwiki/wiki?38345
genexus_version: "18"
---

# Running Unit tests

There are 4 ways to run unit tests:

1. Using the context menu in the Unit Test object
2. Using Test Explorer on GeneXus IDE
3. Using the “Run after build” option
4. Or using a CI/CD tool via msbuild.exe

## [1 - Using the context menu in the Unit Test object](#1+-+Using+the+context+menu+in+the+Unit+Test+object)

Right-click on the unit test object's tab and then select the "Run Test(s)" option

`[imagen omitida: wiki id 52116]`

## [2 - Using the Tests Explorer](#2+-+Using+the+Tests+Explorer+)

`[imagen omitida: wiki id 52235]`

Tests Explorer is a tree view containing all the tests that are currently in your knowledge base. To run the test from GeneXus IDE, go to the Tests Explorer window, select each one you want to run, then press the Run button to execute tests and see the results.

`[imagen omitida: wiki id 52236]`

Also, you can run a test by right-clicking a test and selecting the option *Run.*

`[imagen omitida: wiki id 52237]`

Each time you run test cases from GeneXus IDE, you will find it useful to take a look at the “Tests Results” window, which contains the list of test results grouped by results.   
Each test name contains the time when the test ran and its elapsed time.

After selecting each test, the Execution detail panel appears showing:

* Test Result (pass/fail)
* The time of test when started
* The list of each assertion executed containing expected and obtained results.

This window is used to understand test results when they fail.

## [3 - Using the “Run tests after build” option](#3+-+Using+the+%E2%80%9CRun+tests+after+build%E2%80%9D+option)

This mode enables developers to run unit tests on a local (IDE) environment after each build.  
Once your team created some unit tests, you may find it interesting to run them all automatically, enabling developers to understand if they made a mistake causing some tests to fail almost immediately.   
You can turn this feature on in [Test Settings](https://wiki.genexus.com/commwiki/wiki?45420) inside GeneXus IDE.

## [4 - Using a CI/CD tool](#4+-+Using+a+CI%2FCD+tool+)

The best way to run unit tests is to integrate them into your Continuous Integration cycle, so you can trust that each change that has been sent to GXServer will be tested using this framework.   
This means you can add a step in your cycle that automatically runs all tests after each commit, or you can add them on specific instances that are suitable for your QA process.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
|

---
