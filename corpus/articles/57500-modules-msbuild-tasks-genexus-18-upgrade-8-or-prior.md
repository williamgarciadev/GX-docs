---
title: "Modules MSBuild Tasks (GeneXus 18 Upgrade 8 or prior)"
source_id: 57500
source_url: https://wiki.genexus.com/commwiki/wiki?57500
genexus_version: "18"
---

# Modules MSBuild Tasks (GeneXus 18 Upgrade 8 or prior)

This page lists and describes the MSBuild tasks related to [Modules](https://wiki.genexus.com/commwiki/wiki?22414).

**Summary**

* [AddModulesServer Task](#AddModulesServer+Task)

+ [Parameters](#Parameters)
+ [Example](#Example)

* [InstallModule Task](#InstallModule+Task)

+ [Parameters](#Parameters)
+ [Example](#Example)

* [PackageModule Task](#PackageModule+Task)

+ [Parameters](#Parameters)
+ [Example](#Example)

* [PublishModule Task](#PublishModule+Task)

+ [Parameters](#Parameters)
+ [Example](#Example)

* [RestoreModule Task](#RestoreModule+Task)

+ [Parameters](#Parameters)
+ [Example](#Example)

* [UpdateModule Task](#UpdateModule+Task)

+ [Parameters](#Parameters)
+ [Example](#Example)

## [AddModulesServer Task](#AddModulesServer+Task)

Adds a module server definition that is required for publishing a packaged module.

### [Parameters](#Parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| Type | `Required` string | Specifies the type of server.  **Values:**  * Directory * Nexus - NuGet * Nexus - Maven |
| Name | `Required` string | Specifies the server identifier. The name should be a valid identifier without spaces or special characters. |
| Source | `Required` string | Specifies the server source. Depending on the `Type` of module server, it could be a directory path or a valid URL to a Nexus installation. |
| Preserve | bool | If **true**, saves the server settings for later use. Default **false**. |
| OverwriteDefinition | bool | If **true**, overwrites the existing definition. Default **false**. |
| User | string | Optional parameter to indicate the user name. |
| Password | string | Optional parameter to specify the password. |

### [Example](#Example)

This sample shows how to create a local module server. The modules are going to be stored in the file system.

```
msbuild addserver.msbuild /t:AddServer /p:ServerType=Directory /p:Directory=c:\mymodules /p:ServerName=MyServer
```

addserver.msbuild

```
<Project DefaultTargets="AddServer" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">

	<Import Project="$(MSBuildProjectDirectory)\Genexus.Tasks.targets" />

	<Target Name="AddServer">
		<AddModulesServer Type="$(ServerType)" Name="$(ServerName)" Source="$(Directory)" />
	</Target>
</Project>
			
```

## [InstallModule Task](#InstallModule+Task)

Imports a module from the local cache to the working model.

### [Parameters](#Parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| ModuleName | `Required` string | Module to import. |
| Version | string | Version of the module to import. |

### [Example](#Example)

This sample shows how to install a module for the given KB in the given environment.

```
msbuild installModule.msbuild /t:Install /p:ModuleName=MyModule /p:KBPath=c:\mykb /p:EnvName=NetEnvironment
```

installModule.msbuild

```
<Project DefaultTargets="Install" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">

	<Import Project="$(MSBuildProjectDirectory)\Genexus.Tasks.targets" />

	<Target Name="Install">
		<OpenKnowledgeBase Directory="$(KBPath)"/>
		<SetActiveEnvironment EnvironmentName="$(EnvName)" />
		<InstallModule ModuleName="$(ModuleName)" />
	</Target>
</Project>
			
```

## [PackageModule Task](#PackageModule+Task)

Publishes a module for the working model to the local cache.

### [Parameters](#Parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| ModuleName | `Required` string | Full Module Name to publish. |
| Rebuild | bool | Rebuilds the module. |
| OutputDirectory | string | Output directory where to publish the module. |
| Environments | string[] | List of environment names to be included in the packaged module. If no environment name is specified, the package operation includes all the environments in the Knowledge Base. |

### [Example](#Example)

This sample creates a package for a module named MyModule.

```
msbuild package.msbuild /t:PackageModule /p:PackageModuleName=MyModule /p:PackageModuleVersion=1.0
```

The content for package.msbuild is as follows:

```
<Target Name="PackageModule">
	<Message Text="Packaging Module:$(PackageModuleName)" Importance="high"/>
	<Message Text="Packaging Module Version:$(PackageModuleVersion)" Importance="high"/>
	<SetObjectProperty Object="Module:$(PackageModuleName)" Name="ModuleVersion" Value="$(PackageModuleVersion)"/>
	<PropertyGroup>
		<CSharpEnvName>NetEnvironment</CSharpEnvName>
		<JavaEnvName>JavaEnvironment</JavaEnvName>
		<NetCoreEnvName>NetCoreEnvironment</NetCoreEnvName>
	</PropertyGroup>

	<!-- CSharp -->
	<SetActiveEnvironment EnvironmentName="$(CSharpEnvName)"/>
	<BuildAll ForceRebuild="$(DoForceBuild)" />

	<!-- Java -->
	<SetActiveEnvironment EnvironmentName="$(JavaEnvName)"/>
	<BuildAll ForceRebuild="$(DoForceBuild)" />

	<!-- NetCore -->
	<SetActiveEnvironment EnvironmentName="$(NetCoreEnvName)"/>
	<BuildAll ForceRebuild="$(DoForceBuild)" />

	<ItemGroup>
		<EnvToPackage Include="$(CSharpEnvName)"/>
		<EnvToPackage Include="$(JavaEnvName)"/>
		<EnvToPackage Include="$(NetCoreEnvName)"/>
	</ItemGroup>

	<PackageModule ModuleName="$(PackageModuleName)" Environments="@(EnvToPackage)" OutputDirectory="$(ModulesTMPPath)"/>
</Target>
		
```

## [PublishModule Task](#PublishModule+Task)

Publishes a module for the working model to the local cache.

### [Parameters](#Parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| ModuleName | `Required` string | Module to publish. |
| OpcFile | string | Packaged module to publish. |
| Server | `Required` string | Server identifier where to upload the packaged module. |
| User | string | Optional parameter to indicate the user name. |
| Password | string | Optional parameter to specify the password. |

### [Example](#Example)

This example publishes a package for a module called MyModule:

```
msbuild publish.msbuild /t:Publish /p:ModuleName=MyModule /p:ServerName=MyServer /p:KBPath=c:\mykb /p:User=userName /p:Password=password
```

publish.msbuild:

```
<Project DefaultTargets="Publish" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
    <Import Project="$(MSBuildProjectDirectory)\Genexus.Tasks.targets" />

    <Target Name="Publish">
       <OpenKnowledgeBase Directory="$(KBPath)"/>
       <PublishModule ModuleName="$(ModuleName)" ServerName="$(ServerName)" User="$(userName)" Password="$(password)"/>
    </Target>
</Project>
```

## [RestoreModule Task](#RestoreModule+Task)

Restores the implementation of a packaged module defined in the Knowledge Base.

### [Parameters](#Parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| ModuleName | string | Module to restore; it can be empty, in which case the restore task applies to each packaged module installed in the Knowledge Base. |

### [Example](#Example)

```
msbuild restore.msbuild /t:Restore /p:ModuleName=MyModule /p:KBPath=c:\mykb
```

restore.msbuild

```
<Project DefaultTargets="Restore" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
	<Import Project="$(MSBuildProjectDirectory)\Genexus.Tasks.targets" />

	<Target Name="Install">
		<OpenKnowledgeBase Directory="$(KBPath)"/>
		<RestoreModule ModuleName="$(ModuleName)" />
	</Target>
</Project>
			
```

## [UpdateModule Task](#UpdateModule+Task)

Updates an existing module to the given version or to the latest version.

### [Parameters](#Parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| ModuleName | `Required` string | Module to update. |
| Version | string | Version of the module to import. If empty, the module is updated to the latest version. |

### [Example](#Example)

In this example, the update.msbuild file is used to update a module to the latest version available.

```
msbuild update.msbuild /t:UpdateToLatest /p:ModuleName=MyModule /p:KBPath:c:\mykb
```

update.msbuild

```
<Project DefaultTargets="UpdateToLatest" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
	<Import Project="$(MSBuildProjectDirectory)\Genexus.Tasks.targets" />

	<Target Name="UpdateToLatest">
		<OpenKnowledgeBase Directory="$(KBPath)"/>
		<UpdateModule ModuleName="$(ModuleName)" />
	</Target>
</Project>
```

**Note**: You must define the MSBuildProjectDirectory variable pointing to the GeneXus root folder. Otherwise, the project import may fail.
