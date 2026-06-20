---
title: "Compile using MSBuild instead of CSC"
source_id: 42661
source_url: https://wiki.genexus.com/commwiki/wiki?42661
genexus_version: "18"
---

# Compile using MSBuild instead of CSC

This page explains aspects related to compilation using MSBuild instead of CSC.

The benefits of using this mechanism are as follows:

* Enhanced build & compile performance thanks to parallel compilation.
* A standard project file is generated, so projects can be opened with Visual Studio too. The solution is named *LastBuild.sln* and is located under the Target Environment *build* folder. It includes a solution for every object compiled. Notice the solution file will change on every build process referencing the compiled objects.

### [New Properties associated with this mechanism](#New+Properties+associated+with+this+mechanism)

* [MSBuild options property](https://wiki.genexus.com/commwiki/wiki?44168): Contains the flags that are passed as parameters to msbuild.exe. Therefore, any flag mentioned in <https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2017> is valid.
* [Build Mode property for .NET generator](https://wiki.genexus.com/commwiki/wiki?3936): Contains a new value "**MSBuild**" which is the default value for new knowledge bases. It indicates which compilation mode is used. Existing knowledge bases keep the previous default ("Standard") in order to preserve behavior.

#### [Sample property value](#Sample+property+value)

```
-m /v:quiet /p:Configuration=Debug /p:PlatformTarget=x86 /p:GxExternalReference="MyAPI.dll;MyLibrary.dll"
```

which indicates:

-m => To compile in parallel using all the processors available. If you compile 10 main objects, those 10 main objects will be compiled in parallel, as long as the processors of the machine allow it.   
/v:quiet => Sets the output to quiet, so that it is similar to the previous mechanism (csc).   
/p:Configuration=Debug => To compile in debug mode (generating .pdb files).  
/p:PlatformTarget=x86 => To compile for 32 bits (equivalent to /platform:x86 in csc.exe).  
/p:GxExternalReference="MyAPI.dll;MyLibrary.dll" => To include MyAPI.dll and MyLibrary in references (equivalent to /r:bin\MyAPI.dll  /r:bin\MyLibrary.dll in csc.exe).

**Note**: [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) already uses this mechanism as the only one suitable.

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).

### [See Also](#See+Also)

* [MSBuild flags](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2017)
* [Blog - success story by Enrique Almeida (Spanish)](http://ealmeida.blogspot.com/2020/07/tiempos-de-rebuild-all-en-upgrade-10.html)


|  |
| --- |
| **Backlinks** |
| [Build Mode property for .NET generator](https://wiki.genexus.com/commwiki/wiki?3936) |
| [MSBuild options property](https://wiki.genexus.com/commwiki/wiki?44168) |

---
