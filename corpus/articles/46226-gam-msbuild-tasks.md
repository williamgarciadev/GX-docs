---
title: "GAM MSBuild Tasks"
source_id: 46226
source_url: https://wiki.genexus.com/commwiki/wiki?46226
genexus_version: "18"
---

# GAM MSBuild Tasks

Here is the list of [GeneXus MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) related to [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

When [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) are used, the **GeneXus.Tasks.targets** and **Genexus.GAM.Tasks.targets** files have to be imported in the basic script file, adding the following line:

```
<Import Project="$(GX_PROGRAM_DIR)\Genexus.Tasks.targets" />
<Import Project="$(GX_PROGRAM_DIR)\Genexus.GAM.Tasks.targets" />
```

## [Task List](#Task+List)

### [SetGAMOptions](#SetGAMOptions)

This task can be used when you open or create a new Knowledge Base and set the GAM Options.

#### [Syntax](#Syntax)

```
<SetGAMOptions 
          IncludeFrontendObjects="true|false" 
          IncludeSDSamples="true|false" 
          UpdateMode="never|always|prompt" 
          />
```

#### [Options](#Options)

*IncludeFrontendObjects*: set this to True to import panels for login, change password, user registration form, etc. for your web application; otherwise, set it to False.

*IncludeSDSamples*: set this to True to import the mobile panels for login, change password, user registration form, etc. for your native mobile application; otherwise, set it to False.

*UpdateMode*: this property specifies how the GAM objects that were imported will be updated when you change your GeneXus version. The possible values are:

never: the GAM objects will not be imported when you change the GeneXus version.

always: the GAM objects will always be imported when you change the GeneXus version.

prompt: the GeneXus IDE will ask you if you want to update the GAM objects when you change the GeneXus version.

#### [Samples](#Samples)

Suppose you have the following target in a *test.build* file located under *C:\temp*:

```
<Project DefaultTargets="Open" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">

  <Import Project="$(GX_PROGRAM_DIR)\Genexus.Tasks.targets" />

  <Import Project="$(GX_PROGRAM_DIR)\Genexus.GAM.Tasks.targets" />

  <PropertyGroup> <!--Input Parameters-->

      <WorkingDirectory></WorkingDirectory>

  </PropertyGroup>

  <Target Name="Open">

    <OpenKnowledgeBase Directory="$(WorkingDirectory)" />

  </Target>

  <Target Name="CheckSetGetGAMOptions" DependsOnTargets="SetGAMProperties;CheckGAMOptions"/>

  <Target Name="SetGAMProperties" DependsOnTargets="Open" >

  <SetGAMOptions 

          IncludeFrontendObjects="$(IncludeFrontEnd)" 

          IncludeSDSamples="$(IncludeSDSamples)" 

          UpdateMode="$(UpdateMode)" 

          />

  </Target>

</Project>
```

This script opens a Knowledge Base and sets the GAM options; you can run this by command line:

```
msbuild "c:\temp\test.msbuild" /t:CheckSetGetGAMOptions /p:WorkingDirectory="<KB directory>" /p:IncludeFrontEnd=true /p:IncludeSDSamples=true /p:UpdateMode=never /p:GX_PROGRAM_DIR=<GeneXus installation directory>
```

### [GetGAMOptions](#GetGAMOptions)

This task can be used when you open a new Knowledge Base and get the values for the GAM Options described in the previous task.

#### [Syntax](#Syntax)

```
<GetGAMOptions>
              <Output TaskParameter="IncludeFrontendObjects" PropertyName="GAMIncludeFrontend"/>
              <Output TaskParameter="IncludeSDSamples" PropertyName="GAMIncludeSD"/>
              <Output TaskParameter="UpdateMode" PropertyName="GAMUpdateMode"/>
          </GetGAMOptions>
```

#### [Sample](#Sample)

```
<Target Name="CheckGAMOptions" DependsOnTargets="Open" >
          <GetGAMOptions>
              <Output TaskParameter="IncludeFrontendObjects" PropertyName="GAMIncludeFrontend"/>
              <Output TaskParameter="IncludeSDSamples" PropertyName="GAMIncludeSD"/>
              <Output TaskParameter="UpdateMode" PropertyName="GAMUpdateMode"/>
          </GetGAMOptions>

          <Message Text="GAM option IncludeFrontendObjects: '$(GAMIncludeFrontend)'" />
          <Message Text="GAM option IncludeSDSamples: '$(GAMIncludeSD)'" />
          <Message Text="GAM option UpdateMode: '$(GAMUpdateMode)'" />

          <Error Condition="$(GAMIncludeFrontend) != $(IncludeFrontEnd)" Text="GAM option IncludeFrontendObjects should be $(IncludeFrontEnd), found '$(GAMIncludeFrontend)'" />
          <Error Condition="$(GAMIncludeSD) != $(IncludeSDSamples)" Text="GAM option IncludeSDSamples should be $(IncludeSDSamples), found '$(GAMIncludeSD)'" />
          <Error Condition="'$(GAMUpdateMode)' != $(UpdateMode)" Text="GAM option UpdateMode should be $(UpdateMode), found '$(GAMUpdateMode)'" />
  </Target>
```

### Availability

This feature is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).


|  |
| --- |
| **Backlinks** |
| [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) |

---
