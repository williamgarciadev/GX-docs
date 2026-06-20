---
title: "Export test results to Allure in Jenkins"
source_id: 47611
source_url: https://wiki.genexus.com/commwiki/wiki?47611
genexus_version: "18"
---

# Export test results to Allure in Jenkins

[Allure Framework](http://allure.qatools.ru/) is an open source test result reporting tool that shows a representation of what has been tested in a web report. On this page, you can find a basic guide on how to use it to see and manage test execution results in a wider way.

Anytime you run tests using MSBuild tasks, you can add an [ExportResultsToAllure](https://wiki.genexus.com/commwiki/wiki?40738,,) extra task to output the test results in an Allure compatible format:

```
<ExportResultsToAllure TargetDir="$(AllureResultsPath)" Properties="KB=$(KBPath);Environment=$(EnvironmentName);$(TestingEnvironment)"> 
    <Output TaskParameter="OutputFile" PropertyName="OutputFile" />
</ExportResultsToAllure>
```

## [Example using Jenkins](#Example+using+Jenkins)

This example uses GXtest.msbuild file (located on GeneXus IDE root folder).

First, install the [Allure Jenkins plugin](https://plugins.jenkins.io/allure-jenkins-plugin/) from the [plugins section in Jenkins](https://www.jenkins.io/doc/book/managing/plugins/). Then, add the Allure commandline installation in the Jenkins global tools configurations:

`[imagen omitida: wiki id 47669]`

Note: GXtest is compatible with versions 1.x and 2.x of Allure reports format. We recommend using the latest version.

### [Step 1) Run UI tests step](#Step+1%29+Run+UI+tests+step)

To set the AllureResultsPath in the MSBuild build step, we recommend using the Jenkins variable $WORKSPACE, which targets the directory created by Jenkins for the current project. There are other optional parameters to set as [SourceFile and Properties](https://wiki.genexus.com/commwiki/wiki?40738,,). Note that to see the screenshots in the Allure report you must set the parameter [ScreenshotMode, HtmlMode](https://wiki.genexus.com/commwiki/wiki?45420) to override the values set on KB environment properties.

`[imagen omitida: wiki id 47903]`

By default, if a test fails, the RunTests task will be marked as failed as well. To process the test results, the additional parameter ***/p:AllowFailedTests="true"*** must be set on this step.

### [Step 2) Add Allure reporting step](#Step+2%29+Add+Allure+reporting+step)

Add a post-build step with Allure Report:

`[imagen omitida: wiki id 47629]`

Note that the folder location here is relative to the project folder ($WORKSPACE variable).

### [Test execution report](#Test+execution+report)

Selecting the "Allure Report" option, Jenkins goes to the Overview tab of the Allure Framework. The Overview page hosts several default widgets representing the basic characteristics of your project and testing environment.

`[imagen omitida: wiki id 47670]`

Note that the environment description and the user were above added in the TestingEnvironment target at [RunAllTest MSBuild task](https://wiki.genexus.com/commwiki/wiki?47611#Step+1%29+Run+UI+tests+step').

The list of executed tests is shown in the Suites tab. Selecting the UI test example, on the right side, you can see more details about the execution such as duration, browser and its version, and the executed commands in the selected test and their screenshots if taken.

`[imagen omitida: wiki id 47683]`

As we can set ScreenshotMode = "Always" and HtmlMode="Always", for each command, you can easily see the screenshot and HTML page when the command was executed:

`[imagen omitida: wiki id 47684]`

Selecting the unit test example, you can see the execution information and the assertion details:

`[imagen omitida: wiki id 47637]`

In the Graphs tab, you can see different statistics and trends collected from the test results

`[imagen omitida: wiki id 47666]`

For more details check the [Allure Report structure](https://docs.qameta.io/allure/#_report_structure).

[See the execution video of this example in Jenkins](https://wiki.genexus.com/commwiki/wiki?47689)

### [Availability](#Availability)

This feature is available since GeneXus 17 upgrade 2.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
