---
title: "AssemblyImport MSBuild Task"
source_id: 44422
source_url: https://wiki.genexus.com/commwiki/wiki?44422
genexus_version: "18"
---

# AssemblyImport MSBuild Task

Performs the Assembly import (.Net or .Net core DLL) and creates [External Objects](https://wiki.genexus.com/commwiki/wiki?5737) on the current Knowledge Base.

## [Syntax](#Syntax)

```
<AssemblyImport 
  AssemblyFileName="$(AssemblyFileName)"
  Prefix="$(Prefix)"
  InspectByReflection="$(InspectByReflection)"
  Description="$(Description)"
/>
```

### [Options](#Options)

*AssemblyFileName:*fully or partially qualified name of an Assembly.

*Prefix*: defines the prefix for the imported objects. If it starts with *#toxml*, instead of creating GeneXus objects in the current KB, it will create an XML file with the imported dll.

*InspectByReflection*: Boolean value detailing the kind of process to inspect the Assembly (default is false) which means the *Mono.Cecil* infrastructure is used (supports .Net and .NetCore assemblies). When enabling this property the .Net framework is internally used to inspect the assemblies (.Net assemblies and dependencies are needed).

*Description*: Desired description for the external objects created as a result of the assembly import process.

### [Samples](#Samples)

Import file c:\MyExports\ImportTestFile.xpz into the currently opened Knowledge Base.

```
<Project DefaultTargets="InspectAssemblies" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
    <Import Project="C:\gx16\Genexus.Tasks.targets"/>
    <Import Project="C:\gx16\DotNetAssemblyInspector.Tasks.targets"/>
    <PropertyGroup>
        <DefaultTestPath>.</DefaultTestPath>
    </PropertyGroup>
    <Target  Name="InspectAssemblies">
        <OpenKnowledgeBase Directory="$(DefaultTestPath)"  />
        <AssemblyImport AssemblyFileName="C:\temp\ClassLibrary1.dll"/>
    </Target>
</Project>
```

#### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

### [See Also](#See+Also)

[GeneXus MSBuild Taks](https://wiki.genexus.com/commwiki/wiki?3908)

####
