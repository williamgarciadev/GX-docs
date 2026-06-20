---
title: "Running MSbuild using GXtest Target"
source_id: 40739
source_url: https://wiki.genexus.com/commwiki/wiki?40739
genexus_version: "18"
---

# Running MSbuild using GXtest Target

In order to create MSBuild tasks easier, you will find a **GXtest.msbuild** file in your GeneXus IDE installation folder. This file has predefined dependencies and previous tasks that are mandatory before running tests, such as opening a KB, selecting an environment, updating test references, building the tests runner, etc.

For example, this is how the “**RunTests**” target (which includes [RunTests task](https://wiki.genexus.com/commwiki/wiki?40738,,)) looks like in the GXtest.msbuild file:

```
<Target Name="RunTests">
    <OpenKnowledgeBase Directory="$(KBPath)"/>
    <SetActiveEnvironment EnvironmentName="$(EnvironmentName)"/>
    <ItemGroup>
      <UnitTests Include="$(UnitTests)"/>
      <WebTests Include="$(WebTests)"/>
      <Suites Include="$(Suites)"/>
    </ItemGroup>
    <RunTests Type="$(TestType)" TestObjects="$(TestObjects);$(UnitTests);$(WebTests);$(Suites)"
              Browser="$(Browser)" BaseURL="$(BaseURL)" FileUploadBasePath="$(FileUploadBasePath)" 
              ScreenshotMode="$(ScreenshotMode)" HtmlMode="$(HtmlMode)" Arguments="$(Arguments)"
              DetailedResults="$(DetailedResults)"
              ServerUserName="$(GXServerUser)" ServerPassword="$(GXServerPass)" 
              AllowFailedTests="$(AllowFailedTests)" ResultsFile="$(ResultsFile)">
      <Output TaskParameter="ExecutedCount" PropertyName="ExecutedCount"/>
      <Output TaskParameter="SuccessCount" PropertyName="SuccessCount"/>
      <Output TaskParameter="ErrorCount" PropertyName="ErrorCount"/>
      <Output TaskParameter="WarningCount" PropertyName="WarningCount"/>
      <Output TaskParameter="SkippedCount" PropertyName="SkippedCount"/>
      <Output TaskParameter="ResultsFile" PropertyName="ResultsFile"/>
      <!-- Type can be 'UI' to run only UI tests, 'Unit' to run only unit tests or 'All' to run both.  -->
    </RunTests>
    <JUnitExportTests SourceResultsFile="$(ResultsFile)" JUnitTestFilePath="$(JUnitTestFilePath)" >
      <Output TaskParameter="JUnitTestFilePath" PropertyName="JUnitTestFilePathOutput" />
    </JUnitExportTests>
    <ExportResultsToAllure TargetDir="$(AllureResultsPath)" Properties="KB=$(KBPath);Environment=$(EnvironmentName);$(TestingEnvironment)">
      <Output TaskParameter="OutputFiles" PropertyName="OutputFiles" />      
    </ExportResultsToAllure>
    <CloseKnowledgeBase/>
  </Target>
```

\*Note: you have to set the server user (local or gxtechnical) and password to run the tasks.

## [The next examples will show how to run different test cases in a CI / CD scheme](#The+next+examples+will+show+how+to+run+different+test+cases+in+a+CI+%2F+CD+scheme)

### [Example 1: Running all unit tests](#Example+1%3A+Running+all+unit+tests)

The following command line example runs all unit tests in the KB:

```
MSBuild.exe /t:RunTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestType="Unit"  /p:GXServerUser="local\admin" /p:GXServerPass="password"  PATH_TO_YOUR\GXtest.msbuild
```

### [Example 2: Running web UI tests using Google Chrome browser headless](#Example+2%3A+Running+web+UI+tests+using+Google+Chrome+browser+headless)

The following command line example runs 3 web UI tests (*TestName1, TestName2,*and *TestName3*) using Google Chrome headless:

```
MSBuild.exe /t:RunTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestObjects="TestName1;TestName2;TestName3" /p:Browser="Chrome"  /p:Arguments="--headless" /p:GXServerUser="local\admin" /p:GXServerPass="password" PATH_TO_YOUR\GXtest.msbuild
```

### [Example 3: Running Test Suites](#Example+3%3A+Running+Test+Suites)

You can run any type of test object by passing it as the TestObjects parameter, e.g. a unit test, a web UI test, and a test suite.

```
MSBuild.exe /t:RunTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestObjects="AUnitTest;AWebUITest;ATestSuite"  /p:GXServerUser="local\admin" /p:GXServerPass="password"  PATH_TO_YOUR\GXtest.msbuild
```

### [Example 4: Running tests in parallel](#Example+4%3A+Running+tests+in+parallel)

You can run any type of tests in parallel by setting the target file where results will be saved in. For example, if you have 2 test suites to run in parallel you can do:

```
MSBuild.exe /t:RunTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestObjects="TestSuite1" /p:ResultsFile="C:/TestSuite1.xml" /p:GXServerUser="local\admin" /p:GXServerPass="password"  PATH_TO_YOUR\GXtest.msbuild

MSBuild.exe /t:RunTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestObjects="TestSuite2" /p:ResultsFile="C:/TestSuite2.xml" /p:GXServerUser="local\admin" /p:GXServerPass="password"  PATH_TO_YOUR\GXtest.msbuild
```

Note: for any command execution you could override the properties set for a KB/environment, such as Browser, Base URL, Screenshot and HTML saving modes, Arguments, etc.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Changelog GXtest](https://wiki.genexus.com/commwiki/wiki?43807) | [CI / CD integration for Unit Tests](https://wiki.genexus.com/commwiki/wiki?38332) |
| [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [Junit for Jenkins](https://wiki.genexus.com/commwiki/wiki?41320) | [Running MSbuild using GXtest Target (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54203) |

---
