---
title: "Running UI tests under CI"
source_id: 40737
source_url: https://wiki.genexus.com/commwiki/wiki?40737
genexus_version: "18"
---

# Running UI tests under CI

In the same way that you will use GeneXus Tasks such as OpenKB, BuildAll, RebuildAll, etc. for handling Knowledge Base tasks and Team Development Tasks for handling [GXserver](https://wiki.genexus.com/commwiki/wiki?30869,,), in order to run UI tests, you will need to call some extra tasks/steps. You can take a look at the [documentation of these tasks](https://wiki.genexus.com/commwiki/wiki?40738,,).

## [How to run all your UI tests in your KB](#How+to+run+all+your+UI+tests+in+your+KB)

**GXtest.msbuild**: Assume that this is the filename of the MSBuild File that you are building to run UI Tests.

**In the beginning, you will need to import two MSBuild projects that contain predefined tasks that you are going to use on your file. Those projects are GeneXus.Tasks.targets and GXtest.targets.**

The following is an example of an MSBuild file:

```
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="$(GX_PROGRAM_DIR)\GeneXus.Tasks.targets"/>
  <Import Project="$(GX_PROGRAM_DIR)\GXtest.targets"/>

  <Target Name="RunAllTests">
    <OpenKnowledgeBase Directory="$(KBPath)"/>
    <SetActiveEnvironment EnvironmentName="$(EnvironmentName)"/>
    <RunTests Type="$(TestType)" ServerUserName="$(GXUser)" ServerPassword="$(GXPass)"/>
    <CloseKnowledgeBase/>
  </Target>
</Project>
```

Having this file configured properly, you can launch all UI tests using this command:

```
MSBuild.exe /t:RunAllTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestType="UI" /p:GXUser="local\admin" /p:GXPass="password" $env:GX_PROGRAM_DIR"\GXtest.msbuild"
```

## [How to run a tests list (suite) of your KB](#How+to+run+a+tests+list+%28suite%29+of+your+KB)

As well as the task Run All Tests, you will need to configure an MSBuild file as is shown below:

```
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
<Import Project="$(GX_PROGRAM_DIR)\GeneXus.Tasks.targets"/>
<Import Project="$(GX_PROGRAM_DIR)\GXtest.targets"/>

<Target Name="RunSuite">
    <OpenKnowledgeBase Directory="$(KBPath)"/>
    <SetActiveEnvironment EnvironmentName="$(EnvironmentName)"/>
    <RunTests TestObjects="$(TestObjects)" ServerUserName="$(GXUser)" ServerPassword="$(GXPass)"/>
    <CloseKnowledgeBase/>
</Target>
</Project>
```

Having this file configured properly, you can run a specific test suite using this command:

```
MSBuild.exe /t:RunSuite 
/p:KBPath="C:\Models\KbTests"
/p:EnvironmentName="CSharpWeb"
/p:TestObjects="TestSuite1"
/p:GXUser="local\admin" /p:GXPass="password"
$env:GX_PROGRAM_DIR"\GXtest.msbuild"
```

You can also run any number of test objects, specifying them separated by a comma:

```
/p:TestObjects="UnitTest1;WebUITest1;WebUITest2;TestSuite1;TestSuite2"
```

## [Take into account](#Take+into+account)

In order for UI tests to run properly, it is required that the browser's GUI can be opened by the CI server. For example, with Jenkins, you probably need to execute it as a war by command line instead of as a window service.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
