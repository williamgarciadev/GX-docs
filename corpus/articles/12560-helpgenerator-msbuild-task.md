---
title: "HelpGenerator MSBuild Task"
source_id: 12560
source_url: https://wiki.genexus.com/commwiki/wiki?12560
genexus_version: "18"
---

# HelpGenerator MSBuild Task

The *HelpGenerator* [MSBuild Task](https://wiki.genexus.com/commwiki/wiki?3908) can be applied to generate the [application help](https://wiki.genexus.com/commwiki/wiki?12152).

#### [Syntax](#Syntax)

```
<HelpGenerator
  AttRef="true|false"
  CHMCompilerPath="c:\...\hhc.exe"
  CHMCustomContentPath="c:\...\file.hhc"
  CHMCustomIndexPath="c:\...\file.hhk"
  CHMFullTextSearch="true|false"
  CHMMainPagePath="c:\...\main.htm"
  CSS="CssSampleFile"
  IncludeTitle="true|false"
  Language="KBLanguageName|*All"
  ObjectGeneration="All|Modified"
  ObjRef="true|false"
  OutputType="HTML|CHM"
  SeeAlsoColumns="[1..6]"
  SeeAlsoFormat="Table|List"
  SeeAlsoTitle="See Also Text"
  VarRef="true|false"
  />
```

*Language* (string): associated language name to generate Help. The special value "*\*ALL*" generates help for each language defined in the KB. By default it generates help using the selected KB language.

*ObjectGeneration* (string): valid values are:

* *\*All*: forces the generation of help for all GeneXus objects (default value).
* *Modified*: generates help only for the objects modified since the last help generation.

*IncludeTitle* (boolean): valid values are:

* *true*: includes the object description as Page Title.
* *false*: (default value) No Title is set.

*CSS* (string): references a CSS file to be included in each generated help file.

*SeeAlsoTitle* (string): "See Also" customized Title. In this section all automatic references are generated.

*SeeAlsoFormat* (string): "See Also" Format type section: valid values are:

* *Table*: generates an Html table to group the links.
* *List*: generates a list of links separated by a colon.

*OutputType*(string): valid values are:

* *HTML*: generates help files using HTML format (default value).
* *CHM*: generates help files using CHM format.

*SeeAlsoColumns* (int): Number of columns when using the "*See Also*" section as *Table*; valid values are 1 (default value) to 6.

*VarRef* (boolean): includes variable help references.

*AttRef* (boolean): includes attribute help references.

*ObjRef* (boolean): includes object help references.

*CHMCompilerPath* (string):Complete path for the CHM compiler, generally located in "*C:\Program Files\HTML Help Workshop\hhw.exe*".

*CHMCustomContentPath*(string):Complete path for a custom CHM content file (tree structure shown in the CHM Content tab), generally a file with *hhc* extension.

*CHMCustomIndexPath*(string):Complete path for a custom index file, generally a file with *hhk* extension.

*CHMFullTextSearch* (boolean): valid values are:

* *true*: configures the CHM compiler to define a text search.
* *false*: (default value) No Title is set.

*CHMMainPagePath*(string):Complete path for a customized Main Page; by default it generate a sample one.

#### [Sample](#Sample)

Suppose you have the following target in a *test.build* file located under *C:\temp\MSBuild*:

```
<Target Name="HelpGenerator">
  <HelpGenerator
    Language="$(Language)"
    ObjectGeneration="$(ObjectGeneration)"
    IncludeTitle="$(IncludeTitle)"
    CSS="$(CSS)"
    SeeAlsoTitle="$(SeeAlsoTitle)"
    SeeAlsoFormat="$(SeeAlsoFormat)"
    SeeAlsoColumns="$(SeeAlsoColumns)"
    VarRef="$(VarRef)"
    AttRef="$(AttRef)"
    ObjRef="$(ObjRef)"
  />
</Target>
```

To force the generation of the application help in all languages you need to open the Knowledge Base and run the msbuild task as follows:

```
msbuild.exe /t:OpenKnowledgeBase;HelpGenerator /p:
KBPath=c:\Models\myKnowledgeBase;
Language="*All"
 /nologo "c:\temp\MSBuild\test.msbuild"
```

### [Comments](#Comments)

* The *msbuild.exe* file is located in the Microsoft .net 2.0 folder, generally *C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\*
* Your msbuild file should add a reference to the *Genexus.Tasks.targets* file located under the GeneXus installation using the *Import* keyword, for example

```
<Import Project="c:\GeneXusInstallationDirectory\Genexus.Tasks.targets"/>
```
