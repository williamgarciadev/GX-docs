---
title: "CI / CD integration for Unit Tests"
source_id: 38332
source_url: https://wiki.genexus.com/commwiki/wiki?38332
genexus_version: "18"
---

# CI / CD integration for Unit Tests

As discussed in the [Typical GeneXus development cycle for Agile](https://wiki.genexus.com/commwiki/wiki?38329), the software industry has evolved to enable a set of automations to boost quality and adoption of DevOps practices. Continuous integration is a fundamental step to start working in a proper way with [GXserver](https://wiki.genexus.com/commwiki/wiki?30869,,) and GXtest.

Continuous integration means that every time a developer makes a change in a centralized repository in GXserver KB, that code will trigger some automation to check that recent changes can successfully build a new version without conflicts with other developments. Also, it will check that there are no missing references to be committed and that the build succeeds in a totally different environment than it was developed. With this step in your process, you will be avoiding the typical dev phrase “it works/builds on my machine”. Theoretically, CI means to integrate every time a developer makes a commit, but sometimes in your methodology, you want to do this less often but still getting often (maybe daily) feedback regarding your app status. In other words, that is continuously integrated.

CI tools are usually agnostic, and you can integrate GeneXus with any CI tools using msbuild.exe on windows platforms. As an example, we will be showing some cases using Jenkins CI.

In the same way that you will use GeneXus Tasks such as OpenKB, BuildAll, RebuildAll, etc. for handling Knowledge Base tasks and Team Development Tasks for handling GXServer, to run Unit tests you will need to call some extra tasks/steps. You can find proper information of these tasks in this article: [GXtest MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?40738,,).

## [How to run all the unit tests in your KB](#How+to+run+all+the+unit+tests+in+your+KB)

**GXtest.msbuild**: Assume that this is the filename of the MSBuild File that you are building to run Unit Tests.

**In the beginning, you will need to import two MSBuild projects that contain predefined tasks that you are going to use on your file. Those projects are GeneXus.Tasks.targets and GXtest.targets.**

The following is an example of the MSBuild file:

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

Having this file configured properly, you can launch all unit tests using this command:

```
MSBuild.exe /t:RunAllTests /p:KBPath="C:\Models\KbTests" /p:EnvironmentName="CSharpWeb" /p:TestType="Unit" /p:GXUser="local\admin" /p:GXPass="password" $env:GX_PROGRAM_DIR"\GXtest.msbuild"
```

## [How to run a tests list of your KB](#How+to+run+a+tests+list+of+your+KB)

As well as the task Run All Tests, you will need to configure an MSBuild file as shown below:

```
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">    
<Import Project=".\GeneXus.Tasks.targets"/>    
<Import Project=".\GXtest.targets"/>

<Target Name="RunTestsList">
    <OpenKnowledgeBase Directory="$(KBPath)"/>
    <SetActiveEnvironment EnvironmentName="$(EnvironmentName)"/>
    <RunTests TestObjects="$(TestObjects)" ServerUserName="$(GXUser)" ServerPassword="$(GXPass)"/>
    <CloseKnowledgeBase/>
</Target>
</Project>
```

Having this file configured properly, you can run specific unit tests using this command:

```
MSBuild.exe /t:RunTestsList 
/p:KBPath="C:\Models\KbTests"
/p:EnvironmentName="CSharpWeb"
/p:TestObjects="UnitTest1;UnitTest2;UnitTest3"
/p:GXUser="local\admin" /p:GXPass="password"
$env:GX_PROGRAM_DIR"\GXtest.msbuild"
```

Take into account that you can group any kind of tests on a [Test Suite object](https://wiki.genexus.com/commwiki/wiki?47819) object and run it from MSBuild specifying its name as before.

## [Examples](#Examples)

[See MSbuild examples](https://wiki.genexus.com/commwiki/wiki?40739)


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
