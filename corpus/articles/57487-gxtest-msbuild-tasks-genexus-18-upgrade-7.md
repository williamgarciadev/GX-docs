---
title: "GXtest MSBuild Tasks (GeneXus 18 Upgrade 7)"
source_id: 57487
source_url: https://wiki.genexus.com/commwiki/wiki?57487
genexus_version: "18"
---

# GXtest MSBuild Tasks (GeneXus 18 Upgrade 7)

Running tests in batches is easy using MSBuild tasks. You can do it using the **RunTests** task.

Note: Instead of using this task by itself, it is recommended to start using the GXtest.msbuild file that should be present on your GeneXus installation root folder, and modifying it to fit your own needs. You will see an example in the next article.

## [1 - RunTests (MSBuild Task)](#1+-+RunTests+%28MSBuild+Task%29)

This task allows running all the tests by their type in a specific [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), by their container module, or listed by their names using the TestObjects parameter.

Type: *{All, Unit, Web, SD, UI, Rest}*   
Specifies the type of test to run. Set:  
All: to run all enabled Unit tests first, then enabled web UI tests, and at last, all enabled SD UI tests. **Default value if TestObjects nor Module are set.**  
Unit: to run all enabled Unit tests.  
Web: to run all enabled web UI tests.  
SD: to run all enabled SD tests.  
UI: to run all enabled web and SD UI tests.  
Rest: to run all enabled Rest tests.

TestObjects: List of test object names separated by semicolons(;), including Test Suites  
Specifies the tests to build before the execution.

Note: when used from an MSBuild step in Jenkins semicolons (;) must be escaped so they are correctly passed from Jenkins to MSBuild. There are two options:

1- Surround parameters with single quotes e.g.:

```
'/p:TestObjects="Test1;Test2;Test3"'
```

2- Use %3B instead of ; e.g.:

```
/p:TestObjects="Test1%3BTest2%3BTest3"
```

Module (optional): *string*  
Name of a module object in the KB to run all the tests contained in it.

Build (optional): *bool*  
A boolean parameter to set whether to build test objects before executing them or not.  
If true, a build operation will be performed before executing the selected tests. **Default value.**  
If false, tests are directly executed without building them. Use this option if a build-all operation is already performed before and therefore test's binaries were generated beforehand.

DetailedResults (optional): *bool*  
A boolean parameter to set the verbosity of test results in the console output.  
If true, detailed results will be displayed on the console output. **Default value.**  
If false, only a summary is shown.

