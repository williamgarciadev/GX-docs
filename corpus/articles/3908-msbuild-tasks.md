---
title: "MSBuild Tasks"
source_id: 3908
source_url: https://wiki.genexus.com/commwiki/wiki?3908
genexus_version: "18"
---

# MSBuild Tasks

GeneXus MSBuild Tasks let you automate all about [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) building (i.e., automating import, specification, generation and compilation tasks among others). In a declarative way (creating and programming scripts in XML format) you can easily specify the tasks to be done later with no user interaction.

This technology helps you create night builds of the applications you are developing, running automatic tests on them, etc.

GeneXus MSBuild Tasks are based on the Microsoft Build Engine (MSBuild). It is the new build platform for Microsoft and Visual Studio. It is a generic, extensible build platform and is part of Framework 2.0 (meaning it is free).

## [The basic script](#The+basic+script)

The following is a simple script intended for opening an existing Knowledge Base and building all its objects.

```
<Project DefaultTargets="OpenAndBuildAll" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
   <Import Project="C:\Program Files\Artech\GeneXus\GeneXusX\Genexus.Tasks.targets" />
   <Target Name="OpenAndBuildAll">
     <OpenKnowledgeBase Directory="C:\MyKnowledgeBases\TestKnowledgeBase" />
     <BuildAll />
   </Target>
</Project>
```

The Import directive (second script line) tells MSBuild where to find extensions specific to GeneXus; this is a required directive. Lines 3 through 6 identify a "Target" (something to be built) and specify what actions or "Tasks" must be accomplished to complete it. In this case, the tasks are OpenKnowledgeBase and BuildAll.

As you may have noticed, MSBuild coding is simple but powerful. You can take a closer look at all its features [here)](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild?view=vs-2019).

## [Task list](#Task+list)

The following task list describes all GeneXus MSBuild tasks (provided in GeneXus.MSBuild.Tasks.dll) and their parameters.

### [CreateKnowledgeBase](#CreateKnowledgeBase)

Creates a Knowledge Base in the specified directory based on a KB template.

#### [Syntax](#Syntax)

```
<CreateKnowledgeBase
   Directory="kbDirectory"
   Template="kbTemplate" |  BulkCopyFile="fileNameWithBCPformat"
   TemplatesPath="alternateTemplatesPath"
   Overwrite="true|false"
   IntegratedSecurity="true|false"
   UserId="userId"
   Password="password"  
   CreateDbInKbFolder="true|false"
   ServerInstance="instance"
   DBName="dbName"
   Language="language"
/>
```

#### [Options](#Options)

*Directory:* Itis the directory (absolute or relative) where the Knowledge Base should be created. **REQUIRED.**

*Template:* It is the name of a Knowledge Base template.

They are exported with GeneXus, and there are three of them:

