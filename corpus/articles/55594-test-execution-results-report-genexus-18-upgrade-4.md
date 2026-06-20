---
title: "Test Execution Results Report (GeneXus 18 Upgrade 4)"
source_id: 55594
source_url: https://wiki.genexus.com/commwiki/wiki?55594
genexus_version: "18"
---

# Test Execution Results Report (GeneXus 18 Upgrade 4)

GXtest allows you to export an HTML report that shows the test execution results. The test execution information will be easily available to be shared with the rest of the software development team.

After running the tests, you can export the HTML test case report by clicking the “Export” button (included in the “Tests Results” window, see image below) and selecting the destination path.

`[imagen omitida: wiki id 49838]`

In the HTML report, you can look at the full execution results. For each suite and test, it shows the test result (OK, WARNING, ERROR, SKIPPED, or EXCEPTION), the execution date, the time elapsed, a graphic with passed and failed validations, and a table with detailed information about assertions and test steps.

In the following image, you can look at an HTML report example of “stringConcatenationUnitTest” unit test and “openGXtestWiki” UI test execution:

`[imagen omitida: wiki id 47902]`

Note that when any test step fails, it will be represented in the pie graphic.
