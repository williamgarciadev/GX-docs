---
title: "Patterns MSBuild Tasks"
source_id: 12559
source_url: https://wiki.genexus.com/commwiki/wiki?12559
genexus_version: "18"
---

# Patterns MSBuild Tasks

A [Pattern](https://wiki.genexus.com/commwiki/wiki?2814) can be applied from the User Interface or batch using the [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908). The tasks related to [Patterns](https://wiki.genexus.com/commwiki/wiki?2814) are the following:

* **ApplyPatternOnParent**: applies a [Pattern](https://wiki.genexus.com/commwiki/wiki?2814) to an object.

#### [Syntax](#Syntax)

```
<ApplyPatternOnParent
  ParentName="Object Name"
  ParentType="GeneXus ObjectType, for example Transaction"
  Pattern="Pattern Name to be applied for example WorkWith" 
/>
```

*ParentName*: the associated [GeneXus Object name](https://wiki.genexus.com/commwiki/wiki?1866) to be applied a pattern.

*ParentType*: the [GeneXus Object type](https://wiki.genexus.com/commwiki/wiki?1866) for example Transaction, WebPanel, Procedure, etc...

*Pattern*: Name of the pattern to be applied; for example *[WorkWith](https://wiki.genexus.com/commwiki/wiki?5636)*, etc... If you don't know the exact pattern name, check the *Name* attribute in the Pattern definition file. Locate the <X>.Pattern object under <GX>\Packages\Patterns\X; for example for the *Work With* one you will notice the following:

```
<Pattern xmlns="http://schemas.genexus.com/Patterns/Definition/v1.0" 
    Publisher="Artech" 
    Id="78CECEFE-BE7D-4980-86CE-8D6E91FBA04B" 
    Name="WorkWith" <---
    ...
```

#### [Sample](#Sample)

Suppose you have the following target in a *test.build* file located under *C:\temp\MSBuild*:

```
<Target Name="ApplyPatternOnParent">
  <ApplyPatternOnParent
    Pattern="$(Pattern)"
    ParentType="$(ParentType)"
    ParentName="$(ParentName)"
  />
</Target>
```

To create the [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?5636) on a *Customer* [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) you should open the Knowledge base and run the msbuild task as follows:

```
msbuild.exe /t:OpenKnowledgeBase;ApplyPatternOnParent /p:
KBPath=c:\Models\myKnowledgeBase;
Pattern="WorkWith";
ParentType="Transaction";
ParentName="Customer"
 /nologo "c:\temp\MSBuild\test.msbuild"
 
```

* **ApplyPattern**: Reaplies a [pattern](https://wiki.genexus.com/commwiki/wiki?2814) to an object using the pattern instance.

#### [Syntax](#Syntax)

```
<ApplyPattern
  Pattern="Pattern Name"
  InstanceName="Pattern instance name"
  ForceApply="True|False" (only in GX X Evolution2 version) 
  />
```

*Pattern*: Name of the pattern to be reapplied; valid options are WorkWith, Category etc...

*InstanceName*: Pattern instance name, for example *WorkWithCustomer* (assuming you applied the *WorkWith* pattern to the *Customer* Transaction).   
If the InstanceName is empty, the pattern is applied to all instances (only in GX X Evolution2 version).

*ForceApply*: Refresh all the instances. This flag is ignored when you specify an specific instance to apply (only in GX X Evolution2 version).

#### [Sample](#Sample)

Suppose you have the following target in a *test.build* file located under *C:\temp\MSBuild*:

```
<Target Name="ApplyPattern">
  <ApplyPattern
    Pattern="$(Pattern)"
    InstanceName="$(InstanceName)"
  />
</Target>
```

To reapply the [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?5636) on a *WorkWithCustomer* pattern instance you should run something like the following:

```
msbuild.exe /t:OpenKnowledgeBase;ApplyPattern /p:
KBPath=c:\Models\myKnowledgeBase;
Pattern="WorkWith";
InstanceName="WorkWithCustomer"
 /nologo "c:\temp\MSBuild\test.msbuild"
```

#### [Comments](#Comments)

* The *msbuild.exe* file is located in the Microsoft .net 2.0 folder, generally *C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\*
* Your msbuild file should add a reference to the *Genexus.Tasks.Patterns.targets* file located under the GeneXus installation using the *Import* keyword, for example

```
<Import Project="c:\GeneXusInstallationDirectory\Genexus.Tasks.Patterns.targets"/>
```
