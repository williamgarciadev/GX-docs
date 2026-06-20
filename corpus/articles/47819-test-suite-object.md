---
title: "Test Suite object"
source_id: 47819
source_url: https://wiki.genexus.com/commwiki/wiki?47819
genexus_version: "18"
---

# Test Suite object

Defines a sequence of tests that can be run in the specified order with several execution settings.

All test types can be mixed. Although, UI mobile tests will be executed always at the end of the execution now.

It is possible to add a parameterless main procedure as a setup object and also as a teardown object, i.e. the setup procedure will be executed before the first test in the suite and the teardown procedure will be executed at the end of the suite execution, regardless of the test results.

## [Create a Test Suite](#Create+a+Test+Suite)

`[imagen omitida: wiki id 47879]`

## [How to add tests to a suite](#How+to+add+tests+to+a+suite)

There are two ways for adding test objects to a test suite.

1. Typing in a test name in a test line
2. Dragging and dropping tests inside the test lines part

## [Test Suite object properties](#Test+Suite+object+properties)

There are some properties that can be set for a Test Suite object

* Continue On Error: it indicates whether the next suite must be executed or not if this suite fails. Default: true
* Retries: number of times to retry the suite if it fails. Default: 0
* Set Up Object Name: main procedure without parameters to be executed before the tests of the suite. For example, a procedure that creates some registers in DB needed for test execution.
* Tear Down Object Name: main procedure without parameters to be executed after the tests of the suite. This procedure is always executed regardless of intermediate test results.

## [Test line](#Test+line)

Every test you add to a suite can be configured with some extra settings:

* Continue on error: it indicates whether the next test must be executed or not if this test fails. Default: true
* Retries: number of times to retry the test if it fails. Default: 0
* Iterations: it is a visual shortcut if you want to execute N times an item and, instead of having N lines with the same test and the same configuration for each one, you can have a single line with iterations = N.

## [Running suites](#Running+suites)

You can run a suite by right-clicking on it and selecting the option Run Suite or from the Tests Explorer window similar to running tests.

Suites can also be run from [MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?40738,,) in your CI pipeline.

### [Availability](#Availability)

This object is available since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,).
