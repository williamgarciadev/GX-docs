---
title: "Junit for Jenkins"
source_id: 41320
source_url: https://wiki.genexus.com/commwiki/wiki?41320
genexus_version: "18"
---

# Junit for Jenkins

## [Get test case execution results in JUnit Format](#Get+test+case+execution+results+in+JUnit+Format)

Running test cases in batch mode is achieved by [using MSBuild test tasks](https://wiki.genexus.com/commwiki/wiki?40739).

This is useful in CI Tools like Jenkins since they can read these XML files and show test case reports containing failed assertions.

Anytime you run tests (unit or UI) using MSBuild tasks, you can add an extra task to see test results in XML JUnit format:

```
<JUnitExportTests JUnitTestFilePath="$(JUnitTestFilePath)">
      <Output TaskParameter="JUnitTestFilePath" PropertyName="JUnitTestFilePathOutput" />
</JUnitExportTests>
```

This will create an XML file with the name TestResultJUnit*yyyy-dd-mm--hh-mm-ss*.xml containing test results.

Note: This task needs to run over a previously opened KB after running test cases.

## [Example using Jenkins](#Example+using+Jenkins)

This example uses GXtest.msbuild file (usually located on GeneXus IDE root folder).  
Before starting, make sure you install the [Junit reporting plugin](http://wiki.jenkins.io/display/JENKINS/JUnit+Plugin) in Jenkins.

### [Step 1) Run unit tests step](#Step+1%29+Run+unit+tests+step)

Add JUnitTestFilePath parameter in MSBuild:

`[imagen omitida: wiki id 42559]`

By default, if a test fails, the RunTests task will be marked as failed as well. To prevent be marked as failed and process test results, the additional parameter ***/p:AllowFailedTests="true"*** must be set on this step.

Make sure that the Jenkins' user has writing privileges over the folder you want to store the test results.

### [Step 2) Add reporting in a "post-build" event](#Step+2%29+Add+reporting+in+a+%22post-build%22+event)

Use the JUnit plugin pointing to the previously used folder (in the example it is using WORKSPACE Jenkins folder):

`[imagen omitida: wiki id 42560]`

### [Results](#Results)

You will start viewing Test results :

`[imagen omitida: wiki id 41325]`

and trends...

`[imagen omitida: wiki id 42561]`


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
|

---
