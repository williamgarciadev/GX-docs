---
title: "MSBuild options property"
source_id: 44168
source_url: https://wiki.genexus.com/commwiki/wiki?44168
genexus_version: "18"
---

# MSBuild options property

Defines flags to specify aspects of the build process, such as project properties (that is, Configuration type Debug or Release) or MSBuild process settings (that is, maxcpucount to run builds in parallel).

### [Scope](#Scope)

**Generators:** .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Below are some configuration samples for this property:

1)

```
/p:PlatformTarget=x86 /p:Configuration=Debug /p:GxExternalReference=Artech.Security.Common.dll
```

The above indicates three properties for the projects:

/p:PlatformTarget = x86 --- To be compiled to run in 32 bits.  
/p:Configuration = Debug --- To be compiled in debug mode, so that it generates the PDB of each DLL.  
/p:GxExternalReference=<assembly> --- References to external DLLs are added.

For the build process itself, you could set:  
/maxcpucount or / m --- If you compile several projects, they are compiled in parallel, which is faster.

2)

```
-m /v:quiet /p:Configuration=Debug /p:PlatformTarget=x86 /p:GxExternalReference=\"MyAPI.dll;MyLibrary.dll\"
```

It indicates the following:

-m => To compile in parallel using all the processors available. If you compile 10 main objects, they will be compiled in parallel, as long as the processors of the machine allow it.   
/v:quiet => Sets the output to quiet, so that it is similar to the previous mechanism (csc).   
/p:Configuration=Debug => To compile in debug mode (generating .pdb files).  
/p:PlatformTarget=x86 => To compile for 32 bits (equivalent to /platform:x86 in csc.exe).  
/p:GxExternalReference=\"MyAPI.dll;MyLibrary.dll\" => To include MyAPI.dll and MyLibrary in references (equivalent to /r:bin\MyAPI.dll  /r:bin\MyLibrary.dll in csc.exe).

Note that libraries must be included between "\" when more than one is referenced. Otherwise, compilation errors such as the following will be displayed::

```
========== Compilation for Default (.NET Core) started ==========
dotnet publish -nologo -v q  "E:\kb\NetCoreModel\web\GxDeps.csproj" -o "E:\kb\NetCoreModel\web\bin
dotnet build -nologo --force -c Release /v:q /m /p:GxExternalReference="MyAPI.dll;MyLibrary.dll" "E:\KB\NetCoreModel\build\LastBuild.sln"
MSBUILD : error MSB1006: Property is not valid.
Switch: MyAPI.dll
For switch syntax, type "MSBuild -help"
```

If you are using Mac,PowerShell or Linux Terminal the encoding to use should be like that:

```
/p:GxExternalReference=MyAPI.dll%3bMyLibrary.dll
```

3)

 /p:TargetFrameworkVersion=v4.7.1

It forces a build for a specific TargetFramework (for a valid list of values, see [here](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-target-framework-and-target-platform?view=vs-2019)).

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,).

### [See Also](#See+Also)

* [MSBuild command-line reference](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2017)
* [Compile using MSBuild instead of CSC](https://wiki.genexus.com/commwiki/wiki?42661)


|  |
| --- |
| **Backlinks** |
| [.NET Generator Troubleshooting](https://wiki.genexus.com/commwiki/wiki?50588) | [Compile using MSBuild instead of CSC](https://wiki.genexus.com/commwiki/wiki?42661) |

---