LogLevel (optional): *string*  
Specifies how much information is logged when executing web UI tests.  
The default value is the one set in the [*Log Level* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

Browser (optional): *{Chrome, IE, Firefox, Edge }*  
Specifies the browser name where web UI tests will run.  
The default value is the one set in the Default Browser property on the selected KB.

FullPageScreenshot (optional): *boolean*  
Specifies the default screenshot command behavior.  
The default value is the one set in [*Full Page Screenshot* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

VerifyStopsExecution (optional): *boolean*  
Specifies whether a failed Verify check will stop the test run.  
The default value is the one set in [*Verify Stops Execution* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

BaseURL (optional): *string*  
Specifies the base URL name where web UI tests will run on go commands, except when a full URL is used.  
The default value is the one set in [*Base URL* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

FileUploadBasePath (optional): *string*  
Specifies the base directory path to where files for web UI tests will be looked for in FileUploadBy commands.  
The default value is the one set in the [*File Upload Base Path* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

Arguments (optional): *string*  
Useful for setting properties for the browser at the moment it is opened. Each browser has its own set of properties defined although there are some common arguments for most of them: for example --headless to run tests without a visible interface.  
The default value is the one set in the [*Arguments* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

ScreenshotMode (optional): *string*  
Specifies when the screenshots are taken and saved during web UI tests execution.  
The default value is the one set in the [*Screenshot saving mode* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

HtmlMode (optional): *string*  
Specifies when the page's HTML is saved during web UI tests execution  
The default value is the one set in the [*Html saving mode* property](https://wiki.genexus.com/commwiki/wiki?45420) on the selected environment.

ExecutedCount (output): numeric  
Contains the total number of executed tests

SuccessCount (output): numeric  
Contains the total number of successful tests (includes WarningCount)

WarningCount (output): numeric  
Contains the total number of warned tests

SkippedCount (output): numeric  
Contains the total number of skipped tests

ErrorCount (output): numeric  
Contains the total number of failed tests (exception + error results).

ResultsFile (input/output) (optional): string

A path where to save the GXtest XML results file. As output contains the path of the mentioned file.

Note: for running tests in parallel this field is required, otherwise test execution results files are overwritten.

ServerUserName: *string*  
Specifies the server user name (local\username or gxtechnical\username)

ServerPassword: *string*  
Specifies the server password.

AllowFailedTests: *boolean*  
true: the task will succeed even if a test failed.  
false: if there are any failed tests, this task is set as failed. **Default value.**

Examples of use in an MSBuild file:

```
<RunTests Type="All" Browser="Chrome" BaseURL="http://mytestingenvironment/myApp/" Build="false" FileUploadBasePath="/testingDir/" ServerUserName="gxtechnical\username" ServerPassword="password"/>
```

```
<RunTests Type="Unit" DetailedResults="true" ServerUserName="local\admin" ServerPassword="password"/>

<RunTests Type="UI" Browser="Firefox" BaseURL="http://mytestingenvironment/myApp/" ServerUserName="gxtechnical\username" ServerPassword="password" AllowFailedTests="true"/>

<RunTests TestObjects="BasicTestsSuite;SmokeTestsHomePage;LooseTest2" Browser="Firefox" Arguments="--headless" AllowFailedTests="true">
      <Output TaskParameter="ExecutedCount" PropertyName="ExecutedCount"/>
      <Output TaskParameter="SuccessCount" PropertyName="SuccessCount"/>
      <Output TaskParameter="ErrorCount" PropertyName="ErrorCount"/>
      <Output TaskParameter="WarningCount" PropertyName="WarningCount"/>
      <Output TaskParameter="SkippedCount" PropertyName="SkippedCount"/>
      <Output TaskParameter="ResultsFile" PropertyName="ResultsFile"/>
</RunTests>

// Running in parallel tests from Module1Suite and Module2Suite

<RunTests TestObjects="Module1Suite" Browser="Firefox" BaseURL="http://mytestingenvironment/myApp/" ResultsFile="Module1SuiteResults.xml" ServerUserName="gxtechnical\username" ServerPassword="password" />

<RunTests TestObjects="Module2Suite" Browser="Firefox" BaseURL="http://mytestingenvironment/myApp/" ResultsFile="Module2SuiteResults.xml" ServerUserName="gxtechnical\username" ServerPassword="password" />
```

## [2 - RecordMockingData (MSBuild task)](#2+-+RecordMockingData+%28MSBuild+task%29)

Mocking works by recording data (SQLs / results) used for a test. This information is stored (as mocking data) and will be used in all future executions of the test in different environments.

Parameters:  
TestName: *string*  
Specifies the name of the test to record the mocking data for.

MockDataFilePath (output): *string*  
The absolute path where the mocking data file was saved.

ServerUserName: *string*  
Specifies the server user name (local or gxtechnical)

ServerPassword: *string*  
Specifies the server password.

Examples of use in an MSBuild file:

```
<RecordMockingData TestName="testExample"  ServerUserName="gxtechnical\username" ServerPassword="password">
    <Output TaskParameter="MockDataFilePath" PropertyName="MockPath"/>
</RecordMockingData>
```

```
<RecordMockingData TestName="testExample" ServerUserName="local\admin" ServerPassword="password">
    <Output TaskParameter="MockDataFilePath" PropertyName="MockPath"/>
</RecordMockingData>
```

## [3 - JUnitExportTests (MSBuild task)](#3+-+JUnitExportTests+%28MSBuild+task%29)

Converts the last execution test results to JUnit format.

Parameters:

SourceResultsFile: *string (optional)*  
A source GXtest XML results file to convert to JUnit XML format.

JUnitTestFilePath (input/output): *string (optional)*  
An absolute directory path where the JUnit file will be saved / As output contains the JUnit file's absolute path.  
If the directory path does not exist then GXtest will try to create it.  
Passing an absolute file path where test results will be exported is supported.

ServerUserName: *string*  
Specifies the server user name (local or gxtechnical).

ServerPassword: *string*  
Specifies the server password.

IncludeFirstDifference: *boolean*  
Sets if for each failed assertion the first difference found between the expected and obtained value is included as context in the report.  
This is done only if the values involved exceed the 20 characters.  
The default value is True.

Examples of use in an MSBuild file:

```
<JUnitExportTests JUnitTestFilePath="C:/path" ServerUserName="gxtechnical\username" ServerPassword="password">  
    <Output TaskParameter="JUnitTestFilePath" PropertyName="JUnitTestFilePathOutput"/>
</JUnitExportTests>
```

```
<JUnitExportTests JUnitTestFilePath="C:/non-existingPath" ServerUserName="local\admin" ServerPassword="password"> 
    <Output TaskParameter="JUnitTestFilePath" PropertyName="JUnitTestFilePathOutput"/>
</JUnitExportTests>
```

```
<JUnitExportTests JUnitTestFilePath="C:/path/customName.xml" ServerUserName="local\admin" ServerPassword="password"> 
    <Output TaskParameter="JUnitTestFilePath" PropertyName="JUnitTestFilePathOutput"/>
</JUnitExportTests>
```

## [4 - ExportResultsToHTML (MSBuild task)](#4+-+ExportResultsToHTML+%28MSBuild+task%29)

Converts the last execution test results to custom GXtest HTML format.

Parameters:  
HTMLFilePath (input/output): *string*  
An absolute directory path where the HTML file will be saved / As output contains the HTML file's absolute path.  
If the directory path does not exist then GXtest will try to create it.  
Passing an absolute file path where test results will be exported is supported.  
If empty, the target directory used is a folder 'TestResults' located inside the KB path.

ExportType: string  
All: all tests will be exported.  
Failed: only failed test results (result is Error or Exception) will be exported.  
Passed: only passed test results (result is OK or Warning) will be exported.  
If empty, all test results are exported.

ServerUserName: *string*  
Specifies the server user name (local or gxtechnical).

ServerPassword: *string*  
Specifies the server password.

Examples of use in an MSBuild file:

```
<ExportResultsToHTML ExportType="All" HTMLFilePath="C:\folder\" >
      <Output TaskParameter="HTMLFilePath" PropertyName="HTMLFilePath" />
</ExportResultsToHTML>
```

```
<ExportResultsToHTML HTMLFilePath="myPath\" >
      <Output TaskParameter="HTMLFilePath" PropertyName="HTMLFilePath" />
</ExportResultsToHTML>
```

```
<ExportResultsToHTML ExportType="Failed" HTMLFilePath="$(FilePath)" >
      <Output TaskParameter="HTMLFilePath" PropertyName="HTMLFilePath" />
</ExportResultsToHTML>
```

## [5 - ExportResultsToAllure (MSBuild task)](#5+-+ExportResultsToAllure+%28MSBuild+task%29)

Converts GXtest execution results to [Allure](https://github.com/allure-framework) format. The goal is to have integration with tools that allow us to see execution results including successful steps and screenshots for UI commands.

**Parameters**:

SourceFile: *string (optional)*  
Source GXtest formatted results file to be converted to Allure format. Default value: the path of the current opened KB.

TargetDir (input/output): *string (optional)*  
An absolute directory path where the Allure file will be saved.  
If empty, the target directory used is the same directory as the SourceFile parameter value.  
If the directory path does not exist then GXtest will try to create it.  
It is NOT supported by passing an absolute file path where test results will be exported, since Allure requires a UUID base file name.

Note: this directory is cleaned before the export of results so everything works fine at the Allure report level. Removed files are the ones that end on '*-testsuite.xml*' or contain '*-attachment.*'

Properties: *string (optional)*  
Properties to be shown as environment variables on Allure reports. Typical values can be the KB path, KB version, and environment name, among others.

The format for this is *Properties="var1=value1;var2=value2;var3=value3"*

Note: when used from an MSBuild step in Jenkins semicolons (;) must be escaped so they are correctly passed from Jenkins to MSBuild. There are two options:

1- Surround parameters with single quotes e.g.:

```
'/p:OtherVariables="var1=value1;var2=value2;var3=value3"'
```

2- Use %3B instead of ; e.g.:

```
/p:OtherVariables="var1=value1%3Bvar2=value2%3Bvar3=value3"
```

ServerUserName: *string*  
Specifies the server user name (local or gxtechnical).

ServerPassword: *string*  
Specifies the server password.

Examples of use in an MSBuild file:

```
<ExportResultsToAllure Properties="KB=$(KBPath);Environment=$(EnvironmentName);CustomFixedVar=customValue;$(OtherVariables)" >
      <Output TaskParameter="OutputFile" PropertyName="OutputFile" />
</ExportResultsToAllure>
```

```
<ExportResultsToAllure SourceFile="customPath/myFile.xml" >
      <Output TaskParameter="OutputFile" PropertyName="OutputFile" />
</ExportResultsToAllure>
```

```
// Jenkins example: invoked as /p:AllureResultsPath="$WORKSPACE\allure-results"
<ExportResultsAllure TargetDir="$(AllureResultsPath)" Properties="KB=$(KBPath);Environment=$(EnvironmentName);CustomFixedVar=customValue;$(OtherVariables)" >
      <Output TaskParameter="OutputFile" PropertyName="OutputFile" />
</ExportResultsToAllure>
```


|  |
| --- |
| **Backlinks** |
| [Changelog GXtest](https://wiki.genexus.com/commwiki/wiki?43807) |

---