* CSharp.KBTemplate  
  Sets properties for a [.NET Framework generator](https://wiki.genexus.com/commwiki/wiki?2892).
* NetCore.KBTemplate  
  Sets properties for a [.NET generator](https://wiki.genexus.com/commwiki/wiki?38604).
* Java.KBTemplate  
  Sets properties for a [Java generator](https://wiki.genexus.com/commwiki/wiki?12258).

You can specify this parameter or the *BulkCopyFile* parameter*.* The last alternative is to omit both parameters and define the Default Template in the genexus.exe.config file through the "DefaultEnvironmentForCreate" entry:

```
<add key="DefaultEnvironmentForCreate" value=".NET"/>
```

```
<add key="DefaultEnvironmentForCreate" value="Java"/>
```

The value that you have to specify is the Environment name (as it is shown in the 'Create Knowledge Base' dialog).

*BulkCopyFile*: Name of a file with BCP format to be able to create the KB from it.

*TemplatesPath:* Specifies the directory from which to obtain the template files. Said directory **must** contain the following folders from any GeneXus installation:

* ObjectDefinitions
* Startup
* Templates

*Overwrite:* It is true or false (default value). It indicates whether to delete or not the folder before creating the KB.

*IntegratedSecurity*: "true" indicates to use a trusted connection or "false" to use a specific user Id and password. Default: true.

*UserId*: The user's name to use when IntegratedSecurity is set to false.

*Password*: Password to use when IntegratedSecurity is set to false.

*CreateDbInKbFolder*: "true" to create KB database files in the Knowledge Base folder; "false" to use the DBMS' default data folder. Default: true.

*ServerInstance*: server name and the instance of the SQL Server, for example: ".\SQLEXPRESS" or "localhost". If you don't use this property, the local default instance will be used.

*DBName*: name of the KB database. The default is the KB name prefixed with "GX\_KB\_".

*Language*: the language of the Knowledge Base to create.

#### [Samples](#Samples)

Create a .NET Knowledge Base in the directory C:\MyKnowledgeBases.

```
<CreateKnowledgeBase Directory="C:\MyKnowledgeBases" Template="CSharp.KBTemplate" />
```

### [BulkCopyKnowledgeBase](#BulkCopyKnowledgeBase)

Generates the needed file to recreate the Knowledge Base [(BCP format)](https://docs.microsoft.com/en-us/sql/relational-databases/import-export/import-and-export-bulk-data-by-using-the-bcp-utility-sql-server?view=sql-server-ver16).

#### [Syntax](#Syntax)

```
<BulkCopyKnowledgeBase
   FullKB="true|false"
   Outputfile="outputfile"
/>
```

#### [Options](#Options)

*FullKB*: The "true" value generates the information for each version of the KB; The "false" value generates the information only for the active version. **REQUIRED.**  
  
*OutputFile*: Name of the .zip file that will contain the extracted information. If a value is not specified, this file is generated in the same directory of the KB with the same name.

Basically, the BulkCopyKnowledgeBase task is used to generate a BCP (the format used by GeneXus Server to send a KB or checkout), file with all the information of the current KB. It can be used to save a backup of said KB.

#### [Samples](#Samples)

1. Define the createBackup.msbuild file with the following content:

```
<Project DefaultTargets="RunTests" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="$(GXInstall)\genexus.tasks.targets"/>

  <Target Name="CreateBackupAndRestore">
    <PropertyGroup>
      <BackupFilename>KB_$([System.DateTime]::Now.ToString('yyyyMMddhhmmss')).bcp</BackupFilename>
      <BackupPath>$([System.IO.Path]::Combine('$(KBDir)', '$(BackupFilename)'))</BackupPath>
    </PropertyGroup>

    <!-- Create a backup of the KB located at $(KBDir) -->
    <OpenKnowledgeBase Directory="$(KBDir)"/>
    <BulkcopyKnowledgeBase FullKB="false" OutputFile="$(BackupPath)"/>
    <CloseKnowledgeBase/>

    <!-- Create a new KB from the BCP file in a sibling directory -->
    <CreateKnowledgeBase Directory="$(KBDir)_restore" BulkCopyFile="$(BackupPath)"/>
    <CloseKnowledgeBase/>
  </Target>

</Project>
```

2. Run by command line:

```
c:\>msbuild createBackup.msbuild /t:CreateBackupAndRestore /p:KBDir=c:\Models\MyKB /p:GXInstall="F:\Program Files (x86)\GeneXus\GeneXus17"
```

### [Import](#Import)

Read about the Import task in this article: [Import MSBuild Task](https://wiki.genexus.com/commwiki/wiki?35599).

### [OpenKnowledgeBase](#OpenKnowledgeBase)

Read about the OpenKnowledgeBase task in this article: [OpenKnowledgeBase MSBuild Task](https://wiki.genexus.com/commwiki/wiki?35862).

### [CloseKnowledgeBase](#CloseKnowledgeBase)

You don't have to explicitly close the KB using this task, it will be automatically closed when the MSBuild task finishes processing.

It would be useful when you need to open more than one KB during the same MSBuild task execution, for instance, export objects from one KB and import on another one.

#### [Syntax](#Syntax)

```
<CloseKnowledgeBase/>
```

### [SetEnvironmentProperty](#SetEnvironmentProperty)

Sets the value of a given environment property.

#### [Syntax](#Syntax)

```
<SetEnvironmentProperty Name="$(PropertyName)" Value="$(PropertyValue)"/>
```

#### [Options](#Options)

*Name*: $(PropertyName) is a valid property name. **REQUIRED.**

*Value*: $(PropertyValue) is a valid value for the specified property. **REQUIRED.**

#### [Samples](#Samples)

```
<SetEnvironmentProperty Name="Preserve Table Casing" Value="False" />
```

**Note**: As you notice in the sample code, it is valid to name the property in the MSBuild exactly as it appears in the [IDE](https://wiki.genexus.com/commwiki/wiki?5272)

`[imagen omitida: wiki id 53153]`

### [SetVersionProperty](#SetVersionProperty)

Sets the value of a given version property.

#### [Syntax](#Syntax)

```
<SetVersionProperty Name="$(PropertyName)" Value="$(PropertyValue)"/>
```

#### [Options](#Options)

*Name*: $(PropertyName) is a valid property name. **REQUIRED.**

*Value*: $(PropertyValue) is a valid value for the specified property. **REQUIRED.**

### [SetKnowledgeBaseProperty](#SetKnowledgeBaseProperty)

Sets the value of a Knowledge Base property.

#### [Syntax](#Syntax)

```
<SetKnowledgeBaseProperty Name="$(PropertyName)" Value="$(PropertyValue)" />
```

#### [Options](#Options)

*Name*: $(PropertyName) is a valid property name. **REQUIRED.**

*Value*: $(PropertyValue) is a valid value for the specified property. **REQUIRED.**

### [SetDataStoreProperty](#SetDataStoreProperty)

Sets the value of a given data store property.

#### [Syntax](#Syntax)

```
<SetDataStoreProperty Datastore="$(DataStoreName)" Name="$(PropertyName)" Value="$(PropertyValue)" />
```

#### [Options](#Options)

*Datastore*: $(DataStoreName) is the name of a Data Store defined in the Knowledge Base. Usually, the value of this name is "Default".

* Optional, default value "Default", not implemented yet.

*Name*: $(PropertyName) is a valid model property name. **REQUIRED.**

*Value*: $(PropertyValue) is a valid value for the specified property. **REQUIRED.**

### [SetGeneratorProperty](#SetGeneratorProperty)

Sets the value of a given generator property.

#### [Syntax](#Syntax)

```
<SetGeneratorProperty Generator="$(GeneratorName)" Name="$(PropertyName)" Value="$(PropertyValue)"/>
```

#### [Options](#Options)

*Generator*: $(GeneratorName) is the name of a Generator defined in the Knowledge Base. Usually, the value of this name is "Default" or "Reorg".

* Optional, default value "Default", not implemented yet.

*Name*: $(PropertyName) is a valid model property name. **REQUIRED.**

*Value*: $(PropertyValue) is a valid value for the specified property. **REQUIRED.**

#### [Samples](#Samples)

```
<SetGeneratorProperty Generator="Default" Name="Database access caching" Value="Yes" />
```

**Note**: As you notice in the sample code, it is valid to name the property in the MSBuild exactly as it appears in the [IDE](https://wiki.genexus.com/commwiki/wiki?5272)

`[imagen omitida: wiki id 49559]`

#### [Consideration](#Consideration)

When indicating a GeneratorName, you have to consider the following:

If the Front end generator is of the same type as the Back end generator, you have to indicate the name of the generator as shown below:

```
<SetGeneratorProperty Generator=".NET" Name="Enable Datepicker" Value="Yes" />
```

On the other hand, if the Front end generator doesn't match the Back End, you have to write "SmartDevices" as shown below:

```
<SetGeneratorProperty Generator="SmartDevices" Name="Generate Android" Value="$(DoIncludeSD)"/>
<SetGeneratorProperty Generator="SmartDevices" Name="Generate Apple" Value="$(DoIncludeSD)"/>
<!Apple properties -->
<SetGeneratorProperty Generator="SmartDevices" Name="MAC_HOST" Value="$(MacHostName)"/>
<SetGeneratorProperty Generator="SmartDevices" Name="MAC_USER" Value="$(MacBuilderUser)"/>
<SetGeneratorProperty Generator="SmartDevices" Name="MAC_PASS" Value="$(MacBuilderPsw)"/>
<!Android properties -->
<SetGeneratorProperty Generator="SmartDevices" Name="JDK Directory" Value="$(JAVA_HOME_FOR_ANDROID_GENERATOR)"/>
<SetGeneratorProperty Generator="SmartDevices" Name="ANDROID_SDK_DIR" Value="$(ANDROID_HOME)"/>
```

### [SetObjectProperty](#SetObjectProperty)

Sets the value of a given object property.

#### [Syntax](#Syntax)

```
<SetObjectProperty Object="$(ObjectName)" Name="$(PropertyName)" Value="$(PropertyValue)"/>
```

#### [Options](#Options)

*Object*: $(ObjectName) is the name of an [object](https://wiki.genexus.com/commwiki/wiki?1866) defined in the Knowledge Base to which the property will be assigned. **REQUIRED.**

*Name*: $(PropertyName) is a valid property name. **REQUIRED.**

*Value*: $(PropertyValue) is a valid value for the specified property. **REQUIRED.**

#### [Samples](#Samples)

```
<SetObjectProperty Object="Customer" Name="Business Component" Value="True" />
```

### [ResetEnvironmentProperty](#ResetEnvironmentProperty)

Resets the value of a given [Environment](https://wiki.genexus.com/commwiki/wiki?7115) property to the default value.

Syntax

```
<ResetEnvironmentProperty Name="$(PropertyName)"/>
```

Options

*Name*: $(PropertyName) is a valid environment property name. **REQUIRED.**

#### [Samples](#Samples)

```
<ResetEnvironmentProperty Name="Preserve Table Casing"/>
```

### ResetDataStoreProperty

Resets the value of a given Data Store property to the default value.

#### [Syntax](#Syntax)

```
<ResetDataStoreProperty Datastore="$(DataStoreName)" Name="$(PropertyName)"/>
```

#### [Options](#Options)

*Datastore*: $(DataStoreName) is the name of a Data Store defined in the Knowledge Base. Usually, the value of this name is "Default".

Optional, default value "Default", not implemented yet.

*Name*: $(PropertyName) is a valid Data Store property name. **REQUIRED.**

#### [Samples](#Samples)

```
<ResetDataStoreProperty Name="Database schema"/>
```

### [ResetGeneratorProperty](#ResetGeneratorProperty)

Resets the value of a given generator property to the default value.

#### [Syntax](#Syntax)

```
<ResetGeneratorProperty Generator="$(GeneratorName)" Name="$(PropertyName)"/>
```

#### [Options](#Options)

*Generator*: $(GeneratorName) is the name of a Generator defined in the Knowledge Base. Usually, the value of this name is "Default" or "Reorg".

Optional, default value "Default", not implemented yet.

*Name*: $(PropertyName) is a valid generator property name. **REQUIRED.**

#### [Samples](#Samples)

```
<ResetGeneratorProperty Name="Database access caching" />
```

### [GetKnowledgeBaseProperty, GetVersionProperty, GetEnvironmentProperty, GetGeneratorProperty, GetDataStoreProperty, GetObjectProperty](#GetKnowledgeBaseProperty%2C+GetVersionProperty%2C+GetEnvironmentProperty%2C+GetGeneratorProperty%2C+GetDataStoreProperty%2C+GetObjectProperty)

Gets the values of the given property.

#### [Syntax](#Syntax)

```
<GetKnowledgeBaseProperty Name="$(PName)">
   <Output TaskParameter="PropertyValue" PropertyName="PValue"/>
</GetKnowledgeBaseProperty>
<GetVersionProperty Name="$(PName)">
   <Output TaskParameter="PropertyValue" PropertyName="PValue"/>
</GetVersionProperty>
<GetEnvironmentProperty Name="$(PName)">
   <Output TaskParameter="PropertyValue" PropertyName="PValue"/>
</GetEnvironmentProperty>
<GetGeneratorProperty Name="$(PName)">
   <Output TaskParameter="PropertyValue" PropertyName="PValue"/>
</GetGeneratorProperty>
<GetDataStoreProperty Name="$(PName)">
   <Output TaskParameter="PropertyValue" PropertyName="PValue"/>
</GetDataStoreProperty>
<GetObjectProperty Object="$(SelectedKBObject)" Name="$(PName)">
   <Output TaskParameter="PropertyValue" PropertyName="PValue" />
</GetObjectProperty>
```

### [Export](#Export)

Exports the currently opened Knowledge Base to a file.

#### [Syntax](#Syntax)

```
<Export File="$(ExportFileName)" Objects="$(ObjectList)" DependencyType="$(depType)" 
ReferenceType="$(refType)" IncludeGXMessages="$(includeGXMsg)" IncludeUntranslatedMessages="$(includeUtMsg)" OnlyStructuresForTransactions="$(OnlyStructTrn)" />
```

#### [Options](#Options)

*File*: $(ExportFileName) is the fully or partially qualified name of an export file (.XPZ). **REQUIRED.**

*Objects*: $(ObjectList) is the list of objects to specify (see the section about [object lists in MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?7769).) Unless you use this parameter, all objects in the Knowledge Base will be exported.

*DependencyType*: when using the Objects parameter, you may set DependencyType to “ReferencedBy” or “ReferencesTo” to also export objects that either is *referenced by* or *reference to*, respectively, the original set. Default: “ReferencesTo”.

*ReferenceType*: controls what kinds of references are used when adding objects with a given DependencyType. Possible values are: “None” (no reference is considered, which avoids the effect of the DependencyType parameter); “Minimal” (only the references that would be needed when importing in a new KB); “Hard” (all hard references); and “All”. Default: “Minimal”.

*IncludeGXMessages*: when exporting languages, standard GeneXus messages are not exported unless you use this parameter. Possible values: “true” and “false”. Default “false”.

*IncludeUntranslatedMessages*: exporting languages, untranslated messages are not exported unless you use this parameter. Possible values “true” and “false”. Default “false”.

*OnlyStructuresForTransactions:* exporting the selected Transaction's structure. Possible values: “true” and “false”. Default “false”.

*ExportKBInfo*: include information about the Knowledge Base (KB Guid and source). Possible values "true" and "false". Default "true".

*ExportAll*: specifies to export the entire model and their active objects. Possible values "true" and "false". Default "false".

#### [Samples](#Samples)

Export to file c:\MyExports\ImportTestFile.xpz the content of the currently opened Knowledge Base.

```
<Export File="c:\MyExports\ImportTestFile.xpz" />
```

### [BuildAll](#BuildAll)

Builds all objects in a Knowledge Base optionally forcing its generation. Building means performing all tasks required to successfully run the application. Knowledge Base objects are specified, generated and compiled. If a reorganization is required, it is also automatically run.

#### [Syntax](#Syntax)

```
<BuildAll ForceRebuild="true|false" CompileMains="true|false" DetailedNavigation="true|false" FailIfReorg="true|false" DoNotExecuteReorg="true|false"/>
```

#### [Options](#Options)

*ForceRebuild*: indicates whether a rebuild should be performed; the default value is False.

*CompileMains*: if false it will compile only the Developer menu or [Startup Object](https://wiki.genexus.com/commwiki/wiki?13606), if true it will also compile all main objects in the KB.

*DetailedNavigation*: indicates whether a detailed navigation should be done; the default value is False.

For scenarios where you do not want to continue if there is an implicit reorganization at build time or the reorg is not wanted to be executed, the next 2 options were added:

*FailIfReorg*: When true the build fails if there is a reorganization (that is generated) and nothing else is generated; the default value is False (continue with the build).  
When true the generated reorganization can be executed later.  
If there is no reorganization this option does not apply.

*DoNotExecuteReorg*: indicates if the reorganization will be executed or not; the default value is False (execute the reorganization).  
It is similar to the Reorganization option -donotexecute but in this case, the program is never executed

#### [Samples](#Samples)

Build, without forcing generation, all objects in the currently opened Knowledge Base.

```
<BuildAll ForceRebuild="false" />
```

### [BuildOne](#BuildOne)

Builds the object specified and all objects it calls (direct or indirect). Building means performing all tasks required to successfully run the application. Objects (the one selected and those called by it) are specified, generated and compiled. If a reorganization is required, it is also automatically run.

#### [Syntax](#Syntax)

```
<BuildOne ForceRebuild="true|false" BuildCalled="true|false" ObjectName="$(ObjectName)" DetailedNavigation="true|false" />
```

#### [Options](#Options)

*ForceRebuild*: indicates whether a rebuild should be performed; the default value is False.

*ObjectName*: is the name of an existing object having the Main property set to true. **REQUIRED.**

*DetailedNavigation*: indicates whether a detailed navigation should be done; the default value is False.

#### [Samples](#Samples)

Build object MyMainMenu and all called objects in the currently opened Knowledge Base.

```
<BuildOne ObjectName="MyMainMenu" />
```

### [RebuildArtifacts](#RebuildArtifacts)

Builds the KB/Enviroment artifacts, available from [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?42129,,). Further information: [SAC 45075](https://www.genexus.com/en/developers/websac?data=45075;;)

#### [Syntax](#Syntax)

```
<RebuildArtifacts/>
```

### [Custom Build](#Custom+Build)

Execute the tasks of a [Custom Build](https://wiki.genexus.com/commwiki/wiki?43849) previously defined from GeneXus IDE, through Tools > Options > Build > Custom Build.

#### [Syntax](#Syntax)

```
<CustomBuild Name="$(CustomBuild Name)" ObjectName="$(ObjectName)"/>
```

#### [Options](#Options)

*CustomBuild Name:* Itis the name of the Custom Build command. **REQUIRED.**

*ObjectName*: is the name of an existing object having the Main property set to true. Mandatory when the Custom Build is about an object.

#### [Samples](#Samples)

Suppose that "Build mobile without compiling" is the name of a Custom Build, previously defined in the GeneXus IDE, to carry out all the tasks of the build process except the final compilation.

So the tasks that MSbuild will execute are the tasks defined in "Build mobile without compiling".

```
<CustomBuild Name="Build mobile without compile" ObjectName="MainPanelSD"/>
```

### [DeleteObject](#DeleteObject)

Removes the specified object from the Knowledge Base.

#### [Syntax](#Syntax)

```
<DeleteObject Objects="$(ObjectName)" IncludeChildren="true|false" FailWhenNone="true|false"/>
```

#### [Options](#Options)

*Objects*: $(ObjectName) is the name of the object to be deleted. **REQUIRED.**

*IncludeChildren*: "true|false" can be used if the specified object name is a folder or module.

*FailWhenNone*: error if the object doesn't exist.

### [Run](#Run)

Builds the specified object and all objects it references (direct or indirectly), and executes it. The object must have the Main property set to True. Building means performing all tasks required to successfully run the object. Objects (the one selected and those called by it) are specified, generated and compiled. If a reorganization is required, it is also automatically run. This behavior can be changed specifying *Build=false*, where only the execution of the object is performed.

#### [Syntax](#Syntax)

```
<Run ForceRebuild="true|false" Build="true|false" BuildCalled="true|false" ObjectName="$(ObjectName)" DetailedNavigation="true|false" />
```

#### [Options](#Options)

*ForceRebuild*: indicates whether a rebuild should be performed; the default value is False.

*Build:* indicates whether the object should be built as well; the default value is True.

*BuildCalled*: indicates whether called objects should be built as well; the default value is True.

*ObjectName*: is the name of an existing object having the Main property set to True. **REQUIRED.**

*DetailedNavigation*: indicates whether a detailed navigation should be done; the default value is False.

*Parameters:* allows you to pass parameters to an object's run

#### [Samples](#Samples)

Build object MyMainMenu and all called objects in the currently opened Knowledge Base, and execute object MyMainMenu.

```
<Run ObjectName="MyMainMenu" />
```

### [RestoreRevision](#RestoreRevision)

Restores the specified object to the specified revision.

#### [Syntax](#Syntax)

```
<RestoreRevision Object=<"object type":"object name"> RevisionId=<"revision id"> />
```

### [CreateDatabase](#CreateDatabase)

Creates Database objects (tables, indices, constraints, etc.) as required for the currently opened Knowledge Base.

#### [Syntax](#Syntax)

```
<CreateDatabase ExecuteCreate="true|false" />
```

#### [Options](#Options)

*ExecuteCreate*

### [Create Offline Database](#Create+Offline+Database)

Creates an offline Database for a list of Native Mobile Objects, configured with the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) = "Offline".

#### [Syntax](#Syntax)

```
<CreateOfflineDatabase OfflineObjectNames="$(ObjectName)">
```

#### [Options](#Options)

*OfflineObjectNames*: List of the Offline Object Names separated by semicolons (;). **REQUIRED.**

#### [Samples](#Samples)

Creates and executes the Create Offline Database for the OfflineDatabaseByTable and OfflineDatabaseByRowHash objects, set to "Offline".

```
<CreateOfflineDatabase OfflineObjectNames="OfflineDatabaseByTable;OfflineDatabaseByRowHash"/>
```

### [Reorganize](#Reorganize)

Compiles and Executes the last Impact Data Base specified.

#### [Syntax](#Syntax)

```
<Reorganize />
```

### [SpecifyAll](#SpecifyAll)

Specifies all objects in a Knowledge Base, optionally forcing their generation (but not generating).

#### [Syntax](#Syntax)

```
<SpecifyAll ForceRebuild="true|false" DetailedNavigation="true|false" />
```

#### [Options](#Options)

*ForceRebuild*: indicates whether a rebuild should be performed; the default value is False.

*DetailedNavigation*: indicates whether a detailed navigation should be done; the default value is False.

#### [Samples](#Samples)

Specify, without forcing generation, all objects in the currently opened Knowledge Base.

```
<SpecifyAll ForceRebuild="false" />
```

### [GenerateOnly](#GenerateOnly)

Generates all objects whose generation is pending by the execution of a previous SpecifyAll tasks. It does not compile generated objects.

#### [Syntax](#Syntax)

```
<GenerateOnly />
```

### [Compile](#Compile)

Compiles the object specified in the optional parameter ObjectName. If the ObjectName parameter is omitted, the Developer Menu is compiled.

#### [Syntax](#Syntax)

```
<Compile ObjectName="$(ObjectName)" />
```

#### [Options](#Options)

*ObjectName*: is the name of an existing object having the Main property set to true.

* Optional, default to compile the Developer Menu.

#### [Samples](#Samples)

Compile object MyMainMenu in the currently opened Knowledge Base.

```
<Compile ObjectName="MyMainMenu" />
```

### [UpdateWorkingModel](#UpdateWorkingModel)

Updates the working model with information of the corresponding design model. This task should be executed with care as once executed, GeneXus will "forget" all design changes made. If, for example, a Database change was required due to design changes and you execute the UpdateWorkingModel task, those changes will **not** be applied to your Database.

#### [Syntax](#Syntax)

```
<UpdateWorkingModel />
```

### [WriteKnowledgeBaseSchema](#WriteKnowledgeBaseSchema)

Writes a .xml file with the schema of the database that is defined by a GeneXus project.

#### [Syntax](#Syntax)

```
<WriteKnowledgeBaseSchema File="$(KnowledgeBaseSchemaFile)" DesignModel="true|false" SortByName="true|false" />
```

#### [Options](#Options)

*File*: $(KnowledgeBaseSchemaFile) is the fully or partially qualified name of a Knowledge Base Schema file to be created. **REQUIRED.**

*DesignModel:* "true" to display design model information; "false" to display target model information. Default: false.

*SortByName*: "true" to display table and index information ordered by name. Default: false.

### [WriteDatabaseSchema](#WriteDatabaseSchema)

Writes a .xml file with the schema of the database that is configured in a GeneXus project.

#### [Syntax](#Syntax)

```
<WriteDatabaseSchema File="$(DataBaseSchemaFile)" />
```

#### [Options](#Options)

*File*: $(DataBaseSchemaFile) is the fully or partially qualified name of the Database Schema file to be created. **REQUIRED.**

### [CompareSchemas](#CompareSchemas)

Compares files representing a Database schema and a Knowledge Base Schema. You may have created these files using WriteDatabaseSchema and WriteKnowledgeBaseSchema tasks. This is useful to know if the database schema is synchronized with the schema defined by the KB.

#### [Syntax](#Syntax)

```
<CompareSchemas DBFile="$(DataBaseSchemaFile)" KBFile="$(KnowledgeBaseSchemaFile)" DiffFile="$(ComparisonDifferenceFile)" />
```

#### [Options](#Options)

*DBFile*: $(DataBaseSchemaFile) is the fully or partially qualified name of the Database Schema file to be compared. **REQUIRED.**

*KBFile*: $(KnowledgeBaseSchemaFile) is the fully or partially qualified name of a Knowledge Base Schema file to be compared. **REQUIRED.**

*DiffFile*: $(ComparisonDifferenceFile) is the fully or partially qualified name of a file generated with the differences in the schemas comparison.

### [CheckKnowledgeBase](#CheckKnowledgeBase)

The CheckKnowledgeBase task checks the consistency of a Knowledge Base.

#### [Syntax](#Syntax)

```
<CheckKnowledgeBase Fix="true|false" />
```

#### [Options](#Options)

*Fix*: determines if errors are fixed or not.

### [GetCategoryObjects](#GetCategoryObjects)

The GetCategoryObjects task returns a list of all objects belonging to a given category.

#### [Syntax](#Syntax)

```
<GetCategoryObjects CategoryName="TestCategory">
   <Output TaskParameter="Objects" PropertyName="ObjList"/>
</GetCategoryObjects>

<Message Text="Objects in TestCategory = $(ObjList)"/>
```

### [SetConfiguration](#SetConfiguration)

Changes configuration; it's the combo in the IDE that shows Release, Debug, Performance Test, Live Editing.

#### [Syntax](#Syntax)

```
<SetConfiguration Configuration="$(Configuration)"/>
```

#### [Options](#Options)

*Configuration*: $(Configuration) is a valid configuration: "Release", "Debug", or "Performance Test". Note that "Live Editing" is **not** yet included for this task.

### [SetCredential](#SetCredential)

The SetCredential task changes the GeneXus Account that is later used for some services, for example for deploying to cloud; it's the same one that you can change in the IDE in Tools>GeneXus Account.

#### [Syntax](#Syntax)

```
<SetCredential UserName="$(UserName)" UserPassword="$(UserPassword)" Persist="true|false" />
```

#### [Options](#Options)

*UserName*: $(UserName) is a valid GeneXus Account username.

*UserPassword*: &(UserPassword)is the GeneXus Account password that corresponds to that username.

*Persist*: determines if the information persists or if it's only for this session.

### [Teamworking](#Teamworking)

See also [Team Development MSBuild Tasks](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24612,,)

### [CreateVersion](#CreateVersion)

Creates a new frozen version from the active or specified version.

#### [Syntax](#Syntax)

```
<CreateVersion VersionName="$(VersionName)" VersionDescription="$(VersionDescription)" Parent="$(ParentName)" />
```

#### [Options](#Options)

*VersionName*: is the name that will be assigned to the Version. **REQUIRED.**

*VersionDescription*: is an optional description for the Version. Parent is the name of an existing development version. The special value \*Trunk or the Knowledge Base's name can be used to name the root element of the version tree.

*Parent*: is the name of an existing development or frozen version. The special value \*Trunk or the Knowledge Base's name can be used to name the root element of the version tree.

### [SetActiveVersion](#SetActiveVersion)

Sets a development version as "active" or current. All subsequent commands that do not specify a development version or frozen version work on this version.

#### [Syntax](#Syntax)

```
<SetActiveVersion VersionName="$(VersionName)" />
```

#### [Options](#Options)

*VersionName*: is the name of an existing version. **REQUIRED.**

### [RevertToVersion](#RevertToVersion)

Reverts (overwrites) the Root version with the version specified as the parameter. Any changes to the Root version are lost.

#### [Syntax](#Syntax)

```
<RevertToVersion VersionName="$(VersionName)" />
```

#### [Options](#Options)

*VersionName*: is the name of an existing version. **REQUIRED.**

### [MergeVersions](#MergeVersions)

Makes a merge between two versions.

#### [Syntax](#Syntax)

```
<MergeVersions SourceVersion="$(SourceVersion)" TargetVersion="$(TargetVersion)" SinceDate="$(SinceDate)" />
```

#### [Options](#Options)

*SourceVersion*: is the Version from which the changes will be brought. **REQUIRED.**

*TargetVersion*: is the Version where the changes will be applied. If not indicated, the active Version will be used.

*SinceDate*: is the beginning date to consider the changes to apply. If not indicated, all changes will be applied. The formats supported by the parameter are detailed [here](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings?redirectedfrom=MSDN). Note that some formats depend on the regional configuration of the machine. An independent format is suggested, i.e."yyyy-mm-dd hh:MM:ss".

### [GetActiveVersion](#GetActiveVersion)

Returns the active [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) Version.

#### [Syntax](#Syntax)

```
<GetActiveVersion/>
```

Sample result

```
The active version is 'KBVersionName'
> GetActiveVersion Success
```

It is possible to get the value in a variable if needed:

```
<GetActiveVersion>
        <Output TaskParameter="VersionName" PropertyName="ActiveVersionName" />
</GetActiveVersion>
```

### [CreateEnvironment](#CreateEnvironment)

Creates a new Environment in the active or specified version.

#### [Syntax](#Syntax)

```
<CreateEnvironment Name="$(EnvironmentName)" Template="$(KBTemplate)" />
```

#### [Options](#Options)

*Name*: is the name that will be assigned to the Environment. **REQUIRED.**

*Template*: one of the KBTemplates files located in the Template directory of a GeneXus installation, that has information about generator and DBMS types. **REQUIRED.**

### [SetActiveEnvironment](#SetActiveEnvironment)

Sets an Environment as the active or current one. All subsequent commands that do not specify an environment work on this Environment. The Environment must exist in the active Version.

#### [Syntax](#Syntax)

```
<SetActiveEnvironment EnvironmentName="$(EnvironmentName)" />
```

#### [Options](#Options)

*EnvironmentName*: is the name of an existing Environment. **REQUIRED.**

### [GetActiveEnvironment](#GetActiveEnvironment)

Returns the active Environment.

#### [Syntax](#Syntax)

```
<GetActiveEnvironment/>
```

Sample result

```
The active environment is 'NETSQLServer'
> GetActiveEnvironment Success
```

It is possible to get the value in a variable if needed:

```
<GetActiveEnvironment>
        <Output TaskParameter="EnvironmentName" PropertyName="ActiveEnvironmentName" />
</GetActiveEnvironment>
```

### [Modules Handling](#Modules+Handling)

See [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376).

## [Output](#Output)

When you run an MSBuild script, the results are displayed in the standard output by default. You can also indicate an XML output to be generated to a file, using the following parameter:

XmlOutputFile="$(XmlOutputFile)"

To process the result programmatically, check the [CaptureOutput](https://wiki.genexus.com/commwiki/wiki?35863) property.

## [Executing MSBuild Scripts](#Executing+MSBuild+Scripts)

MSBuild scripts can be executed from the command line by invoking MSBuild.exe (stored in folder C:\WINDOWS\Microsoft.NET\Framework\v4.0 if you have installed all products leaving default path names). A sample command line to execute the script called Demo.msbuild is as follows.

```
msbuild Demo.msbuild
```

**Note**: Be sure to execute the MSBuild tasks using the Microsoft.Net Framework 32 bits 4.0 or higher. If you instead use the 64 bits framework the following error will be shown:

```
error : Could not load file or assembly 'gxio, Version=0.0.0.0, Culture=neutral, PublicKeyToken=6f5bf81c27b6b8aa' or one of its dependencies. The system cannot find the file specified.
```

## [Sample scripts](#Sample+scripts)

### [Test all GeneXus MSBuild Tasks](#Test+all+GeneXus+MSBuild+Tasks)

This test just invokes every GeneXus MSBuild Task

```
<Project DefaultTargets="Test" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
    <Import Project="C:\Program Files\Artech\GeneXus\GeneXusX\GeneXus.Tasks.targets" />

    <PropertyGroup>
        <KBTemplate>csharp.kbtemplate</KBTemplate>
        <KBPath>c:\TestKnowledgeBases</KBPath>
    </PropertyGroup>

	<Target Name="CreateKnowledgeBase">
		<RemoveDir Directories="$(KBPath)" />
		<CreateKnowledgeBase Directory="$(KBPath)\TestCreate" Template="$(KBTemplate)" />
	</Target>
	<Target Name="Import">
		<Import File="c:\NameOfFileToImport.xpz" />
	</Target>
	<Target Name="OpenKnowledgeBase">
		<OpenKnowledgeBase Directory="$(KBPath)\TestCreate" />
	</Target>
	<Target Name="Export">
		<Export File="c:\NameOfDistributionFile.xpz" />
	</Target>
	<Target Name="Reorganize">
		<Reorganize />
	</Target>
	<Target Name="SpecifyAll">
		<SpecifyAll ForceRebuild="false" />
	</Target>
	<Target Name="Generate">
		<Generate />
	</Target>
	<Target Name="Compile">
		<Compile ObjectName="NameOfObjectToCompile" />
	</Target>
	<Target Name="UpdateWorkingModel">
		<UpdateWorkingModel />
	</Target>
	<Target Name="BuildOne">
		<BuildOne ObjectName="NameOfObjectToBuild" />
	</Target>
	<Target Name="BuildAll">
		<BuildAll />
	</Target>
    <Target Name="RestoreRevision">
        <OpenKnowledgeBase Directory="$(KBPath)" />
        <RestoreRevision Object="ObjectType:ObjectName" RevisioID="RevisionId" /> 
    </Target>
</Project>
```

To run this script, you should use a command line like the following

```
MSBuild /t:CreateKnowledgeBase;Import;OpenKnowledgeBase;Export;Reorganize;SpecifyAll;Generate;Compile;UpdateworkingModel;BuildOne;BuildAll 
TestAlPrimitives.msbuild
```

If you want to execute each function separately:

```
MSBuild /t:CreateKnowledgeBase TestAlPrimitives.msbuild
MSBuild /t:OpenKnowledgeBase;Import TestAlPrimitives.msbuild
MSBuild /t:OpenKnowledgeBase;SpecifyAll TestAlPrimitives.msbuild
...
```

### [Building all objects of an existing Knowledge Base](#Building+all+objects+of+an+existing+Knowledge+Base)

```
<Project DefaultTargets="TestGenexus" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
   <Import Project="C:\Program Files\Artech\GeneXus\GeneXusX\Genexus.Tasks.targets" />
   <PropertyGroup>
      <KBPath>C:\MyKnowledgeBases\test</KBPath>
   </PropertyGroup>
   <Target Name="TestGenexus">
      <OpenKnowledgeBase Directory="$(KBPath)" />
      <SpecifyAll />
   </Target>
</Project>
```

### [See Also](#See+Also)

[CaptureOutput MSBuild Property](https://wiki.genexus.com/commwiki/wiki?35863)  
[How to create a unit test and add a task using the GeneXus Jenkins Plugin](https://wiki.genexus.com/commwiki/wiki?38359)  
[Team Development MSBuild Tasks](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24612,,)  
[Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073)  
[GAM MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?46226)


|  |
| --- |
| **Backlinks** |
| [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073) | [Application Deployment MSBuild tasks (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58040) |
| [Application Deployment MSBuild tasks (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58052) | [AssemblyImport MSBuild Task](https://wiki.genexus.com/commwiki/wiki?44422) | [Automated DevOps with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51574) | [Category:Build Menu](https://wiki.genexus.com/commwiki/wiki?5690) |
| [CaptureOutput MSBuild Property](https://wiki.genexus.com/commwiki/wiki?35863) | [Table of contents:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Category:Continuous Integration](https://wiki.genexus.com/commwiki/wiki?38331) | [GAM MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?46226) |
| [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) |
| [GeneXus SAP Systems Deployment to a Production Environment](https://wiki.genexus.com/commwiki/wiki?35466) | [GeneXus Task MSBuild Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?51033) | [HelpGenerator MSBuild Task](https://wiki.genexus.com/commwiki/wiki?12560) |
| [How to specify an object list in a MSBuild task](https://wiki.genexus.com/commwiki/wiki?44328) | [HowTo: Deploy Frontend applications to Azure Blob Storage](https://wiki.genexus.com/commwiki/wiki?49878) | [HowTo: Deploy Static Front end to Docker using MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?51115) | [HowTo: Deploy Static Front end to Docker using MSBuild Tasks (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?58901) |
| [Import MSBuild Task](https://wiki.genexus.com/commwiki/wiki?35599) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) | [Offline scenario of the .NET Generator](https://wiki.genexus.com/commwiki/wiki?53793) |
| [Patterns MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?12559) | [Tools - Options - Custom Build](https://wiki.genexus.com/commwiki/wiki?43849) |

---
